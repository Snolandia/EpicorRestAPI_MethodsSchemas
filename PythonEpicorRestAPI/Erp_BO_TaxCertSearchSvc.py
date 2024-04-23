import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxCertSearchSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxCertSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxCertSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxCertSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches",headers=creds) as resp:
           return await resp.json()

async def post_TaxCertSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxCertSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxCertSearches_Company_TranDate_TranNum(Company, TranDate, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxCertSearch item
   Description: Calls GetByID to retrieve the TaxCertSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxCertSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches(" + Company + "," + TranDate + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxCertSearches_Company_TranDate_TranNum(Company, TranDate, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxCertSearch for the service
   Description: Calls UpdateExt to update TaxCertSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxCertSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches(" + Company + "," + TranDate + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxCertSearches_Company_TranDate_TranNum(Company, TranDate, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxCertSearch item
   Description: Call UpdateExt to delete TaxCertSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxCertSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/TaxCertSearches(" + Company + "," + TranDate + "," + TranNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxTranListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxTran, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTaxTran=" + whereClauseTaxTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tranDate, tranNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "tranDate=" + tranDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranNum=" + tranNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListPercCertificates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListPercCertificates
   Description: Returns List of AR Perception Certificates.
   OperationID: GetListPercCertificates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListPercCertificates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPercCertificates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxCertSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxTranListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxTranRow] = obj["value"]
      pass

class Erp_Tablesets_TaxTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  a number which is used to allow create a unique key for the file.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  identifies a Tax Region master record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.CompTaxID:str = obj["CompTaxID"]
      """  Company Tax ID  """  
      self.VendorTaxID:str = obj["VendorTaxID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.CustomerTaxID:str = obj["CustomerTaxID"]
      """  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this TaxTran  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this TaxTran.  """  
      self.InvoiceMemo:bool = obj["InvoiceMemo"]
      """  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for tax statement  """  
      self.TaxPrintDate:str = obj["TaxPrintDate"]
      """  Date Tax Document was printed  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  If field is non-blank it is considered exempt.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Key to link to Payment  """  
      self.ARInvoiceDate:str = obj["ARInvoiceDate"]
      """  Field To save the AR Invoice Date  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  a number which is used to allow create a unique key for the file.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InEC:bool = obj["InEC"]
      """  Tax Region is in the European Community.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  identifies a Tax Region master record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.CompTaxID:str = obj["CompTaxID"]
      """  Company Tax ID  """  
      self.VendorTaxID:str = obj["VendorTaxID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.CustomerTaxID:str = obj["CustomerTaxID"]
      """  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from CurrRate.CurrentRate.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this report closed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting Date  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.   Allow the VAT report to Keep seperate totals for the 2 records used for this transaction.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this TaxTran  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this TaxTran.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax transaction is for a Reverse Charge.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  """  
      self.InvoiceMemo:bool = obj["InvoiceMemo"]
      """  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for tax statement  """  
      self.TaxPrintDate:str = obj["TaxPrintDate"]
      """  Date Tax Document was printed  """  
      self.TaxPosted:bool = obj["TaxPosted"]
      """  Indicates if Tax Statement was posted  """  
      self.TaxPostDate:str = obj["TaxPostDate"]
      """  Date Tax Statement was posted  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EU Third Party flag  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  If field is non-blank it is considered exempt.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Key to link to Payment  """  
      self.RecoverableAmt:int = obj["RecoverableAmt"]
      """  The amount of tax recoverable (deductible).  """  
      self.DocRecoverableAmt:int = obj["DocRecoverableAmt"]
      """  The amount of tax recoverable (deductible)  """  
      self.Rpt1RecoverableAmt:int = obj["Rpt1RecoverableAmt"]
      """  The amout of tax recoverable (deductible) in Rpt1 currency  """  
      self.Rpt2RecoverableAmt:int = obj["Rpt2RecoverableAmt"]
      """  Tha amount of tax recoverable (deductible) in RPT2 currency.  """  
      self.Rpt3RecoverableAmt:int = obj["Rpt3RecoverableAmt"]
      """  The amount of tax recoverable (deductible) in RPT3 currency  """  
      self.ARInvoiceDate:str = obj["ARInvoiceDate"]
      """  Field To save the AR Invoice Date  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.RevRptCatCode:str = obj["RevRptCatCode"]
      """  Reverse Tax Report Category  """  
      self.APTranNo:int = obj["APTranNo"]
      """  APTranNo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReturnFlag:bool = obj["ReturnFlag"]
      """  Return Flag  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  GL Journal Code  associated with this TaxTran  """  
      self.JournalNum:int = obj["JournalNum"]
      """  GL Journal Number  associated with this TaxTran  """  
      self.JournalLine:int = obj["JournalLine"]
      """  GL Journal Line  associated with this TaxTran  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  OneTimeID  """  
      self.TempVendorTaxID:str = obj["TempVendorTaxID"]
      """  Vendor Tax ID  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicate that record was created for Reverse transaction  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.NLICPReportID:str = obj["NLICPReportID"]
      """  NLICPReportID  """  
      self.MscNum:int = obj["MscNum"]
      """  MscNum  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode  """  
      self.SourceTranDocTypeID:str = obj["SourceTranDocTypeID"]
      self.TransactionSource:str = obj["TransactionSource"]
      self.SourceLegalNumber:str = obj["SourceLegalNumber"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.ReportIDDescription:str = obj["ReportIDDescription"]
      self.TaxRateCodeDescription:str = obj["TaxRateCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tranDate
   tranNum
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      self.tranNum:int = obj["tranNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxCertListTableset:
   def __init__(self, obj):
      self.TaxTranList:list[Erp_Tablesets_TaxTranListRow] = obj["TaxTranList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxCertSearchTableset:
   def __init__(self, obj):
      self.TaxTran:list[Erp_Tablesets_TaxTranRow] = obj["TaxTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxTranListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  a number which is used to allow create a unique key for the file.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  identifies a Tax Region master record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.CompTaxID:str = obj["CompTaxID"]
      """  Company Tax ID  """  
      self.VendorTaxID:str = obj["VendorTaxID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.CustomerTaxID:str = obj["CustomerTaxID"]
      """  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this TaxTran  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this TaxTran.  """  
      self.InvoiceMemo:bool = obj["InvoiceMemo"]
      """  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for tax statement  """  
      self.TaxPrintDate:str = obj["TaxPrintDate"]
      """  Date Tax Document was printed  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  If field is non-blank it is considered exempt.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Key to link to Payment  """  
      self.ARInvoiceDate:str = obj["ARInvoiceDate"]
      """  Field To save the AR Invoice Date  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranNum:int = obj["TranNum"]
      """  a number which is used to allow create a unique key for the file.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.InEC:bool = obj["InEC"]
      """  Tax Region is in the European Community.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  identifies a Tax Region master record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this invoice. This is defaulted from the SalesTax.Percent.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this tax transaction.  This is assigned by the system.
Values can be; AR, AP.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.DocTaxableAmt:int = obj["DocTaxableAmt"]
      """  Taxable Amount for this line item/Misc charge. This value is set as an accumulation of non-exempt sales amount from the line and its associated miscellaneous records.  It could be tax exempt for two reasons, either the customer is exempt (invcdtl.TaxExempt > blank) or the item is exempt. In either case the detail amounts would not be added into the taxable amount.  To see if the item is exempt use the InvcDt/InvcMisc.TaxCat and the InvcTax.TaxCode to find a record in the SalesTxC. If a record is  found then it is exempt.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount. This is user maintainable and also defaulted when/if the user changes the tax code, tax percent or the taxable amount or the tax classification changes to non-taxable when the InvcDtl.TaxCat is changed.  They can override the calculated figure to provide for any tax calculations other than the simple percent of taxable. No tax is calculated when the InvcDtl.TaxExempt <> blank or a record is found in the SalesTxC file indicating that this item is not taxable. Otherwise it is calculated as TaxableAmt * Percent.  """  
      self.CompTaxID:str = obj["CompTaxID"]
      """  Company Tax ID  """  
      self.VendorTaxID:str = obj["VendorTaxID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.CustomerTaxID:str = obj["CustomerTaxID"]
      """  Optional field used to record the customers State Tax Identification number. Which is used on Sales Acknowledgments.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from CurrRate.CurrentRate.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.ReportID:str = obj["ReportID"]
      """  Sales tax report ID  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this report closed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting Date  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Tax Report Date  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """  Used to allow a second tax record using the same tax code on an invoice.   Allow the VAT report to Keep seperate totals for the 2 records used for this transaction.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this TaxTran  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this TaxTran.  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Indicates if this tax transaction is for a Reverse Charge.  """  
      self.ReportableAmt:int = obj["ReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction.  """  
      self.DocReportableAmt:int = obj["DocReportableAmt"]
      """  The reportable sales amount to the tax jurisdiction expressed in the Vendor's currency.  """  
      self.InvoiceMemo:bool = obj["InvoiceMemo"]
      """  Indicates the type of AP or AR invoice. Depending on the Source of the tax transaction (AR or AP): Yes = Debit/Credit Memo,  No = Regular AR/AP Invoice.  """  
      self.Rpt1ReportableAmt:int = obj["Rpt1ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ReportableAmt:int = obj["Rpt2ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ReportableAmt:int = obj["Rpt3ReportableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxableAmt:int = obj["Rpt1TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxableAmt:int = obj["Rpt2TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxableAmt:int = obj["Rpt3TaxableAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Tax Category.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited. Examples: SERV = Service, FRT = Freight, etc.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate Code  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  The date this invoice will get applied to the books when it is posted.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number for tax statement  """  
      self.TaxPrintDate:str = obj["TaxPrintDate"]
      """  Date Tax Document was printed  """  
      self.TaxPosted:bool = obj["TaxPosted"]
      """  Indicates if Tax Statement was posted  """  
      self.TaxPostDate:str = obj["TaxPostDate"]
      """  Date Tax Statement was posted  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EU Third Party flag  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  If field is non-blank it is considered exempt.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  Key to link to Payment  """  
      self.RecoverableAmt:int = obj["RecoverableAmt"]
      """  The amount of tax recoverable (deductible).  """  
      self.DocRecoverableAmt:int = obj["DocRecoverableAmt"]
      """  The amount of tax recoverable (deductible)  """  
      self.Rpt1RecoverableAmt:int = obj["Rpt1RecoverableAmt"]
      """  The amout of tax recoverable (deductible) in Rpt1 currency  """  
      self.Rpt2RecoverableAmt:int = obj["Rpt2RecoverableAmt"]
      """  Tha amount of tax recoverable (deductible) in RPT2 currency.  """  
      self.Rpt3RecoverableAmt:int = obj["Rpt3RecoverableAmt"]
      """  The amount of tax recoverable (deductible) in RPT3 currency  """  
      self.ARInvoiceDate:str = obj["ARInvoiceDate"]
      """  Field To save the AR Invoice Date  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.TaxAmtVar:int = obj["TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.DocTaxAmtVar:int = obj["DocTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt1TaxAmtVar:int = obj["Rpt1TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt2TaxAmtVar:int = obj["Rpt2TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.Rpt3TaxAmtVar:int = obj["Rpt3TaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate  """  
      self.RevRptCatCode:str = obj["RevRptCatCode"]
      """  Reverse Tax Report Category  """  
      self.APTranNo:int = obj["APTranNo"]
      """  APTranNo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReturnFlag:bool = obj["ReturnFlag"]
      """  Return Flag  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  GL Journal Code  associated with this TaxTran  """  
      self.JournalNum:int = obj["JournalNum"]
      """  GL Journal Number  associated with this TaxTran  """  
      self.JournalLine:int = obj["JournalLine"]
      """  GL Journal Line  associated with this TaxTran  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  OneTimeID  """  
      self.TempVendorTaxID:str = obj["TempVendorTaxID"]
      """  Vendor Tax ID  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicate that record was created for Reverse transaction  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.NLICPReportID:str = obj["NLICPReportID"]
      """  NLICPReportID  """  
      self.MscNum:int = obj["MscNum"]
      """  MscNum  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode  """  
      self.SourceTranDocTypeID:str = obj["SourceTranDocTypeID"]
      self.TransactionSource:str = obj["TransactionSource"]
      self.SourceLegalNumber:str = obj["SourceLegalNumber"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.ReportIDDescription:str = obj["ReportIDDescription"]
      self.TaxRateCodeDescription:str = obj["TaxRateCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtTaxCertSearchTableset:
   def __init__(self, obj):
      self.TaxTran:list[Erp_Tablesets_TaxTranRow] = obj["TaxTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   tranDate
   tranNum
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      self.tranNum:int = obj["tranNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxCertSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxCertSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxCertSearchTableset] = obj["returnObj"]
      pass

class GetListPercCertificates_input:
   """ Required : 
   taxTranWhereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.taxTranWhereClause:str = obj["taxTranWhereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListPercCertificates_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxCertListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxCertListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxTran_input:
   """ Required : 
   ds
   tranDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxCertSearchTableset] = obj["ds"]
      self.tranDate:str = obj["tranDate"]
      pass

class GetNewTaxTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxCertSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxTran:str = obj["whereClauseTaxTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxCertSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtTaxCertSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxCertSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxCertSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxCertSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

