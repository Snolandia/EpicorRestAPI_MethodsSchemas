import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.TokenServiceSvc
# Description: Generates tokens for token authentication
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetAccessToken(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAccessToken
   Description: Receive Access Token for currently logged in user and default client
   OperationID: GetAccessToken
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAccessToken_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAccessToken_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsTokenAuthenticationEnabled(epicorHeaders = None):
   """  
   Summary: Invoke method IsTokenAuthenticationEnabled
   Description: Checks if Token Authentication is enabled in web.config
   OperationID: IsTokenAuthenticationEnabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTokenAuthenticationEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_IsTokenValid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsTokenValid
   Description: Checks if given token is valid
   OperationID: IsTokenValid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsTokenValid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsTokenValid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AdminGetTokenConfig(epicorHeaders = None):
   """  
   Summary: Invoke method AdminGetTokenConfig
   Description: Returns current settings for token authentication, available for security manager
   OperationID: AdminGetTokenConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminGetTokenConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_AdminSetTokenConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AdminSetTokenConfig
   Description: Configure token resource
   OperationID: AdminSetTokenConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AdminSetTokenConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminSetTokenConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AdminSetIdentityProvider(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AdminSetIdentityProvider
   Description: Set Identity provider connection
   OperationID: AdminSetIdentityProvider
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AdminSetIdentityProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminSetIdentityProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AdminSetScimProvider(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AdminSetScimProvider
   Description: Setup Scim endpoint for Identity provider
   OperationID: AdminSetScimProvider
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AdminSetScimProvider_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AdminSetScimProvider_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.TokenServiceSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AdminGetTokenConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.tokenEnabled:bool = obj["tokenEnabled"]
      self.signKey:str = obj["parameters"]
      self.lifeTime:int = obj["parameters"]
      self.refreshTokenEnabled:bool = obj["refreshTokenEnabled"]
      self.refreshTokenLifeTime:int = obj["parameters"]
      pass

      """  output parameters  """  

class AdminSetIdentityProvider_input:
   """ Required : 
   enable
   endpoint
   scope
   webClientID
   nativeClientID
   """  
   def __init__(self, obj):
      self.enable:bool = obj["enable"]
      """  Enable or disable usage of identity provider in current App Server installation  """  
      self.endpoint:str = obj["endpoint"]
      """  URL where Identity provider is installed  """  
      self.scope:str = obj["scope"]
      """  Scope used in tokens  """  
      self.webClientID:str = obj["webClientID"]
      """  Client ID for the Web applications  """  
      self.nativeClientID:str = obj["nativeClientID"]
      """  Client ID for the native applications  """  
      pass

class AdminSetIdentityProvider_output:
   def __init__(self, obj):
      pass

class AdminSetScimProvider_input:
   """ Required : 
   enable
   clientId
   clientSecret
   scope
   """  
   def __init__(self, obj):
      self.enable:bool = obj["enable"]
      """  Enable or disable authomatic user export  """  
      self.clientId:str = obj["clientId"]
      """  Client ID used for SCIM export  """  
      self.clientSecret:str = obj["clientSecret"]
      """  Client secret used for SCIM export  """  
      self.scope:str = obj["scope"]
      """  Scope used for SCIM export  """  
      pass

class AdminSetScimProvider_output:
   def __init__(self, obj):
      pass

class AdminSetTokenConfig_input:
   """ Required : 
   tokenEnabled
   signKey
   lifeTime
   refreshTokenEnabled
   refreshTokenLifeTime
   """  
   def __init__(self, obj):
      self.tokenEnabled:bool = obj["tokenEnabled"]
      """  Token authentication is enabled  """  
      self.signKey:str = obj["signKey"]
      """  Token signature key  """  
      self.lifeTime:int = obj["lifeTime"]
      """  token lifetime in seconds  """  
      self.refreshTokenEnabled:bool = obj["refreshTokenEnabled"]
      """  Refresh token. Not implemented  """  
      self.refreshTokenLifeTime:int = obj["refreshTokenLifeTime"]
      """  Refresh token life time. Not implemented  """  
      pass

class AdminSetTokenConfig_output:
   def __init__(self, obj):
      pass

class GetAccessToken_input:
   """ Required : 
   clientId
   clientSecret
   scope
   """  
   def __init__(self, obj):
      self.clientId:str = obj["clientId"]
      self.clientSecret:str = obj["clientSecret"]
      self.scope:str = obj["scope"]
      pass

class GetAccessToken_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_TokenServiceTableset] = obj["returnObj"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Ice_Tablesets_TokenServiceRow:
   def __init__(self, obj):
      self.AccessToken:str = obj["AccessToken"]
      """  Aceess Token to use in Authentication  """  
      self.ExpiresIn:int = obj["ExpiresIn"]
      """  Seconds to token expiration  """  
      self.RefreshToken:str = obj["RefreshToken"]
      """  Refresh token to get new access token when current is expired  """  
      self.TokenType:str = obj["TokenType"]
      """  Type of token - now is always Bearer  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_TokenServiceTableset:
   def __init__(self, obj):
      self.TokenService:list[Ice_Tablesets_TokenServiceRow] = obj["TokenService"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class IsTokenAuthenticationEnabled_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if token authentication is enabled  """  
      pass

class IsTokenValid_input:
   """ Required : 
   token
   userId
   """  
   def __init__(self, obj):
      self.token:str = obj["token"]
      """  serialized token  """  
      self.userId:str = obj["userId"]
      """  if specified, checks that token is valid and was issued for this user. If empty - just checks that token is valid  """  
      pass

class IsTokenValid_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if token is valid for current user  """  
      pass

   def parameters(self, obj):
      self.validTillUtc:str = obj["parameters"]
      pass

      """  output parameters  """  

