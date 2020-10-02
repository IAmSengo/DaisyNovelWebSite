API Doc
==

# Operation
## 获取邀请码
* URL `op/gen_invitation_code` 
* Method: GET 

## 使用邀请码 
* URL `op/redeem_invitation_code` 
* Method: POST 
* Body:  
    * invitation_code
    * user_name (length < 8)
    * invitation_code 
    * password
    * email
 
    
    
 