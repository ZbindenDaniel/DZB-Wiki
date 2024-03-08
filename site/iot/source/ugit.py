# ugit
# micropython OTA update from github
# Created by TURFPTAx for the openmuscle project
# Check out https://openmuscle.org for more info
#
# Pulls files and folders from open github repository

import os
try:
 import urequests as requests        #importing socket
except:
 import requests
import ujson
import hashlib
import binascii
import machine
import time
import network
import utime
from logger import logger
from configuration import Config

global internal_tree

#### -------------User Variables----------------####
####

# Config
config = Config()

# Logging
log = logger("ugit", int(config.getValue("git.logLevel")), True)

# WiFi
ssid = config.getValue("webServer.STA.ssid")
password = config.getValue("webServer.STA.password")

# Git
# https://github.com/ZbindenDaniel/Birgisch
user = config.getValue("git.user")
repository = config.getValue("git.repository")
default_branch = config.getValue("git.default_branch")
token = config.getValue("git.token") # https://github.com/settings/tokens
raw = f'https://raw.githubusercontent.com/{user}/{repository}/{default_branch}/'

# Don't remove ugit.py from the ignore_files unless you know what you are doing :D
# Put the files you don't want deleted or updated here use '/filename.ext'
ignore_files = ['/ugit.py', '/config.json', '/boot.py']
ignore = ignore_files
### -----------END OF USER VARIABLES ----------####

# Static URLS
# GitHub uses 'main' instead of master for python repository trees
giturl = 'https://github.com/{user}/{repository}'
call_trees_url = f'https://api.github.com/repos/ZbindenDaniel/Birgisch/git/trees/main?recursive=1'

def pull(f_path, raw_url):
  log.debug(f'pulling {f_path} from github: {raw_url}')
  f_path = os.path.basename(f_path)
  headers = {'User-Agent': config.getValue("device.userAgent")}
  headers['Accept'] = 'application/json'
  if len(token) > 0:
      headers['Authorization'] = f'Bearer {token}'
  r = requests.get(raw_url, headers=headers, timeout=2000)
  log.debug(f'HERE')
  if r is None:
     log.warning("Could not Get request!")
     return False
  if(r.status_code == 200):
    try:
      log.debug(f'Got 200 response, write to {f_path}')
      new_file = open(f'{f_path}', 'w')
      new_file.write(f"{r.content.decode('utf-8')}")
      new_file.close()
      return True
    except:
      log.error(f'ERROR: Pulling {f_path}')
  log.error(f'Pulling file {f_path} got response code: {r.status_code}!')
  return False

def pull_all(tree=call_trees_url,ignore = ignore,isconnected=False):
  if not isconnected:
      wlan = wificonnect()
  os.chdir('/')
  tree = get_git_tree()
  internal_tree = build_internal_tree()
  internal_tree = remove_ignore(internal_tree)

  log.debug('download and save all files')
  os.chdir('update')
  response = True ## To see if all files got pulled
  for i in tree['tree']:
    try:
      response = pull(i['path'], raw + i['path']) # TODO: throw exception, don't delete files if they cannot be pulled
      log.debug(i['path'] + ' updated\n')
    except:
      log.warning(i['path'] + ' failed to pull\n')
  #TODO: delete files not in Github tree
  #if len(internal_tree) > 0:
      #for i in internal_tree:
      #    os.remove(i)
      #    log.append(i + ' removed from int mem')
  
  os.chdir('/')
  log.toFileWhenError()
  
  log.debug('resetting machine')
  if response:
    time.sleep(5)
    machine.reset()
    time.sleep(5)

def wificonnect(ssid=ssid,password=password):
    log.debug('Use: like ugit.wificonnect(SSID,Password)')
    log.debug('otherwise uses ssid,password in top of ugit.py code')
    log.debug(f'connection to SSID: {ssid}')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.connect(ssid,password)
    while not wlan.isconnected():
        pass
    log.debug(f'SSID: {ssid}')
    log.debug(wlan.ifconfig())
    return wlan
  
def build_internal_tree():
    log.debug('build_internal_tree')
    global internal_tree
    internal_tree = []
    os.chdir('/')
    for i in os.listdir():
        add_to_tree(i)
    return(internal_tree)

def add_to_tree(dir_item):
  global internal_tree
  exclude = ['lib', 'update', 'logs' ]
  if dir_item in exclude:
    return
  if os.path.isdir(dir_item) and len(os.listdir(dir_item)) >= 1:
    os.chdir(dir_item)
    for i in os.listdir():
      add_to_tree(i)
    os.chdir('..')
  else:
    if os.getcwd() != '/':
      subfile_path = os.getcwd() + '/' + dir_item
    else:
      subfile_path = os.getcwd() + dir_item
    try:
      internal_tree.append([subfile_path, get_hash(subfile_path)])
    except OSError: # type: ignore # for removing the type error indicator :)
      log.error(f'{dir_item} could not be added to tree')


def get_hash(file):
  o_file = open(file)
  r_file = o_file.read()
  o_file.close()                     # close it
  sha1obj = hashlib.sha1(r_file)
  hash = sha1obj.digest()
  return(binascii.hexlify(hash))

def get_data_hash(data):
    sha1obj = hashlib.sha1(data)
    hash = sha1obj.digest()
    return(binascii.hexlify(hash))
    
def get_git_tree(tree_url=call_trees_url):
   with open("gitTree.json", "r") as gitTree_file:
    log.debug('get_git_tree')
    tree = ujson.load(gitTree_file)
    gitTree_file.close()
    return tree

# This is not functioning at the moment
def pull_git_tree(tree_url=call_trees_url,):
  raw = f'https://raw.githubusercontent.com/{user}/{repository}/{default_branch}/'
  headers = {'User-Agent': 'DZB-iot'} 
  # ^^^ Github Requires user-agent header otherwise 403
  if len(token) > 0:
      headers['authorization'] = "bearer %s" % token 
  r = requests.get(tree_url,headers=headers)
  log.debug(r.status_code)
  data = ujson.load(r.content.decode('utf-8'))
  if 'tree' not in data:
      log.error('\nDefault branch not found. Set "default_branch" variable to your default branch.\n')
      raise Exception(f'Default branch {default_branch} not found.') 
  tree = ujson.load(r.content.decode('utf-8'))
  return(tree)
  
def parse_git_tree():
  tree = get_git_tree()
  dirs = []
  files = []
  for i in tree['tree']:
    if i['type'] == 'tree':
      dirs.append(i['path'])
    if i['type'] == 'blob':
      files.append([i['path'],i['sha'],i['mode']])
   
   
def check_ignore(tree=call_trees_url,ignore = ignore):
  os.chdir('/')
  tree = pull_git_tree()
  check = []
  # download and save all files
  for i in tree['tree']:
    if i['path'] not in ignore:
        log.debug(i['path'] + ' not in ignore')
    if i['path'] in ignore:
        log.debug(i['path']+ ' is in ignore')
        
def remove_ignore(internal_tree,ignore=ignore):
    clean_tree = []
    int_tree = []
    for i in internal_tree:
        int_tree.append(i[0])
    for i in int_tree:
        if i not in ignore:
            clean_tree.append(i)
    return(clean_tree)
        
def remove_item(item,tree):
    culled = []
    for i in tree:
        if item not in i:
            culled.append(i)
    return(culled)

def update():
    log.debug('updates ugit.py to newest version')
    raw_url = 'https://raw.githubusercontent.com/turfptax/ugit/master/'
    pull('ugit.py', raw_url+'ugit.py')

def backup():
    int_tree = build_internal_tree()
    backup_text = "ugit Backup Version 1.0\n\n"
    for i in int_tree:
        data = open(i[0],'r')
        backup_text += f'FN:SHA1{i[0]},{i[1]}\n'
        backup_text += '---'+data.read()+'---\n'
        data.close()
    backup = open('ugit.backup','w')
    backup.write(backup_text)
    backup.close()

