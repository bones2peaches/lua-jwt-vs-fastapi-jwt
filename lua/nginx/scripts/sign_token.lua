local M = {}

function M.write_token()
    local cjson = require "cjson"
    local jwt = require "resty.jwt"
    local validators = require "resty.jwt-validators"
    local  expiry_seconds = 120
    validators.set_system_leeway(expiry_seconds)  
    local expiry = ngx.time() + expiry_seconds 

    
    local jwt_token = jwt:sign(
        "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7", 
        {
            header={typ="JWT", alg="HS256"},
            payload={
                user_id=tostring(ngx.var.remote_user),

            }
        }
    )

    local jwt_obj = {
        ["access_token"] = jwt_token,
        ["expires"] = expiry
    }
    ngx.say(cjson.encode(jwt_obj))
end



return M
