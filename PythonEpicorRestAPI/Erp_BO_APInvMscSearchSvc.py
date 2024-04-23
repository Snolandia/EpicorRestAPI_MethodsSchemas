import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APInvMscSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APInvMscSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APInvMscSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APInvMscSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches",headers=creds) as resp:
           return await resp.json()

async def post_APInvMscSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APInvMscSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APInvMscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APInvMscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APInvMscSearches_Company_VendorNum_InvoiceNum_InvoiceLine_MscNum(Company, VendorNum, InvoiceNum, InvoiceLine, MscNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APInvMscSearch item
   Description: Calls GetByID to retrieve the APInvMscSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APInvMscSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param MscNum: Desc: MscNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APInvMscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + "," + MscNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APInvMscSearches_Company_VendorNum_InvoiceNum_InvoiceLine_MscNum(Company, VendorNum, InvoiceNum, InvoiceLine, MscNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APInvMscSearch for the service
   Description: Calls UpdateExt to update APInvMscSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APInvMscSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param MscNum: Desc: MscNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APInvMscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + "," + MscNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APInvMscSearches_Company_VendorNum_InvoiceNum_InvoiceLine_MscNum(Company, VendorNum, InvoiceNum, InvoiceLine, MscNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APInvMscSearch item
   Description: Call UpdateExt to delete APInvMscSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APInvMscSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param MscNum: Desc: MscNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/APInvMscSearches(" + Company + "," + VendorNum + "," + InvoiceNum + "," + InvoiceLine + "," + MscNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APInvMscListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPInvMsc, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPInvMsc=" + whereClauseAPInvMsc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, invoiceNum, invoiceLine, mscNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
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
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceLine=" + invoiceLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mscNum=" + mscNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPInvMsc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPInvMsc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPInvMsc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPInvMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPInvMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APInvMscSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvMscListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APInvMscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APInvMscRow] = obj["value"]
      pass

class Erp_Tablesets_APInvMscListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  """  
      self.MscNum:int = obj["MscNum"]
      """  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  miscellaneous amount.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  miscellaneous amount in the vendor currency.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number of the Miscellaneous Charge  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.GlbMscNum:int = obj["GlbMscNum"]
      """  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InvExpSeq:int = obj["InvExpSeq"]
      """  Reference to the APInvExp record that contains the gl distribution for this charge.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the AP Miscellaneous Charge is for Landed Cost.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Container Shipment ID (also known as the ContainerID).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID of the associated receipt's indirect cost.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the associated receipt's indirect cost.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.LCVendorNum:int = obj["LCVendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.RecordSource:str = obj["RecordSource"]
      self.Posted:bool = obj["Posted"]
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.LCEnabled:bool = obj["LCEnabled"]
      self.Selected:bool = obj["Selected"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  """  
      self.MscNum:int = obj["MscNum"]
      """  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  miscellaneous amount.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  miscellaneous amount in the vendor currency.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number of the Miscellaneous Charge  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.GlbMscNum:int = obj["GlbMscNum"]
      """  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InvExpSeq:int = obj["InvExpSeq"]
      """  Reference to the APInvExp record that contains the gl distribution for this charge.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the AP Miscellaneous Charge is for Landed Cost.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Container Shipment ID (also known as the ContainerID).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID of the associated receipt's indirect cost.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the associated receipt's indirect cost.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.LCVendorNum:int = obj["LCVendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  miscellaneous amount including taxes.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  miscellaneous amount in the vendor currency including taxes.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  Reserved for development  - logical  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Reserved for development  - character  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  NoTaxRecalc  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Gen1099Code  """  
      self.TaxExemptReasonCode:str = obj["TaxExemptReasonCode"]
      """  TaxExemptReasonCode  """  
      self.PlasticPackTaxReportID:str = obj["PlasticPackTaxReportID"]
      """  The Plastic Packaging Tax Report ID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DocScrTotalDedTax:int = obj["DocScrTotalDedTax"]
      self.DocScrTotalSATax:int = obj["DocScrTotalSATax"]
      self.DocScrTotalTax:int = obj["DocScrTotalTax"]
      self.GroupID:str = obj["GroupID"]
      self.InPrice:bool = obj["InPrice"]
      self.LCEnabled:bool = obj["LCEnabled"]
      self.Posted:bool = obj["Posted"]
      self.RecordSource:str = obj["RecordSource"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt1ScrTotalDedTax:int = obj["Rpt1ScrTotalDedTax"]
      self.Rpt1ScrTotalSATax:int = obj["Rpt1ScrTotalSATax"]
      self.Rpt1ScrTotalTax:int = obj["Rpt1ScrTotalTax"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt2ScrTotalDedTax:int = obj["Rpt2ScrTotalDedTax"]
      self.Rpt2ScrTotalSATax:int = obj["Rpt2ScrTotalSATax"]
      self.Rpt2ScrTotalTax:int = obj["Rpt2ScrTotalTax"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.Rpt3ScrTotalDedTax:int = obj["Rpt3ScrTotalDedTax"]
      self.Rpt3ScrTotalSATax:int = obj["Rpt3ScrTotalSATax"]
      self.Rpt3ScrTotalTax:int = obj["Rpt3ScrTotalTax"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.ScrTotalDedTax:int = obj["ScrTotalDedTax"]
      self.ScrTotalSATax:int = obj["ScrTotalSATax"]
      self.ScrTotalTax:int = obj["ScrTotalTax"]
      self.Selected:bool = obj["Selected"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   invoiceLine
   mscNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.mscNum:int = obj["mscNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APInvMscListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  """  
      self.MscNum:int = obj["MscNum"]
      """  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  miscellaneous amount.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  miscellaneous amount in the vendor currency.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number of the Miscellaneous Charge  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.GlbMscNum:int = obj["GlbMscNum"]
      """  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InvExpSeq:int = obj["InvExpSeq"]
      """  Reference to the APInvExp record that contains the gl distribution for this charge.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the AP Miscellaneous Charge is for Landed Cost.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Container Shipment ID (also known as the ContainerID).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID of the associated receipt's indirect cost.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the associated receipt's indirect cost.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.LCVendorNum:int = obj["LCVendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.DebitMemo:bool = obj["DebitMemo"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.RecordSource:str = obj["RecordSource"]
      self.Posted:bool = obj["Posted"]
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.LCEnabled:bool = obj["LCEnabled"]
      self.Selected:bool = obj["Selected"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
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
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvMscListTableset:
   def __init__(self, obj):
      self.APInvMscList:list[Erp_Tablesets_APInvMscListRow] = obj["APInvMscList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APInvMscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  Duplicated  from the related APInvHed record.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table. The system generates this number during entry of new detail records. The system determines next available number by finding the InvcDetl record for the Invoice and the adding 1 to it.  """  
      self.MscNum:int = obj["MscNum"]
      """  Number automatically assigned by invoice entry which is used along with VendorNum, InvoiceNum and InvoiceLine to uniquely identify the miscellaneous record within the invoice.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Code that relates this invoice miscellaneous charge to the PurMisc master. Entered via a DDSL widget.  """  
      self.Description:str = obj["Description"]
      """  Description of the miscellaneous charge. Defaulted from PurMisc.Description.  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  miscellaneous amount.  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  miscellaneous amount in the vendor currency.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that this miscellaneous record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  PO line number that this miscellaneous record is related to. If related to the PO Header then this field is zero.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence number of the Miscellaneous Charge  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """   Identifies Tax Category for this Misc. item.
Defaults from PurMisc.TaxCatID.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceNum:str = obj["GlbInvoiceNum"]
      """  Global Invoice identifier.  Used in Consolidated Purchasing.  """  
      self.GlbInvoiceLine:int = obj["GlbInvoiceLine"]
      """  Global Invoice Line identifier.  Used in Consolidated Purchasing.  """  
      self.GlbMscNum:int = obj["GlbMscNum"]
      """  Global Invoice Miscellaneous Charge identifier.  Used in Consolidated Purchasing.  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Reporting currency value of this field  """  
      self.InvExpSeq:int = obj["InvExpSeq"]
      """  Reference to the APInvExp record that contains the gl distribution for this charge.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the AP Miscellaneous Charge is for Landed Cost.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  The Container Shipment ID (also known as the ContainerID).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID of the associated receipt's indirect cost.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the associated receipt's indirect cost.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.LCVendorNum:int = obj["LCVendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  This field, together with the PackSlip and PurPoint, is used to link the APInvMsc to the RcvMisc record that references this misc charge as a Landed Cost's Indirect Cost.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Like PurMisc.LCDisburseMethod. Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.InMiscAmt:int = obj["InMiscAmt"]
      """  miscellaneous amount including taxes.  """  
      self.DocInMiscAmt:int = obj["DocInMiscAmt"]
      """  miscellaneous amount in the vendor currency including taxes.  """  
      self.Rpt1InMiscAmt:int = obj["Rpt1InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2InMiscAmt:int = obj["Rpt2InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3InMiscAmt:int = obj["Rpt3InMiscAmt"]
      """  Reporting currency value of this field  """  
      self.DevInt1:int = obj["DevInt1"]
      """  Reserved for Development - Integer  """  
      self.DevInt2:int = obj["DevInt2"]
      """  Reserved for Development - Integer  """  
      self.DevDec1:int = obj["DevDec1"]
      """  Reserved for development - decimal  """  
      self.DevDec2:int = obj["DevDec2"]
      """  Reserved for development - decimal  """  
      self.DevDec3:int = obj["DevDec3"]
      """  Reserved for development - decimal  """  
      self.DevDec4:int = obj["DevDec4"]
      """  Reserved for development - decimal  """  
      self.DevLog1:bool = obj["DevLog1"]
      """  Reserved for development  - logical  """  
      self.DevLog2:bool = obj["DevLog2"]
      """  Reserved for development - logical  """  
      self.DevChar1:str = obj["DevChar1"]
      """  Reserved for development  - character  """  
      self.DevChar2:str = obj["DevChar2"]
      """  Reserved for development - character  """  
      self.DevDate1:str = obj["DevDate1"]
      """  Reserved for development - date  """  
      self.DevDate2:str = obj["DevDate2"]
      """  Reserved for development - date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the AP Invoice Dtl was created by the Correction (Reversing) logic.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  NoTaxRecalc  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.Gen1099Code:str = obj["Gen1099Code"]
      """  Gen1099Code  """  
      self.TaxExemptReasonCode:str = obj["TaxExemptReasonCode"]
      """  TaxExemptReasonCode  """  
      self.PlasticPackTaxReportID:str = obj["PlasticPackTaxReportID"]
      """  The Plastic Packaging Tax Report ID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DocScrTotalDedTax:int = obj["DocScrTotalDedTax"]
      self.DocScrTotalSATax:int = obj["DocScrTotalSATax"]
      self.DocScrTotalTax:int = obj["DocScrTotalTax"]
      self.GroupID:str = obj["GroupID"]
      self.InPrice:bool = obj["InPrice"]
      self.LCEnabled:bool = obj["LCEnabled"]
      self.Posted:bool = obj["Posted"]
      self.RecordSource:str = obj["RecordSource"]
      self.Rpt1ScrMiscAmt:int = obj["Rpt1ScrMiscAmt"]
      self.Rpt1ScrTotalDedTax:int = obj["Rpt1ScrTotalDedTax"]
      self.Rpt1ScrTotalSATax:int = obj["Rpt1ScrTotalSATax"]
      self.Rpt1ScrTotalTax:int = obj["Rpt1ScrTotalTax"]
      self.Rpt2ScrMiscAmt:int = obj["Rpt2ScrMiscAmt"]
      self.Rpt2ScrTotalDedTax:int = obj["Rpt2ScrTotalDedTax"]
      self.Rpt2ScrTotalSATax:int = obj["Rpt2ScrTotalSATax"]
      self.Rpt2ScrTotalTax:int = obj["Rpt2ScrTotalTax"]
      self.Rpt3ScrMiscAmt:int = obj["Rpt3ScrMiscAmt"]
      self.Rpt3ScrTotalDedTax:int = obj["Rpt3ScrTotalDedTax"]
      self.Rpt3ScrTotalSATax:int = obj["Rpt3ScrTotalSATax"]
      self.Rpt3ScrTotalTax:int = obj["Rpt3ScrTotalTax"]
      self.ScrDocMiscAmt:int = obj["ScrDocMiscAmt"]
      self.ScrMiscAmt:int = obj["ScrMiscAmt"]
      self.ScrTotalDedTax:int = obj["ScrTotalDedTax"]
      self.ScrTotalSATax:int = obj["ScrTotalSATax"]
      self.ScrTotalTax:int = obj["ScrTotalTax"]
      self.Selected:bool = obj["Selected"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APInvMscSearchTableset:
   def __init__(self, obj):
      self.APInvMsc:list[Erp_Tablesets_APInvMscRow] = obj["APInvMsc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAPInvMscSearchTableset:
   def __init__(self, obj):
      self.APInvMsc:list[Erp_Tablesets_APInvMscRow] = obj["APInvMsc"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   invoiceNum
   invoiceLine
   mscNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.mscNum:int = obj["mscNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvMscSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvMscSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvMscSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APInvMscListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPInvMsc_input:
   """ Required : 
   ds
   vendorNum
   invoiceNum
   invoiceLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvMscSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      pass

class GetNewAPInvMsc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvMscSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPInvMsc
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPInvMsc:str = obj["whereClauseAPInvMsc"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APInvMscSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtAPInvMscSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPInvMscSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APInvMscSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APInvMscSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

