using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SceneLikeCam : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] public float movingSpeed = 1;
    [SerializeField] public float rotationSpeed = 5;
    [SerializeField] public float zoomSpeed = 5;

    [Header("Focus")]
    [SerializeField] public float focusLimit = 100;
    [SerializeField] public float doubleClickTime = .25f;
    [SerializeField] public float cooldown = 1;
    [SerializeField] public float targetedDistance = 10;
    

    [Header("Controls")]
    [SerializeField] private KeyCode forwardKey = KeyCode.W;
    [SerializeField] private KeyCode backKey = KeyCode.S;
    [SerializeField] private KeyCode leftKey = KeyCode.A;
    [SerializeField] private KeyCode rightKey = KeyCode.D;
    [SerializeField] private KeyCode upKey = KeyCode.UpArrow;
    [SerializeField] private KeyCode downKey = KeyCode.DownArrow;

    [SerializeField] private KeyCode anchoredMoveKey = KeyCode.Mouse2;
    [SerializeField] private KeyCode anchoredRotateKey = KeyCode.Mouse1;
    // Update is called once per frame
    void Update()
    {
        if(cooldown > 0 && Input.GetKeyDown(KeyCode.Mouse0)) // DoubleCLick
        {
            FocusObject();
        }
        if (Input.GetKeyDown(KeyCode.Mouse0))
            cooldown = doubleClickTime;

        cooldown -= Time.deltaTime;
    }

    private void FocusObject()
    {
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        RaycastHit hit;

        if (Physics.Raycast(ray, out hit, focusLimit))
        {
            // TODO: Still a bit shakey but works in general
            GameObject target = hit.collider.gameObject;
            var targetPosition = target.transform.position;
            var targetSize = hit.collider.bounds.size;
            var focusVector = new Vector3(0, 2, -5);//(target.transform.position - transform.position).normalized * targetedDistance;
            var targetedPosition = target.transform.position + focusVector;

            transform.position = targetedPosition;
            transform.LookAt(target.transform);
        }

    }

    private void FixedUpdate() 
    {
        Vector3 move = Vector3.zero;

        if (Input.GetKey(forwardKey))
            move += Vector3.forward * movingSpeed;
        if (Input.GetKey(backKey))
            move += Vector3.back * movingSpeed;
        if (Input.GetKey(leftKey))
            move += Vector3.left * movingSpeed;
        if (Input.GetKey(rightKey))
            move += Vector3.right * movingSpeed;
        if (Input.GetKey(upKey))
            move += Vector3.up * movingSpeed;
        if (Input.GetKey(downKey))
            move += Vector3.down * movingSpeed;

        float mouseMovementX = Input.GetAxis("Mouse X");
        float mouseMovementY = Input.GetAxis("Mouse Y");

        if (Input.GetKey(anchoredMoveKey)) 
        {
            move += Vector3.down * mouseMovementY * movingSpeed / 2;
            move += Vector3.left * mouseMovementX * movingSpeed / 2;
        }

        var rotate = transform.rotation;
        if (Input.GetKey(anchoredRotateKey))
        {
            transform.RotateAround(transform.position, Vector3.up, -mouseMovementX * rotationSpeed);
            transform.RotateAround(transform.position, transform.right, mouseMovementY * rotationSpeed);
        }
        transform.Translate(move);
    }

    private void LateUpdate() 
    {
        var scroll = Input.GetAxis("Mouse ScrollWheel");
        transform.Translate(Vector3.forward * scroll * zoomSpeed);
    }
}
