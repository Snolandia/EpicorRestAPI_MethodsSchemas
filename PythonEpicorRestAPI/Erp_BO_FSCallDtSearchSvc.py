import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FSCallDtSearchSvc
# Description: Search for Field Service Call Detail Line
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FSCallDtSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FSCallDtSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FSCallDtSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches",headers=creds) as resp:
           return await resp.json()

async def post_FSCallDtSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FSCallDtSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FSCallDtSearches_Company_CallNum_CallLine(Company, CallNum, CallLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FSCallDtSearch item
   Description: Calls GetByID to retrieve the FSCallDtSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FSCallDtSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches(" + Company + "," + CallNum + "," + CallLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FSCallDtSearches_Company_CallNum_CallLine(Company, CallNum, CallLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FSCallDtSearch for the service
   Description: Calls UpdateExt to update FSCallDtSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FSCallDtSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FSCallDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches(" + Company + "," + CallNum + "," + CallLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FSCallDtSearches_Company_CallNum_CallLine(Company, CallNum, CallLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FSCallDtSearch item
   Description: Call UpdateExt to delete FSCallDtSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FSCallDtSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CallNum: Desc: CallNum   Required: True
      :param CallLine: Desc: CallLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/FSCallDtSearches(" + Company + "," + CallNum + "," + CallLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FSCallDtListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFSCallDt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFSCallDt=" + whereClauseFSCallDt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(callNum, callLine, epicorHeaders = None):
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
   params += "callNum=" + callNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "callLine=" + callLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFSCallDt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFSCallDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFSCallDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFSCallDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFSCallDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FSCallDtSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallDtListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FSCallDtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FSCallDtRow] = obj["value"]
      pass

class Erp_Tablesets_FSCallDtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProbReasonDesc:str = obj["ProbReasonDesc"]
      """  Reson Code Description  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol of the "BASE" currency  """  
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Currency.CurrSymbol of the customer's currency  """  
      self.TotLineCall:int = obj["TotLineCall"]
      """  Total Actual Call Amount for the line  """  
      self.DocTotLineCall:int = obj["DocTotLineCall"]
      """  Total Actual Call Amount for the line in customer's currency  """  
      self.TotLineBillCall:int = obj["TotLineBillCall"]
      """  Total Billable Call Amount for the line  """  
      self.DocTotLineBillCall:int = obj["DocTotLineBillCall"]
      """  Total Billable Call Amount for the line in customer's currency  """  
      self.TotLineEstCall:int = obj["TotLineEstCall"]
      """  Total Estimated Call Amount for the line  """  
      self.DocTotLineEstCall:int = obj["DocTotLineEstCall"]
      """  Total Estimated Call AMount for the line in customer's currency  """  
      self.EnableContract:bool = obj["EnableContract"]
      """  Indicates if Contract entry should be enabled.  """  
      self.EnableWarranty:bool = obj["EnableWarranty"]
      """  Indicates if Warranty entry should be enabled.  """  
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1TotLineBillCall:int = obj["Rpt1TotLineBillCall"]
      self.Rpt2TotLineBillCall:int = obj["Rpt2TotLineBillCall"]
      self.Rpt3TotLineBillCall:int = obj["Rpt3TotLineBillCall"]
      self.Rpt1TotLineCall:int = obj["Rpt1TotLineCall"]
      self.Rpt2TotLineCall:int = obj["Rpt2TotLineCall"]
      self.Rpt3TotLineCall:int = obj["Rpt3TotLineCall"]
      self.Rpt1TotLineEstCall:int = obj["Rpt1TotLineEstCall"]
      self.Rpt2TotLineEstCall:int = obj["Rpt2TotLineEstCall"]
      self.Rpt3TotLineEstCall:int = obj["Rpt3TotLineEstCall"]
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.ContractLineLineDesc:str = obj["ContractLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line Description  """  
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      """  Description of the warranty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  IssueTopicID1  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  IssueTopicID2  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  IssueTopicID3  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  IssueTopicID4  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  IssueTopicID5  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  IssueTopicID6  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  IssueTopicID7  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  IssueTopicID8  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  IssueTopicID9  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  IssueTopicID10  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  IssueTopics  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  ResTopicID1  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  ResTopicID2  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  ResTopicID3  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  ResTopicID4  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  ResTopicID5  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  ResTopicID6  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  ResTopicID7  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  ResTopicID8  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  ResTopicID9  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  ResTopicID10  """  
      self.ResTopics:str = obj["ResTopics"]
      """  ResTopics  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates the invoice processing has been done for this call line.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call line can be invoiced.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol of the "BASE" currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Currency.CurrSymbol of the customer's currency  """  
      self.DocTotLineBillCall:int = obj["DocTotLineBillCall"]
      """  Total Billable Call Amount for the line in customer's currency  """  
      self.DocTotLineCall:int = obj["DocTotLineCall"]
      """  Total Actual Call Amount for the line in customer's currency  """  
      self.DocTotLineEstCall:int = obj["DocTotLineEstCall"]
      """  Total Estimated Call AMount for the line in customer's currency  """  
      self.EnableContract:bool = obj["EnableContract"]
      """  Indicates if Contract entry should be enabled.  """  
      self.EnableWarranty:bool = obj["EnableWarranty"]
      """  Indicates if Warranty entry should be enabled.  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.ProbReasonDesc:str = obj["ProbReasonDesc"]
      """  Reson Code Description  """  
      self.Rpt1TotLineBillCall:int = obj["Rpt1TotLineBillCall"]
      self.Rpt1TotLineCall:int = obj["Rpt1TotLineCall"]
      self.Rpt1TotLineEstCall:int = obj["Rpt1TotLineEstCall"]
      self.Rpt2TotLineBillCall:int = obj["Rpt2TotLineBillCall"]
      self.Rpt2TotLineCall:int = obj["Rpt2TotLineCall"]
      self.Rpt2TotLineEstCall:int = obj["Rpt2TotLineEstCall"]
      self.Rpt3TotLineBillCall:int = obj["Rpt3TotLineBillCall"]
      self.Rpt3TotLineCall:int = obj["Rpt3TotLineCall"]
      self.Rpt3TotLineEstCall:int = obj["Rpt3TotLineEstCall"]
      self.TotLineBillCall:int = obj["TotLineBillCall"]
      """  Total Billable Call Amount for the line  """  
      self.TotLineCall:int = obj["TotLineCall"]
      """  Total Actual Call Amount for the line  """  
      self.TotLineEstCall:int = obj["TotLineEstCall"]
      """  Total Estimated Call Amount for the line  """  
      self.JobClosed:bool = obj["JobClosed"]
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractLineLineDesc:str = obj["ContractLineLineDesc"]
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   callNum
   callLine
   """  
   def __init__(self, obj):
      self.callNum:int = obj["callNum"]
      self.callLine:int = obj["callLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FSCallDtListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProbReasonDesc:str = obj["ProbReasonDesc"]
      """  Reson Code Description  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol of the "BASE" currency  """  
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Currency.CurrSymbol of the customer's currency  """  
      self.TotLineCall:int = obj["TotLineCall"]
      """  Total Actual Call Amount for the line  """  
      self.DocTotLineCall:int = obj["DocTotLineCall"]
      """  Total Actual Call Amount for the line in customer's currency  """  
      self.TotLineBillCall:int = obj["TotLineBillCall"]
      """  Total Billable Call Amount for the line  """  
      self.DocTotLineBillCall:int = obj["DocTotLineBillCall"]
      """  Total Billable Call Amount for the line in customer's currency  """  
      self.TotLineEstCall:int = obj["TotLineEstCall"]
      """  Total Estimated Call Amount for the line  """  
      self.DocTotLineEstCall:int = obj["DocTotLineEstCall"]
      """  Total Estimated Call AMount for the line in customer's currency  """  
      self.EnableContract:bool = obj["EnableContract"]
      """  Indicates if Contract entry should be enabled.  """  
      self.EnableWarranty:bool = obj["EnableWarranty"]
      """  Indicates if Warranty entry should be enabled.  """  
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1TotLineBillCall:int = obj["Rpt1TotLineBillCall"]
      self.Rpt2TotLineBillCall:int = obj["Rpt2TotLineBillCall"]
      self.Rpt3TotLineBillCall:int = obj["Rpt3TotLineBillCall"]
      self.Rpt1TotLineCall:int = obj["Rpt1TotLineCall"]
      self.Rpt2TotLineCall:int = obj["Rpt2TotLineCall"]
      self.Rpt3TotLineCall:int = obj["Rpt3TotLineCall"]
      self.Rpt1TotLineEstCall:int = obj["Rpt1TotLineEstCall"]
      self.Rpt2TotLineEstCall:int = obj["Rpt2TotLineEstCall"]
      self.Rpt3TotLineEstCall:int = obj["Rpt3TotLineEstCall"]
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.ContractLineLineDesc:str = obj["ContractLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      """  Defaults from PODetail LineDesc.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line Description  """  
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      """  Description of the warranty.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallDtListTableset:
   def __init__(self, obj):
      self.FSCallDtList:list[Erp_Tablesets_FSCallDtListRow] = obj["FSCallDtList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FSCallDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  When creating a new Service Call ,the user is prompted for an Call number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the Call  of the last record on file and then a 1 to it.  """  
      self.CallLine:int = obj["CallLine"]
      """  This field along with Company and CallNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last FSCalPrt record for the Call and the adding 1 to it.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the Part.RevisionNum field.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the part being repaired.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  """  
      self.CallQty:int = obj["CallQty"]
      """  TotalCall Quantity for the line item.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this Service call is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line that holds the warranty information for this service call  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Unique code for the Warranty  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number if this item is under a contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This is the contract line the relates to the item on the service call.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.CallComment:str = obj["CallComment"]
      """  Contains comments about the Item in need of service. These will be printed on the ServiceCall.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to establish invoice comments about the repaired item. These will copied into the Invoice detail file as defaults.  """  
      self.ProbReasonCode:str = obj["ProbReasonCode"]
      """  Problem reason code from the reason master table. type problem.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code. Use the xasyst.CallProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  """  
      self.MatCovered:bool = obj["MatCovered"]
      """  Are Material cost covered  """  
      self.LabCovered:bool = obj["LabCovered"]
      """  Is Labor Cost Covered  """  
      self.MiscCovered:bool = obj["MiscCovered"]
      """  Are misc. Costs Covered  """  
      self.TotLabor:int = obj["TotLabor"]
      """  total Labor Amount.  """  
      self.DocTotLabor:int = obj["DocTotLabor"]
      """  total Labor Amount. In customers currency  """  
      self.TotBillLabor:int = obj["TotBillLabor"]
      """  total Billable Labor Amount.  """  
      self.DocTotBillLabor:int = obj["DocTotBillLabor"]
      """  total Billable Labor Amount. In Customers currency.  """  
      self.TotMaterial:int = obj["TotMaterial"]
      """  total Material Amount.  """  
      self.DocTotMaterial:int = obj["DocTotMaterial"]
      """  total Material Amount. In Customers currency  """  
      self.TotBillMaterial:int = obj["TotBillMaterial"]
      """  total Billable Material Amount.  """  
      self.DocTotBillMaterial:int = obj["DocTotBillMaterial"]
      """  total Billable Material Amount. In Customers Currency.  """  
      self.TotMisc:int = obj["TotMisc"]
      """  total Misc. Amount.  """  
      self.DocTotMisc:int = obj["DocTotMisc"]
      """  total Misc. Amount. In customers currency.  """  
      self.TotBillableMisc:int = obj["TotBillableMisc"]
      """  total Billable Misc. Amount.  """  
      self.DocTotBillableMisc:int = obj["DocTotBillableMisc"]
      """  total Billable Misc. Amount. In customer's currency.  """  
      self.TotMaterialCost:int = obj["TotMaterialCost"]
      """  total Material Cost.  """  
      self.TotMiscCost:int = obj["TotMiscCost"]
      """  total Misc. Cost.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project ID of the Project table record that this FSCallDt record. Can be blank.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the Call Line record back its linked JobHead record.  Not directly maintainable.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.TotSubCont:int = obj["TotSubCont"]
      """  Total Subcontract Amount.  """  
      self.DocTotSubCont:int = obj["DocTotSubCont"]
      """  total Subcontract Amount. In customers currency  """  
      self.TotBillSubCont:int = obj["TotBillSubCont"]
      """  total Billable Subcontract Amount.  """  
      self.DocTotBillSubCont:int = obj["DocTotBillSubCont"]
      """  total Billable Subcontract Amount. In Customers currency.  """  
      self.TotEstLabor:int = obj["TotEstLabor"]
      """  total Estimated Labor Amount.  """  
      self.DocTotEstLabor:int = obj["DocTotEstLabor"]
      """  total estimated Labor Amount. In customers currency  """  
      self.TotEstMaterial:int = obj["TotEstMaterial"]
      """  total Estimated Material Amount.  """  
      self.DocTotEstMaterial:int = obj["DocTotEstMaterial"]
      """  total Estimated Material Amount. In Customers currency  """  
      self.TotEstMisc:int = obj["TotEstMisc"]
      """  total Estimated Misc. Amount.  Future Use.  """  
      self.DocTotEstMisc:int = obj["DocTotEstMisc"]
      """  total Est. Misc. Amount. In customers currency. Future use  """  
      self.TotEstSubCont:int = obj["TotEstSubCont"]
      """  Total estimated Subcontract Amount.  """  
      self.DocTotEstSubCont:int = obj["DocTotEstSubCont"]
      """  total Estimated Subcontract Amount. In customers currency  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.Rpt1TotBillableMisc:int = obj["Rpt1TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillableMisc:int = obj["Rpt2TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillableMisc:int = obj["Rpt3TotBillableMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillLabor:int = obj["Rpt1TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillLabor:int = obj["Rpt2TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillLabor:int = obj["Rpt3TotBillLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillMaterial:int = obj["Rpt1TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillMaterial:int = obj["Rpt2TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillMaterial:int = obj["Rpt3TotBillMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotBillSubCont:int = obj["Rpt1TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotBillSubCont:int = obj["Rpt2TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotBillSubCont:int = obj["Rpt3TotBillSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstLabor:int = obj["Rpt1TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstLabor:int = obj["Rpt2TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstLabor:int = obj["Rpt3TotEstLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMaterial:int = obj["Rpt1TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMaterial:int = obj["Rpt2TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMaterial:int = obj["Rpt3TotEstMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstMisc:int = obj["Rpt1TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstMisc:int = obj["Rpt2TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstMisc:int = obj["Rpt3TotEstMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotEstSubCont:int = obj["Rpt1TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotEstSubCont:int = obj["Rpt2TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotEstSubCont:int = obj["Rpt3TotEstSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotLabor:int = obj["Rpt1TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotLabor:int = obj["Rpt2TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotLabor:int = obj["Rpt3TotLabor"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMaterial:int = obj["Rpt1TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMaterial:int = obj["Rpt2TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMaterial:int = obj["Rpt3TotMaterial"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotMisc:int = obj["Rpt1TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotMisc:int = obj["Rpt2TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotMisc:int = obj["Rpt3TotMisc"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotSubCont:int = obj["Rpt1TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotSubCont:int = obj["Rpt2TotSubCont"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotSubCont:int = obj["Rpt3TotSubCont"]
      """  Reporting currency value of this field  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  The drop shipment packing slip number that this Service call is linked with  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  The drop shipment packing slip line that holds the warranty information for this service call  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The supplier purchase point id of the drop shipment and part of the primary key of a drop shipment line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  IssueTopicID1  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  IssueTopicID2  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  IssueTopicID3  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  IssueTopicID4  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  IssueTopicID5  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  IssueTopicID6  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  IssueTopicID7  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  IssueTopicID8  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  IssueTopicID9  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  IssueTopicID10  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  IssueTopics  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  ResTopicID1  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  ResTopicID2  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  ResTopicID3  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  ResTopicID4  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  ResTopicID5  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  ResTopicID6  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  ResTopicID7  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  ResTopicID8  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  ResTopicID9  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  ResTopicID10  """  
      self.ResTopics:str = obj["ResTopics"]
      """  ResTopics  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates the invoice processing has been done for this call line.  """  
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      """  Indicates that the call line can be invoiced.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol of the "BASE" currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DisplayContractType:str = obj["DisplayContractType"]
      self.DocCurrSymbol:str = obj["DocCurrSymbol"]
      """  Currency.CurrSymbol of the customer's currency  """  
      self.DocTotLineBillCall:int = obj["DocTotLineBillCall"]
      """  Total Billable Call Amount for the line in customer's currency  """  
      self.DocTotLineCall:int = obj["DocTotLineCall"]
      """  Total Actual Call Amount for the line in customer's currency  """  
      self.DocTotLineEstCall:int = obj["DocTotLineEstCall"]
      """  Total Estimated Call AMount for the line in customer's currency  """  
      self.EnableContract:bool = obj["EnableContract"]
      """  Indicates if Contract entry should be enabled.  """  
      self.EnableWarranty:bool = obj["EnableWarranty"]
      """  Indicates if Warranty entry should be enabled.  """  
      self.IUMDesc:str = obj["IUMDesc"]
      """  Unit of Measure Description  """  
      self.ProbReasonDesc:str = obj["ProbReasonDesc"]
      """  Reson Code Description  """  
      self.Rpt1TotLineBillCall:int = obj["Rpt1TotLineBillCall"]
      self.Rpt1TotLineCall:int = obj["Rpt1TotLineCall"]
      self.Rpt1TotLineEstCall:int = obj["Rpt1TotLineEstCall"]
      self.Rpt2TotLineBillCall:int = obj["Rpt2TotLineBillCall"]
      self.Rpt2TotLineCall:int = obj["Rpt2TotLineCall"]
      self.Rpt2TotLineEstCall:int = obj["Rpt2TotLineEstCall"]
      self.Rpt3TotLineBillCall:int = obj["Rpt3TotLineBillCall"]
      self.Rpt3TotLineCall:int = obj["Rpt3TotLineCall"]
      self.Rpt3TotLineEstCall:int = obj["Rpt3TotLineEstCall"]
      self.TotLineBillCall:int = obj["TotLineBillCall"]
      """  Total Billable Call Amount for the line  """  
      self.TotLineCall:int = obj["TotLineCall"]
      """  Total Actual Call Amount for the line  """  
      self.TotLineEstCall:int = obj["TotLineEstCall"]
      """  Total Estimated Call Amount for the line  """  
      self.JobClosed:bool = obj["JobClosed"]
      self.BitFlag:int = obj["BitFlag"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractLineLineDesc:str = obj["ContractLineLineDesc"]
      self.DropShipDtlLineDesc:str = obj["DropShipDtlLineDesc"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumShipStatus:str = obj["PackNumShipStatus"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.WarrantyCodeWarrDescription:str = obj["WarrantyCodeWarrDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FSCallDtSearchTableset:
   def __init__(self, obj):
      self.FSCallDt:list[Erp_Tablesets_FSCallDtRow] = obj["FSCallDt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFSCallDtSearchTableset:
   def __init__(self, obj):
      self.FSCallDt:list[Erp_Tablesets_FSCallDtRow] = obj["FSCallDt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   callNum
   callLine
   """  
   def __init__(self, obj):
      self.callNum:int = obj["callNum"]
      self.callLine:int = obj["callLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FSCallDtListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFSCallDt_input:
   """ Required : 
   ds
   callNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["ds"]
      self.callNum:int = obj["callNum"]
      pass

class GetNewFSCallDt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFSCallDt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFSCallDt:str = obj["whereClauseFSCallDt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtFSCallDtSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFSCallDtSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FSCallDtSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

