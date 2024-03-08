def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    @env.macro
    def include_local():
        return "HERE COME THE LOCAL CONTENT"