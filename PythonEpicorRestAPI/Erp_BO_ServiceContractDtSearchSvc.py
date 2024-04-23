import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ServiceContractDtSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ServiceContractDtSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ServiceContractDtSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ServiceContractDtSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches",headers=creds) as resp:
           return await resp.json()

async def post_ServiceContractDtSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ServiceContractDtSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ServiceContractDtSearches_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ServiceContractDtSearch item
   Description: Calls GetByID to retrieve the ServiceContractDtSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ServiceContractDtSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches(" + Company + "," + ContractNum + "," + ContractLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ServiceContractDtSearches_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ServiceContractDtSearch for the service
   Description: Calls UpdateExt to update ServiceContractDtSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ServiceContractDtSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSContDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches(" + Company + "," + ContractNum + "," + ContractLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ServiceContractDtSearches_Company_ContractNum_ContractLine(Company, ContractNum, ContractLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ServiceContractDtSearch item
   Description: Call UpdateExt to delete ServiceContractDtSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ServiceContractDtSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ContractNum: Desc: ContractNum   Required: True
      :param ContractLine: Desc: ContractLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/ServiceContractDtSearches(" + Company + "," + ContractNum + "," + ContractLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSContDtListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFSContDt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFSContDt=" + whereClauseFSContDt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(contractNum, contractLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "contractNum=" + contractNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "contractLine=" + contractLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSContDt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSContDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSContDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSContDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSContDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ServiceContractDtSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContDtListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSContDtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSContDtRow] = obj["value"]
      pass

class Erp_Tablesets_FSContDtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Contract comments.  """  
      self.ContractType:str = obj["ContractType"]
      """   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sold to Order Number  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sold To Order line  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ReturnQty:int = obj["ReturnQty"]
      """  Return Quantity used in the create RMA process.  """  
      self.SelectedforRMA:bool = obj["SelectedforRMA"]
      """  Indicates if the contract line is selected to create RMA for.  """  
      self.HdCurrencyCode:str = obj["HdCurrencyCode"]
      self.HdCurrencyCodeDesc:str = obj["HdCurrencyCodeDesc"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Document currency symbol.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Contract comments.  """  
      self.ContractType:str = obj["ContractType"]
      """   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sold to Order Number  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sold To Order line  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ReturnQty:int = obj["ReturnQty"]
      """  Return Quantity used in the create RMA process.  """  
      self.SelectedforRMA:bool = obj["SelectedforRMA"]
      """  Indicates if the contract line is selected to create RMA for.  """  
      self.HdCurrencyCode:str = obj["HdCurrencyCode"]
      self.HdCurrencyCodeDesc:str = obj["HdCurrencyCodeDesc"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Document currency symbol.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.PriceMulti:int = obj["PriceMulti"]
      """  The calculated PriceMulti is based on the parent FSContHd record.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   contractNum
   contractLine
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      self.contractLine:int = obj["contractLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FSContDtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Contract comments.  """  
      self.ContractType:str = obj["ContractType"]
      """   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sold to Order Number  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sold To Order line  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ReturnQty:int = obj["ReturnQty"]
      """  Return Quantity used in the create RMA process.  """  
      self.SelectedforRMA:bool = obj["SelectedforRMA"]
      """  Indicates if the contract line is selected to create RMA for.  """  
      self.HdCurrencyCode:str = obj["HdCurrencyCode"]
      self.HdCurrencyCodeDesc:str = obj["HdCurrencyCodeDesc"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Document currency symbol.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSContDtListTableset:
   def __init__(self, obj):
      self.FSContDtList:list[Erp_Tablesets_FSContDtListRow] = obj["FSContDtList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSContDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.PricePerUnit:int = obj["PricePerUnit"]
      """  Price per unit for the Contract in base currency.  Defaults from the FScontCd table  """  
      self.DocPricePerUnit:int = obj["DocPricePerUnit"]
      """  Price per unit for the Contract in customers currency.  Defaults from the FScontCd table  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the Contract line item. These will copied into the Invoice detail  file as defaults.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSContDt record. Can be blank.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Contract comments.  """  
      self.ContractType:str = obj["ContractType"]
      """   A value of "ORD-ENT" indicates that this Service contract is related to a specific Sales Order and its line items and will be created and maintained from there, It will print on the Order acknowledgment and be invoiced with the sales order item as they are shipped.  A Value of "Cnt-Ent" indicates that this Service Contract was created from the service contract entry programs.  It is not directly related to a sales order; it will be printed by itself and invoiced by itself.
(Duplicated from FSContHd for Browse)  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.SoldOrderNum:int = obj["SoldOrderNum"]
      """  Sold to Order Number  """  
      self.SoldOrderLine:int = obj["SoldOrderLine"]
      """  Sold To Order line  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1PricePerUnit:int = obj["Rpt1PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt2PricePerUnit:int = obj["Rpt2PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Rpt3PricePerUnit:int = obj["Rpt3PricePerUnit"]
      """  Reporting currency value of this field  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.DateInactivated:str = obj["DateInactivated"]
      """  This is the date the contract line was set to inactive.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.DateInvoiced:str = obj["DateInvoiced"]
      """  Date this line was invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowUpdate:bool = obj["AllowUpdate"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.ExtPrice:int = obj["ExtPrice"]
      self.DocExtPrice:int = obj["DocExtPrice"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.ReturnQty:int = obj["ReturnQty"]
      """  Return Quantity used in the create RMA process.  """  
      self.SelectedforRMA:bool = obj["SelectedforRMA"]
      """  Indicates if the contract line is selected to create RMA for.  """  
      self.HdCurrencyCode:str = obj["HdCurrencyCode"]
      self.HdCurrencyCodeDesc:str = obj["HdCurrencyCodeDesc"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Document currency symbol.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.TrackSerialNumbers:bool = obj["TrackSerialNumbers"]
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      self.PriceMulti:int = obj["PriceMulti"]
      """  The calculated PriceMulti is based on the parent FSContHd record.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ServiceContractDtSearchTableset:
   def __init__(self, obj):
      self.FSContDt:list[Erp_Tablesets_FSContDtRow] = obj["FSContDt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtServiceContractDtSearchTableset:
   def __init__(self, obj):
      self.FSContDt:list[Erp_Tablesets_FSContDtRow] = obj["FSContDt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   contractNum
   contractLine
   """  
   def __init__(self, obj):
      self.contractNum:int = obj["contractNum"]
      self.contractLine:int = obj["contractLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FSContDtListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFSContDt_input:
   """ Required : 
   ds
   contractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["ds"]
      self.contractNum:int = obj["contractNum"]
      pass

class GetNewFSContDt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFSContDt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSContDt:str = obj["whereClauseFSContDt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtServiceContractDtSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtServiceContractDtSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ServiceContractDtSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

