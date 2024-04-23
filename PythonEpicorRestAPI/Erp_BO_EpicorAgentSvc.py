import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EpicorAgentSvc
# Description: Epicor Virtual Assistant main object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ProcessSkill(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessSkill
   Description: Invoked by Epicor Agent framework to cause a selected skill to be fully processed.
Has the potential of making state changes (alter database state)
   OperationID: ProcessSkill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessSkill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessSkill_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSkillVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSkillVersion
   Description: Gets the API version with which a given skill is registered.
This returns the first api version for a given skill that is found.
   OperationID: GetSkillVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSkillVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSkillVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateEntity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateEntity
   Description: Performs validation of user-supplied (typically) parameters/entities for a given skill
   OperationID: ValidateEntity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkillSupported(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkillSupported
   Description: Verify if requested skill is supported by this platform
   OperationID: SkillSupported
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkillSupported_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkillSupported_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSupportedSkills(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSupportedSkills
   Description: Return the list of skills supported for the specified api version
   OperationID: GetSupportedSkills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSupportedSkills_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSupportedSkills_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProviderId(epicorHeaders = None):
   """  
   Summary: Invoke method GetProviderId
   Description: Return unique identifier for this system previously set by <seealso cref="M:Erp.Services.BO.EpicorAgentSvc.SetProviderId(System.String)" />
   OperationID: GetProviderId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProviderId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_SetProviderId(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetProviderId
   Description: Persist unique identifier assigned to this system by Epicor Agent framework
   OperationID: SetProviderId
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetProviderId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetProviderId_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EpicorAgentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AssistantDataModel_AssistantAttachment:
   def __init__(self, obj):
      self.ContentType:str = obj["ContentType"]
      self.Content      #schema had no properties on an object.
      self.ContentUrl:str = obj["ContentUrl"]
      self.ContentId:str = obj["ContentId"]
      self.Name:str = obj["Name"]
      self.ThumbnailUrl:str = obj["ThumbnailUrl"]
      self.TokenDictionary      #schema had no properties on an object.
      pass

class AssistantDataModel_AssistantChoice:
   def __init__(self, obj):
      self.Description:str = obj["Description"]
      self.PlatformObject      #schema had no properties on an object.
      self.Synonyms:str = obj["Synonyms"]
      self.SecondaryContextId:str = obj["SecondaryContextId"]
      pass

class AssistantDataModel_AssistantDialogState:
   def __init__(self, obj):
      self.IntentId:str = obj["IntentId"]
      self.Entities      #schema had no properties on an object.
      self.CurrentEntityIndex:int = obj["CurrentEntityIndex"]
      pass

class AssistantDataModel_AssistantEntity:
   def __init__(self, obj):
      self.UserInput:str = obj["UserInput"]
      self.Description:str = obj["Description"]
      self.PlatformObject      #schema had no properties on an object.
      self.SecondaryContextId:str = obj["SecondaryContextId"]
      self.IsValid:bool = obj["IsValid"]
      self.EntityDefinition:list[AssistantDataModel_AssistantEntityDefinition] = obj["EntityDefinition"]
      pass

class AssistantDataModel_AssistantEntityDefinition:
   def __init__(self, obj):
      self.EntityId:str = obj["EntityId"]
      self.IsUserInput:bool = obj["IsUserInput"]
      self.IsSavedToContext:bool = obj["IsSavedToContext"]
      self.IsInformational:bool = obj["IsInformational"]
      self.RequiresSecondaryContext:bool = obj["RequiresSecondaryContext"]
      pass

class AssistantDataModel_AssistantProcessRequest:
   def __init__(self, obj):
      self.UserId:str = obj["UserId"]
      self.PlatformUrl:str = obj["PlatformUrl"]
      self.Token:str = obj["Token"]
      self.Locale:str = obj["Locale"]
      self.State:list[AssistantDataModel_AssistantDialogState] = obj["State"]
      pass

class AssistantDataModel_AssistantResponse:
   def __init__(self, obj):
      self.State:list[AssistantDataModel_AssistantDialogState] = obj["State"]
      self.IsValid:bool = obj["IsValid"]
      self.ResponseToUser:str = obj["ResponseToUser"]
      self.Choices:list[AssistantDataModel_AssistantChoice] = obj["Choices"]
      self.Attachment:list[AssistantDataModel_AssistantAttachment] = obj["Attachment"]
      pass

class AssistantDataModel_AssistantValidationRequest:
   def __init__(self, obj):
      self.UserId:str = obj["UserId"]
      self.PlatformUrl:str = obj["PlatformUrl"]
      self.Token:str = obj["Token"]
      self.Locale:str = obj["Locale"]
      self.EntityId:str = obj["EntityId"]
      self.ValueToValidate:str = obj["ValueToValidate"]
      self.State:list[AssistantDataModel_AssistantDialogState] = obj["State"]
      pass

class GetProviderId_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  String identifier of this platform for use of Agent framework  """  
      pass

class GetSkillVersion_input:
   """ Required : 
   skillIntentId
   """  
   def __init__(self, obj):
      self.skillIntentId:str = obj["skillIntentId"]
      """  Agent skill identifier  """  
      pass

class GetSkillVersion_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSupportedSkills_input:
   """ Required : 
   apiVersion
   """  
   def __init__(self, obj):
      self.apiVersion:str = obj["apiVersion"]
      """  Api version to permit coexistence of different iterations of skills  """  
      pass

class GetSupportedSkills_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ProcessSkill_input:
   """ Required : 
   skillIntentId
   request
   apiVersion
   """  
   def __init__(self, obj):
      self.skillIntentId:str = obj["skillIntentId"]
      """  Agent skill to invoke  """  
      self.request:list[AssistantDataModel_AssistantProcessRequest] = obj["request"]
      self.apiVersion:str = obj["apiVersion"]
      """  Api version to permit coexistence of different iterations of skills  """  
      pass

class ProcessSkill_output:
   def __init__(self, obj):
      self.returnObj:list[AssistantDataModel_AssistantResponse] = obj["returnObj"]
      pass

class SetProviderId_input:
   """ Required : 
   providerId
   """  
   def __init__(self, obj):
      self.providerId:str = obj["providerId"]
      """  Unique identifier for this system  """  
      pass

class SetProviderId_output:
   def __init__(self, obj):
      pass

class SkillSupported_input:
   """ Required : 
   skillIntentId
   apiVersion
   """  
   def __init__(self, obj):
      self.skillIntentId:str = obj["skillIntentId"]
      """  Epicor agent skill identifier  """  
      self.apiVersion:str = obj["apiVersion"]
      """  Api version to permit coexistence of different iterations of skills  """  
      pass

class SkillSupported_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateEntity_input:
   """ Required : 
   skillIntentId
   request
   apiVersion
   """  
   def __init__(self, obj):
      self.skillIntentId:str = obj["skillIntentId"]
      """  Agent skill identifier  """  
      self.request:list[AssistantDataModel_AssistantValidationRequest] = obj["request"]
      self.apiVersion:str = obj["apiVersion"]
      """  Api version to permit coexistence of different iterations of skills  """  
      pass

class ValidateEntity_output:
   def __init__(self, obj):
      self.returnObj:list[AssistantDataModel_AssistantResponse] = obj["returnObj"]
      pass

