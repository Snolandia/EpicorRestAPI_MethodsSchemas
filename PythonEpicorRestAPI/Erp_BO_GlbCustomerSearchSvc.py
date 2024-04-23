import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbCustomerSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbCustomerSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbCustomerSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCustomerSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches",headers=creds) as resp:
           return await resp.json()

async def post_GlbCustomerSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCustomerSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbCustomerSearches_Company_GlbCompany_GlbCustNum(Company, GlbCompany, GlbCustNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbCustomerSearch item
   Description: Calls GetByID to retrieve the GlbCustomerSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCustomerSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbCustNum: Desc: GlbCustNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches(" + Company + "," + GlbCompany + "," + GlbCustNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbCustomerSearches_Company_GlbCompany_GlbCustNum(Company, GlbCompany, GlbCustNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbCustomerSearch for the service
   Description: Calls UpdateExt to update GlbCustomerSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCustomerSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbCustNum: Desc: GlbCustNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCustomerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches(" + Company + "," + GlbCompany + "," + GlbCustNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbCustomerSearches_Company_GlbCompany_GlbCustNum(Company, GlbCompany, GlbCustNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbCustomerSearch item
   Description: Call UpdateExt to delete GlbCustomerSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCustomerSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbCustNum: Desc: GlbCustNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/GlbCustomerSearches(" + Company + "," + GlbCompany + "," + GlbCustNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustomerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbCustomer, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGlbCustomer=" + whereClauseGlbCustomer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, glbCustNum, epicorHeaders = None):
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
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glbCustNum=" + glbCustNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbCustomer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbCustomerSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCustomerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustomerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbCustomerRow] = obj["value"]
      pass

class Erp_Tablesets_GlbCustomerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbCustID:str = obj["GlbCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  """  
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The Sales Territory for the Customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  """  
      self.PrintStatements:bool = obj["PrintStatements"]
      """  Controls the selection for printing of Accounts Receivable statements for a customer.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  """  
      self.PrintAck:bool = obj["PrintAck"]
      """   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  """  
      self.FinCharges:bool = obj["FinCharges"]
      """  Controls whether or not the customer included in the finance charge calculation process.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  """  
      self.PrimBCon:int = obj["PrimBCon"]
      """  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.EstDate:str = obj["EstDate"]
      """  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  """  
      self.BillDay:int = obj["BillDay"]
      """   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  """  
      self.OneInvPerPS:bool = obj["OneInvPerPS"]
      """  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date that the next credit check should be made for that customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      self.CreditClearDate:str = obj["CreditClearDate"]
      self.CreditClearTime:str = obj["CreditClearTime"]
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.EDITest:bool = obj["EDITest"]
      """  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.EDITranslator:str = obj["EDITranslator"]
      """  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.BTName:str = obj["BTName"]
      self.BTAddress1:str = obj["BTAddress1"]
      self.BTAddress2:str = obj["BTAddress2"]
      self.BTAddress3:str = obj["BTAddress3"]
      self.BTCity:str = obj["BTCity"]
      self.BTState:str = obj["BTState"]
      self.BTZip:str = obj["BTZip"]
      self.BTCountryNum:int = obj["BTCountryNum"]
      """  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  Country is used as part of the bill-to address. It can be left blank.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The bill-to address Phone Number for the customer.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The bill-to address Fax telephone number for the customer. Optional field.  """  
      self.BTFormatStr:str = obj["BTFormatStr"]
      """  Optional bill-to address format.  Controls the address format used on crystal forms.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The unique Customer Number of the Parent.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.ICCust:bool = obj["ICCust"]
      """  This is an inter-company customer.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the customer.  """  
      self.ShippingQualifier:str = obj["ShippingQualifier"]
      """  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  """  
      self.LinkPortNum:int = obj["LinkPortNum"]
      """  Used with Global alerts  """  
      self.WebCustomer:bool = obj["WebCustomer"]
      """  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  """  
      self.CustomerType:str = obj["CustomerType"]
      """   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is not included in marketing lists  """  
      self.TerritoryLock:bool = obj["TerritoryLock"]
      """  This customers territory cannot be changed by any process that changes territories  """  
      self.CustURL:str = obj["CustURL"]
      """  Customers Website URL .  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The sales territory that the system will assign based on new values in the Sales territory boundary table.  """  
      self.ExtID:str = obj["ExtID"]
      self.ConsolidateSO:bool = obj["ConsolidateSO"]
      """  APK - added for consolidation accross multiple SO's for the same customer  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Marks the customer as a global customer, available to be sent out to other companies  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldCustNum:int = obj["OldCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.OldCustID:str = obj["OldCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  """  
      self.ExternalID:str = obj["ExternalID"]
      self.CheckDuplicatePO:bool = obj["CheckDuplicatePO"]
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.RfqAttachAllow:bool = obj["RfqAttachAllow"]
      """  Indicates whether RFQ Attachments are allowed for this Customer  """  
      self.DiscountQualifier:str = obj["DiscountQualifier"]
      """   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  """  
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DemandAddAction:str = obj["DemandAddAction"]
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      self.DemandAutoAccept:bool = obj["DemandAutoAccept"]
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      self.DemandDateType:str = obj["DemandDateType"]
      self.DemandDayOfWeek:int = obj["DemandDayOfWeek"]
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      self.DemandUseSysDate:bool = obj["DemandUseSysDate"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.CreditDays:int = obj["CreditDays"]
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      self.LateBuffer:int = obj["LateBuffer"]
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      self.AddressVal:bool = obj["AddressVal"]
      self.ExcFromVal:bool = obj["ExcFromVal"]
      self.RebateForm:str = obj["RebateForm"]
      self.RebateVendorNum:int = obj["RebateVendorNum"]
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.ChargeCode:str = obj["ChargeCode"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFAddress3:str = obj["FFAddress3"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFCountryNum:int = obj["FFCountryNum"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVEmailType:str = obj["UPSQVEmailType"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.ARCreditTotal:int = obj["ARCreditTotal"]
      self.PICreditTotal:int = obj["PICreditTotal"]
      self.SOCreditTotal:int = obj["SOCreditTotal"]
      self.TaxMethod:str = obj["TaxMethod"]
      self.TaxRoundRule:int = obj["TaxRoundRule"]
      self.AcrossNatAcc:bool = obj["AcrossNatAcc"]
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      self.OverrideRlsClass:bool = obj["OverrideRlsClass"]
      self.ValidPayer:bool = obj["ValidPayer"]
      self.ValidShipTo:bool = obj["ValidShipTo"]
      self.ValidSoldTo:bool = obj["ValidSoldTo"]
      self.AllowOTS:bool = obj["AllowOTS"]
      self.ManagedVendID:str = obj["ManagedVendID"]
      self.ManagedVendNum:int = obj["ManagedVendNum"]
      self.ThirdPLCust:bool = obj["ThirdPLCust"]
      self.NARlsClassCode:str = obj["NARlsClassCode"]
      self.AutoGenPromNotes:bool = obj["AutoGenPromNotes"]
      self.DirectDebiting:bool = obj["DirectDebiting"]
      self.PartPayment:bool = obj["PartPayment"]
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      self.NAParentsCreditUsed:int = obj["NAParentsCreditUsed"]
      self.NASharedCreditUsed:int = obj["NASharedCreditUsed"]
      self.NAOwnCreditUsed:int = obj["NAOwnCreditUsed"]
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      self.GlbNAParentsCreditUsed:int = obj["GlbNAParentsCreditUsed"]
      self.GlbNASharedCreditUsed:int = obj["GlbNASharedCreditUsed"]
      self.ReminderCode:str = obj["ReminderCode"]
      self.AllowShipTo3:bool = obj["AllowShipTo3"]
      self.NACreditUpdate:str = obj["NACreditUpdate"]
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      self.CustPartOpts:str = obj["CustPartOpts"]
      self.HasBank:bool = obj["HasBank"]
      self.PMUID:int = obj["PMUID"]
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      self.AcctRefNumber:str = obj["AcctRefNumber"]
      self.DemandCheckCUMM:bool = obj["DemandCheckCUMM"]
      self.DemandCheckCUMMAction:str = obj["DemandCheckCUMMAction"]
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      self.DemandPricing:str = obj["DemandPricing"]
      self.DmdCheckPartialShip:bool = obj["DmdCheckPartialShip"]
      self.DmdCheckShipAction:str = obj["DmdCheckShipAction"]
      self.InvPerPackLine:bool = obj["InvPerPackLine"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.OurBankCode:str = obj["OurBankCode"]
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      self.DemandSplitSched:bool = obj["DemandSplitSched"]
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      self.ERSOrder:bool = obj["ERSOrder"]
      self.PBTerms:int = obj["PBTerms"]
      self.PeriodicBilling:bool = obj["PeriodicBilling"]
      self.PreferredBank:str = obj["PreferredBank"]
      self.SICCode:int = obj["SICCode"]
      self.ICCode:str = obj["ICCode"]
      self.OTSmartString:bool = obj["OTSmartString"]
      self.DeferredRev:bool = obj["DeferredRev"]
      self.RACode:str = obj["RACode"]
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkCustID:str = obj["LinkCustID"]
      """  Customer.CustID to link to (new or existing)  """  
      self.DisplayHold:str = obj["DisplayHold"]
      self.DisplayCustomerType:str = obj["DisplayCustomerType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbCustID:str = obj["GlbCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  """  
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The Sales Territory for the Customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  """  
      self.PrintStatements:bool = obj["PrintStatements"]
      """  Controls the selection for printing of Accounts Receivable statements for a customer.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  """  
      self.PrintAck:bool = obj["PrintAck"]
      """   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  """  
      self.FinCharges:bool = obj["FinCharges"]
      """  Controls whether or not the customer included in the finance charge calculation process.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  """  
      self.PrimBCon:int = obj["PrimBCon"]
      """  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.EstDate:str = obj["EstDate"]
      """  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  """  
      self.BillDay:int = obj["BillDay"]
      """   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  """  
      self.OneInvPerPS:bool = obj["OneInvPerPS"]
      """  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date that the next credit check should be made for that customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      self.CreditClearDate:str = obj["CreditClearDate"]
      self.CreditClearTime:str = obj["CreditClearTime"]
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.EDITest:bool = obj["EDITest"]
      """  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.EDITranslator:str = obj["EDITranslator"]
      """  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.BTName:str = obj["BTName"]
      self.BTAddress1:str = obj["BTAddress1"]
      self.BTAddress2:str = obj["BTAddress2"]
      self.BTAddress3:str = obj["BTAddress3"]
      self.BTCity:str = obj["BTCity"]
      self.BTState:str = obj["BTState"]
      self.BTZip:str = obj["BTZip"]
      self.BTCountryNum:int = obj["BTCountryNum"]
      """  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  Country is used as part of the bill-to address. It can be left blank.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The bill-to address Phone Number for the customer.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The bill-to address Fax telephone number for the customer. Optional field.  """  
      self.BTFormatStr:str = obj["BTFormatStr"]
      """  Optional bill-to address format.  Controls the address format used on crystal forms.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The unique Customer Number of the Parent.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.ICCust:bool = obj["ICCust"]
      """  This is an inter-company customer.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the customer.  """  
      self.ShippingQualifier:str = obj["ShippingQualifier"]
      """  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  """  
      self.LinkPortNum:int = obj["LinkPortNum"]
      """  Used with Global alerts  """  
      self.WebCustomer:bool = obj["WebCustomer"]
      """  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  """  
      self.CustomerType:str = obj["CustomerType"]
      """   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is not included in marketing lists  """  
      self.TerritoryLock:bool = obj["TerritoryLock"]
      """  This customers territory cannot be changed by any process that changes territories  """  
      self.CustURL:str = obj["CustURL"]
      """  Customers Website URL .  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The sales territory that the system will assign based on new values in the Sales territory boundary table.  """  
      self.ExtID:str = obj["ExtID"]
      self.ConsolidateSO:bool = obj["ConsolidateSO"]
      """  APK - added for consolidation accross multiple SO's for the same customer  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Marks the customer as a global customer, available to be sent out to other companies  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldCustNum:int = obj["OldCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.OldCustID:str = obj["OldCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  """  
      self.ExternalID:str = obj["ExternalID"]
      self.CheckDuplicatePO:bool = obj["CheckDuplicatePO"]
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.RfqAttachAllow:bool = obj["RfqAttachAllow"]
      """  Indicates whether RFQ Attachments are allowed for this Customer  """  
      self.DiscountQualifier:str = obj["DiscountQualifier"]
      """   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  """  
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DemandAddAction:str = obj["DemandAddAction"]
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      self.DemandAutoAccept:bool = obj["DemandAutoAccept"]
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      self.DemandDateType:str = obj["DemandDateType"]
      self.DemandDayOfWeek:int = obj["DemandDayOfWeek"]
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      self.DemandUseSysDate:bool = obj["DemandUseSysDate"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.CreditDays:int = obj["CreditDays"]
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      self.LateBuffer:int = obj["LateBuffer"]
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      self.AddressVal:bool = obj["AddressVal"]
      self.ExcFromVal:bool = obj["ExcFromVal"]
      self.RebateForm:str = obj["RebateForm"]
      self.RebateVendorNum:int = obj["RebateVendorNum"]
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.ChargeCode:str = obj["ChargeCode"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFAddress3:str = obj["FFAddress3"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFCountryNum:int = obj["FFCountryNum"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVEmailType:str = obj["UPSQVEmailType"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.ARCreditTotal:int = obj["ARCreditTotal"]
      self.PICreditTotal:int = obj["PICreditTotal"]
      self.SOCreditTotal:int = obj["SOCreditTotal"]
      self.TaxMethod:str = obj["TaxMethod"]
      self.TaxRoundRule:int = obj["TaxRoundRule"]
      self.AcrossNatAcc:bool = obj["AcrossNatAcc"]
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      self.OverrideRlsClass:bool = obj["OverrideRlsClass"]
      self.ValidPayer:bool = obj["ValidPayer"]
      self.ValidShipTo:bool = obj["ValidShipTo"]
      self.ValidSoldTo:bool = obj["ValidSoldTo"]
      self.AllowOTS:bool = obj["AllowOTS"]
      self.ManagedVendID:str = obj["ManagedVendID"]
      self.ManagedVendNum:int = obj["ManagedVendNum"]
      self.ThirdPLCust:bool = obj["ThirdPLCust"]
      self.NARlsClassCode:str = obj["NARlsClassCode"]
      self.AutoGenPromNotes:bool = obj["AutoGenPromNotes"]
      self.DirectDebiting:bool = obj["DirectDebiting"]
      self.PartPayment:bool = obj["PartPayment"]
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      self.NAParentsCreditUsed:int = obj["NAParentsCreditUsed"]
      self.NASharedCreditUsed:int = obj["NASharedCreditUsed"]
      self.NAOwnCreditUsed:int = obj["NAOwnCreditUsed"]
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      self.GlbNAParentsCreditUsed:int = obj["GlbNAParentsCreditUsed"]
      self.GlbNASharedCreditUsed:int = obj["GlbNASharedCreditUsed"]
      self.ReminderCode:str = obj["ReminderCode"]
      self.AllowShipTo3:bool = obj["AllowShipTo3"]
      self.NACreditUpdate:str = obj["NACreditUpdate"]
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      self.CustPartOpts:str = obj["CustPartOpts"]
      self.HasBank:bool = obj["HasBank"]
      self.PMUID:int = obj["PMUID"]
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      self.AcctRefNumber:str = obj["AcctRefNumber"]
      self.DemandCheckCUMM:bool = obj["DemandCheckCUMM"]
      self.DemandCheckCUMMAction:str = obj["DemandCheckCUMMAction"]
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      self.DemandPricing:str = obj["DemandPricing"]
      self.DmdCheckPartialShip:bool = obj["DmdCheckPartialShip"]
      self.DmdCheckShipAction:str = obj["DmdCheckShipAction"]
      self.InvPerPackLine:bool = obj["InvPerPackLine"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.OurBankCode:str = obj["OurBankCode"]
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      self.DemandSplitSched:bool = obj["DemandSplitSched"]
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      self.ERSOrder:bool = obj["ERSOrder"]
      self.PBTerms:int = obj["PBTerms"]
      self.PeriodicBilling:bool = obj["PeriodicBilling"]
      self.PreferredBank:str = obj["PreferredBank"]
      self.SICCode:int = obj["SICCode"]
      self.ICCode:str = obj["ICCode"]
      self.OTSmartString:bool = obj["OTSmartString"]
      self.DeferredRev:bool = obj["DeferredRev"]
      self.RACode:str = obj["RACode"]
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.CustPricingSchema:str = obj["CustPricingSchema"]
      """  CustPricingSchema  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGBillToProvinceCode:str = obj["AGBillToProvinceCode"]
      """  AGBillToProvinceCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocTypeCode:str = obj["AGIDDocTypeCode"]
      """  AGIDDocTypeCode  """  
      self.AGIDDocumentNumber:str = obj["AGIDDocumentNumber"]
      """  AGIDDocumentNumber  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.Collections:bool = obj["Collections"]
      """  Collections  """  
      self.CollectionsDate:str = obj["CollectionsDate"]
      """  CollectionsDate  """  
      self.DateCollectionPosted:str = obj["DateCollectionPosted"]
      """  DateCollectionPosted  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PEIdentityDocType  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PEDocumentID  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  PEGoodsContributor  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  PEWithholdAgent  """  
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  PECollectionAgent  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  PENotFound  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  PENoAddress  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.InvcOrderCmpDflt:bool = obj["InvcOrderCmpDflt"]
      """  InvcOrderCmpDflt  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.RegistrationCode:str = obj["RegistrationCode"]
      """  RegistrationCode  """  
      self.EAddress:str = obj["EAddress"]
      """  EAddress  """  
      self.DemandCheckForRunOutPart:bool = obj["DemandCheckForRunOutPart"]
      """  DemandCheckForRunOutPart  """  
      self.DemandCheckForRunOutPartAction:str = obj["DemandCheckForRunOutPartAction"]
      """  DemandCheckForRunOutPartAction  """  
      self.EInvCompanyIDAttr:str = obj["EInvCompanyIDAttr"]
      """  EInvCompanyIDAttr  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.COIsOneTimeCust:bool = obj["COIsOneTimeCust"]
      """  COIsOneTimeCust  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  OurSupplierCode  """  
      self.ECCType:str = obj["ECCType"]
      """  ECCType  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  SyncToExternalCRM  """  
      self.ExternalCRMGlbCustomerID:str = obj["ExternalCRMGlbCustomerID"]
      """  ExternalCRMGlbCustomerID  """  
      self.ExternalCRMGlbCustomerType:str = obj["ExternalCRMGlbCustomerType"]
      """  ExternalCRMGlbCustomerType  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  ExternalCRMLastSync  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  ExternalCRMSyncRequired  """  
      self.Ownership:str = obj["Ownership"]
      """  Ownership  """  
      self.Industry:str = obj["Industry"]
      """  Industry  """  
      self.AnnualRevenue:int = obj["AnnualRevenue"]
      """  AnnualRevenue  """  
      self.NumberOfEmployees:int = obj["NumberOfEmployees"]
      """  NumberOfEmployees  """  
      self.TickerLocation:str = obj["TickerLocation"]
      """  TickerLocation  """  
      self.TickerSymbol:str = obj["TickerSymbol"]
      """  TickerSymbol  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TWGUIRegNum  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.ConsolidateLinesPerPart:bool = obj["ConsolidateLinesPerPart"]
      """  ConsolidateLinesPerPart  """  
      self.TWTaxPayerType:int = obj["TWTaxPayerType"]
      """  TWTaxPayerType  """  
      self.TWDeductGUIFormatCode:str = obj["TWDeductGUIFormatCode"]
      """  TWDeductGUIFormatCode  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PEPerceptionRegime:str = obj["PEPerceptionRegime"]
      """  PEPerceptionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  INGSTComplianceRate  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  SendToFSA  """  
      self.MXGeneralPublic:bool = obj["MXGeneralPublic"]
      """  MXGeneralPublic  """  
      self.AgingCreditHold:bool = obj["AgingCreditHold"]
      """  AgingCreditHold  """  
      self.AgingCreditHoldDate:str = obj["AgingCreditHoldDate"]
      """  AgingCreditHoldDate  """  
      self.AgingCreditHoldSource:str = obj["AgingCreditHoldSource"]
      """  AgingCreditHoldSource  """  
      self.AgingCreditClearUserID:str = obj["AgingCreditClearUserID"]
      """  AgingCreditClearUserID  """  
      self.AgingCreditClearDate:str = obj["AgingCreditClearDate"]
      """  AgingCreditClearDate  """  
      self.AgingCreditCode:str = obj["AgingCreditCode"]
      """  AgingCreditCode  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  ImporterOfRecord  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.EInvEndpointIDAttr:str = obj["EInvEndpointIDAttr"]
      """  EInvEndpointIDAttr  """  
      self.UseBlindShipping:bool = obj["UseBlindShipping"]
      """  Indicates whether sales orders from this sold to customer should be treated as Blind Shipments by Manifest.  """  
      self.ELIEinvoice:bool = obj["ELIEinvoice"]
      """  ELIEinvoice  """  
      self.ELIDefReportID:str = obj["ELIDefReportID"]
      """  ELIDefReportID  """  
      self.ELIDefStyleNum:int = obj["ELIDefStyleNum"]
      """  ELIDefStyleNum  """  
      self.ELIDefToMail:str = obj["ELIDefToMail"]
      """  ELIDefToMail  """  
      self.ELIDefCCMail:str = obj["ELIDefCCMail"]
      """  ELIDefCCMail  """  
      self.ELIDefMailTempID:str = obj["ELIDefMailTempID"]
      """  ELIDefMailTempID  """  
      self.ELISendMail:bool = obj["ELISendMail"]
      """  ELISendMail  """  
      self.COFiscalResp1:str = obj["COFiscalResp1"]
      """  COFiscalResp1  """  
      self.COFiscalResp2:str = obj["COFiscalResp2"]
      """  COFiscalResp2  """  
      self.COFiscalResp3:str = obj["COFiscalResp3"]
      """  COFiscalResp3  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Central Collection  """  
      self.NettingVendorNum:int = obj["NettingVendorNum"]
      """  NettingVendorNum  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORINumber  """  
      self.AGIsElectronicCreditInvEligible:bool = obj["AGIsElectronicCreditInvEligible"]
      """  AGIsElectronicCreditInvEligible  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  TaxValidationStatus  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  TaxValidationDate  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.ELIOperatorCode:str = obj["ELIOperatorCode"]
      """  ELIOperatorCode  """  
      self.ELISendingOption:int = obj["ELISendingOption"]
      """  ELISendingOption  """  
      self.ELIOperatorID:str = obj["ELIOperatorID"]
      """  ELIOperatorID  """  
      self.EInvExternalID:str = obj["EInvExternalID"]
      """  EInvExternalID  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.ExclusionMonth:int = obj["ExclusionMonth"]
      """  ExclusionMonth  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMRegionCode:str = obj["FSMRegionCode"]
      """  FSMRegionCode  """  
      self.FSMArea:str = obj["FSMArea"]
      """  FSMArea  """  
      self.ELIRcptDefStyleNum:int = obj["ELIRcptDefStyleNum"]
      """  ELIRcptDefStyleNum  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.DisplayCustomerType:str = obj["DisplayCustomerType"]
      self.LinkCustID:str = obj["LinkCustID"]
      """  Customer.CustID to link to (new or existing)  """  
      self.DisplayHold:str = obj["DisplayHold"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   glbCompany
   glbCustNum
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbCustNum:int = obj["glbCustNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbCustomerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbCustID:str = obj["GlbCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  """  
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The Sales Territory for the Customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  """  
      self.PrintStatements:bool = obj["PrintStatements"]
      """  Controls the selection for printing of Accounts Receivable statements for a customer.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  """  
      self.PrintAck:bool = obj["PrintAck"]
      """   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  """  
      self.FinCharges:bool = obj["FinCharges"]
      """  Controls whether or not the customer included in the finance charge calculation process.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  """  
      self.PrimBCon:int = obj["PrimBCon"]
      """  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.EstDate:str = obj["EstDate"]
      """  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  """  
      self.BillDay:int = obj["BillDay"]
      """   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  """  
      self.OneInvPerPS:bool = obj["OneInvPerPS"]
      """  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date that the next credit check should be made for that customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      self.CreditClearDate:str = obj["CreditClearDate"]
      self.CreditClearTime:str = obj["CreditClearTime"]
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.EDITest:bool = obj["EDITest"]
      """  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.EDITranslator:str = obj["EDITranslator"]
      """  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.BTName:str = obj["BTName"]
      self.BTAddress1:str = obj["BTAddress1"]
      self.BTAddress2:str = obj["BTAddress2"]
      self.BTAddress3:str = obj["BTAddress3"]
      self.BTCity:str = obj["BTCity"]
      self.BTState:str = obj["BTState"]
      self.BTZip:str = obj["BTZip"]
      self.BTCountryNum:int = obj["BTCountryNum"]
      """  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  Country is used as part of the bill-to address. It can be left blank.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The bill-to address Phone Number for the customer.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The bill-to address Fax telephone number for the customer. Optional field.  """  
      self.BTFormatStr:str = obj["BTFormatStr"]
      """  Optional bill-to address format.  Controls the address format used on crystal forms.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The unique Customer Number of the Parent.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.ICCust:bool = obj["ICCust"]
      """  This is an inter-company customer.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the customer.  """  
      self.ShippingQualifier:str = obj["ShippingQualifier"]
      """  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  """  
      self.LinkPortNum:int = obj["LinkPortNum"]
      """  Used with Global alerts  """  
      self.WebCustomer:bool = obj["WebCustomer"]
      """  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  """  
      self.CustomerType:str = obj["CustomerType"]
      """   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is not included in marketing lists  """  
      self.TerritoryLock:bool = obj["TerritoryLock"]
      """  This customers territory cannot be changed by any process that changes territories  """  
      self.CustURL:str = obj["CustURL"]
      """  Customers Website URL .  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The sales territory that the system will assign based on new values in the Sales territory boundary table.  """  
      self.ExtID:str = obj["ExtID"]
      self.ConsolidateSO:bool = obj["ConsolidateSO"]
      """  APK - added for consolidation accross multiple SO's for the same customer  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Marks the customer as a global customer, available to be sent out to other companies  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldCustNum:int = obj["OldCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.OldCustID:str = obj["OldCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  """  
      self.ExternalID:str = obj["ExternalID"]
      self.CheckDuplicatePO:bool = obj["CheckDuplicatePO"]
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.RfqAttachAllow:bool = obj["RfqAttachAllow"]
      """  Indicates whether RFQ Attachments are allowed for this Customer  """  
      self.DiscountQualifier:str = obj["DiscountQualifier"]
      """   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  """  
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DemandAddAction:str = obj["DemandAddAction"]
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      self.DemandAutoAccept:bool = obj["DemandAutoAccept"]
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      self.DemandDateType:str = obj["DemandDateType"]
      self.DemandDayOfWeek:int = obj["DemandDayOfWeek"]
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      self.DemandUseSysDate:bool = obj["DemandUseSysDate"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.CreditDays:int = obj["CreditDays"]
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      self.LateBuffer:int = obj["LateBuffer"]
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      self.AddressVal:bool = obj["AddressVal"]
      self.ExcFromVal:bool = obj["ExcFromVal"]
      self.RebateForm:str = obj["RebateForm"]
      self.RebateVendorNum:int = obj["RebateVendorNum"]
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.ChargeCode:str = obj["ChargeCode"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFAddress3:str = obj["FFAddress3"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFCountryNum:int = obj["FFCountryNum"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVEmailType:str = obj["UPSQVEmailType"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.ARCreditTotal:int = obj["ARCreditTotal"]
      self.PICreditTotal:int = obj["PICreditTotal"]
      self.SOCreditTotal:int = obj["SOCreditTotal"]
      self.TaxMethod:str = obj["TaxMethod"]
      self.TaxRoundRule:int = obj["TaxRoundRule"]
      self.AcrossNatAcc:bool = obj["AcrossNatAcc"]
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      self.OverrideRlsClass:bool = obj["OverrideRlsClass"]
      self.ValidPayer:bool = obj["ValidPayer"]
      self.ValidShipTo:bool = obj["ValidShipTo"]
      self.ValidSoldTo:bool = obj["ValidSoldTo"]
      self.AllowOTS:bool = obj["AllowOTS"]
      self.ManagedVendID:str = obj["ManagedVendID"]
      self.ManagedVendNum:int = obj["ManagedVendNum"]
      self.ThirdPLCust:bool = obj["ThirdPLCust"]
      self.NARlsClassCode:str = obj["NARlsClassCode"]
      self.AutoGenPromNotes:bool = obj["AutoGenPromNotes"]
      self.DirectDebiting:bool = obj["DirectDebiting"]
      self.PartPayment:bool = obj["PartPayment"]
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      self.NAParentsCreditUsed:int = obj["NAParentsCreditUsed"]
      self.NASharedCreditUsed:int = obj["NASharedCreditUsed"]
      self.NAOwnCreditUsed:int = obj["NAOwnCreditUsed"]
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      self.GlbNAParentsCreditUsed:int = obj["GlbNAParentsCreditUsed"]
      self.GlbNASharedCreditUsed:int = obj["GlbNASharedCreditUsed"]
      self.ReminderCode:str = obj["ReminderCode"]
      self.AllowShipTo3:bool = obj["AllowShipTo3"]
      self.NACreditUpdate:str = obj["NACreditUpdate"]
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      self.CustPartOpts:str = obj["CustPartOpts"]
      self.HasBank:bool = obj["HasBank"]
      self.PMUID:int = obj["PMUID"]
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      self.AcctRefNumber:str = obj["AcctRefNumber"]
      self.DemandCheckCUMM:bool = obj["DemandCheckCUMM"]
      self.DemandCheckCUMMAction:str = obj["DemandCheckCUMMAction"]
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      self.DemandPricing:str = obj["DemandPricing"]
      self.DmdCheckPartialShip:bool = obj["DmdCheckPartialShip"]
      self.DmdCheckShipAction:str = obj["DmdCheckShipAction"]
      self.InvPerPackLine:bool = obj["InvPerPackLine"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.OurBankCode:str = obj["OurBankCode"]
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      self.DemandSplitSched:bool = obj["DemandSplitSched"]
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      self.ERSOrder:bool = obj["ERSOrder"]
      self.PBTerms:int = obj["PBTerms"]
      self.PeriodicBilling:bool = obj["PeriodicBilling"]
      self.PreferredBank:str = obj["PreferredBank"]
      self.SICCode:int = obj["SICCode"]
      self.ICCode:str = obj["ICCode"]
      self.OTSmartString:bool = obj["OTSmartString"]
      self.DeferredRev:bool = obj["DeferredRev"]
      self.RACode:str = obj["RACode"]
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkCustID:str = obj["LinkCustID"]
      """  Customer.CustID to link to (new or existing)  """  
      self.DisplayHold:str = obj["DisplayHold"]
      self.DisplayCustomerType:str = obj["DisplayCustomerType"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCustomerListTableset:
   def __init__(self, obj):
      self.GlbCustomerList:list[Erp_Tablesets_GlbCustomerListRow] = obj["GlbCustomerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbCustomerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GlbCustID:str = obj["GlbCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the owner company  """  
      self.GlbCustNum:int = obj["GlbCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the owner company  """  
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.ResaleID:str = obj["ResaleID"]
      """  Optional field used to record the customer's State Tax Identification number, which is used on Sales Acknowledgments.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """   Contains the default SalesRep for the specific customer. This field is used to supply defaults to Order Entry and Invoice entry for invoices that do not reference Orders.
It can be left blank or must be valid in the SalesRep master file.  """  
      self.TerritoryID:str = obj["TerritoryID"]
      """  The Sales Territory for the Customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Contains the key of the default ship to for a customer. A blank value indicates that the name and address in the Customer file is considered the default ship to. This field is updated when the user marks the check box in shipto maintenance indicating that the ship to is to be designated as the default. This default will be used in areas such as Sales Order entry.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default sales terms that should be used for this customer. This field can't be left blank, it must be valid in the Terms file. A default may be supplied by XaSyst.TermsCode if not blank.  It supplies the default in Order entry and Invoice entry.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the default ShipVia for a customer. This is an optional field, it can be left blank or it must be valid in the ShipVia master file.  """  
      self.PrintStatements:bool = obj["PrintStatements"]
      """  Controls the selection for printing of Accounts Receivable statements for a customer.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only customers that are PrintLabels = Yes will be selected for printing of mailing labels.  """  
      self.PrintAck:bool = obj["PrintAck"]
      """   Allows the user to establish whether or not a specific customer requires Sales Order Acknowledgments.  This does not force or limit the printing of sales acknowledgments directly from within Order Entry.  Order entry displays this setting to the user so that they know  if they should print the acknowledgment.
For batch mode printing, (where ranges of sales orders are selected...future release) this setting will be used to exclude orders from printing.  """  
      self.FinCharges:bool = obj["FinCharges"]
      """  Controls whether or not the customer included in the finance charge calculation process.  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Customer Group code for a customer.  This can be blank or it must be valid in the CustsGrup file. This field will be used as a sort and selection parameter for reporting.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  An optional field used to establish a default purchasing discount percentage for a customer. This value is supplied to order entry as a default for line item discount percent.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Order Entry and Quoting.  """  
      self.PrimBCon:int = obj["PrimBCon"]
      """  The same as the PrimPCon except that this is the Billing contact and this is used as a default in invoice entry.  """  
      self.PrimSCon:int = obj["PrimSCon"]
      """  Same as PrimPCon except that this the Shipping contact and is used as a default in Packing Slip entry.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific customer. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.EstDate:str = obj["EstDate"]
      """  The date when they were established as a customer. Use the system date as a default when creating new customers. This is user maintainable.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field. Field is displayed in Order entry when no contact is specifically given or the contact has a blank fax number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates the reason why  customer is normally exempt from sales tax. Used as a default in invoice entry.  If field is non-blank it is considered exempt.   This code is totally user definable and no validation is required.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  The ID that establishes link to the default QMarkUp record which provides default markup percents used by quote entry for this customer. This ID is not directly entered. Instead it is derived via the user entering the description of the QMarkUp record. This can be left blank, else must be valid.  """  
      self.BillDay:int = obj["BillDay"]
      """   ** 6.0 extended functionality
Represents the day of the week that this customer is billed. The valid values are 0-7 where 0=All,1=Sun,2=Mon,...,7=Sat.  
** (where the bill-frequency = 'W' (weekly)
** (where bill-frequency = 'M' (monthly) this field is 1 -> 31
    representing the day of the month to bill on.
This is used during the "Get Shipments" function of invoice entry. For example, if the customer has BillDay = 4(Wed),  the Get Shipments function will select all the packing slips with a ship date that is less  than or equal to the latest Wednesday's date.
** The same also applies to monthly billing (1-31)  """  
      self.OneInvPerPS:bool = obj["OneInvPerPS"]
      """  "Combine" Multiple Packing Slips into one Invoice.  NOTE: The field name does not correctly represent what this actually does !  This value is used during the "Get Shipments" function of invoice entry to control how invoices should be created when there are multiple packing slips for the same customer. Basically, if this value is YES then packing slips for the same Order, Fiscal Period are combined into a single invoice. If this value is NO then each packing slip will create a single invoice.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for a customers orders.  Order Entry uses this as a default to OrderHed.FOB.  """  
      self.CreditIncludeOrders:bool = obj["CreditIncludeOrders"]
      """  Indicates that Open Orders are to be included in the credit limit checking. This checkbox will also include open service contracts.  """  
      self.CreditReviewDate:str = obj["CreditReviewDate"]
      """  Date that the next credit check should be made for that customer.  """  
      self.CreditHoldDate:str = obj["CreditHoldDate"]
      self.CreditHoldSource:str = obj["CreditHoldSource"]
      self.CreditClearUserID:str = obj["CreditClearUserID"]
      self.CreditClearDate:str = obj["CreditClearDate"]
      self.CreditClearTime:str = obj["CreditClearTime"]
      self.EDICode:str = obj["EDICode"]
      """  This is the Trading Partner ID that is used for incoming and outgoing EDI.  """  
      self.EDITest:bool = obj["EDITest"]
      """  EDI test mode.  When customers are first set up for EDI it is useful to send all documents in test mode so trading partners can verify the data before going into production mode.  """  
      self.EDITranslator:str = obj["EDITranslator"]
      """  Identifies which EDI package the customer is using.  If not null in must be valid in the EDITrnsl table.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.BTName:str = obj["BTName"]
      self.BTAddress1:str = obj["BTAddress1"]
      self.BTAddress2:str = obj["BTAddress2"]
      self.BTAddress3:str = obj["BTAddress3"]
      self.BTCity:str = obj["BTCity"]
      self.BTState:str = obj["BTState"]
      self.BTZip:str = obj["BTZip"]
      self.BTCountryNum:int = obj["BTCountryNum"]
      """  Country part of Bill-to address. This field is in sync with the Country field. Must be a valid entry in the Country table.  """  
      self.BTCountry:str = obj["BTCountry"]
      """  Country is used as part of the bill-to address. It can be left blank.  """  
      self.BTPhoneNum:str = obj["BTPhoneNum"]
      """  The bill-to address Phone Number for the customer.  """  
      self.BTFaxNum:str = obj["BTFaxNum"]
      """  The bill-to address Fax telephone number for the customer. Optional field.  """  
      self.BTFormatStr:str = obj["BTFormatStr"]
      """  Optional bill-to address format.  Controls the address format used on crystal forms.  """  
      self.ParentCustNum:int = obj["ParentCustNum"]
      """  The unique Customer Number of the Parent.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.ICCust:bool = obj["ICCust"]
      """  This is an inter-company customer.  """  
      self.ContBillDay:int = obj["ContBillDay"]
      """  The day of the month that service contracts that are marked for recurring invoices are billed for this customer.  If the Invoice group invoice date is greater than or equal to this date then the invoice will be generated.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the customer.  """  
      self.ShippingQualifier:str = obj["ShippingQualifier"]
      """  Indicates if the customer has any qualifications on completeness of the order before it can be shipped. The valid values are; "O" - Order must be 100% complete,  "L" - Order Line must be 100% complete, "blank" - None.  This setting is a default for orders of a specific customer. See OrderHed.ShipOrderComplete, OrderDtl.ShipLineComplete  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  Code used to relate a AllocPri record to the customer.  This is used as a default to OrderHed.AllocPriCode for order for this customer.  """  
      self.LinkPortNum:int = obj["LinkPortNum"]
      """  Used with Global alerts  """  
      self.WebCustomer:bool = obj["WebCustomer"]
      """  Indicates if this customer is for eCommerce.  Only Customers with this equal to YES will be synchronized between the Manufacturing System DB and StoreFront DB (VntgSF).  """  
      self.CustomerType:str = obj["CustomerType"]
      """   Describe the type of Customer this is.
SUS = Suspect
PRO =  Prospect
CUS = Customer  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is not included in marketing lists  """  
      self.TerritoryLock:bool = obj["TerritoryLock"]
      """  This customers territory cannot be changed by any process that changes territories  """  
      self.CustURL:str = obj["CustURL"]
      """  Customers Website URL .  """  
      self.PendingTerritoryID:str = obj["PendingTerritoryID"]
      """  The sales territory that the system will assign based on new values in the Sales territory boundary table.  """  
      self.ExtID:str = obj["ExtID"]
      self.ConsolidateSO:bool = obj["ConsolidateSO"]
      """  APK - added for consolidation accross multiple SO's for the same customer  """  
      self.BillFrequency:str = obj["BillFrequency"]
      """  BillFrequency  """  
      self.CreditIncludePI:bool = obj["CreditIncludePI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCust:bool = obj["GlobalCust"]
      """  Marks the customer as a global customer, available to be sent out to other companies  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this customer participates in the Inter-Company Trading.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  """  
      self.GlobalCredIncOrd:bool = obj["GlobalCredIncOrd"]
      """  Indicates that Open Orders are to be included in the global credit limit checking. This checkbox will also include open service contracts.  """  
      self.GlobalCredIncPI:bool = obj["GlobalCredIncPI"]
      """  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  """  
      self.GlobalCurrencyCode:str = obj["GlobalCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.GlobalCreditHold:str = obj["GlobalCreditHold"]
      """  Indicates if customer has been placed into a "Global Credit Hold" status. Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldCustNum:int = obj["OldCustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.OldCustID:str = obj["OldCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This is the unique key in the original owner company - NOT CURRENTLY IN USE  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this customer.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required for the customer.  This field is available only when send shipments for financial integration is turned on.  This will provide the default for the ShipHead record.  """  
      self.ExternalID:str = obj["ExternalID"]
      self.CheckDuplicatePO:bool = obj["CheckDuplicatePO"]
      self.CreditLimit:int = obj["CreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.CustPILimit:int = obj["CustPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalCreditLimit:int = obj["GlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalPILimit:int = obj["GlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.DocGlobalCreditLimit:int = obj["DocGlobalCreditLimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  """  
      self.DocGlobalPILimit:int = obj["DocGlobalPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  """  
      self.RfqAttachAllow:bool = obj["RfqAttachAllow"]
      """  Indicates whether RFQ Attachments are allowed for this Customer  """  
      self.DiscountQualifier:str = obj["DiscountQualifier"]
      """   The discount qualifier is primarily used when applying order value based discounts to the customer's sales orders.  The value of this field affects the discount percent given to the customer.  Here's the rule:
"MIN" = means that the default order discount percent is the minimum discount the customer could get as compared to the order value based discount.
"MAX" = means that the default order discount percent is the maximum discount the customer could get as compared to the order value based discount.
"ADD" = means that the customer could get the order value based discount in addition to the default order discount.  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global customers.  The user can come back at a later time and choose to link a skipped customer if they need to.  """  
      self.AllowAltBillTo:bool = obj["AllowAltBillTo"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DemandAddAction:str = obj["DemandAddAction"]
      self.DemandAddLeadTime:int = obj["DemandAddLeadTime"]
      self.DemandAutoAccept:bool = obj["DemandAutoAccept"]
      self.DemandCancelAction:str = obj["DemandCancelAction"]
      self.DemandCancelLeadTime:int = obj["DemandCancelLeadTime"]
      self.DemandChangeAction:str = obj["DemandChangeAction"]
      self.DemandChangeDateAction:str = obj["DemandChangeDateAction"]
      self.DemandChangeDateLeadTime:int = obj["DemandChangeDateLeadTime"]
      self.DemandChangeLeadTime:int = obj["DemandChangeLeadTime"]
      self.DemandDateType:str = obj["DemandDateType"]
      self.DemandDayOfWeek:int = obj["DemandDayOfWeek"]
      self.DemandDeliveryDays:int = obj["DemandDeliveryDays"]
      self.DemandNewLineAction:str = obj["DemandNewLineAction"]
      self.DemandNewLineLeadTime:int = obj["DemandNewLineLeadTime"]
      self.DemandQtyChangeAction:str = obj["DemandQtyChangeAction"]
      self.DemandQtyChangeLeadTime:int = obj["DemandQtyChangeLeadTime"]
      self.DemandUseSysDate:bool = obj["DemandUseSysDate"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.TradingPartnerName:str = obj["TradingPartnerName"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.PeriodicityCode:int = obj["PeriodicityCode"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.CreditDays:int = obj["CreditDays"]
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      self.LateBuffer:int = obj["LateBuffer"]
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.DemandUnitPriceDiff:bool = obj["DemandUnitPriceDiff"]
      self.DemandUnitPriceDiffAction:str = obj["DemandUnitPriceDiffAction"]
      self.AddressVal:bool = obj["AddressVal"]
      self.ExcFromVal:bool = obj["ExcFromVal"]
      self.RebateForm:str = obj["RebateForm"]
      self.RebateVendorNum:int = obj["RebateVendorNum"]
      self.CreditCardOrder:bool = obj["CreditCardOrder"]
      self.DemandCheckForPart:bool = obj["DemandCheckForPart"]
      self.DemandCheckForPartAction:str = obj["DemandCheckForPartAction"]
      self.ChangeDate:str = obj["ChangeDate"]
      self.ChangedBy:str = obj["ChangedBy"]
      self.ChangeTime:int = obj["ChangeTime"]
      self.ChargeCode:str = obj["ChargeCode"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.ETCAddrChg:bool = obj["ETCAddrChg"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFAddress3:str = obj["FFAddress3"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFCountryNum:int = obj["FFCountryNum"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVEmailType:str = obj["UPSQVEmailType"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.ARCreditTotal:int = obj["ARCreditTotal"]
      self.PICreditTotal:int = obj["PICreditTotal"]
      self.SOCreditTotal:int = obj["SOCreditTotal"]
      self.TaxMethod:str = obj["TaxMethod"]
      self.TaxRoundRule:int = obj["TaxRoundRule"]
      self.AcrossNatAcc:bool = obj["AcrossNatAcc"]
      self.NACreditIsShare:bool = obj["NACreditIsShare"]
      self.NACreditPreferenceList:str = obj["NACreditPreferenceList"]
      self.NACreditSharedPrc:int = obj["NACreditSharedPrc"]
      self.NAParentCreditIsUsed:bool = obj["NAParentCreditIsUsed"]
      self.NAParentCreditPrc:int = obj["NAParentCreditPrc"]
      self.OverrideRlsClass:bool = obj["OverrideRlsClass"]
      self.ValidPayer:bool = obj["ValidPayer"]
      self.ValidShipTo:bool = obj["ValidShipTo"]
      self.ValidSoldTo:bool = obj["ValidSoldTo"]
      self.AllowOTS:bool = obj["AllowOTS"]
      self.ManagedVendID:str = obj["ManagedVendID"]
      self.ManagedVendNum:int = obj["ManagedVendNum"]
      self.ThirdPLCust:bool = obj["ThirdPLCust"]
      self.NARlsClassCode:str = obj["NARlsClassCode"]
      self.AutoGenPromNotes:bool = obj["AutoGenPromNotes"]
      self.DirectDebiting:bool = obj["DirectDebiting"]
      self.PartPayment:bool = obj["PartPayment"]
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      self.NAParentsCreditUsed:int = obj["NAParentsCreditUsed"]
      self.NASharedCreditUsed:int = obj["NASharedCreditUsed"]
      self.NAOwnCreditUsed:int = obj["NAOwnCreditUsed"]
      self.GlbNACreditIsShare:bool = obj["GlbNACreditIsShare"]
      self.GlbNACreditSharedPrc:int = obj["GlbNACreditSharedPrc"]
      self.GlbNAParentCreditIsUsed:bool = obj["GlbNAParentCreditIsUsed"]
      self.GlbNAParentCreditPrc:int = obj["GlbNAParentCreditPrc"]
      self.GlbNAParentsCreditUsed:int = obj["GlbNAParentsCreditUsed"]
      self.GlbNASharedCreditUsed:int = obj["GlbNASharedCreditUsed"]
      self.ReminderCode:str = obj["ReminderCode"]
      self.AllowShipTo3:bool = obj["AllowShipTo3"]
      self.NACreditUpdate:str = obj["NACreditUpdate"]
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      self.CustPartOpts:str = obj["CustPartOpts"]
      self.HasBank:bool = obj["HasBank"]
      self.PMUID:int = obj["PMUID"]
      self.DemandCheckForRev:bool = obj["DemandCheckForRev"]
      self.DemandCheckForRevAction:str = obj["DemandCheckForRevAction"]
      self.OrderHoldForReview:bool = obj["OrderHoldForReview"]
      self.ShipToTerrList:str = obj["ShipToTerrList"]
      self.AcctRefNumber:str = obj["AcctRefNumber"]
      self.DemandCheckCUMM:bool = obj["DemandCheckCUMM"]
      self.DemandCheckCUMMAction:str = obj["DemandCheckCUMMAction"]
      self.DemandCloseNoMatch:bool = obj["DemandCloseNoMatch"]
      self.DemandCloseRejSkd:bool = obj["DemandCloseRejSkd"]
      self.DemandPricing:str = obj["DemandPricing"]
      self.DmdCheckPartialShip:bool = obj["DmdCheckPartialShip"]
      self.DmdCheckShipAction:str = obj["DmdCheckShipAction"]
      self.InvPerPackLine:bool = obj["InvPerPackLine"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.OurBankCode:str = obj["OurBankCode"]
      self.PriceTolerance:int = obj["PriceTolerance"]
      """  Defines the tolerance for price difference validations  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.CheckConfirmCapPromise:bool = obj["CheckConfirmCapPromise"]
      self.CheckDateCapPromise:bool = obj["CheckDateCapPromise"]
      self.CheckUpdateCapPromise:bool = obj["CheckUpdateCapPromise"]
      self.DemandCapPromiseAction:str = obj["DemandCapPromiseAction"]
      self.DemandCapPromiseDate:str = obj["DemandCapPromiseDate"]
      self.DemandCapPromiseUpdate:str = obj["DemandCapPromiseUpdate"]
      self.DemandSplitSched:bool = obj["DemandSplitSched"]
      self.DueDateCriteria:str = obj["DueDateCriteria"]
      self.ERSOrder:bool = obj["ERSOrder"]
      self.PBTerms:int = obj["PBTerms"]
      self.PeriodicBilling:bool = obj["PeriodicBilling"]
      self.PreferredBank:str = obj["PreferredBank"]
      self.SICCode:int = obj["SICCode"]
      self.ICCode:str = obj["ICCode"]
      self.OTSmartString:bool = obj["OTSmartString"]
      self.DeferredRev:bool = obj["DeferredRev"]
      self.RACode:str = obj["RACode"]
      self.DemandCheckCfgAction:str = obj["DemandCheckCfgAction"]
      self.DemandCheckConfig:bool = obj["DemandCheckConfig"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.CustPricingSchema:str = obj["CustPricingSchema"]
      """  CustPricingSchema  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGBillToProvinceCode:str = obj["AGBillToProvinceCode"]
      """  AGBillToProvinceCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocTypeCode:str = obj["AGIDDocTypeCode"]
      """  AGIDDocTypeCode  """  
      self.AGIDDocumentNumber:str = obj["AGIDDocumentNumber"]
      """  AGIDDocumentNumber  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.Collections:bool = obj["Collections"]
      """  Collections  """  
      self.CollectionsDate:str = obj["CollectionsDate"]
      """  CollectionsDate  """  
      self.DateCollectionPosted:str = obj["DateCollectionPosted"]
      """  DateCollectionPosted  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  MXMunicipio  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PEIdentityDocType  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PEDocumentID  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  PEGoodsContributor  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  PEWithholdAgent  """  
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  PECollectionAgent  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  PENotFound  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  PENoAddress  """  
      self.EntityUseCode:str = obj["EntityUseCode"]
      """  EntityUseCode  """  
      self.InvcOrderCmpDflt:bool = obj["InvcOrderCmpDflt"]
      """  InvcOrderCmpDflt  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.RegistrationCode:str = obj["RegistrationCode"]
      """  RegistrationCode  """  
      self.EAddress:str = obj["EAddress"]
      """  EAddress  """  
      self.DemandCheckForRunOutPart:bool = obj["DemandCheckForRunOutPart"]
      """  DemandCheckForRunOutPart  """  
      self.DemandCheckForRunOutPartAction:str = obj["DemandCheckForRunOutPartAction"]
      """  DemandCheckForRunOutPartAction  """  
      self.EInvCompanyIDAttr:str = obj["EInvCompanyIDAttr"]
      """  EInvCompanyIDAttr  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.COIsOneTimeCust:bool = obj["COIsOneTimeCust"]
      """  COIsOneTimeCust  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PEGuaranteeName:str = obj["PEGuaranteeName"]
      """  PEGuaranteeName  """  
      self.PEGuaranteeAddress1:str = obj["PEGuaranteeAddress1"]
      """  PEGuaranteeAddress1  """  
      self.PEGuaranteeAddress2:str = obj["PEGuaranteeAddress2"]
      """  PEGuaranteeAddress2  """  
      self.PEGuaranteeAddress3:str = obj["PEGuaranteeAddress3"]
      """  PEGuaranteeAddress3  """  
      self.PEGuaranteeCity:str = obj["PEGuaranteeCity"]
      """  PEGuaranteeCity  """  
      self.PEGuaranteeState:str = obj["PEGuaranteeState"]
      """  PEGuaranteeState  """  
      self.PEGuaranteeZip:str = obj["PEGuaranteeZip"]
      """  PEGuaranteeZip  """  
      self.PEGuaranteeCountry:str = obj["PEGuaranteeCountry"]
      """  PEGuaranteeCountry  """  
      self.PEGuaranteePhoneNum:str = obj["PEGuaranteePhoneNum"]
      """  PEGuaranteePhoneNum  """  
      self.PEGuaranteeTaxID:str = obj["PEGuaranteeTaxID"]
      """  PEGuaranteeTaxID  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  OurSupplierCode  """  
      self.ECCType:str = obj["ECCType"]
      """  ECCType  """  
      self.MYIndustryCode:str = obj["MYIndustryCode"]
      """  MYIndustryCode  """  
      self.SyncToExternalCRM:bool = obj["SyncToExternalCRM"]
      """  SyncToExternalCRM  """  
      self.ExternalCRMGlbCustomerID:str = obj["ExternalCRMGlbCustomerID"]
      """  ExternalCRMGlbCustomerID  """  
      self.ExternalCRMGlbCustomerType:str = obj["ExternalCRMGlbCustomerType"]
      """  ExternalCRMGlbCustomerType  """  
      self.ExternalCRMLastSync:str = obj["ExternalCRMLastSync"]
      """  ExternalCRMLastSync  """  
      self.ExternalCRMSyncRequired:bool = obj["ExternalCRMSyncRequired"]
      """  ExternalCRMSyncRequired  """  
      self.Ownership:str = obj["Ownership"]
      """  Ownership  """  
      self.Industry:str = obj["Industry"]
      """  Industry  """  
      self.AnnualRevenue:int = obj["AnnualRevenue"]
      """  AnnualRevenue  """  
      self.NumberOfEmployees:int = obj["NumberOfEmployees"]
      """  NumberOfEmployees  """  
      self.TickerLocation:str = obj["TickerLocation"]
      """  TickerLocation  """  
      self.TickerSymbol:str = obj["TickerSymbol"]
      """  TickerSymbol  """  
      self.Rating:str = obj["Rating"]
      """  Rating  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TWGUIRegNum  """  
      self.MXAccountNumber:str = obj["MXAccountNumber"]
      """  MXAccountNumber  """  
      self.ConsolidateLinesPerPart:bool = obj["ConsolidateLinesPerPart"]
      """  ConsolidateLinesPerPart  """  
      self.TWTaxPayerType:int = obj["TWTaxPayerType"]
      """  TWTaxPayerType  """  
      self.TWDeductGUIFormatCode:str = obj["TWDeductGUIFormatCode"]
      """  TWDeductGUIFormatCode  """  
      self.MXCURP:str = obj["MXCURP"]
      """  MXCURP  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PEPerceptionRegime:str = obj["PEPerceptionRegime"]
      """  PEPerceptionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  INGSTComplianceRate  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXPurchaseType:str = obj["MXPurchaseType"]
      """  MXPurchaseType  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  SendToFSA  """  
      self.MXGeneralPublic:bool = obj["MXGeneralPublic"]
      """  MXGeneralPublic  """  
      self.AgingCreditHold:bool = obj["AgingCreditHold"]
      """  AgingCreditHold  """  
      self.AgingCreditHoldDate:str = obj["AgingCreditHoldDate"]
      """  AgingCreditHoldDate  """  
      self.AgingCreditHoldSource:str = obj["AgingCreditHoldSource"]
      """  AgingCreditHoldSource  """  
      self.AgingCreditClearUserID:str = obj["AgingCreditClearUserID"]
      """  AgingCreditClearUserID  """  
      self.AgingCreditClearDate:str = obj["AgingCreditClearDate"]
      """  AgingCreditClearDate  """  
      self.AgingCreditCode:str = obj["AgingCreditCode"]
      """  AgingCreditCode  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  ImporterOfRecord  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.EInvEndpointIDAttr:str = obj["EInvEndpointIDAttr"]
      """  EInvEndpointIDAttr  """  
      self.UseBlindShipping:bool = obj["UseBlindShipping"]
      """  Indicates whether sales orders from this sold to customer should be treated as Blind Shipments by Manifest.  """  
      self.ELIEinvoice:bool = obj["ELIEinvoice"]
      """  ELIEinvoice  """  
      self.ELIDefReportID:str = obj["ELIDefReportID"]
      """  ELIDefReportID  """  
      self.ELIDefStyleNum:int = obj["ELIDefStyleNum"]
      """  ELIDefStyleNum  """  
      self.ELIDefToMail:str = obj["ELIDefToMail"]
      """  ELIDefToMail  """  
      self.ELIDefCCMail:str = obj["ELIDefCCMail"]
      """  ELIDefCCMail  """  
      self.ELIDefMailTempID:str = obj["ELIDefMailTempID"]
      """  ELIDefMailTempID  """  
      self.ELISendMail:bool = obj["ELISendMail"]
      """  ELISendMail  """  
      self.COFiscalResp1:str = obj["COFiscalResp1"]
      """  COFiscalResp1  """  
      self.COFiscalResp2:str = obj["COFiscalResp2"]
      """  COFiscalResp2  """  
      self.COFiscalResp3:str = obj["COFiscalResp3"]
      """  COFiscalResp3  """  
      self.COOperType:str = obj["COOperType"]
      """  COOperType  """  
      self.CentralCollection:bool = obj["CentralCollection"]
      """  Central Collection  """  
      self.NettingVendorNum:int = obj["NettingVendorNum"]
      """  NettingVendorNum  """  
      self.EORINumber:str = obj["EORINumber"]
      """  EORINumber  """  
      self.AGIsElectronicCreditInvEligible:bool = obj["AGIsElectronicCreditInvEligible"]
      """  AGIsElectronicCreditInvEligible  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  TaxValidationStatus  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  TaxValidationDate  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.ELIOperatorCode:str = obj["ELIOperatorCode"]
      """  ELIOperatorCode  """  
      self.ELISendingOption:int = obj["ELISendingOption"]
      """  ELISendingOption  """  
      self.ELIOperatorID:str = obj["ELIOperatorID"]
      """  ELIOperatorID  """  
      self.EInvExternalID:str = obj["EInvExternalID"]
      """  EInvExternalID  """  
      self.MXTaxRegime:str = obj["MXTaxRegime"]
      """  MXTaxRegime  """  
      self.ExclusionMonth:int = obj["ExclusionMonth"]
      """  ExclusionMonth  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMRegionCode:str = obj["FSMRegionCode"]
      """  FSMRegionCode  """  
      self.FSMArea:str = obj["FSMArea"]
      """  FSMArea  """  
      self.ELIRcptDefStyleNum:int = obj["ELIRcptDefStyleNum"]
      """  ELIRcptDefStyleNum  """  
      self.CovenantDiscPercent:int = obj["CovenantDiscPercent"]
      """  CovenantDiscPercent  """  
      self.DisplayCustomerType:str = obj["DisplayCustomerType"]
      self.LinkCustID:str = obj["LinkCustID"]
      """  Customer.CustID to link to (new or existing)  """  
      self.DisplayHold:str = obj["DisplayHold"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbCustomerSearchTableset:
   def __init__(self, obj):
      self.GlbCustomer:list[Erp_Tablesets_GlbCustomerRow] = obj["GlbCustomer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbCustomerSearchTableset:
   def __init__(self, obj):
      self.GlbCustomer:list[Erp_Tablesets_GlbCustomerRow] = obj["GlbCustomer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   glbCustNum
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbCustNum:int = obj["glbCustNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbCustomerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbCustomer_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewGlbCustomer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbCustomer
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbCustomer:str = obj["whereClauseGlbCustomer"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGlbCustomerSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbCustomerSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbCustomerSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

