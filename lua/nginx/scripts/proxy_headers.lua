local M = {}

function M.check_auth()
    local auth_header = ngx.req.get_headers()["Authorization"]
    local cjson = require "cjson"
    local jwt = require "resty.jwt"



    if auth_header == nil then
        ngx.status = ngx.HTTP_UNAUTHORIZED
        ngx.header.content_type = "application/json; charset=utf-8"
        ngx.say("{\"error\": \"missing JWT token or Authorization header\"}")
        ngx.exit(ngx.HTTP_UNAUTHORIZED)        

    end
    
    local token = string.match(auth_header, "Bearer%s+(%S+)")


    local jwt_obj = jwt:verify("09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7", token)   

    if not jwt_obj["verified"] then
        ngx.status = ngx.HTTP_UNAUTHORIZED
        ngx.log(ngx.WARN, jwt_obj.reason)
        ngx.header.content_type = "application/json; charset=utf-8"
        ngx.say("{\"error\": \"" .. jwt_obj.reason .. "\"}")
        ngx.exit(ngx.HTTP_UNAUTHORIZED)
    end

    local location_id = jwt_obj.payload.user_id
    if location_id then
        ngx.req.set_header("X-USER-ID", tostring(location_id))
        ngx.req.clear_header("Authorization")
    end
end


return M
