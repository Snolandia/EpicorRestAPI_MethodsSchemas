import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.LIB.CdcSubscriberSvc
# Description: Cdc Subscriber API
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Register(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Register
   Description: Register a new subscriber for the API
   OperationID: Register
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Register_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Register_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Unregister(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Unregister
   Description: Unregister a subscriber
   OperationID: Unregister
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Unregister_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Unregister_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubscriberUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubscriberUpdate
   Description: Update a subscriber's configuration
   OperationID: SubscriberUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubscriberUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubscriberUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegenerateSecret(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegenerateSecret
   Description: Generate a new secret for a subscriber
   OperationID: RegenerateSecret
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenerateSecret_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateSecret_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleGet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleGet
   OperationID: RuleGet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleGet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleGet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleAdd
   Description: Add a rule for a specific subscriber
   OperationID: RuleAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleRemove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleRemove
   Description: Remove a rule from a specific subscriber
   OperationID: RuleRemove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleRemove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleRemove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleUpdate
   Description: Update a rule
   OperationID: RuleUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RulesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RulesList
   Description: List out all the rules for a specific subscriber
   OperationID: RulesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RulesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RuleTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RuleTableList
   Description: List tables that have been enabled for CDC and can be used for rules
   OperationID: RuleTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RuleTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RuleTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSampleData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSampleData
   Description: Generate sample data for a given table
   OperationID: GenerateSampleData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateLookupSampleData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateLookupSampleData
   Description: Generate sample data for the lookups on a given table
   OperationID: GenerateLookupSampleData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLookupSampleData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLookupSampleData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateKeyTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateKeyTags
   Description: Generate Tags based on the primary key columns
   OperationID: GenerateKeyTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateKeyTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateKeyTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupLinks
   Description: Get look up links available for a specific table
   OperationID: GetLookupLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupLinks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupLinks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLookupDataFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLookupDataFields
   Description: Get data fields for a specific look up on a table
   OperationID: GetLookupDataFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLookupDataFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLookupDataFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Pull(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Pull
   Description: Pull messages from the subscriber queue.
   OperationID: Pull
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Pull_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Pull_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.LIB.CdcSubscriberSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class GenerateKeyTags_input:
   """ Required : 
   subscriberID
   secret
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber's ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      pass

class GenerateKeyTags_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Tags  """  
      pass

class GenerateLookupSampleData_input:
   """ Required : 
   subscriberID
   secret
   schemaName
   tableName
   lookupIDs
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      self.secret:str = obj["secret"]
      """  Secret  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema name  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      self.lookupIDs:str = obj["lookupIDs"]
      """  Lookup IDs to include  """  
      pass

class GenerateLookupSampleData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Sample data for table  """  
      pass

class GenerateSampleData_input:
   """ Required : 
   subscriberID
   secret
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      self.secret:str = obj["secret"]
      """  Secret  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema name  """  
      self.tableName:str = obj["tableName"]
      """  Table name  """  
      pass

class GenerateSampleData_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Sample data for table  """  
      pass

class GetLookupDataFields_input:
   """ Required : 
   subscriberID
   secret
   schemaName
   tableName
   lookupID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber's ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      self.lookupID:str = obj["lookupID"]
      """  Lookup ID  """  
      pass

class GetLookupDataFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of lookup links  """  
      pass

class GetLookupLinks_input:
   """ Required : 
   subscriberID
   secret
   schemaName
   tableName
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber's ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema  """  
      self.tableName:str = obj["tableName"]
      """  Table  """  
      pass

class GetLookupLinks_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  List of lookup links  """  
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

class Ice_Lib_CdcSubscriber_PullResponse:
   def __init__(self, obj):
      self.results:list[Ice_Lib_CdcSubscriber_SubscriberQueue] = obj["results"]
      self.morePages:bool = obj["morePages"]
      self.lastOffset:int = obj["lastOffset"]
      pass

class Ice_Lib_CdcSubscriber_SubscriberQueue:
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.schemaName:str = obj["schemaName"]
      self.tableName:str = obj["tableName"]
      self.keys:str = obj["keys"]
      self.ruleID:str = obj["ruleID"]
      self.data:str = obj["data"]
      self.metadata:str = obj["metadata"]
      self.occurredWhenUtc:str = obj["occurredWhenUtc"]
      pass

class Ice_Tablesets_CdcSubscriberRuleRow:
   def __init__(self, obj):
      self.SubscriberID:str = obj["SubscriberID"]
      self.RuleID:str = obj["RuleID"]
      self.SchemaName:str = obj["SchemaName"]
      self.TableName:str = obj["TableName"]
      self.ChangeType:str = obj["ChangeType"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.Inactive:bool = obj["Inactive"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.LastUpdatedBy:str = obj["LastUpdatedBy"]
      self.Description:str = obj["Description"]
      self.Company:str = obj["Company"]
      self.SecCode:str = obj["SecCode"]
      """  Security Code  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CdcSubscriberRuleTableset:
   def __init__(self, obj):
      self.CdcSubscriberRule:list[Ice_Tablesets_CdcSubscriberRuleRow] = obj["CdcSubscriberRule"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Pull_input:
   """ Required : 
   subscriberID
   secret
   offset
   pageSize
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.offset:int = obj["offset"]
      """  Offset to start from, when 0 is supplied will read from end of last offset read up to  """  
      self.pageSize:int = obj["pageSize"]
      """  Max amount of messages to return  """  
      pass

class Pull_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Lib_CdcSubscriber_PullResponse] = obj["returnObj"]
      pass

class RegenerateSecret_input:
   """ Required : 
   subscriberID
   oldSecret
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.oldSecret:str = obj["oldSecret"]
      """  Old secret  """  
      pass

class RegenerateSecret_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newSecret:str = obj["parameters"]
      pass

      """  output parameters  """  

class Register_input:
   """ Required : 
   description
   mode
   webHookURI
   webHookHeaders
   """  
   def __init__(self, obj):
      self.description:str = obj["description"]
      """  Description of Subscriber  """  
      self.mode:str = obj["mode"]
      """  Subscriber Mode - "PUSH", "PUSHPULL" or "PULL"  """  
      self.webHookURI:str = obj["webHookURI"]
      """  Web Hook URI for Push or Push-Pull  """  
      self.webHookHeaders:str = obj["webHookHeaders"]
      """  Web Hook Headers, only valid for Push or Push-Pull  """  
      pass

class Register_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.subscriberID:str = obj["parameters"]
      self.secret:str = obj["parameters"]
      pass

      """  output parameters  """  

class RuleAdd_input:
   """ Required : 
   subscriberID
   secret
   companyID
   ruleID
   description
   schemaName
   tableName
   changeType
   rule
   metadataRule
   lookupLinks
   inactive
   secCode
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.companyID:str = obj["companyID"]
      """  Company the rule is assigned to  """  
      self.ruleID:str = obj["ruleID"]
      """  Rule ID  """  
      self.description:str = obj["description"]
      """  Description of rule  """  
      self.schemaName:str = obj["schemaName"]
      """  Schema rule applies to  """  
      self.tableName:str = obj["tableName"]
      """  Table rule applies to  """  
      self.changeType:str = obj["changeType"]
      """  Change type rule applies to, valid options are insert, update and delete  """  
      self.rule:str = obj["rule"]
      """  Rule JSON logic  """  
      self.metadataRule:str = obj["metadataRule"]
      """  Metadata JSON logic output  """  
      self.lookupLinks:str = obj["lookupLinks"]
      """  Look up links  """  
      self.inactive:bool = obj["inactive"]
      """  Whether rule is currently active  """  
      self.secCode:str = obj["secCode"]
      """  Security code assigned to rule  """  
      pass

class RuleAdd_output:
   def __init__(self, obj):
      pass

class RuleGet_input:
   """ Required : 
   subscriberID
   secret
   companyID
   ruleID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      self.secret:str = obj["secret"]
      self.companyID:str = obj["companyID"]
      self.ruleID:str = obj["ruleID"]
      pass

class RuleGet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.description:str = obj["parameters"]
      self.schemaName:str = obj["parameters"]
      self.tableName:str = obj["parameters"]
      self.changeType:str = obj["parameters"]
      self.rule:str = obj["parameters"]
      self.metadataRule:str = obj["parameters"]
      self.lookupLinks:str = obj["parameters"]
      self.systemFlag:bool = obj["systemFlag"]
      self.inactive:bool = obj["inactive"]
      self.lastUpdated:str = obj["parameters"]
      self.lastUpdatedBy:str = obj["parameters"]
      self.secCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class RuleRemove_input:
   """ Required : 
   subscriberID
   secret
   companyID
   ruleID
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.companyID:str = obj["companyID"]
      """  Company the rule is assigned to  """  
      self.ruleID:str = obj["ruleID"]
      """  Rule ID  """  
      pass

class RuleRemove_output:
   def __init__(self, obj):
      pass

class RuleTableList_input:
   """ Required : 
   subscriberID
   secret
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Secret  """  
      pass

class RuleTableList_output:
   def __init__(self, obj):
      self.returnObj:array
      """  List of available tables  """  
      pass

class RuleUpdate_input:
   """ Required : 
   subscriberID
   secret
   companyID
   ruleID
   description
   changeType
   rule
   metadataRule
   lookupLinks
   inactive
   secCode
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.companyID:str = obj["companyID"]
      """  Company the rule is assigned to  """  
      self.ruleID:str = obj["ruleID"]
      """  ID of rule being updated  """  
      self.description:str = obj["description"]
      """  Description of rule  """  
      self.changeType:str = obj["changeType"]
      """  Change types rule applies to, valid options are insert, update and delete  """  
      self.rule:str = obj["rule"]
      """  Rule JSON logic, passing null will ignore column from updating  """  
      self.metadataRule:str = obj["metadataRule"]
      """  Metadata JSON logic output  """  
      self.lookupLinks:str = obj["lookupLinks"]
      """  Look up links  """  
      self.inactive:bool = obj["inactive"]
      """  Set the rule to active/inactive  """  
      self.secCode:str = obj["secCode"]
      """  Security code assigned to rule  """  
      pass

class RuleUpdate_output:
   def __init__(self, obj):
      pass

class RulesList_input:
   """ Required : 
   subscriberID
   secret
   companyID
   description
   schemaName
   tableName
   excludeSystem
   skip
   pageSize
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.companyID:str = obj["companyID"]
      """  Company, blank to list all available companies  """  
      self.description:str = obj["description"]
      """  Contains description  """  
      self.schemaName:str = obj["schemaName"]
      """  Filter to specific schema  """  
      self.tableName:str = obj["tableName"]
      """  Filter to specific table  """  
      self.excludeSystem:bool = obj["excludeSystem"]
      """  Exclude System rules  """  
      self.skip:int = obj["skip"]
      """  Skip n results  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size, maximum 200  """  
      pass

class RulesList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CdcSubscriberRuleTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pageSize:int = obj["parameters"]
      self.morePages:bool = obj["morePages"]
      self.total:int = obj["parameters"]
      pass

      """  output parameters  """  

class SubscriberUpdate_input:
   """ Required : 
   subscriberID
   secret
   description
   inactive
   webHookURI
   webHookHeaders
   pageSize
   TTLRead
   TTLUnread
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      self.description:str = obj["description"]
      """  New description  """  
      self.inactive:bool = obj["inactive"]
      """  Set subscriber to inactive  """  
      self.webHookURI:str = obj["webHookURI"]
      """  Web Hook URI, only valid for Push or Push-Pull  """  
      self.webHookHeaders:str = obj["webHookHeaders"]
      """  Web Hook Headers, only valid for Push or Push-Pull  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size for messages are pushed/pulled  """  
      self.TTLRead:int = obj["TTLRead"]
      """  How long to keep read messages, in seconds  """  
      self.TTLUnread:int = obj["TTLUnread"]
      """  How long to keep unread messages, in seconds  """  
      pass

class SubscriberUpdate_output:
   def __init__(self, obj):
      pass

class Unregister_input:
   """ Required : 
   subscriberID
   secret
   """  
   def __init__(self, obj):
      self.subscriberID:str = obj["subscriberID"]
      """  Subscriber ID  """  
      self.secret:str = obj["secret"]
      """  Subscriber's secret  """  
      pass

class Unregister_output:
   def __init__(self, obj):
      pass

