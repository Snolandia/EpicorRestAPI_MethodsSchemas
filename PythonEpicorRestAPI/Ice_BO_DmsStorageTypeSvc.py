import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.DmsStorageTypeSvc
# Description: The DmsStorageType service used by attachments.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DmsStorageTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DmsStorageTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DmsStorageTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DmsStorageTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/DmsStorageTypes",headers=creds) as resp:
           return await resp.json()

async def post_DmsStorageTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DmsStorageTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.DmsStorageTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.DmsStorageTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/DmsStorageTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DmsStorageTypes_Company_StorageType(Company, StorageType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DmsStorageType item
   Description: Calls GetByID to retrieve the DmsStorageType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DmsStorageType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param StorageType: Desc: StorageType   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.DmsStorageTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/DmsStorageTypes(" + Company + "," + StorageType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DmsStorageTypes_Company_StorageType(Company, StorageType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DmsStorageType for the service
   Description: Calls UpdateExt to update DmsStorageType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DmsStorageType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param StorageType: Desc: StorageType   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.DmsStorageTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/DmsStorageTypes(" + Company + "," + StorageType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DmsStorageTypes_Company_StorageType(Company, StorageType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DmsStorageType item
   Description: Call UpdateExt to delete DmsStorageType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DmsStorageType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param StorageType: Desc: StorageType   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/DmsStorageTypes(" + Company + "," + StorageType + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DmsStorageTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDmsStorageType, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDmsStorageType=" + whereClauseDmsStorageType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(storageType, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "storageType=" + storageType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_TestConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestConnection
   Description: Allows you to test the connection to the storage type.
   OperationID: TestConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEnableStorageType(epicorHeaders = None):
   """  
   Summary: Invoke method GetEnableStorageType
   Description: Gets the enabled storage types.
   OperationID: GetEnableStorageType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnableStorageType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultCompanyStorage(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultCompanyStorage
   Description: Gets the default storagetype for the current company.
   OperationID: GetDefaultCompanyStorage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultCompanyStorage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewDmsStorageType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDmsStorageType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDmsStorageType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDmsStorageType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDmsStorageType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.DmsStorageTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DmsStorageTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DmsStorageTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DmsStorageTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_DmsStorageTypeRow] = obj["value"]
      pass

class Ice_Tablesets_DmsStorageTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.StorageType:int = obj["StorageType"]
      """  StorageType  """  
      self.StorageTypeEnabled:bool = obj["StorageTypeEnabled"]
      """  StorageTypeEnabled  """  
      self.BaseURI:str = obj["BaseURI"]
      """  BaseURI  """  
      self.CompanyDefaultStorage:bool = obj["CompanyDefaultStorage"]
      """  CompanyDefaultStorage  """  
      self.CanViewInProvider:bool = obj["CanViewInProvider"]
      """  CanViewInProvider  """  
      self.ApplicationName:str = obj["ApplicationName"]
      """  ApplicationName  """  
      self.AppKey:str = obj["AppKey"]
      """  AppKey  """  
      self.CredentialToken:str = obj["CredentialToken"]
      """  CredentialToken  """  
      self.UserName:str = obj["UserName"]
      """  UserName  """  
      self.UserPwd:str = obj["UserPwd"]
      """  UserPwd  """  
      self.Domain:str = obj["Domain"]
      """  Domain  """  
      self.AuthType:str = obj["AuthType"]
      """  AuthType  """  
      self.TransferType:str = obj["TransferType"]
      """  TransferType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.CertificateThumbPrint:str = obj["CertificateThumbPrint"]
      """  CertificateThumbPrint  """  
      self.AuthorityEndpoint:str = obj["AuthorityEndpoint"]
      """  AuthorityEndpoint  """  
      self.DuplicateAttachmentMode:str = obj["DuplicateAttachmentMode"]
      """  DuplicateAttachmentMode  """  
      self.StorageTypeDesc:str = obj["StorageTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DmsStorageTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.StorageType:int = obj["StorageType"]
      """  StorageType  """  
      self.StorageTypeEnabled:bool = obj["StorageTypeEnabled"]
      """  StorageTypeEnabled  """  
      self.BaseURI:str = obj["BaseURI"]
      """  BaseURI  """  
      self.CompanyDefaultStorage:bool = obj["CompanyDefaultStorage"]
      """  CompanyDefaultStorage  """  
      self.CanViewInProvider:bool = obj["CanViewInProvider"]
      """  CanViewInProvider  """  
      self.ApplicationName:str = obj["ApplicationName"]
      """  ApplicationName  """  
      self.AppKey:str = obj["AppKey"]
      """  AppKey  """  
      self.CredentialToken:str = obj["CredentialToken"]
      """  CredentialToken  """  
      self.UserName:str = obj["UserName"]
      """  UserName  """  
      self.UserPwd:str = obj["UserPwd"]
      """  UserPwd  """  
      self.Domain:str = obj["Domain"]
      """  Domain  """  
      self.AuthType:str = obj["AuthType"]
      """  AuthType  """  
      self.TransferType:str = obj["TransferType"]
      """  TransferType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.CertificateThumbPrint:str = obj["CertificateThumbPrint"]
      """  CertificateThumbPrint  """  
      self.AuthorityEndpoint:str = obj["AuthorityEndpoint"]
      """  AuthorityEndpoint  """  
      self.DuplicateAttachmentMode:str = obj["DuplicateAttachmentMode"]
      """  DuplicateAttachmentMode  """  
      self.StorageTypeDesc:str = obj["StorageTypeDesc"]
      """  Storage Type Description  """  
      self.TempUserPwd:str = obj["TempUserPwd"]
      """  User Password  """  
      self.StorageTypeCodeDesc:str = obj["StorageTypeCodeDesc"]
      self.UseDefaultEndpoint:bool = obj["UseDefaultEndpoint"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   storageType
   """  
   def __init__(self, obj):
      self.storageType:int = obj["storageType"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   storageType
   """  
   def __init__(self, obj):
      self.storageType:int = obj["storageType"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["returnObj"]
      pass

class GetDefaultCompanyStorage_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      """  An int representing the default storage type. Possible values are -
            SharePoint = 1,
            FileSystem = 2,
            Link = 3,
            DocStar = 5,
            Dropbox = 6,
            GoogleDrive = 7  """  
      pass

class GetEnableStorageType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  A list of enabled storage types.  """  
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DmsStorageTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDmsStorageType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["ds"]
      pass

class GetNewDmsStorageType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDmsStorageType
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDmsStorageType:str = obj["whereClauseDmsStorageType"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Ice_Tablesets_DmsStorageTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.StorageType:int = obj["StorageType"]
      """  StorageType  """  
      self.StorageTypeEnabled:bool = obj["StorageTypeEnabled"]
      """  StorageTypeEnabled  """  
      self.BaseURI:str = obj["BaseURI"]
      """  BaseURI  """  
      self.CompanyDefaultStorage:bool = obj["CompanyDefaultStorage"]
      """  CompanyDefaultStorage  """  
      self.CanViewInProvider:bool = obj["CanViewInProvider"]
      """  CanViewInProvider  """  
      self.ApplicationName:str = obj["ApplicationName"]
      """  ApplicationName  """  
      self.AppKey:str = obj["AppKey"]
      """  AppKey  """  
      self.CredentialToken:str = obj["CredentialToken"]
      """  CredentialToken  """  
      self.UserName:str = obj["UserName"]
      """  UserName  """  
      self.UserPwd:str = obj["UserPwd"]
      """  UserPwd  """  
      self.Domain:str = obj["Domain"]
      """  Domain  """  
      self.AuthType:str = obj["AuthType"]
      """  AuthType  """  
      self.TransferType:str = obj["TransferType"]
      """  TransferType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.CertificateThumbPrint:str = obj["CertificateThumbPrint"]
      """  CertificateThumbPrint  """  
      self.AuthorityEndpoint:str = obj["AuthorityEndpoint"]
      """  AuthorityEndpoint  """  
      self.DuplicateAttachmentMode:str = obj["DuplicateAttachmentMode"]
      """  DuplicateAttachmentMode  """  
      self.StorageTypeDesc:str = obj["StorageTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DmsStorageTypeListTableset:
   def __init__(self, obj):
      self.DmsStorageTypeList:list[Ice_Tablesets_DmsStorageTypeListRow] = obj["DmsStorageTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_DmsStorageTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.StorageType:int = obj["StorageType"]
      """  StorageType  """  
      self.StorageTypeEnabled:bool = obj["StorageTypeEnabled"]
      """  StorageTypeEnabled  """  
      self.BaseURI:str = obj["BaseURI"]
      """  BaseURI  """  
      self.CompanyDefaultStorage:bool = obj["CompanyDefaultStorage"]
      """  CompanyDefaultStorage  """  
      self.CanViewInProvider:bool = obj["CanViewInProvider"]
      """  CanViewInProvider  """  
      self.ApplicationName:str = obj["ApplicationName"]
      """  ApplicationName  """  
      self.AppKey:str = obj["AppKey"]
      """  AppKey  """  
      self.CredentialToken:str = obj["CredentialToken"]
      """  CredentialToken  """  
      self.UserName:str = obj["UserName"]
      """  UserName  """  
      self.UserPwd:str = obj["UserPwd"]
      """  UserPwd  """  
      self.Domain:str = obj["Domain"]
      """  Domain  """  
      self.AuthType:str = obj["AuthType"]
      """  AuthType  """  
      self.TransferType:str = obj["TransferType"]
      """  TransferType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DirectoryID:str = obj["DirectoryID"]
      """  DirectoryID  """  
      self.ApplicationID:str = obj["ApplicationID"]
      """  ApplicationID  """  
      self.CertificateThumbPrint:str = obj["CertificateThumbPrint"]
      """  CertificateThumbPrint  """  
      self.AuthorityEndpoint:str = obj["AuthorityEndpoint"]
      """  AuthorityEndpoint  """  
      self.DuplicateAttachmentMode:str = obj["DuplicateAttachmentMode"]
      """  DuplicateAttachmentMode  """  
      self.StorageTypeDesc:str = obj["StorageTypeDesc"]
      """  Storage Type Description  """  
      self.TempUserPwd:str = obj["TempUserPwd"]
      """  User Password  """  
      self.StorageTypeCodeDesc:str = obj["StorageTypeCodeDesc"]
      self.UseDefaultEndpoint:bool = obj["UseDefaultEndpoint"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DmsStorageTypeTableset:
   def __init__(self, obj):
      self.DmsStorageType:list[Ice_Tablesets_DmsStorageTypeRow] = obj["DmsStorageType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtDmsStorageTypeTableset:
   def __init__(self, obj):
      self.DmsStorageType:list[Ice_Tablesets_DmsStorageTypeRow] = obj["DmsStorageType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class TestConnection_input:
   """ Required : 
   ds
   storageType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["ds"]
      self.storageType:int = obj["storageType"]
      """  Only supports SharePoint, ECM and Google Drive.  """  
      pass

class TestConnection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDmsStorageTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtDmsStorageTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_DmsStorageTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

