import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MiscShipToSearchSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MiscShipToSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MiscShipToSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MiscShipToSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MiscShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/MiscShipToSearches",headers=creds) as resp:
           return await resp.json()

async def post_MiscShipToSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MiscShipToSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MiscShipToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MiscShipToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/MiscShipToSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MiscShipToSearches_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MiscShipToSearch item
   Description: Calls GetByID to retrieve the MiscShipToSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MiscShipToSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MiscShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/MiscShipToSearches(" + Company + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MiscShipToSearches_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MiscShipToSearch for the service
   Description: Calls UpdateExt to update MiscShipToSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MiscShipToSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MiscShipToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/MiscShipToSearches(" + Company + "," + CustNum + "," + ShipToNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MiscShipToSearches_Company_CustNum_ShipToNum(Company, CustNum, ShipToNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MiscShipToSearch item
   Description: Call UpdateExt to delete MiscShipToSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MiscShipToSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/MiscShipToSearches(" + Company + "," + CustNum + "," + ShipToNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MiscShipToListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMiscShipTo, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMiscShipTo=" + whereClauseMiscShipTo
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(custNum, shipToNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_MiscShipToList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MiscShipToList
   Description: MiscShipTo is not a real database table.  It stores results from
ShipTo and VendorPP tables.
The UI needs the standard methods (GetByID, GetRows, GetList etc..) for the
Search model to work.  So we have to use core/BOBase.i .
When we do that we get compilation error.  To overcome that we have defined
PHYSICAL_TABLE_01 ShipTo.
This solves most of the problems i.e. we can compile the code and
generate a dll.  The GetList also works, except it displays invalid query
when we try to use a where clause on non ShipTo fields.
To overcome that problem.  This method is developed.
It is a copy of GetList.  Except it fills the data from both the tables
and then applies the where condition.
   OperationID: MiscShipToList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MiscShipToList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MiscShipToList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendID
   OperationID: GetVendID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMiscShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMiscShipTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMiscShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMiscShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMiscShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipToSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MiscShipToListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MiscShipToListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MiscShipToRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MiscShipToRow] = obj["value"]
      pass

class Erp_Tablesets_MiscShipToListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecordType:str = obj["RecordType"]
      """  Valid values are ShipTo or VendorPP.  Defines the type of record.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ID:str = obj["ID"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.PurPoint:str = obj["PurPoint"]
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MiscShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecordType:str = obj["RecordType"]
      """  Valid values are ShipTo or VendorPP.  Defines the type of record.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ID:str = obj["ID"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.PurPoint:str = obj["PurPoint"]
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MiscShipToListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecordType:str = obj["RecordType"]
      """  Valid values are ShipTo or VendorPP.  Defines the type of record.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ID:str = obj["ID"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.PurPoint:str = obj["PurPoint"]
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MiscShipToListTableset:
   def __init__(self, obj):
      self.MiscShipToList:list[Erp_Tablesets_MiscShipToListRow] = obj["MiscShipToList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MiscShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RecordType:str = obj["RecordType"]
      """  Valid values are ShipTo or VendorPP.  Defines the type of record.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the record is related to.  """  
      self.ID:str = obj["ID"]
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  """  
      self.PurPoint:str = obj["PurPoint"]
      self.Address1:str = obj["Address1"]
      """  The first line of the ShipTo address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the ShipTo address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the ShipTo address.  """  
      self.City:str = obj["City"]
      """  The city portion of the ShipTo address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the ShipTo address.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the ShipTo address.  """  
      self.Country:str = obj["Country"]
      """  The country portion of the ShipTo address.  """  
      self.VendorNum:int = obj["VendorNum"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MiscShipToSearchTableset:
   def __init__(self, obj):
      self.MiscShipTo:list[Erp_Tablesets_MiscShipToRow] = obj["MiscShipTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMiscShipToSearchTableset:
   def __init__(self, obj):
      self.MiscShipTo:list[Erp_Tablesets_MiscShipToRow] = obj["MiscShipTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MiscShipToListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMiscShipTo_input:
   """ Required : 
   ds
   custNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["ds"]
      self.custNum:int = obj["custNum"]
      pass

class GetNewMiscShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMiscShipTo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMiscShipTo:str = obj["whereClauseMiscShipTo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendID_input:
   """ Required : 
   piVendorNum
   """  
   def __init__(self, obj):
      self.piVendorNum:int = obj["piVendorNum"]
      pass

class GetVendID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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

class MiscShipToList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause to filter the query results.  """  
      self.pageSize:int = obj["pageSize"]
      """  page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolute page  """  
      pass

class MiscShipToList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipToListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMiscShipToSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMiscShipToSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipToSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

