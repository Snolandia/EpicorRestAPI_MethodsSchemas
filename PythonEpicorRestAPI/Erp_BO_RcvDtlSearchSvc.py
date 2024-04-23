import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RcvDtlSearchSvc
# Description: bo/RcvDtlSearch/RcvDtlSearch.p
           RcvDtl Search Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RcvDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RcvDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_RcvDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RcvDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RcvDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RcvDtlSearch item
   Description: Calls GetByID to retrieve the RcvDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RcvDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RcvDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RcvDtlSearch for the service
   Description: Calls UpdateExt to update RcvDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RcvDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RcvDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RcvDtlSearches_Company_VendorNum_PurPoint_PackSlip_PackLine(Company, VendorNum, PurPoint, PackSlip, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RcvDtlSearch item
   Description: Call UpdateExt to delete RcvDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RcvDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PackSlip: Desc: PackSlip   Required: True   Allow empty value : True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/RcvDtlSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + PackSlip + "," + PackLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RcvDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRcvDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRcvDtl=" + whereClauseRcvDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, purPoint, packSlip, packLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "purPoint=" + purPoint
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packSlip=" + packSlip
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packLine=" + packLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRcvDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRcvDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRcvDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRcvDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRcvDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RcvDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RcvDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RcvDtlRow] = obj["value"]
      pass

class Erp_Tablesets_RcvDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackLine:int = obj["GlbPackLine"]
      """  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country (defaults from Part Country of Origin).  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  Duty Amount portion of the landed cost for this receipt line.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  Indirect Cost portion of the landed cost for this receipt line.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate that the receipt line has been received.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.POType:str = obj["POType"]
      """  Identifier of associated PO ('Std', 'CMI', 'SMI')  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      """  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1VendorUnitCost:int = obj["Rpt1VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2VendorUnitCost:int = obj["Rpt2VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3VendorUnitCost:int = obj["Rpt3VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  """  
      self.ICPackNum:int = obj["ICPackNum"]
      """  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  """  
      self.ShipRcv:str = obj["ShipRcv"]
      """  Shipment Received  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Can be different from value on header.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Can be different from value on header.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Can be different from Header value.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SearchPONum:int = obj["SearchPONum"]
      self.InputOurQty:int = obj["InputOurQty"]
      """  OurQty not divided by dimension conversion factor for entry  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether to Enable the Serial Number button  """  
      self.DisplayUMField:str = obj["DisplayUMField"]
      """  Indicates whether the IUM or DUM field should be displayed/enabled  """  
      self.EnableLot:bool = obj["EnableLot"]
      self.JobRequiredQty:int = obj["JobRequiredQty"]
      self.JobIUM:str = obj["JobIUM"]
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.EnableBin:bool = obj["EnableBin"]
      self.EnableWhse:bool = obj["EnableWhse"]
      self.TagMtlSeq:int = obj["TagMtlSeq"]
      """  MtlSeq used in PrintTag option  """  
      self.TagOprSeq:int = obj["TagOprSeq"]
      """  Operation Sequence used in PrintTag  """  
      self.InspectionFlag:bool = obj["InspectionFlag"]
      """  Flag used to switch other Received To's to Pur-Ins  """  
      self.PODueDate:str = obj["PODueDate"]
      """  PO Line Due Date  """  
      self.VenRemQty:int = obj["VenRemQty"]
      self.OurRemQty:int = obj["OurRemQty"]
      """  Our Remaining Quantity  """  
      self.POPUM:str = obj["POPUM"]
      self.POIUM:str = obj["POIUM"]
      self.POFactor:int = obj["POFactor"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.POHold:bool = obj["POHold"]
      self.OrderQty:int = obj["OrderQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  PORel Received Qty for MassReceipts  """  
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Link to the IMRcvDtl table  """  
      self.EnableDim:bool = obj["EnableDim"]
      """  Indicates whether to enable/disable the dimension fields  """  
      self.POComment:str = obj["POComment"]
      self.MassReceipt:bool = obj["MassReceipt"]
      """  Indicates if created through Mass Receipts  """  
      self.AsmPartDescription:str = obj["AsmPartDescription"]
      self.DisableInspection:bool = obj["DisableInspection"]
      """  Flag to set disable/enable the InspectionReq field.  """  
      self.Plant:str = obj["Plant"]
      """  The Plant to which the warehouse belongs to  """  
      self.SetToLocation:bool = obj["SetToLocation"]
      """  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      self.DueDate:str = obj["DueDate"]
      """  PORel.DueDate  """  
      self.OnTime:str = obj["OnTime"]
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      """  Container Detail Landed Cost Amount  """  
      self.POFactorDirection:str = obj["POFactorDirection"]
      self.ContainerExtCost:int = obj["ContainerExtCost"]
      """  This is the extended cost of the container detail item this RcvDtl entry is tied to.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.SNStusChanged:bool = obj["SNStusChanged"]
      self.DropShipment:bool = obj["DropShipment"]
      """  DropShipment  """  
      self.RcvdSMIQty:int = obj["RcvdSMIQty"]
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.SMIComplete:bool = obj["SMIComplete"]
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended receipt detail cost.  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.VendorCurrSymbol:str = obj["VendorCurrSymbol"]
      self.Selected:bool = obj["Selected"]
      self.MangCustID:str = obj["MangCustID"]
      self.MangCustName:str = obj["MangCustName"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CommodityDescription:str = obj["CommodityDescription"]
      """  Full description of the Commodity Code.  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.InspectorIDName:str = obj["InspectorIDName"]
      """  Inspector's Full Name.  """  
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.PONumShipName:str = obj["PONumShipName"]
      """  defaults from the company file.  """  
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.PurchCodePurchDesc:str = obj["PurchCodePurchDesc"]
      """  Description of the purchase type. Appears in drop-down lists for selection.  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackLine:int = obj["GlbPackLine"]
      """  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country (defaults from Part Country of Origin).  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  Duty Amount portion of the landed cost for this receipt line.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  Indirect Cost portion of the landed cost for this receipt line.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate that the receipt line has been received.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.POType:str = obj["POType"]
      """  Identifier of associated PO ('Std', 'CMI', 'SMI')  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      """  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1VendorUnitCost:int = obj["Rpt1VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2VendorUnitCost:int = obj["Rpt2VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3VendorUnitCost:int = obj["Rpt3VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  """  
      self.ICPackNum:int = obj["ICPackNum"]
      """  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  """  
      self.ShipRcv:str = obj["ShipRcv"]
      """  Shipment Received  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Can be different from value on header.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Can be different from value on header.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Can be different from Header value.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.ConvOverride:bool = obj["ConvOverride"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.SMITransNum:int = obj["SMITransNum"]
      """  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.Delivered:bool = obj["Delivered"]
      """  Delivered  """  
      self.DeliveredComments:str = obj["DeliveredComments"]
      """  DeliveredComments  """  
      self.InOurCost:int = obj["InOurCost"]
      """  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Reporting currency value of this field  """  
      self.InVendorUnitCost:int = obj["InVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.DocInVendorUnitCost:int = obj["DocInVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1InVendorUnitCost:int = obj["Rpt1InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InVendorUnitCost:int = obj["Rpt2InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InVendorUnitCost:int = obj["Rpt3InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.SupplierUnInvcReceiptQty:int = obj["SupplierUnInvcReceiptQty"]
      """  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  """  
      self.OurUnInvcReceiptQty:int = obj["OurUnInvcReceiptQty"]
      """  Value that indicates the un-invoiced quantity of the receipt.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  """  
      self.InLCMtlBurUnitCost:int = obj["InLCMtlBurUnitCost"]
      """  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeBackoutRequired:bool = obj["AttributeBackoutRequired"]
      """  AttributeBackoutRequired  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.AsmPartDescription:str = obj["AsmPartDescription"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      """  Consolidated PO flag.  Used in Consolidated Purchasing.  """  
      self.ContainerExtCost:int = obj["ContainerExtCost"]
      """  This is the extended cost of the container detail item this RcvDtl entry is tied to.  """  
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      """  Container Detail Landed Cost Amount  """  
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableInspection:bool = obj["DisableInspection"]
      """  Flag to set disable/enable the InspectionReq field.  """  
      self.DisplayUMField:str = obj["DisplayUMField"]
      """  Indicates whether the IUM or DUM field should be displayed/enabled  """  
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.DocScrVendorUnitCost:int = obj["DocScrVendorUnitCost"]
      """  PO currency value of this field  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  DropShipment  """  
      self.DueDate:str = obj["DueDate"]
      """  PORel.DueDate  """  
      self.EnableBin:bool = obj["EnableBin"]
      self.EnableDim:bool = obj["EnableDim"]
      """  Indicates whether to enable/disable the dimension fields  """  
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.EnableLot:bool = obj["EnableLot"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether to Enable the Serial Number button  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.EnableWhse:bool = obj["EnableWhse"]
      self.ExtCost:int = obj["ExtCost"]
      """  Extended receipt detail cost.  """  
      self.HHReceiveToPCID:bool = obj["HHReceiveToPCID"]
      """  This is true when using the Receive To PCID option in HH PO Receipt.  """  
      self.InputOurQty:int = obj["InputOurQty"]
      """  OurQty not divided by dimension conversion factor for entry.  """  
      self.InspectionFlag:bool = obj["InspectionFlag"]
      """  Flag used to switch other Received To's to Pur-Ins  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Link to the IMRcvDtl table  """  
      self.JobIUM:str = obj["JobIUM"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.JobRequiredQty:int = obj["JobRequiredQty"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.MangCustID:str = obj["MangCustID"]
      self.MangCustName:str = obj["MangCustName"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.MassReceipt:bool = obj["MassReceipt"]
      """  Indicates if created through Mass Receipts  """  
      self.OnTime:str = obj["OnTime"]
      self.OpenRelease:bool = obj["OpenRelease"]
      self.OrderQty:int = obj["OrderQty"]
      self.OurRemQty:int = obj["OurRemQty"]
      """  Our Remaining Quantity  """  
      self.PCIDOutboundContainer:bool = obj["PCIDOutboundContainer"]
      """  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  Package Control Header Status  """  
      self.Plant:str = obj["Plant"]
      """  The Plant to which the warehouse belongs to  """  
      self.POComment:str = obj["POComment"]
      self.PODueDate:str = obj["PODueDate"]
      """  PO Line Due Date  """  
      self.POFactor:int = obj["POFactor"]
      self.POFactorDirection:str = obj["POFactorDirection"]
      self.POHold:bool = obj["POHold"]
      self.POIUM:str = obj["POIUM"]
      self.POPUM:str = obj["POPUM"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      """  The total quantity that has arrived for this purchase order release.  """  
      self.PORelStatus:str = obj["PORelStatus"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  """  
      self.RcvdSMIQty:int = obj["RcvdSMIQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  PORel Received Qty for MassReceipts  """  
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1ScrVendorUnitCost:int = obj["Rpt1ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrVendorUnitCost:int = obj["Rpt2ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrVendorUnitCost:int = obj["Rpt3ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.ScrOurUnitCost:int = obj["ScrOurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.ScrVendorUnitCost:int = obj["ScrVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  """  
      self.SearchPONum:int = obj["SearchPONum"]
      self.Selected:bool = obj["Selected"]
      self.SetToLocation:bool = obj["SetToLocation"]
      """  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  """  
      self.SkipMaterialQueueCreation:bool = obj["SkipMaterialQueueCreation"]
      """  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  """  
      self.SMIComplete:bool = obj["SMIComplete"]
      self.SNStusChanged:bool = obj["SNStusChanged"]
      self.TagMtlSeq:int = obj["TagMtlSeq"]
      """  MtlSeq used in PrintTag option  """  
      self.TagOprSeq:int = obj["TagOprSeq"]
      """  Operation Sequence used in PrintTag  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  """  
      self.TotLineAmt:int = obj["TotLineAmt"]
      """  Receipt line amount using vendor unit cost.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.VendorCurrSymbol:str = obj["VendorCurrSymbol"]
      self.VenRemQty:int = obj["VenRemQty"]
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.PCIDStatusChanged:bool = obj["PCIDStatusChanged"]
      """  Indicates if the status of the PCID has changed since the receipt took place.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.SerialNoAttributeSetID:int = obj["SerialNoAttributeSetID"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackSlipInPrice:bool = obj["PackSlipInPrice"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumConfirmed:bool = obj["PONumConfirmed"]
      self.PONumApprovalStatus:str = obj["PONumApprovalStatus"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumApprove:bool = obj["PONumApprove"]
      self.PurchCodePurchDesc:str = obj["PurchCodePurchDesc"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointName:str = obj["PurPointName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RcvDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackLine:int = obj["GlbPackLine"]
      """  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country (defaults from Part Country of Origin).  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  Duty Amount portion of the landed cost for this receipt line.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  Indirect Cost portion of the landed cost for this receipt line.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate that the receipt line has been received.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.POType:str = obj["POType"]
      """  Identifier of associated PO ('Std', 'CMI', 'SMI')  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      """  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1VendorUnitCost:int = obj["Rpt1VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2VendorUnitCost:int = obj["Rpt2VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3VendorUnitCost:int = obj["Rpt3VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  """  
      self.ICPackNum:int = obj["ICPackNum"]
      """  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  """  
      self.ShipRcv:str = obj["ShipRcv"]
      """  Shipment Received  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Can be different from value on header.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Can be different from value on header.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Can be different from Header value.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SearchPONum:int = obj["SearchPONum"]
      self.InputOurQty:int = obj["InputOurQty"]
      """  OurQty not divided by dimension conversion factor for entry  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether to Enable the Serial Number button  """  
      self.DisplayUMField:str = obj["DisplayUMField"]
      """  Indicates whether the IUM or DUM field should be displayed/enabled  """  
      self.EnableLot:bool = obj["EnableLot"]
      self.JobRequiredQty:int = obj["JobRequiredQty"]
      self.JobIUM:str = obj["JobIUM"]
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.EnableBin:bool = obj["EnableBin"]
      self.EnableWhse:bool = obj["EnableWhse"]
      self.TagMtlSeq:int = obj["TagMtlSeq"]
      """  MtlSeq used in PrintTag option  """  
      self.TagOprSeq:int = obj["TagOprSeq"]
      """  Operation Sequence used in PrintTag  """  
      self.InspectionFlag:bool = obj["InspectionFlag"]
      """  Flag used to switch other Received To's to Pur-Ins  """  
      self.PODueDate:str = obj["PODueDate"]
      """  PO Line Due Date  """  
      self.VenRemQty:int = obj["VenRemQty"]
      self.OurRemQty:int = obj["OurRemQty"]
      """  Our Remaining Quantity  """  
      self.POPUM:str = obj["POPUM"]
      self.POIUM:str = obj["POIUM"]
      self.POFactor:int = obj["POFactor"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.POHold:bool = obj["POHold"]
      self.OrderQty:int = obj["OrderQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  PORel Received Qty for MassReceipts  """  
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Link to the IMRcvDtl table  """  
      self.EnableDim:bool = obj["EnableDim"]
      """  Indicates whether to enable/disable the dimension fields  """  
      self.POComment:str = obj["POComment"]
      self.MassReceipt:bool = obj["MassReceipt"]
      """  Indicates if created through Mass Receipts  """  
      self.AsmPartDescription:str = obj["AsmPartDescription"]
      self.DisableInspection:bool = obj["DisableInspection"]
      """  Flag to set disable/enable the InspectionReq field.  """  
      self.Plant:str = obj["Plant"]
      """  The Plant to which the warehouse belongs to  """  
      self.SetToLocation:bool = obj["SetToLocation"]
      """  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      self.DueDate:str = obj["DueDate"]
      """  PORel.DueDate  """  
      self.OnTime:str = obj["OnTime"]
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      """  Container Detail Landed Cost Amount  """  
      self.POFactorDirection:str = obj["POFactorDirection"]
      self.ContainerExtCost:int = obj["ContainerExtCost"]
      """  This is the extended cost of the container detail item this RcvDtl entry is tied to.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.SNStusChanged:bool = obj["SNStusChanged"]
      self.DropShipment:bool = obj["DropShipment"]
      """  DropShipment  """  
      self.RcvdSMIQty:int = obj["RcvdSMIQty"]
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.ContractOrder:bool = obj["ContractOrder"]
      self.SMIComplete:bool = obj["SMIComplete"]
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.ExtCost:int = obj["ExtCost"]
      """  Extended receipt detail cost.  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.VendorCurrSymbol:str = obj["VendorCurrSymbol"]
      self.Selected:bool = obj["Selected"]
      self.MangCustID:str = obj["MangCustID"]
      self.MangCustName:str = obj["MangCustName"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.CommodityDescription:str = obj["CommodityDescription"]
      """  Full description of the Commodity Code.  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.InspectorIDName:str = obj["InspectorIDName"]
      """  Inspector's Full Name.  """  
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.PONumShipName:str = obj["PONumShipName"]
      """  defaults from the company file.  """  
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.PurchCodePurchDesc:str = obj["PurchCodePurchDesc"]
      """  Description of the purchase type. Appears in drop-down lists for selection.  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlListTableset:
   def __init__(self, obj):
      self.RcvDtlList:list[Erp_Tablesets_RcvDtlListRow] = obj["RcvDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RcvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """   A\P invoice entry sets this to "Yes" when the receipt detail line is invoiced.  A value of NO either means that the system was not configured to 'Save Receipts for Invoicing" when the receipt line was created or that it has not yet been invoiced via A/P.
(See RcvHead.SaveForInvoicing, RcvHead.Invoiced)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number on which this receipt detail was invoiced. This is updated from the A\P invoice entry process.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line on which this receipt detail was invoiced. Updated by the A\P invoice entry process.  """  
      self.PartNum:str = obj["PartNum"]
      """  Our Part Number of the item that has been received. Captured from the related PODetail.PartNum for receipts of PO item. Entered by the user for miscellaneous receipts in which case it can't be blank. It must be valid in the Part file for receipt to stock.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID that received the item.  Only applicable for receipt to stock. Must be valid in the PartWhse file.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location of the warehouse which received the item. Only applicable for a receipt of Stock.  """  
      self.OurQty:int = obj["OurQty"]
      """  Receipt quantity in our unit of measure.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of Measure.  """  
      self.OurUnitCost:int = obj["OurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that received the item. Only applicable for receipt to Job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence # that the receipt was made against. Only applicable for receipt to job.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "S" = SubContract Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record to which this receipt was made against. Only applicable for a receipt to job.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.TranReference:str = obj["TranReference"]
      """  A generic fill-in field that could be used to allow the user to enter data such as Heat, Lot #'s.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.VendorUnitCost:int = obj["VendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  An internal flag which indicates if this is a receipt of a Purchase Order (P) or Miscellaneous (M) item. If "P" then this record is related to a PORel record. If "M" there is no PO reference. the transaction.  """  
      self.ReceivedTo:str = obj["ReceivedTo"]
      """  Indicates where the item is received to. Items can be received to a Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN")  """  
      self.ReceivedComplete:bool = obj["ReceivedComplete"]
      """   Indicates if this receipt transaction should flag the related purchase order release (PORel) as being received complete (PORel.OpenRelease = No).  When the user toggles this field   Receipt entry considers it  a direct update to the PORel.OpenRelease flag.  What we mean is that the user can change the PORel.OpenRelease flag by maintaining this field on  ANY related receipt transaction for the PORel. Therefore this field should not be used to determine the true status of the PORel record.
Receipt Entry allows displays this field based on the current setting of PORel.OpenRelease field. Another point is that if the a receipt transaction is update to a different PO/Line/Release the original PORel will be reopened if there are no other receipt detail records that indicate the release is closed.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """   Indicates if this receipt transaction should flag the related job material/subcontract as being issued complete. (JobMtl.IssuedComplete/JobOper.OpComplete)   When the user toggles this field Receipt entry considers it  a direct update to the job record.  What we mean is that the user can change the status of the job record by maintaining this field on  ANY related receipt transaction. Therefore this field should not be used to determine the true status of the JobMtl/JobOper record.
Receipt Entry allows displays this field based on the current status of JobMtl/JobOper field. Another point is that if the a receipt transaction is update to a different job record, the original Job record will be reopened if there are no other receipt detail records that indicate that it is complete.  All this Open/Close logic occurs in the write trigger of RcvDtl.  """  
      self.PUM:str = obj["PUM"]
      """  Vendor's selling Unit of Measure.  """  
      self.VenPartNum:str = obj["VenPartNum"]
      """  Vendor's Part Number. Defaulted from PODetail.  """  
      self.CostPerCode:str = obj["CostPerCode"]
      """  Indicates the costing per quantity.  This is copied from the PODetail.CostPerCode at time of receipt entry. A/P Invoice entry uses it when creating the invoice line item for the receipt. Values are "E" = per each, "C" = per hundred,  "M" = per thousand.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.NumLabels:int = obj["NumLabels"]
      """  Number of labels  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure. Cannot be blank. Defaults to part's unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.InspectionReq:bool = obj["InspectionReq"]
      """  Indicates if this receipt will be categorized as requiring inspection. It is set to Yes if any of the related Vendor, PartClass, PoDetail, JobMtl, JobOper have their RcvInspectionReq field = Yes.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """   Indicates if the receipt is pending inspection.
Set to Yes  if InspectionReq = Yes. Set to No after receipt has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectedDate:str = obj["InspectedDate"]
      """  Date when item was inspected.  """  
      self.InspectedTime:int = obj["InspectedTime"]
      """   Time of day when inspection transaction was recorded.
(seconds since midnight format)  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt date. Mirror image of related RCVHead.ReceiptDate.  Maintained by the RcvHead/RcvDtl write triggers.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Only used if failing quantity from inspection.  """  
      self.TotCostVariance:int = obj["TotCostVariance"]
      """  Total Purchase Price Variance amount placed on a receipt in inspection when the variance is received.  Only set if the receipt is currently in inspection (not moved to DMR, job, or stock).  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.NonConformnce:bool = obj["NonConformnce"]
      """  Indicates if the transaction is a non-conformance type transaction.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this part.  """  
      self.OurMtlBurUnitCost:int = obj["OurMtlBurUnitCost"]
      """   Mtl Bur Unit cost base on our unit of measure. The mtl burden rate
defaults from the Part file.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.PurchCode:str = obj["PurchCode"]
      """  If the ExtCompany.APPurchType field is yes, then this field cannot be blank (EuroFin)  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackLine:int = obj["GlbPackLine"]
      """  Global Packing Slip Line identifier.  Used in Consolidated Purchasing.  """  
      self.DocUnitCost:int = obj["DocUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Volume:int = obj["Volume"]
      """  Container volume, frequently specified in cubic sq feet.  """  
      self.Rpt1UnitCost:int = obj["Rpt1UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCost:int = obj["Rpt2UnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCost:int = obj["Rpt3UnitCost"]
      """  Reporting currency value of this field  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Num related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order line related to the purchase order that is being received. Used only for Buy To Order POs.  """  
      self.OrigCountryNum:int = obj["OrigCountryNum"]
      """  Country Number of the Origin Country (defaults from Part Country of Origin).  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  Duty Amount portion of the landed cost for this receipt line.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  Indirect Cost portion of the landed cost for this receipt line.  """  
      self.POTransValue:int = obj["POTransValue"]
      """  This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ExtTransValue:int = obj["ExtTransValue"]
      """  This is the PO Base Transaction Value plus all indirect costs which are marked to include as transaction value costs.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate that the receipt line has been received.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System (HS) goods classification code.  """  
      self.POType:str = obj["POType"]
      """  Identifier of associated PO ('Std', 'CMI', 'SMI')  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  Flag representing whether or not this receipt was auto generated by the consumption process (GenSMIReceipt.p).  This is only pertinent for SMI type PO Receipts.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """   Qualifies the unit of measure of the Volume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  if Part.NetVolumeUOM is not known.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment detail arrived. Defaults as current system date.  """  
      self.LCSpecLineDutyAmt:int = obj["LCSpecLineDutyAmt"]
      """  This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.LCAmt:int = obj["LCAmt"]
      """  The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.LCMtlBurUnitCost:int = obj["LCMtlBurUnitCost"]
      """  Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.DocVendorUnitCost:int = obj["DocVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1VendorUnitCost:int = obj["Rpt1VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2VendorUnitCost:int = obj["Rpt2VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3VendorUnitCost:int = obj["Rpt3VendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its destination, that can be Inventory, Job Material, Job Subcontract, Sales Order.  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  Originally defaults from PORel.MangCustNum.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegNumCnfg.  """  
      self.ICPackNum:int = obj["ICPackNum"]
      """  Relation between this RcvDtl and the ShipHead.PackNum where this Intercompany Shipment originated.  """  
      self.ShipRcv:str = obj["ShipRcv"]
      """  Shipment Received  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Can be different from value on header.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Can be different from value on header.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Can be different from Header value.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.QtyOption:str = obj["QtyOption"]
      """  It indicates the option of what type of quantity will be able to be changed in the POLine. The actual options are "Our" and "Supplier"  """  
      self.ConvOverride:bool = obj["ConvOverride"]
      """  When True, the Supplier Quantity field is entered directly instead of being calculated from Our Quantity with a UOM conversion  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.SMITransNum:int = obj["SMITransNum"]
      """  Used to identify what has been consumed during an SMI Receipt for a particular transaction.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.Delivered:bool = obj["Delivered"]
      """  Delivered  """  
      self.DeliveredComments:str = obj["DeliveredComments"]
      """  DeliveredComments  """  
      self.InOurCost:int = obj["InOurCost"]
      """  Internal usage for inclusive taxes - Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.DocInUnitCost:int = obj["DocInUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.Rpt1InUnitCost:int = obj["Rpt1InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitCost:int = obj["Rpt2InUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitCost:int = obj["Rpt3InUnitCost"]
      """  Reporting currency value of this field  """  
      self.InVendorUnitCost:int = obj["InVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the OurlUnitCost field which is used as cost to job or stock.  """  
      self.DocInVendorUnitCost:int = obj["DocInVendorUnitCost"]
      """  PO currency value of this field  """  
      self.Rpt1InVendorUnitCost:int = obj["Rpt1InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2InVendorUnitCost:int = obj["Rpt2InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3InVendorUnitCost:int = obj["Rpt3InVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.SupplierUnInvcReceiptQty:int = obj["SupplierUnInvcReceiptQty"]
      """  Value that indicates the remaining quantity of the receipt that is waiting to be invoiced.  """  
      self.OurUnInvcReceiptQty:int = obj["OurUnInvcReceiptQty"]
      """  Value that indicates the un-invoiced quantity of the receipt.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  ** NOT USED TO BE DROPPED 10.2 ** The Tax Liability for this Receipt line  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Receipt line. Used as a default to Order line items or Invoice line items. Can be left blank which indicates item is taxable. If entered must be valid in the TaxCat master file.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Indicates if the Receipt line is Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from tax for this receipt line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a receipt line, if this is set to True the tax engine will not calculate any receipt detail line tax information  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt line.  This is the actual cost that will determine the MtlBurUnitCost of the receipt transaction.  """  
      self.InLCAmt:int = obj["InLCAmt"]
      """  Internal usage for inclusive taxes - The total amount of disbursed landed cost for this receipt detail.  This amount includes the duties and indirect costs per receipt line. The total disbursed LCAmt is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - Duty Amount portion of the landed cost for this receipt line.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - Indirect Cost portion of the landed cost for this receipt line.  """  
      self.InLCMtlBurUnitCost:int = obj["InLCMtlBurUnitCost"]
      """  Internal usage for inclusive taxes - Landed Cost calculated Mtl Bur Unit Cost based on our unit of measure.  The value of this field is copied to the OurMtlBurUnitCost when the Landed Cost is disbursed and applied to the receipt line.  """  
      self.InLCSpecLineDutyAmt:int = obj["InLCSpecLineDutyAmt"]
      """  Internal usage for inclusive taxes - This is the prorated portion of the Specific Duty Amount based on the line tariffs as factor. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt line. The total disbursed LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and LCSpecLineDutyAmt.  """  
      self.InPOTransValue:int = obj["InPOTransValue"]
      """  Internal usage for inclusive taxes - This is by default the PO line value (including discounts, excluding VAT/Sales Tax) but can be overriden by the user.  It is a system option allowing the user to update this base transaction value manually.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  ProjProcessed  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  This will contain the non deductable tax portion for this Receipt line.  This will be calculated based on the Receipt Header or Receipt Line tax records depending on the Tax Liability type and Company Tax Configuration.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeBackoutRequired:bool = obj["AttributeBackoutRequired"]
      """  AttributeBackoutRequired  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if landed cost info can be updated.  """  
      self.AsmPartDescription:str = obj["AsmPartDescription"]
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      """  Consolidated PO flag.  Used in Consolidated Purchasing.  """  
      self.ContainerExtCost:int = obj["ContainerExtCost"]
      """  This is the extended cost of the container detail item this RcvDtl entry is tied to.  """  
      self.ContainerLCAmt:int = obj["ContainerLCAmt"]
      """  Container Detail Landed Cost Amount  """  
      self.ContractOrder:bool = obj["ContractOrder"]
      self.CostPerFactor:int = obj["CostPerFactor"]
      """  Interger value of CostPerCode  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.DisableInspection:bool = obj["DisableInspection"]
      """  Flag to set disable/enable the InspectionReq field.  """  
      self.DisplayUMField:str = obj["DisplayUMField"]
      """  Indicates whether the IUM or DUM field should be displayed/enabled  """  
      self.DocScrUnitCost:int = obj["DocScrUnitCost"]
      """  item's unit cost in the vendors unit of measure and currency.  Default can be obtained from the PODetail.DocUnitCost if related.  """  
      self.DocScrVendorUnitCost:int = obj["DocScrVendorUnitCost"]
      """  PO currency value of this field  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  DropShipment  """  
      self.DueDate:str = obj["DueDate"]
      """  PORel.DueDate  """  
      self.EnableBin:bool = obj["EnableBin"]
      self.EnableDim:bool = obj["EnableDim"]
      """  Indicates whether to enable/disable the dimension fields  """  
      self.EnableInventoryAttributes:bool = obj["EnableInventoryAttributes"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.EnableLot:bool = obj["EnableLot"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  Internal flag used for the row rules to control whether the PCID columns should be enabled or not.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether to Enable the Serial Number button  """  
      self.EnableSupplierXRef:bool = obj["EnableSupplierXRef"]
      """  Use this field to enable\disable the Supplier Part XRef button  """  
      self.EnableTransValue:bool = obj["EnableTransValue"]
      """  Flag to indicate if PO Trans Value can be updated.  """  
      self.EnableUplift:bool = obj["EnableUplift"]
      """  Flag to indicate if UpliftPercent can be updated.  """  
      self.EnableWhse:bool = obj["EnableWhse"]
      self.ExtCost:int = obj["ExtCost"]
      """  Extended receipt detail cost.  """  
      self.HHReceiveToPCID:bool = obj["HHReceiveToPCID"]
      """  This is true when using the Receive To PCID option in HH PO Receipt.  """  
      self.InputOurQty:int = obj["InputOurQty"]
      """  OurQty not divided by dimension conversion factor for entry.  """  
      self.InspectionFlag:bool = obj["InspectionFlag"]
      """  Flag used to switch other Received To's to Pur-Ins  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Link to the IMRcvDtl table  """  
      self.JobIUM:str = obj["JobIUM"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.JobRequiredQty:int = obj["JobRequiredQty"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.MangCustID:str = obj["MangCustID"]
      self.MangCustName:str = obj["MangCustName"]
      self.ManualLC:bool = obj["ManualLC"]
      """  Flag to indicate if LCIdCost can be manually updated.  """  
      self.MassReceipt:bool = obj["MassReceipt"]
      """  Indicates if created through Mass Receipts  """  
      self.OnTime:str = obj["OnTime"]
      self.OpenRelease:bool = obj["OpenRelease"]
      self.OrderQty:int = obj["OrderQty"]
      self.OurRemQty:int = obj["OurRemQty"]
      """  Our Remaining Quantity  """  
      self.PCIDOutboundContainer:bool = obj["PCIDOutboundContainer"]
      """  Linked to the outbound container flag taken from either the PkgControlStageHeader / PkgControlHeader.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  Package Control Header Status  """  
      self.Plant:str = obj["Plant"]
      """  The Plant to which the warehouse belongs to  """  
      self.POComment:str = obj["POComment"]
      self.PODueDate:str = obj["PODueDate"]
      """  PO Line Due Date  """  
      self.POFactor:int = obj["POFactor"]
      self.POFactorDirection:str = obj["POFactorDirection"]
      self.POHold:bool = obj["POHold"]
      self.POIUM:str = obj["POIUM"]
      self.POPUM:str = obj["POPUM"]
      self.PORelArrivedQty:int = obj["PORelArrivedQty"]
      """  The total quantity that has arrived for this purchase order release.  """  
      self.PORelStatus:str = obj["PORelStatus"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Closed (C), Voided (V).  """  
      self.RcvdSMIQty:int = obj["RcvdSMIQty"]
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  PORel Received Qty for MassReceipts  """  
      self.RemainingSMIQty:int = obj["RemainingSMIQty"]
      self.Rpt1ScrUnitCost:int = obj["Rpt1ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt1ScrVendorUnitCost:int = obj["Rpt1ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrUnitCost:int = obj["Rpt2ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2ScrVendorUnitCost:int = obj["Rpt2ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrUnitCost:int = obj["Rpt3ScrUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3ScrVendorUnitCost:int = obj["Rpt3ScrVendorUnitCost"]
      """  Reporting currency value of this field  """  
      self.ScrOurUnitCost:int = obj["ScrOurUnitCost"]
      """  Unit cost base on our unit of measure. Defaults from PODetail.IUM for purchase order receipt.  """  
      self.ScrVendorUnitCost:int = obj["ScrVendorUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. RIO- With the currency module it is calculated based on the current exchange rate.  This is defaulted from the POdetail record. PO receipts uses this along with the calculated purchasing conversion factor to determine  """  
      self.SearchPONum:int = obj["SearchPONum"]
      self.Selected:bool = obj["Selected"]
      self.SetToLocation:bool = obj["SetToLocation"]
      """  This boolean is set by the user in Receipt Entry to initiate the SetToLocation logic for this line.  """  
      self.SkipMaterialQueueCreation:bool = obj["SkipMaterialQueueCreation"]
      """  When this flag is true, skip the Material Queue creation logic for the current RcvDtl line.  """  
      self.SMIComplete:bool = obj["SMIComplete"]
      self.SNStusChanged:bool = obj["SNStusChanged"]
      self.TagMtlSeq:int = obj["TagMtlSeq"]
      """  MtlSeq used in PrintTag option  """  
      self.TagOprSeq:int = obj["TagOprSeq"]
      """  Operation Sequence used in PrintTag  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.ThisTranUOM:str = obj["ThisTranUOM"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvDtl.LCSpecLineDutyAmt + RcvDtl.LCDutyAmt  """  
      self.TotLineAmt:int = obj["TotLineAmt"]
      """  Receipt line amount using vendor unit cost.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.UsePurchaseCode:bool = obj["UsePurchaseCode"]
      self.VendorCurrSymbol:str = obj["VendorCurrSymbol"]
      self.VenRemQty:int = obj["VenRemQty"]
      self.AllowUpdSuppPrice:bool = obj["AllowUpdSuppPrice"]
      """  It is true, if RcvDtl.ReceipteType = 'P' and XbSyst.AllowUpdSuppPrice is true.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.PCIDStatusChanged:bool = obj["PCIDStatusChanged"]
      """  Indicates if the status of the PCID has changed since the receipt took place.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      self.SerialNoAttributeSetID:int = obj["SerialNoAttributeSetID"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CommodityDescription:str = obj["CommodityDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PackSlipInPrice:bool = obj["PackSlipInPrice"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumConfirmed:bool = obj["PONumConfirmed"]
      self.PONumApprovalStatus:str = obj["PONumApprovalStatus"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumApprove:bool = obj["PONumApprove"]
      self.PurchCodePurchDesc:str = obj["PurchCodePurchDesc"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointName:str = obj["PurPointName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.WareHouseCodeDescription:str = obj["WareHouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RcvDtlSearchTableset:
   def __init__(self, obj):
      self.RcvDtl:list[Erp_Tablesets_RcvDtlRow] = obj["RcvDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRcvDtlSearchTableset:
   def __init__(self, obj):
      self.RcvDtl:list[Erp_Tablesets_RcvDtlRow] = obj["RcvDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   purPoint
   packSlip
   packLine
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.packLine:int = obj["packLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RcvDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRcvDtl_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   packSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      pass

class GetNewRcvDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRcvDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRcvDtl:str = obj["whereClauseRcvDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtRcvDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRcvDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RcvDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

