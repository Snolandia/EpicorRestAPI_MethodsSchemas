import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.XAttachMetaDataSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_XAttachMetaDatas(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get XAttachMetaDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_XAttachMetaDatas
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XAttachMetaDataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/XAttachMetaDatas",headers=creds) as resp:
           return await resp.json()

async def post_XAttachMetaDatas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_XAttachMetaDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.XAttachMetaDataRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.XAttachMetaDataRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/XAttachMetaDatas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_XAttachMetaDatas_Company_TableName_DocTypeID_PropertyName(Company, TableName, DocTypeID, PropertyName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the XAttachMetaData item
   Description: Calls GetByID to retrieve the XAttachMetaData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XAttachMetaData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
      :param PropertyName: Desc: PropertyName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.XAttachMetaDataRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/XAttachMetaDatas(" + Company + "," + TableName + "," + DocTypeID + "," + PropertyName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_XAttachMetaDatas_Company_TableName_DocTypeID_PropertyName(Company, TableName, DocTypeID, PropertyName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update XAttachMetaData for the service
   Description: Calls UpdateExt to update XAttachMetaData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_XAttachMetaData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
      :param PropertyName: Desc: PropertyName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.XAttachMetaDataRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/XAttachMetaDatas(" + Company + "," + TableName + "," + DocTypeID + "," + PropertyName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_XAttachMetaDatas_Company_TableName_DocTypeID_PropertyName(Company, TableName, DocTypeID, PropertyName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete XAttachMetaData item
   Description: Call UpdateExt to delete XAttachMetaData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_XAttachMetaData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TableName: Desc: TableName   Required: True   Allow empty value : True
      :param DocTypeID: Desc: DocTypeID   Required: True   Allow empty value : True
      :param PropertyName: Desc: PropertyName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/XAttachMetaDatas(" + Company + "," + TableName + "," + DocTypeID + "," + PropertyName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.XAttachMetaDataListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseXAttachMetaData, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseXAttachMetaData=" + whereClauseXAttachMetaData
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tableName, docTypeID, propertyName, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "tableName=" + tableName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "docTypeID=" + docTypeID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "propertyName=" + propertyName

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddFieldToContentType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddFieldToContentType
   Description: Add field to SharePoint content folder
   OperationID: AddFieldToContentType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddFieldToContentType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddFieldToContentType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateCustomFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateCustomFields
   Description: Create custom fields in DocStar library
   OperationID: CreateCustomFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCustomFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCustomFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewXAttachMetaData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewXAttachMetaData
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXAttachMetaData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewXAttachMetaData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXAttachMetaData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.XAttachMetaDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XAttachMetaDataListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_XAttachMetaDataListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_XAttachMetaDataRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_XAttachMetaDataRow] = obj["value"]
      pass

class Ice_Tablesets_XAttachMetaDataListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """   Unique identifier of a DocType. Assigned by the user.
Cannot be blank.  """  
      self.PropertyName:str = obj["PropertyName"]
      """  Name of meta data property within external document type system  """  
      self.PropertyDesc:str = obj["PropertyDesc"]
      """  General description of meta data property.  """  
      self.Mapping:str = obj["Mapping"]
      """  Column mapping information  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Determines whether this metadata is mandatory.  """  
      self.AllowOverride:bool = obj["AllowOverride"]
      """  Determines whether the user can manually enter or change the calculated meta data field.  """  
      self.SPColumnID:str = obj["SPColumnID"]
      """  Share Point Column ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XAttachMetaDataRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """   Unique identifier of a DocType. Assigned by the user.
Cannot be blank.  """  
      self.PropertyName:str = obj["PropertyName"]
      """  Name of meta data property within external document type system  """  
      self.PropertyDesc:str = obj["PropertyDesc"]
      """  General description of meta data property.  """  
      self.Mapping:str = obj["Mapping"]
      """  Column mapping information  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Determines whether this metadata is mandatory.  """  
      self.AllowOverride:bool = obj["AllowOverride"]
      """  Determines whether the user can manually enter or change the calculated meta data field.  """  
      self.SPColumnID:str = obj["SPColumnID"]
      """  Share Point Column ID  """  
      self.PropertyValue:str = obj["PropertyValue"]
      """  PropertyValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrentValue:str = obj["CurrentValue"]
      """  Holds the current metadata value.  This is not stored on the Epicor database, instead it is used to decorate the SharePoint column value for the attachment record.  """  
      self.Storage:str = obj["Storage"]
      self.StorageType:int = obj["StorageType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddFieldToContentType_input:
   """ Required : 
   tableName
   contentTypeName
   columnName
   displayName
   dataType
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.contentTypeName:str = obj["contentTypeName"]
      self.columnName:str = obj["columnName"]
      self.displayName:str = obj["displayName"]
      self.dataType:str = obj["dataType"]
      pass

class AddFieldToContentType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class CreateCustomFields_input:
   """ Required : 
   docTypeID
   customFieldName
   """  
   def __init__(self, obj):
      self.docTypeID:str = obj["docTypeID"]
      self.customFieldName:str = obj["customFieldName"]
      pass

class CreateCustomFields_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   tableName
   docTypeID
   propertyName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.docTypeID:str = obj["docTypeID"]
      self.propertyName:str = obj["propertyName"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   tableName
   docTypeID
   propertyName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.docTypeID:str = obj["docTypeID"]
      self.propertyName:str = obj["propertyName"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_XAttachMetaDataListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewXAttachMetaData_input:
   """ Required : 
   ds
   tableName
   docTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["ds"]
      self.tableName:str = obj["tableName"]
      self.docTypeID:str = obj["docTypeID"]
      pass

class GetNewXAttachMetaData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseXAttachMetaData
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseXAttachMetaData:str = obj["whereClauseXAttachMetaData"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["returnObj"]
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

class Ice_Tablesets_UpdExtXAttachMetaDataTableset:
   def __init__(self, obj):
      self.XAttachMetaData:list[Ice_Tablesets_XAttachMetaDataRow] = obj["XAttachMetaData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_XAttachMetaDataListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """   Unique identifier of a DocType. Assigned by the user.
Cannot be blank.  """  
      self.PropertyName:str = obj["PropertyName"]
      """  Name of meta data property within external document type system  """  
      self.PropertyDesc:str = obj["PropertyDesc"]
      """  General description of meta data property.  """  
      self.Mapping:str = obj["Mapping"]
      """  Column mapping information  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Determines whether this metadata is mandatory.  """  
      self.AllowOverride:bool = obj["AllowOverride"]
      """  Determines whether the user can manually enter or change the calculated meta data field.  """  
      self.SPColumnID:str = obj["SPColumnID"]
      """  Share Point Column ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XAttachMetaDataListTableset:
   def __init__(self, obj):
      self.XAttachMetaDataList:list[Ice_Tablesets_XAttachMetaDataListRow] = obj["XAttachMetaDataList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_XAttachMetaDataRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TableName:str = obj["TableName"]
      """  Table Name  """  
      self.DocTypeID:str = obj["DocTypeID"]
      """   Unique identifier of a DocType. Assigned by the user.
Cannot be blank.  """  
      self.PropertyName:str = obj["PropertyName"]
      """  Name of meta data property within external document type system  """  
      self.PropertyDesc:str = obj["PropertyDesc"]
      """  General description of meta data property.  """  
      self.Mapping:str = obj["Mapping"]
      """  Column mapping information  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Determines whether this metadata is mandatory.  """  
      self.AllowOverride:bool = obj["AllowOverride"]
      """  Determines whether the user can manually enter or change the calculated meta data field.  """  
      self.SPColumnID:str = obj["SPColumnID"]
      """  Share Point Column ID  """  
      self.PropertyValue:str = obj["PropertyValue"]
      """  PropertyValue  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrentValue:str = obj["CurrentValue"]
      """  Holds the current metadata value.  This is not stored on the Epicor database, instead it is used to decorate the SharePoint column value for the attachment record.  """  
      self.Storage:str = obj["Storage"]
      self.StorageType:int = obj["StorageType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_XAttachMetaDataTableset:
   def __init__(self, obj):
      self.XAttachMetaData:list[Ice_Tablesets_XAttachMetaDataRow] = obj["XAttachMetaData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtXAttachMetaDataTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtXAttachMetaDataTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_XAttachMetaDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

