import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARInvcDtlSearchSvc
# Description: bo/ARInvcDtlSearch
           Search used to find AR Invoice Lines (InvcDtl)
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ARInvcDtlSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARInvcDtlSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARInvcDtlSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches",headers=creds) as resp:
           return await resp.json()

async def post_ARInvcDtlSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARInvcDtlSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARInvcDtlSearches_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARInvcDtlSearch item
   Description: Calls GetByID to retrieve the ARInvcDtlSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARInvcDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARInvcDtlSearches_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARInvcDtlSearch for the service
   Description: Calls UpdateExt to update ARInvcDtlSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARInvcDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARInvcDtlSearches_Company_InvoiceNum_InvoiceLine(Company, InvoiceNum, InvoiceLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARInvcDtlSearch item
   Description: Call UpdateExt to delete ARInvcDtlSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARInvcDtlSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/ARInvcDtlSearches(" + Company + "," + InvoiceNum + "," + InvoiceLine + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseInvcDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseInvcDtl=" + whereClauseInvcDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(invoiceNum, invoiceLine, epicorHeaders = None):
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
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceLine=" + invoiceLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListAlternalSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListAlternalSearch
   Description: Allows use of InvcHead filter but returns only InvcDtl records.
   OperationID: GetListAlternalSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListAlternalSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListAlternalSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARInvcDtlSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcDtlRow] = obj["value"]
      pass

class Erp_Tablesets_InvcDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.InPrice:bool = obj["InPrice"]
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.RADesc:str = obj["RADesc"]
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      """  Description of the Call Type Code.  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      """  Contact's middle name.  """  
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      """  Contact's first name.  """  
      self.CustCntName:str = obj["CustCntName"]
      """  Full name of the contact.  """  
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.CustCntLastName:str = obj["CustCntLastName"]
      """  Contact's last name.  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      """  Description  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      """  Country name  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line description.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
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
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      """  Description of the sales category.  """  
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustName:str = obj["ShipToCustName"]
      """  The full name of the customer.  """  
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description for the Tax Region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefRevPosted:bool = obj["DefRevPosted"]
      """  DefRevPosted  """  
      self.LinkedInvcUnitPrice:int = obj["LinkedInvcUnitPrice"]
      """  Unit price of Invoice linked to Bill of Exchange in original currency.  """  
      self.DspWithholdAmt:int = obj["DspWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.DocDspWithholdAmt:int = obj["DocDspWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1DspWithholdAmt:int = obj["Rpt1DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt2DspWithholdAmt:int = obj["Rpt2DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt3DspWithholdAmt:int = obj["Rpt3DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.LinkedCurrencyCode:str = obj["LinkedCurrencyCode"]
      """  Currency code from linked Invoice Header  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.PEBOEHeadNum:int = obj["PEBOEHeadNum"]
      """  PEBOEHeadNum  """  
      self.MXSellingShipQty:int = obj["MXSellingShipQty"]
      """  MXSellingShipQty  """  
      self.MXUnitPrice:int = obj["MXUnitPrice"]
      """  MXUnitPrice  """  
      self.DocMXUnitPrice:int = obj["DocMXUnitPrice"]
      """  DocMXUnitPrice  """  
      self.Rpt1MXUnitPrice:int = obj["Rpt1MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2MXUnitPrice:int = obj["Rpt2MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3MXUnitPrice:int = obj["Rpt3MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CustCostCenter:str = obj["CustCostCenter"]
      """  CustCostCenter  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DefRevEndDate:str = obj["DefRevEndDate"]
      """  DefRevEndDate  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.Reclassified:bool = obj["Reclassified"]
      """  Indicates tha this invoice Line was reclassified.  """  
      self.PartiallyDefer:bool = obj["PartiallyDefer"]
      """  Enables the user the ability to override the Percent or Amount of revenue to be deferred  """  
      self.DeferredPercent:int = obj["DeferredPercent"]
      """  Percentage of revenue to be deferred for this line item  """  
      self.Reclass:bool = obj["Reclass"]
      """  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  """  
      self.DeferredOnly:bool = obj["DeferredOnly"]
      """  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  """  
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      """  Reclassification Code. This field will be required if Reclass is checked.  """  
      self.ReclassReasonCode:str = obj["ReclassReasonCode"]
      """  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  """  
      self.ReclassComments:str = obj["ReclassComments"]
      """  Internal comments for reclassification entered by the user.  """  
      self.DeferredRevAmt:int = obj["DeferredRevAmt"]
      """  Deferred Revenue Amount in base currency  """  
      self.DocDeferredRevAmt:int = obj["DocDeferredRevAmt"]
      """  Deferred Revenue Amount in document currency  """  
      self.Rpt1DeferredRevAmt:int = obj["Rpt1DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt2DeferredRevAmt:int = obj["Rpt2DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt3DeferredRevAmt:int = obj["Rpt3DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.ChargeReclass:bool = obj["ChargeReclass"]
      """  ChargeReclass  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.DropShipPONum:int = obj["DropShipPONum"]
      """  DropShipPONum  """  
      self.DocInAdvanceBillCredit:int = obj["DocInAdvanceBillCredit"]
      """  DocInAdvanceBillCredit  """  
      self.InAdvanceBillCredit:int = obj["InAdvanceBillCredit"]
      """  InAdvanceBillCredit  """  
      self.Rpt1InAdvanceBillCredit:int = obj["Rpt1InAdvanceBillCredit"]
      """  Rpt1InAdvanceBillCredit  """  
      self.Rpt2InAdvanceBillCredit:int = obj["Rpt2InAdvanceBillCredit"]
      """  Rpt2InAdvanceBillCredit  """  
      self.Rpt3InAdvanceBillCredit:int = obj["Rpt3InAdvanceBillCredit"]
      """  Rpt3InAdvanceBillCredit  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  ConsolidateLines  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this invoice line was created from.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PETaxExempt:str = obj["PETaxExempt"]
      """  PETaxExempt  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the Invoicing Company.  """  
      self.CColOrderLine:int = obj["CColOrderLine"]
      """  Order number line the Invoicing Company.  """  
      self.CColOrderRel:int = obj["CColOrderRel"]
      """  Order number release the Invoicing Company.  """  
      self.CColInvoiceLineRef:int = obj["CColInvoiceLineRef"]
      """  Invoice Line reference on the Invoicing Company.  """  
      self.CColPackNum:int = obj["CColPackNum"]
      """  Packing slip number on the Invoicing Company.  """  
      self.CColPackLine:int = obj["CColPackLine"]
      """  Packing slip line number on the Invoicing Company.  """  
      self.CColDropShipPackSlip:str = obj["CColDropShipPackSlip"]
      """  Drop shipment packing slip number on the Invoicing Company.  """  
      self.CColDropShipPackSlipLine:int = obj["CColDropShipPackSlipLine"]
      """  Drop shipment packing slip line number on the Invoicing Company.  """  
      self.CColShipToCustID:str = obj["CColShipToCustID"]
      """  Ship To Customer ID from the Invoice Line in the subsidiary company.  """  
      self.CColShipToNum:str = obj["CColShipToNum"]
      """  Ship To from the Invoice Line in the subsidiary company.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.ServiceSource:str = obj["ServiceSource"]
      """  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Mtl seq used to create invoice line from service call job  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job subcontract oper seq used to create invoice line from service call job  """  
      self.LaborType:str = obj["LaborType"]
      """  Indicates the labor type of the LaborDtl used to create invoice from service call job.  """  
      self.BillableLaborHrs:int = obj["BillableLaborHrs"]
      """  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable rate used to create invoice line from labor related to service call job. In base currency.  """  
      self.ServiceSourceType:str = obj["ServiceSourceType"]
      """  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.AllowUpdPartDefer:bool = obj["AllowUpdPartDefer"]
      """  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CNGTIDescription1:str = obj["CNGTIDescription1"]
      self.CNGTIDescription2:str = obj["CNGTIDescription2"]
      self.CNGTIDescription3:str = obj["CNGTIDescription3"]
      self.CNGTIDiscountTaxAmount:int = obj["CNGTIDiscountTaxAmount"]
      """  CSF China, discount tax amount  """  
      self.CNGTIIUM:str = obj["CNGTIIUM"]
      self.CNGTINetAmount:int = obj["CNGTINetAmount"]
      self.CNGTIPartDescription:str = obj["CNGTIPartDescription"]
      self.CNGTISpecification:str = obj["CNGTISpecification"]
      self.CNGTITaxAmount:int = obj["CNGTITaxAmount"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.CNGTITaxPercent:int = obj["CNGTITaxPercent"]
      self.CNGTITotalAmount:int = obj["CNGTITotalAmount"]
      self.CNGTIUnitPrice:int = obj["CNGTIUnitPrice"]
      """  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  """  
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.EmpID:str = obj["EmpID"]
      """  FSA Technician  """  
      self.EnableDspWithholdAmt:bool = obj["EnableDspWithholdAmt"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.InPrice:bool = obj["InPrice"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.LinkedCurrencySymbol:str = obj["LinkedCurrencySymbol"]
      self.NoShipTaxRgnInfo:bool = obj["NoShipTaxRgnInfo"]
      """  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEVATExemptionReason:str = obj["PEVATExemptionReason"]
      """  PE VAT Exemption Reason  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.RADesc:str = obj["RADesc"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  """  
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.AllowReclassify:bool = obj["AllowReclassify"]
      """  This flag allow updating Reclassification data.  """  
      self.LineAmtRecalcd:bool = obj["LineAmtRecalcd"]
      """  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  """  
      self.IsExtrastatSensitive:bool = obj["IsExtrastatSensitive"]
      """  Set to true if extra trade statistics is enabled.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReclassCodeDescription:str = obj["ReclassCodeDescription"]
      self.ReclassReasonDescription:str = obj["ReclassReasonDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   invoiceNum
   invoiceLine
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ARInvcDtlSearchTableset:
   def __init__(self, obj):
      self.InvcDtl:list[Erp_Tablesets_InvcDtlRow] = obj["InvcDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvcDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.InPrice:bool = obj["InPrice"]
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.RADesc:str = obj["RADesc"]
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      """  Description of the Call Type Code.  """  
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      """  Description of the service contract.  """  
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      """  Indicates if the contract has been suspended.  A suspended contract cannot have any calls linked to it.  """  
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      """  Contact's middle name.  """  
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      """  Contact's first name.  """  
      self.CustCntName:str = obj["CustCntName"]
      """  Full name of the contact.  """  
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.CustCntLastName:str = obj["CustCntLastName"]
      """  Contact's last name.  """  
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      """  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      """  Description  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      """  Country name  """  
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      """  Line description.  """  
      self.PackNumName:str = obj["PackNumName"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
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
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      """  Full description of Product Group.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      """  Description of the sales category.  """  
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.ShipToCustName:str = obj["ShipToCustName"]
      """  The full name of the customer.  """  
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Full description for the Tax Region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvcDtlListTableset:
   def __init__(self, obj):
      self.InvcDtlList:list[Erp_Tablesets_InvcDtlListRow] = obj["InvcDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvcDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT" and line for service calls  "CALL".  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  """  
      self.XPartNum:str = obj["XPartNum"]
      """  An optional field that is used if the customer has a different Part number than the internal part number.  This field is defaulted from the OrderDtl or ShipDtl files.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision.  Default from the ShipDtl.XRevisionNum for shipment lines or from OrderDtl.XRevisionNum, otherwise left blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number used to identify line item part.  This would be used as "Our" part number if there is a difference between us and the customers part numbering scheme.  Defaults from the OrderDtl.PartNum or the ShipDtl.PartNum.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Description of the line item.  Defaults from ShipDtl.LineDesc, OrderDtl.LineDesc or Part.PartDescription.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure.  Defaulted from ShipDtl.IUM, OrderRel.IUM or Part.IUM.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Our Current Revision Number for this Part.  """  
      self.POLine:str = obj["POLine"]
      """  Contains the line reference of the item on the customers PO. This is for reference and printing purposes.  Defaults from the OrderDtl.POLine.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this customer is exempt from sales tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field will be printed on the Tax report if this item is reportable.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the sales tax info in the InvcTax file.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this record.  Defaults from the OrderDtl if related to an Order or from the Part Master.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """   Indicates if this line is commissionable for the related sales rep's.
Defaults from the OrderDtl.  Note: "Deposit" invoice is always No.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """   Unit price discount percent.  User can enter a percentage and the system calculates the  discount amount.
NOT MAINTAINABLE & zero if Advance Bill.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  Can be defaulted from the OrderDtl.UnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.OurOrderQty:int = obj["OurOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.OurReqQty.  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.Discount:int = obj["Discount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """   A flat discount amount for the line item.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * UnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, UnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.TotalMiscChrg:int = obj["TotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.DocTotalMiscChrg:int = obj["DocTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Contains the foreign key to the ProdGrup file.  Can be blank or must be valid.  Defaults from the OrderDtl or Part file.  """  
      self.OurShipQty:int = obj["OurShipQty"]
      """  Our Quantity Shipped/billed.  Can be defaulted from ShipDtl.OurShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  The packing slip line number that is being invoiced.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order number.  This is not maintainable by the user.  The system duplicates it from the InvcHead.OrderNum.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The associated sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Contains the release number of the order line item that is being invoiced.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Customer Ship To ID for the item.  Defaults from the Customer, OrderRel or ShipDtl records.  If invoice details reference only one ship to then the ship to info is printed as heading info. otherwise a "See Below" message is printed and the Ship To info is printed as part of the invoice detail body.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  Ship date of the invoice line item.  Defaults from the ShipHead or from the invoice date when not referencing a packing slip.  When printed on the invoice it is printed as part of the heading if only one date exists else it is printed as part of the detail line.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipVia for the invoice detail lines.  Contains the Foreign key to the SHIPVIA master file. Can be left blank or must be valid.  Default from the OrderRel, ShipHead, Customer or ShipTo.  If invoice contains only a single ship via then it is printed as part of the heading; otherwise, it prints as part of the line item detail.  """  
      self.AdvanceBillCredit:int = obj["AdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.DocAdvanceBillCredit:int = obj["DocAdvanceBillCredit"]
      """  The amount this line item that is reduced by due to prior advanced billings.  This is only valid for "Shipment" or Miscellaneous" types.  It is defaulted from the OrderDtl.AdvanceBillBal.  This value reduces the OrderDtl.AdvanceBillBal.  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal number that is used to link the invoice to the Customer master file.  This is not maintainable, it is duplicated from the InvcHead.CustNum field.  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  Used to enter comments about the invoice line item.  These are printed on the invoice.  When invoice is referenced to a sales order line then this is defaulted from OrderDtl.InvoiceComment.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table.  Can be blank or must be valid in the CUSTCNT table.  Use the Customer.PrimSCon as a default or from OrderRel record.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost. The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced. If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost.  If shipped from inventory then it is zero. (Subcontract cost is combined with material cost on part master) The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process. Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost.  The cost is initially captured on the PartTran record for the shipments (MFG-CUS, STK-CUS).  It is duplicated from the PartTran when invoiced.  If shipped from inventory then it is the cost captured from the part master at time of shipment.  If shipped from job it is calculated during the Calculate WIP/COS period end process.  Note: the Calculate WIP/COS will also update this cost for invoiced job shipments which had been invoiced prior to having the costs calculated.  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """  Answers the question, "Does this InvcDtl need to have cost of sales posted to G/L?"  If the Manufacturing System is not using a A/R clearing account (XASyst.ARClearingDiv = "") then the costs were already posted to the Cost Of Sales account by the COS/WIP procedure (JCP80.W), so there are no costs to move.  """  
      self.COSPosted:bool = obj["COSPosted"]
      """   If the amount of this InvcDtl was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped it's costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  """  
      self.CallNum:int = obj["CallNum"]
      """  this is a link to the service call that this invoice is for.  Linetype = "CALL"  """  
      self.CallCode:str = obj["CallCode"]
      """  A unique code that identifies the type of service call.  Link to GL accounts when LineType = "CALL"  """  
      self.RMANum:int = obj["RMANum"]
      """   The related RMA number. Note: This only applies to Credit Memos.
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  """  
      self.RMALine:int = obj["RMALine"]
      """   The related RMA Line number.  This along with the RMANum provides the foreign key to the related RMADtl record.
(See InvcDtl.RMANum)  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  A Cod which uniquely identfies SalesCat record. Can't be blank.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that clearing/cos entry was posted to in G/L.
Note: The Fiscal Year, Period, Journal Code, JournalNum pertain only to records which were used to post to the ARClearing/COS. This condition is indicated if  COSPostingReqd = Yes.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalCode:str = obj["JournalCode"]
      """   Journal Code of the related GLJrnDtl.
Note: This is set as the Inventory Journal code defined in the inventory configuration options.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.SellingOrderQty:int = obj["SellingOrderQty"]
      """  The planned order release quantity.  This is not maintainable.  If and only if an order is referenced then it is set equal to the OrderRel.SellingReqQty.  """  
      self.SellingShipQty:int = obj["SellingShipQty"]
      """  Selling Quantity Shipped/billed.  Can be defaulted from ShipDtl.SellingShipQty.  Not maintainable & Zero for ProgressBill.  """  
      self.SalesUM:str = obj["SalesUM"]
      """  Selling Unit Of Measure.  Defaulted from ShipDtl.SUM, OrderDtl.SUM or Part.SUM.  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Project Id that links the invoice detail  to the Project table.  """  
      self.MilestoneID:str = obj["MilestoneID"]
      """  Milestone id that links the invoice detail  to the ProjectMilestone.  """  
      self.ListPrice:int = obj["ListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied.  Will default from the OrderDtl.ListPrice.  """  
      self.DocListPrice:int = obj["DocListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocListPrice.  """  
      self.OrdBasedPrice:int = obj["OrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied.  Will default from the OrderDtl.OrdBasedPrice.  """  
      self.DocOrdBasedPrice:int = obj["DocOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocOrdBasedPrice.  """  
      self.AdvGainLoss:int = obj["AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.RepRate1:int = obj["RepRate1"]
      """  Sales representative commission rate.  """  
      self.RepRate2:int = obj["RepRate2"]
      """  Sales representative commission rate.  """  
      self.RepRate3:int = obj["RepRate3"]
      """  Sales representative commission rate.  """  
      self.RepRate4:int = obj["RepRate4"]
      """  Sales representative commission rate.  """  
      self.RepRate5:int = obj["RepRate5"]
      """  Sales representative commission rate.  """  
      self.RepSplit1:int = obj["RepSplit1"]
      """  Sales representative commission percentage.  """  
      self.RepSplit2:int = obj["RepSplit2"]
      """  Sales representative commission percentage.  """  
      self.RepSplit3:int = obj["RepSplit3"]
      """  Sales representative commission percentage.  """  
      self.RepSplit4:int = obj["RepSplit4"]
      """  Sales representative commission percentage.  """  
      self.RepSplit5:int = obj["RepSplit5"]
      """  Sales representative commission percentage.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number used for consolidated invoices  """  
      self.JCMtlUnitCost:int = obj["JCMtlUnitCost"]
      """  Job Closing Material Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCLbrUnitCost:int = obj["JCLbrUnitCost"]
      """  Job Closing Labor Unit Cost. The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCBurUnitCost:int = obj["JCBurUnitCost"]
      """  Job Closing Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCSubUnitCost:int = obj["JCSubUnitCost"]
      """  Job Closing Subcontract Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.JCMtlBurUnitCost:int = obj["JCMtlBurUnitCost"]
      """  Job Closing Material Burden Unit Cost.  The cost is captured on the final Job Assembley. It is  duplicated from the JobAsmbl when the job is closed.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this invoice line.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AR invoice line.  """  
      self.OverrideReverseCharge:bool = obj["OverrideReverseCharge"]
      """  Indicates if the user overrides the Reverse Charge Method.  """  
      self.RevChargeApplied:bool = obj["RevChargeApplied"]
      """  Indicates if Reverse Charge tax line has been applied.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the InvcTax records tied to this line are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.Rpt1AdvanceBillCredit:int = obj["Rpt1AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2AdvanceBillCredit:int = obj["Rpt2AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3AdvanceBillCredit:int = obj["Rpt3AdvanceBillCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1ListPrice:int = obj["Rpt1ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ListPrice:int = obj["Rpt2ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ListPrice:int = obj["Rpt3ListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1OrdBasedPrice:int = obj["Rpt1OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2OrdBasedPrice:int = obj["Rpt2OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3OrdBasedPrice:int = obj["Rpt3OrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1TotalMiscChrg:int = obj["Rpt1TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2TotalMiscChrg:int = obj["Rpt2TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3TotalMiscChrg:int = obj["Rpt3TotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1AdvGainLoss:int = obj["Rpt1AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt2AdvGainLoss:int = obj["Rpt2AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.Rpt3AdvGainLoss:int = obj["Rpt3AdvGainLoss"]
      """  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Unique identifier of the Tax Region assigned by the user.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  Contains the TaxRgn.TaxRegionCode value of the One Time ShipTo tax region for purposes of Sales Tax calculations.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping adress country Number.  """  
      self.Plant:str = obj["Plant"]
      """  Value is copied from PartTran for PE  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  value is copied from PartTran for PE  """  
      self.CallLine:int = obj["CallLine"]
      """  value is copied from PartTran for PE  """  
      self.DropShipPackLine:int = obj["DropShipPackLine"]
      """  Drop Shipment Pack Line  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.FinChargeCode:str = obj["FinChargeCode"]
      """  FK to the Finance Charges table  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID, used in PostingEngine  """  
      self.InUnitPrice:int = obj["InUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.DocInUnitPrice:int = obj["DocInUnitPrice"]
      """  Unit Price including taxes.  Can be defaulted from the OrderDtl.InUnitPrice.  Always zero and not maintainable if this is a progress billing type of invoice.  """  
      self.InExtPrice:int = obj["InExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.DocInExtPrice:int = obj["DocInExtPrice"]
      """  Extended Price for the invoice line item including taxes.  If not a ProgressBill or "Deposit" invoice then it is not maintainable and is calculated as the (ShipQty/PricePer) * UnitPrice.  If it is a ProgressBill or "Deposit Invoice"  then the ShipQty and UnitPrice fields are zero and the user is allowed entry to this field.  """  
      self.InDiscount:int = obj["InDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.DocInDiscount:int = obj["DocInDiscount"]
      """   A flat discount amount for the line item including taxes.  It can be zero.  This is calculated using the DiscountPercent * (ShipQty * InUnitPrice)).  This field can also be directly updated by the user, however it is refreshed whenever the DiscountPercent, InUnitPrice or ShipQty fields are changed.  Discount CANNOT EXCEED THE EXTENDED LINE AMOUNT.  Note a discount entered here reduces the "net" sale amount, while miscellaneous amounts are not.
NOT MAINTAINABLE & Zero if ProgressBill.  """  
      self.InTotalMiscChrg:int = obj["InTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.DocInTotalMiscChrg:int = obj["DocInTotalMiscChrg"]
      """  Non-Maintainable.  Rolled up total of all misc. charge records for this invoice detail line (includes taxes).  """  
      self.InListPrice:int = obj["InListPrice"]
      """  This is the unit price returned by the price list before quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InListPrice.  """  
      self.DocInListPrice:int = obj["DocInListPrice"]
      """  This is the list price in customer currency.  Will default from the OrderDtl.DocInListPrice.  """  
      self.InOrdBasedPrice:int = obj["InOrdBasedPrice"]
      """  This is the unit price after quantity based or order value based discounts are applied (includes taxes).  Will default from the OrderDtl.InOrdBasedPrice.  """  
      self.DocInOrdBasedPrice:int = obj["DocInOrdBasedPrice"]
      """  This is the order based price in customer currency.  Will default from the OrderDtl.DocInOrdBasedPrice.  """  
      self.Rpt1InDiscount:int = obj["Rpt1InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt2InDiscount:int = obj["Rpt2InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt3InDiscount:int = obj["Rpt3InDiscount"]
      """  Reporting currency value of this field  """  
      self.Rpt1InExtPrice:int = obj["Rpt1InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InExtPrice:int = obj["Rpt2InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InExtPrice:int = obj["Rpt3InExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InListPrice:int = obj["Rpt1InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InListPrice:int = obj["Rpt2InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InListPrice:int = obj["Rpt3InListPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InOrdBasedPrice:int = obj["Rpt1InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InOrdBasedPrice:int = obj["Rpt2InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InOrdBasedPrice:int = obj["Rpt3InOrdBasedPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt1InTotalMiscChrg:int = obj["Rpt1InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt2InTotalMiscChrg:int = obj["Rpt2InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt3InTotalMiscChrg:int = obj["Rpt3InTotalMiscChrg"]
      """  Reporting currency value of this field  """  
      self.Rpt1InUnitPrice:int = obj["Rpt1InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2InUnitPrice:int = obj["Rpt2InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3InUnitPrice:int = obj["Rpt3InUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CorrectionDtl:bool = obj["CorrectionDtl"]
      """  Will be set to Yes if the Invoice Detail was created by the Correction (Reversing) logic.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the linked Asset Disposal transaction.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the linked Asset Disposal transaction.  """  
      self.PBLineType:str = obj["PBLineType"]
      """   Project Billing transactuion type with following options:
MWA = Measured Work, 
LBD = Employee Labor (Direct Labor), 
LBC = Contract Labor, 
MTL = Material, 
SUB = Subcontract, 
MSC = Other,
RET = Retention, 
FLBR = Fee Labor
FMTL = Fee Material,
FSUB = Fee Subcontract, 
FMSC = Fee ODC,
FPRJ = Fee of total project,
FRET = Fee retention,
BDN  = Burden,
CEIL = Reduce by Ceiling,
CLFR = Close ? Fee retention,
CLPR = Close ? Project Retention (CP)
CLSR = Close Billing schedule - Reverse retention
CLSA = Close Project ? Unassigned activities  """  
      self.InvoiceLineRef:int = obj["InvoiceLineRef"]
      """  Invoice line reference  """  
      self.InvoiceRef:int = obj["InvoiceRef"]
      """  Invoice Number Reference  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number.  This field should be set according to the linked Shipment Line.  """  
      self.PBInvoiceLine:int = obj["PBInvoiceLine"]
      """  Reference to the draft invoice line created in Invoice Preparation  """  
      self.RAID:int = obj["RAID"]
      """  Contains the value of the AC_RAHead.RAID client accommodation.  """  
      self.RADtlID:int = obj["RADtlID"]
      """  Contains the value of the AC_RADtl.RADtlID client detail accommodation.  """  
      self.DeferredRev:bool = obj["DeferredRev"]
      """  Indicates if revenue is deferred for contracts assigned to this group.  """  
      self.RACode:str = obj["RACode"]
      """  Revenue Amortization Code.  """  
      self.DefRevStart:str = obj["DefRevStart"]
      """  Starting date the revenue is deferred.  """  
      self.ChargeDefRev:bool = obj["ChargeDefRev"]
      """  When Yes the decision to defer revenue on an invoice line was made after the invoice was posted and the deferred revenue account has not yet been charged.  This flag is used internally to determine whether or not a journal clearing the sales and charging the deferrred revenue account needs to be created.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefRevPosted:bool = obj["DefRevPosted"]
      """  DefRevPosted  """  
      self.LinkedInvcUnitPrice:int = obj["LinkedInvcUnitPrice"]
      """  Unit price of Invoice linked to Bill of Exchange in original currency.  """  
      self.DspWithholdAmt:int = obj["DspWithholdAmt"]
      """  Withholding Tax Amount in reporting currency  """  
      self.DocDspWithholdAmt:int = obj["DocDspWithholdAmt"]
      """  Withholding Tax Amount in document currency  """  
      self.Rpt1DspWithholdAmt:int = obj["Rpt1DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt2DspWithholdAmt:int = obj["Rpt2DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.Rpt3DspWithholdAmt:int = obj["Rpt3DspWithholdAmt"]
      """  Withholding tax amount in reporting currency  """  
      self.LinkedCurrencyCode:str = obj["LinkedCurrencyCode"]
      """  Currency code from linked Invoice Header  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.PEBOEHeadNum:int = obj["PEBOEHeadNum"]
      """  PEBOEHeadNum  """  
      self.MXSellingShipQty:int = obj["MXSellingShipQty"]
      """  MXSellingShipQty  """  
      self.MXUnitPrice:int = obj["MXUnitPrice"]
      """  MXUnitPrice  """  
      self.DocMXUnitPrice:int = obj["DocMXUnitPrice"]
      """  DocMXUnitPrice  """  
      self.Rpt1MXUnitPrice:int = obj["Rpt1MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2MXUnitPrice:int = obj["Rpt2MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3MXUnitPrice:int = obj["Rpt3MXUnitPrice"]
      """  Reporting currency value of this field  """  
      self.CustCostCenter:str = obj["CustCostCenter"]
      """  CustCostCenter  """  
      self.DEIsServices:bool = obj["DEIsServices"]
      """  DEIsServices  """  
      self.DEIsSecurityFinancialDerivative:bool = obj["DEIsSecurityFinancialDerivative"]
      """  DEIsSecurityFinancialDerivative  """  
      self.DEInternationalSecuritiesID:str = obj["DEInternationalSecuritiesID"]
      """  DEInternationalSecuritiesID  """  
      self.DEIsInvestment:bool = obj["DEIsInvestment"]
      """  DEIsInvestment  """  
      self.DEPayStatCode:str = obj["DEPayStatCode"]
      """  DEPayStatCode  """  
      self.DefRevEndDate:str = obj["DefRevEndDate"]
      """  DefRevEndDate  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.Reclassified:bool = obj["Reclassified"]
      """  Indicates tha this invoice Line was reclassified.  """  
      self.PartiallyDefer:bool = obj["PartiallyDefer"]
      """  Enables the user the ability to override the Percent or Amount of revenue to be deferred  """  
      self.DeferredPercent:int = obj["DeferredPercent"]
      """  Percentage of revenue to be deferred for this line item  """  
      self.Reclass:bool = obj["Reclass"]
      """  Enables the user the ability tp reclassify deferred revenue and select a reclassification code and reason code.  """  
      self.DeferredOnly:bool = obj["DeferredOnly"]
      """  Defines if the reclassification posting will only reclass the deferred revenue, or if the recognized revenue will be reclassed as well  """  
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      """  Reclassification Code. This field will be required if Reclass is checked.  """  
      self.ReclassReasonCode:str = obj["ReclassReasonCode"]
      """  Reason Code for reclassification from Reason Code Maintanance that have type 'Deferred Revenue'. This field will be required if reclass is checked.  """  
      self.ReclassComments:str = obj["ReclassComments"]
      """  Internal comments for reclassification entered by the user.  """  
      self.DeferredRevAmt:int = obj["DeferredRevAmt"]
      """  Deferred Revenue Amount in base currency  """  
      self.DocDeferredRevAmt:int = obj["DocDeferredRevAmt"]
      """  Deferred Revenue Amount in document currency  """  
      self.Rpt1DeferredRevAmt:int = obj["Rpt1DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt2DeferredRevAmt:int = obj["Rpt2DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.Rpt3DeferredRevAmt:int = obj["Rpt3DeferredRevAmt"]
      """  Reporting currency value of Deferred Revenue Amount  """  
      self.ChargeReclass:bool = obj["ChargeReclass"]
      """  ChargeReclass  """  
      self.DEDenomination:str = obj["DEDenomination"]
      """  DEDenomination  """  
      self.DropShipPONum:int = obj["DropShipPONum"]
      """  DropShipPONum  """  
      self.DocInAdvanceBillCredit:int = obj["DocInAdvanceBillCredit"]
      """  DocInAdvanceBillCredit  """  
      self.InAdvanceBillCredit:int = obj["InAdvanceBillCredit"]
      """  InAdvanceBillCredit  """  
      self.Rpt1InAdvanceBillCredit:int = obj["Rpt1InAdvanceBillCredit"]
      """  Rpt1InAdvanceBillCredit  """  
      self.Rpt2InAdvanceBillCredit:int = obj["Rpt2InAdvanceBillCredit"]
      """  Rpt2InAdvanceBillCredit  """  
      self.Rpt3InAdvanceBillCredit:int = obj["Rpt3InAdvanceBillCredit"]
      """  Rpt3InAdvanceBillCredit  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.DockingStation:str = obj["DockingStation"]
      """  The dockingstation of the shipto address.  For future use.  """  
      self.ConsolidateLines:bool = obj["ConsolidateLines"]
      """  ConsolidateLines  """  
      self.MXCustomsDuty:str = obj["MXCustomsDuty"]
      """  MXCustomsDuty  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  CommodityCode  """  
      self.MXProdServCode:str = obj["MXProdServCode"]
      """  MXProdServCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Quote number to which this line item detail record is associated with.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Quote Line number from which this invoice line was created from.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.MXCustomsUMFrom:str = obj["MXCustomsUMFrom"]
      """  MXCustomsUMFrom  """  
      self.PEDetrGoodServiceCode:str = obj["PEDetrGoodServiceCode"]
      """  PE Detraction good or service code  """  
      self.PETaxExempt:str = obj["PETaxExempt"]
      """  PETaxExempt  """  
      self.CColOrderNum:int = obj["CColOrderNum"]
      """  Order number on the Invoicing Company.  """  
      self.CColOrderLine:int = obj["CColOrderLine"]
      """  Order number line the Invoicing Company.  """  
      self.CColOrderRel:int = obj["CColOrderRel"]
      """  Order number release the Invoicing Company.  """  
      self.CColInvoiceLineRef:int = obj["CColInvoiceLineRef"]
      """  Invoice Line reference on the Invoicing Company.  """  
      self.CColPackNum:int = obj["CColPackNum"]
      """  Packing slip number on the Invoicing Company.  """  
      self.CColPackLine:int = obj["CColPackLine"]
      """  Packing slip line number on the Invoicing Company.  """  
      self.CColDropShipPackSlip:str = obj["CColDropShipPackSlip"]
      """  Drop shipment packing slip number on the Invoicing Company.  """  
      self.CColDropShipPackSlipLine:int = obj["CColDropShipPackSlipLine"]
      """  Drop shipment packing slip line number on the Invoicing Company.  """  
      self.CColShipToCustID:str = obj["CColShipToCustID"]
      """  Ship To Customer ID from the Invoice Line in the subsidiary company.  """  
      self.CColShipToNum:str = obj["CColShipToNum"]
      """  Ship To from the Invoice Line in the subsidiary company.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  Exempt Reason Code  """  
      self.JobNum:str = obj["JobNum"]
      """  Associates the Call Line record back its linked jobnum  """  
      self.ServiceSource:str = obj["ServiceSource"]
      """  Indicates where invoice detail was created from when created from a service call job. Not maintainable. “Summarized Labor”, “Summarized Material”, “Labor”, “Material”  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq related to JobMtl or JobOper used to create invoice line from service call job  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Job Mtl seq used to create invoice line from service call job  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job subcontract oper seq used to create invoice line from service call job  """  
      self.LaborType:str = obj["LaborType"]
      """  Indicates the labor type of the LaborDtl used to create invoice from service call job.  """  
      self.BillableLaborHrs:int = obj["BillableLaborHrs"]
      """  LaborDtl hours summed by labor rate. Used to create invoice line from labor related to service call job.  """  
      self.BillableLaborRate:int = obj["BillableLaborRate"]
      """  Billable rate used to create invoice line from labor related to service call job. In base currency.  """  
      self.ServiceSourceType:str = obj["ServiceSourceType"]
      """  Indicates the type of service call transaction data used to create the invoice detail from a service call job. MT (material), LB (labor), SC (subcontract), MC (misc charge), SM (summarized material), SL (summarized labor), SS (summarized subcontract) No summarization for MC.  """  
      self.TotalCovenantDiscount:int = obj["TotalCovenantDiscount"]
      """  TotalCovenantDiscount  """  
      self.DocCovenantDiscount:int = obj["DocCovenantDiscount"]
      """  DocCovenantDiscount  """  
      self.Rpt1CovenantDiscount:int = obj["Rpt1CovenantDiscount"]
      """  Rpt1CovenantDiscount  """  
      self.Rpt2CovenantDiscount:int = obj["Rpt2CovenantDiscount"]
      """  Rpt2CovenantDiscount  """  
      self.Rpt3CovenantDiscount:int = obj["Rpt3CovenantDiscount"]
      """  Rpt3CovenantDiscount  """  
      self.TotalInCovenantDiscount:int = obj["TotalInCovenantDiscount"]
      """  TotalInCovenantDiscount  """  
      self.DocInCovenantDiscount:int = obj["DocInCovenantDiscount"]
      """  DocInCovenantDiscount  """  
      self.Rpt1InCovenantDiscount:int = obj["Rpt1InCovenantDiscount"]
      """  Rpt1InCovenantDiscount  """  
      self.Rpt2InCovenantDiscount:int = obj["Rpt2InCovenantDiscount"]
      """  Rpt2InCovenantDiscount  """  
      self.Rpt3InCovenantDiscount:int = obj["Rpt3InCovenantDiscount"]
      """  Rpt3InCovenantDiscount  """  
      self.AdvBillEnabled:bool = obj["AdvBillEnabled"]
      """  Adv bill enabled flag  """  
      self.AllowTaxCodeUpd:bool = obj["AllowTaxCodeUpd"]
      self.AllowUpdPartDefer:bool = obj["AllowUpdPartDefer"]
      """  This flag not allow updating PartiallyDefer in 'Posted Invoice Update' if  AR Invoice Line was  marked as Partially Defer in AR Invoice Entry.  """  
      self.BillToCustID:str = obj["BillToCustID"]
      """  CustID associated with the InvcDtl.BTCustNum field.  """  
      self.BTCustName:str = obj["BTCustName"]
      """  Customer Name associated with the InvcDtl.BTCustNum field.  """  
      self.ChangeDateTime:str = obj["ChangeDateTime"]
      """  The date and time that the record was last changed  """  
      self.CheckAmortAmounts:bool = obj["CheckAmortAmounts"]
      """  Used internally to determine when the user needs to be prompted to recalculate the amortization schedules.  This is not intended for use by the customers.  """  
      self.CNGTIDescription1:str = obj["CNGTIDescription1"]
      self.CNGTIDescription2:str = obj["CNGTIDescription2"]
      self.CNGTIDescription3:str = obj["CNGTIDescription3"]
      self.CNGTIDiscountTaxAmount:int = obj["CNGTIDiscountTaxAmount"]
      """  CSF China, discount tax amount  """  
      self.CNGTIIUM:str = obj["CNGTIIUM"]
      self.CNGTINetAmount:int = obj["CNGTINetAmount"]
      self.CNGTIPartDescription:str = obj["CNGTIPartDescription"]
      self.CNGTISpecification:str = obj["CNGTISpecification"]
      self.CNGTITaxAmount:int = obj["CNGTITaxAmount"]
      self.CNGTITaxCode:str = obj["CNGTITaxCode"]
      self.CNGTITaxPercent:int = obj["CNGTITaxPercent"]
      self.CNGTITotalAmount:int = obj["CNGTITotalAmount"]
      self.CNGTIUnitPrice:int = obj["CNGTIUnitPrice"]
      """  CSF China, Unit price = if InvcHead.InPrice then InvcDtl.InUnitPrice else InvcDtl.UnitPrice  """  
      self.ContractSuspended:bool = obj["ContractSuspended"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code from InvcHead.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currncy switch used to determine what currency to display amounts in.  """  
      self.CustID:str = obj["CustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.CustName:str = obj["CustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Invoice Detail Customer Name  """  
      self.DeleteRASchedule:bool = obj["DeleteRASchedule"]
      """  Intended for internal use.  This is set to yes when the user answers yes to the prompt asking if they want to delete schedules after they unchecked the deferred revenue flag.  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      self.DisplaySymbol:str = obj["DisplaySymbol"]
      """  Currency display symbol  """  
      self.DispPONum:str = obj["DispPONum"]
      """  PO number for display.  """  
      self.DispShipToAddr:str = obj["DispShipToAddr"]
      """  Ship to display address  """  
      self.DocDisplaySymbol:str = obj["DocDisplaySymbol"]
      """  Document display symbol.  """  
      self.DocDspUnitPrice:int = obj["DocDspUnitPrice"]
      self.DocLessDiscount:int = obj["DocLessDiscount"]
      """  Document discount amount  """  
      self.DocLineTax:int = obj["DocLineTax"]
      """  Doc line tax  """  
      self.DocLineTotal:int = obj["DocLineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.DocPEDetAmt:int = obj["DocPEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.DropShipment:bool = obj["DropShipment"]
      """  Drop Shipment  """  
      self.DspAdvanceBillCredit:int = obj["DspAdvanceBillCredit"]
      """  Display advance bill credit  """  
      self.DspDiscount:int = obj["DspDiscount"]
      """  Display discount  """  
      self.DspDocAdvanceBillCredit:int = obj["DspDocAdvanceBillCredit"]
      """  Display documents advance bill credit  """  
      self.DspDocDiscount:int = obj["DspDocDiscount"]
      """  Display document discount  """  
      self.DspDocExtPrice:int = obj["DspDocExtPrice"]
      """  Display document ext price  """  
      self.DspDocLessDiscount:int = obj["DspDocLessDiscount"]
      """  Display document less discount  """  
      self.DspDocLineTax:int = obj["DspDocLineTax"]
      """  Display document line tax  """  
      self.DspDocLineTotal:int = obj["DspDocLineTotal"]
      """  Display document line total  """  
      self.DspDocTotalMiscChrg:int = obj["DspDocTotalMiscChrg"]
      """  Display document total misc. charge  """  
      self.DspExtPrice:int = obj["DspExtPrice"]
      """  Display ext price  """  
      self.DspInvoiceRef:int = obj["DspInvoiceRef"]
      """  Display Invoice Reference  """  
      self.DspLessDiscount:int = obj["DspLessDiscount"]
      """  Display less discount  """  
      self.DspLineTax:int = obj["DspLineTax"]
      """  Display line tax  """  
      self.DspLineTotal:int = obj["DspLineTotal"]
      """  Display line total  """  
      self.DspOurShipQty:int = obj["DspOurShipQty"]
      """  Display our ship qty  """  
      self.DspSellingShipQty:int = obj["DspSellingShipQty"]
      """  Display selling ship qty  """  
      self.DspTaxExempt:str = obj["DspTaxExempt"]
      self.DspTotalMiscChrg:int = obj["DspTotalMiscChrg"]
      """  Display total misc. charges  """  
      self.DspUnitPrice:int = obj["DspUnitPrice"]
      self.DueDate:str = obj["DueDate"]
      """  Invoice head due date.  """  
      self.EmpID:str = obj["EmpID"]
      """  FSA Technician  """  
      self.EnableDspWithholdAmt:bool = obj["EnableDspWithholdAmt"]
      self.EnableRMADelete:bool = obj["EnableRMADelete"]
      self.EnableRMAUpdate:bool = obj["EnableRMAUpdate"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GroupID:str = obj["GroupID"]
      """  Group associated to the invoice  """  
      self.InPrice:bool = obj["InPrice"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.InvLegalNum:str = obj["InvLegalNum"]
      """  Invoice Header Legal Number  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date from InvcHead.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  Invoice header type  """  
      self.IsCommisBtnSensitive:bool = obj["IsCommisBtnSensitive"]
      """  Is commission button sensitive  """  
      self.IsIntrastatSensitive:bool = obj["IsIntrastatSensitive"]
      """  Set to true if intrastat is enabled.  """  
      self.IsTaxBtnSensitive:bool = obj["IsTaxBtnSensitive"]
      """  Tax buton sensitive or not.  """  
      self.LessDiscount:int = obj["LessDiscount"]
      """  display discount  """  
      self.LineTax:int = obj["LineTax"]
      """  Line tax amount  """  
      self.LineTotal:int = obj["LineTotal"]
      """  ExtPrice-disc+misc charges.  """  
      self.LinkedCurrencySymbol:str = obj["LinkedCurrencySymbol"]
      self.NoShipTaxRgnInfo:bool = obj["NoShipTaxRgnInfo"]
      """  The flag based on the user responce to indicate if Ship To to be chnaged on Invoice detail record without tax information from Ship To because of the different tax pricing  """  
      self.OpenInvoice:bool = obj["OpenInvoice"]
      """  Open invoice flag from InvcHead.  """  
      self.OrderUM:str = obj["OrderUM"]
      """  OrderUM display  """  
      self.OrigTaxCat:str = obj["OrigTaxCat"]
      """  original tax category  """  
      self.PEDetAmt:int = obj["PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.PEDetrGoodServiceCodeDesc:str = obj["PEDetrGoodServiceCodeDesc"]
      """  PE Detraction good or service code description  """  
      self.PEDspCurrencySymbol:str = obj["PEDspCurrencySymbol"]
      self.PEVATExemptionReason:str = obj["PEVATExemptionReason"]
      """  PE VAT Exemption Reason  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag from the InvcHead.  """  
      self.RADesc:str = obj["RADesc"]
      self.RASchedExists:bool = obj["RASchedExists"]
      """  Intended for internal use.  Indicates whether or not revenue amortization schedules exist.  """  
      self.RemoveManAdTax:bool = obj["RemoveManAdTax"]
      """  The internal flag to indicate if the logic is supposed to remove manual and/or manually added tax records per User request if the Line Tax Exempt field is populated  """  
      self.Rpt1DspAdvanceBillCredit:int = obj["Rpt1DspAdvanceBillCredit"]
      self.Rpt1DspDiscount:int = obj["Rpt1DspDiscount"]
      self.Rpt1DspExtPrice:int = obj["Rpt1DspExtPrice"]
      self.Rpt1DspLessDiscount:int = obj["Rpt1DspLessDiscount"]
      self.Rpt1DspLineTax:int = obj["Rpt1DspLineTax"]
      self.Rpt1DspLineTotal:int = obj["Rpt1DspLineTotal"]
      self.Rpt1DspTotalMiscChrg:int = obj["Rpt1DspTotalMiscChrg"]
      self.Rpt1DspUnitPrice:int = obj["Rpt1DspUnitPrice"]
      self.Rpt1LineTax:int = obj["Rpt1LineTax"]
      self.Rpt1LineTotal:int = obj["Rpt1LineTotal"]
      self.Rpt1PEDetAmt:int = obj["Rpt1PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt2DspAdvanceBillCredit:int = obj["Rpt2DspAdvanceBillCredit"]
      self.Rpt2DspDiscount:int = obj["Rpt2DspDiscount"]
      self.Rpt2DspExtPrice:int = obj["Rpt2DspExtPrice"]
      self.Rpt2DspLessDiscount:int = obj["Rpt2DspLessDiscount"]
      self.Rpt2DspLineTax:int = obj["Rpt2DspLineTax"]
      self.Rpt2DspLineTotal:int = obj["Rpt2DspLineTotal"]
      self.Rpt2DspTotalMiscChrg:int = obj["Rpt2DspTotalMiscChrg"]
      self.Rpt2DspUnitPrice:int = obj["Rpt2DspUnitPrice"]
      self.Rpt2LineTax:int = obj["Rpt2LineTax"]
      self.Rpt2LineTotal:int = obj["Rpt2LineTotal"]
      self.Rpt2PEDetAmt:int = obj["Rpt2PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.Rpt3DspAdvanceBillCredit:int = obj["Rpt3DspAdvanceBillCredit"]
      self.Rpt3DspDiscount:int = obj["Rpt3DspDiscount"]
      self.Rpt3DspExtPrice:int = obj["Rpt3DspExtPrice"]
      self.Rpt3DspLessDiscount:int = obj["Rpt3DspLessDiscount"]
      self.Rpt3DspLineTax:int = obj["Rpt3DspLineTax"]
      self.Rpt3DspLineTotal:int = obj["Rpt3DspLineTotal"]
      self.Rpt3DspTotalMiscChrg:int = obj["Rpt3DspTotalMiscChrg"]
      self.Rpt3DspUnitPrice:int = obj["Rpt3DspUnitPrice"]
      self.Rpt3LineTax:int = obj["Rpt3LineTax"]
      self.Rpt3LineTotal:int = obj["Rpt3LineTotal"]
      self.Rpt3PEDetAmt:int = obj["Rpt3PEDetAmt"]
      """  CSF Peru - Field used to display Detraction Amount for Bill of Exchange Invoices.  """  
      self.SalesRepCode1:str = obj["SalesRepCode1"]
      """  1st sales rep of the invoice.  """  
      self.SalesRepCode2:str = obj["SalesRepCode2"]
      """  2nd sales rep of the invoice header.  """  
      self.SalesRepCode3:str = obj["SalesRepCode3"]
      """  3rd sales rep code of the invoice header.  """  
      self.SalesRepCode4:str = obj["SalesRepCode4"]
      """  4th sales rep code of the invoice header.  """  
      self.SalesRepCode5:str = obj["SalesRepCode5"]
      """  5th salesrep code of the invoice header.  """  
      self.SalesRepName1:str = obj["SalesRepName1"]
      """  1st sales rep name  """  
      self.SalesRepName2:str = obj["SalesRepName2"]
      """  2nd sales rep name  """  
      self.SalesRepName3:str = obj["SalesRepName3"]
      """  3rd sales rep name  """  
      self.SalesRepName4:str = obj["SalesRepName4"]
      """  4th sales rep name  """  
      self.SalesRepName5:str = obj["SalesRepName5"]
      """  5th sales rep name  """  
      self.ShipToContactEMailAddress:str = obj["ShipToContactEMailAddress"]
      self.ShipToContactFaxNum:str = obj["ShipToContactFaxNum"]
      self.ShipToContactName:str = obj["ShipToContactName"]
      self.ShipToContactPhoneNum:str = obj["ShipToContactPhoneNum"]
      self.ShpLegalNum:str = obj["ShpLegalNum"]
      """  Ship Head Legal Number  """  
      self.SoldToCustID:str = obj["SoldToCustID"]
      """  CustID associated with the InvcDtl.CustNum field.  """  
      self.SoldToCustName:str = obj["SoldToCustName"]
      """  Customer Name associated with the InvcDtl.CustNum field.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code from InvcHead.  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.AllowReclassify:bool = obj["AllowReclassify"]
      """  This flag allow updating Reclassification data.  """  
      self.LineAmtRecalcd:bool = obj["LineAmtRecalcd"]
      """  The flag to indicate if the amount  is re-calculated to doc/base/rpt currencies after entered and no need to re-calculate on save.  """  
      self.IsExtrastatSensitive:bool = obj["IsExtrastatSensitive"]
      """  Set to true if extra trade statistics is enabled.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CallCodeCallDescription:str = obj["CallCodeCallDescription"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.ContractCodeContractDescription:str = obj["ContractCodeContractDescription"]
      self.ContractNumSuspended:bool = obj["ContractNumSuspended"]
      self.CustCntName:str = obj["CustCntName"]
      self.CustCntMiddleName:str = obj["CustCntMiddleName"]
      self.CustCntFirstName:str = obj["CustCntFirstName"]
      self.CustCntFaxNum:str = obj["CustCntFaxNum"]
      self.CustCntCorpName:str = obj["CustCntCorpName"]
      self.CustCntPhoneNum:str = obj["CustCntPhoneNum"]
      self.CustCntLastName:str = obj["CustCntLastName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumAllowShipTo3:bool = obj["CustNumAllowShipTo3"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.MilestoneIDDescription:str = obj["MilestoneIDDescription"]
      self.MXProdServCodeDesc:str = obj["MXProdServCodeDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OTSCntryEUMember:bool = obj["OTSCntryEUMember"]
      self.OTSCntryISOCode:str = obj["OTSCntryISOCode"]
      self.OTSCntryDescription:str = obj["OTSCntryDescription"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReclassCodeDescription:str = obj["ReclassCodeDescription"]
      self.ReclassReasonDescription:str = obj["ReclassReasonDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.SalesCatIDDescription:str = obj["SalesCatIDDescription"]
      self.ShipToCustCustID:str = obj["ShipToCustCustID"]
      self.ShipToCustName:str = obj["ShipToCustName"]
      self.ShipToCustBTName:str = obj["ShipToCustBTName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.ShipToNumName:str = obj["ShipToNumName"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtARInvcDtlSearchTableset:
   def __init__(self, obj):
      self.InvcDtl:list[Erp_Tablesets_InvcDtlRow] = obj["InvcDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   invoiceNum
   invoiceLine
   """  
   def __init__(self, obj):
      self.invoiceNum:int = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["returnObj"]
      pass

class GetListAlternalSearch_input:
   """ Required : 
   invcHeadWhereClause
   invcDtlWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.invcHeadWhereClause:str = obj["invcHeadWhereClause"]
      """  Whereclause for invcHead table.  """  
      self.invcDtlWhereClause:str = obj["invcDtlWhereClause"]
      """  Whereclause for InvcDtl table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListAlternalSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_InvcDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInvcDtl_input:
   """ Required : 
   ds
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["ds"]
      self.invoiceNum:int = obj["invoiceNum"]
      pass

class GetNewInvcDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseInvcDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInvcDtl:str = obj["whereClauseInvcDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtARInvcDtlSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARInvcDtlSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARInvcDtlSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

