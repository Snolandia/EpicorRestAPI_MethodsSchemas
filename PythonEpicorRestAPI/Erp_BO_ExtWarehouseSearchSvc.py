import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ExtWarehouseSearchSvc
# Description: ExtWarehouse search object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ExtWarehouseSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ExtWarehouseSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtWarehouseSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtWarehouseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/ExtWarehouseSearches",headers=creds) as resp:
           return await resp.json()

async def post_ExtWarehouseSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtWarehouseSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/ExtWarehouseSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ExtWarehouseSearches_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ExtWarehouseSearch item
   Description: Calls GetByID to retrieve the ExtWarehouseSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtWarehouseSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/ExtWarehouseSearches(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ExtWarehouseSearches_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ExtWarehouseSearch for the service
   Description: Calls UpdateExt to update ExtWarehouseSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtWarehouseSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtWarehouseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/ExtWarehouseSearches(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ExtWarehouseSearches_Company_ExtSystemID_TransferMethod_ExtCompanyID_ExtPlantID_ExtWarehouseID(Company, ExtSystemID, TransferMethod, ExtCompanyID, ExtPlantID, ExtWarehouseID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ExtWarehouseSearch item
   Description: Call UpdateExt to delete ExtWarehouseSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtWarehouseSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtSystemID: Desc: ExtSystemID   Required: True   Allow empty value : True
      :param TransferMethod: Desc: TransferMethod   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param ExtPlantID: Desc: ExtPlantID   Required: True   Allow empty value : True
      :param ExtWarehouseID: Desc: ExtWarehouseID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/ExtWarehouseSearches(" + Company + "," + ExtSystemID + "," + TransferMethod + "," + ExtCompanyID + "," + ExtPlantID + "," + ExtWarehouseID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtWarehouseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseExtWarehouse, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseExtWarehouse=" + whereClauseExtWarehouse
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extSystemID, transferMethod, extCompanyID, extPlantID, extWarehouseID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "extSystemID=" + extSystemID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "transferMethod=" + transferMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "extCompanyID=" + extCompanyID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "extPlantID=" + extPlantID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "extWarehouseID=" + extWarehouseID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewExtWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewExtWarehouse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewExtWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ExtWarehouseSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtWarehouseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtWarehouseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ExtWarehouseRow] = obj["value"]
      pass

class Erp_Tablesets_ExtWarehouseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this external Site assigned by the user.  """  
      self.ExtWarehouseID:str = obj["ExtWarehouseID"]
      """  Unique identifier of this warehouse assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CountryDescription:str = obj["CountryDescription"]
      """  Country name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtWarehouseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this external Site assigned by the user.  """  
      self.ExtWarehouseID:str = obj["ExtWarehouseID"]
      """  Unique identifier of this warehouse assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extSystemID
   transferMethod
   extCompanyID
   extPlantID
   extWarehouseID
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extPlantID:str = obj["extPlantID"]
      self.extWarehouseID:str = obj["extWarehouseID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ExtWarehouseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this external Site assigned by the user.  """  
      self.ExtWarehouseID:str = obj["ExtWarehouseID"]
      """  Unique identifier of this warehouse assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CountryDescription:str = obj["CountryDescription"]
      """  Country name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtWarehouseListTableset:
   def __init__(self, obj):
      self.ExtWarehouseList:list[Erp_Tablesets_ExtWarehouseListRow] = obj["ExtWarehouseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ExtWarehouseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  Code for the external package to be interfaced with  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  Option of how to transfer the data to the package (e.g. direct connect, ascii, xml) and will identify the specific programs to run  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company  """  
      self.ExtPlantID:str = obj["ExtPlantID"]
      """  Unique identifier of this external Site assigned by the user.  """  
      self.ExtWarehouseID:str = obj["ExtWarehouseID"]
      """  Unique identifier of this warehouse assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name. Used on shipping reports.  """  
      self.Address1:str = obj["Address1"]
      """  Site address line 1.  """  
      self.Address2:str = obj["Address2"]
      """  Site address line 2.  """  
      self.Address3:str = obj["Address3"]
      """  Site address line 3.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of the address. This field is in sync with the Country.Country field. Must be a valid entry in the Country table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ExtWarehouseSearchTableset:
   def __init__(self, obj):
      self.ExtWarehouse:list[Erp_Tablesets_ExtWarehouseRow] = obj["ExtWarehouse"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtExtWarehouseSearchTableset:
   def __init__(self, obj):
      self.ExtWarehouse:list[Erp_Tablesets_ExtWarehouseRow] = obj["ExtWarehouse"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   extSystemID
   transferMethod
   extCompanyID
   extPlantID
   extWarehouseID
   """  
   def __init__(self, obj):
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extPlantID:str = obj["extPlantID"]
      self.extWarehouseID:str = obj["extWarehouseID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ExtWarehouseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewExtWarehouse_input:
   """ Required : 
   ds
   extSystemID
   transferMethod
   extCompanyID
   extPlantID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["ds"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.extPlantID:str = obj["extPlantID"]
      pass

class GetNewExtWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseExtWarehouse
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseExtWarehouse:str = obj["whereClauseExtWarehouse"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtWarehouseSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtExtWarehouseSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ExtWarehouseSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

