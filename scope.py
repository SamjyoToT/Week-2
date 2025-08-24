global_var = "global"

def modify_global_var():
    global global_var
    local_var = "local-var"
    print(global_var, local_var)
    global_var = "modified-global"
    print(global_var, local_var)

modify_global_var()
