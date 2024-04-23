import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbVendorSearchSvc
# Description: Search object for Global Vendors
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbVendorSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbVendorSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbVendorSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches",headers=creds) as resp:
           return await resp.json()

async def post_GlbVendorSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbVendorSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbVendorSearches_Company_GlbCompany_GlbVendorNum(Company, GlbCompany, GlbVendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbVendorSearch item
   Description: Calls GetByID to retrieve the GlbVendorSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbVendorSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbVendorNum: Desc: GlbVendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches(" + Company + "," + GlbCompany + "," + GlbVendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbVendorSearches_Company_GlbCompany_GlbVendorNum(Company, GlbCompany, GlbVendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbVendorSearch for the service
   Description: Calls UpdateExt to update GlbVendorSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbVendorSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbVendorNum: Desc: GlbVendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbVendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches(" + Company + "," + GlbCompany + "," + GlbVendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbVendorSearches_Company_GlbCompany_GlbVendorNum(Company, GlbCompany, GlbVendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbVendorSearch item
   Description: Call UpdateExt to delete GlbVendorSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbVendorSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbVendorNum: Desc: GlbVendorNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/GlbVendorSearches(" + Company + "," + GlbCompany + "," + GlbVendorNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbVendorListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbVendor, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGlbVendor=" + whereClauseGlbVendor
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, glbVendorNum, epicorHeaders = None):
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
   params += "glbVendorNum=" + glbVendorNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_RefreshGlbVendorRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshGlbVendorRow
   Description: Refresh global vendor data
   OperationID: RefreshGlbVendorRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendorRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendorRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbVendor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbVendorSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbVendorListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbVendorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbVendorRow] = obj["value"]
      pass

class Erp_Tablesets_GlbVendorListRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.Box1099:int = obj["Box1099"]
      """  A user definable field which controls in which box on the 1099 that the amount should be printed.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CurrencyBaseCurrCode:str = obj["CurrencyBaseCurrCode"]
      """  A unique code that identifies the currency.  """  
      self.CalendarID:str = obj["CalendarID"]
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldVendorID:str = obj["OldVendorID"]
      """  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
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
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.CPay:bool = obj["CPay"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
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
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.ManagedCust:bool = obj["ManagedCust"]
      self.ManagedCustID:str = obj["ManagedCustID"]
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      self.PartPayment:bool = obj["PartPayment"]
      self.PMUID:int = obj["PMUID"]
      self.HasBank:bool = obj["HasBank"]
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.VendAccountType:str = obj["VendAccountType"]
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.TINType:str = obj["TINType"]
      """  TINType  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  SecondTINNotice  """  
      self.NameControl:str = obj["NameControl"]
      """  NameControl  """  
      self.DispVendorID:str = obj["DispVendorID"]
      self.LinkVendorID:str = obj["LinkVendorID"]
      """  The VendorId to link to (new or existing)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbVendorRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.Box1099:int = obj["Box1099"]
      """  A user definable field which controls in which box on the 1099 that the amount should be printed.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CurrencyBaseCurrCode:str = obj["CurrencyBaseCurrCode"]
      """  A unique code that identifies the currency.  """  
      self.CalendarID:str = obj["CalendarID"]
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldVendorID:str = obj["OldVendorID"]
      """  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
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
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.CPay:bool = obj["CPay"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
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
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.ManagedCust:bool = obj["ManagedCust"]
      self.ManagedCustID:str = obj["ManagedCustID"]
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      self.PartPayment:bool = obj["PartPayment"]
      self.PMUID:int = obj["PMUID"]
      self.HasBank:bool = obj["HasBank"]
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.VendAccountType:str = obj["VendAccountType"]
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocumentTypeCode:str = obj["AGIDDocumentTypeCode"]
      """  AGIDDocumentTypeCode  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.NoBankingReference:bool = obj["NoBankingReference"]
      """  NoBankingReference  """  
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
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PEIdentityDocType  """  
      self.COIsOneTimeVend:bool = obj["COIsOneTimeVend"]
      """  COIsOneTimeVend  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PEDocumentID  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  MaxLateDaysPORel  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.TINType:str = obj["TINType"]
      """  TINType  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  SecondTINNotice  """  
      self.NameControl:str = obj["NameControl"]
      """  NameControl  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.NonUS:bool = obj["NonUS"]
      """  NonUS  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.INSupplierType:str = obj["INSupplierType"]
      """  INSupplierType  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PaymentReporting:bool = obj["PaymentReporting"]
      """  PaymentReporting  """  
      self.ExternalPurchasing:bool = obj["ExternalPurchasing"]
      """  ExternalPurchasing  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.Reporting1099Name:str = obj["Reporting1099Name"]
      """  Reporting1099Name  """  
      self.Reporting1099Name2:str = obj["Reporting1099Name2"]
      """  Reporting1099Name2  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.AccountNum:str = obj["AccountNum"]
      """  AccountNum  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TWGUIRegNum  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PERetentionRegime:str = obj["PERetentionRegime"]
      """  PERetentionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  INGSTComplianceRate  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      """  TINValidationStatus  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  ImporterOfRecord  """  
      self.PLAutomaticAPInvoiceNum:bool = obj["PLAutomaticAPInvoiceNum"]
      """  PLAutomaticAPInvoiceNum  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  MXDIOTTranType  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  US1099KMerchCatCode  """  
      self.MXTaxpayerType:str = obj["MXTaxpayerType"]
      """  MXTaxpayerType  """  
      self.MXLegalRepRFC:str = obj["MXLegalRepRFC"]
      """  MXLegalRepRFC  """  
      self.MXLegalRepCURP:str = obj["MXLegalRepCURP"]
      """  MXLegalRepCURP  """  
      self.MXLegalRepName:str = obj["MXLegalRepName"]
      """  MXLegalRepName  """  
      self.MXLegalRepTaxpayerType:str = obj["MXLegalRepTaxpayerType"]
      """  MXLegalRepTaxpayerType  """  
      self.US1099State:str = obj["US1099State"]
      """  US1099State  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  TaxValidationStatus  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  TaxValidationDate  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EDISupplier:bool = obj["EDISupplier"]
      """  Flag used to mark a Supplier as EDI.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DispVendorID:str = obj["DispVendorID"]
      self.LinkVendorID:str = obj["LinkVendorID"]
      """  The VendorId to link to (new or existing)  """  
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
   glbVendorNum
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbVendorNum:int = obj["glbVendorNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbVendorListRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.Box1099:int = obj["Box1099"]
      """  A user definable field which controls in which box on the 1099 that the amount should be printed.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CurrencyBaseCurrCode:str = obj["CurrencyBaseCurrCode"]
      """  A unique code that identifies the currency.  """  
      self.CalendarID:str = obj["CalendarID"]
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldVendorID:str = obj["OldVendorID"]
      """  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
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
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.CPay:bool = obj["CPay"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
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
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.ManagedCust:bool = obj["ManagedCust"]
      self.ManagedCustID:str = obj["ManagedCustID"]
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      self.PartPayment:bool = obj["PartPayment"]
      self.PMUID:int = obj["PMUID"]
      self.HasBank:bool = obj["HasBank"]
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.VendAccountType:str = obj["VendAccountType"]
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.TINType:str = obj["TINType"]
      """  TINType  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  SecondTINNotice  """  
      self.NameControl:str = obj["NameControl"]
      """  NameControl  """  
      self.DispVendorID:str = obj["DispVendorID"]
      self.LinkVendorID:str = obj["LinkVendorID"]
      """  The VendorId to link to (new or existing)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbVendorListTableset:
   def __init__(self, obj):
      self.GlbVendorList:list[Erp_Tablesets_GlbVendorListRow] = obj["GlbVendorList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbVendorRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.Box1099:int = obj["Box1099"]
      """  A user definable field which controls in which box on the 1099 that the amount should be printed.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CurrencyBaseCurrCode:str = obj["CurrencyBaseCurrCode"]
      """  A unique code that identifies the currency.  """  
      self.CalendarID:str = obj["CalendarID"]
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldVendorID:str = obj["OldVendorID"]
      """  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
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
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.CPay:bool = obj["CPay"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
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
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.ManagedCust:bool = obj["ManagedCust"]
      self.ManagedCustID:str = obj["ManagedCustID"]
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      self.PartPayment:bool = obj["PartPayment"]
      self.PMUID:int = obj["PMUID"]
      self.HasBank:bool = obj["HasBank"]
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.VendAccountType:str = obj["VendAccountType"]
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocumentTypeCode:str = obj["AGIDDocumentTypeCode"]
      """  AGIDDocumentTypeCode  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.NoBankingReference:bool = obj["NoBankingReference"]
      """  NoBankingReference  """  
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
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PEIdentityDocType  """  
      self.COIsOneTimeVend:bool = obj["COIsOneTimeVend"]
      """  COIsOneTimeVend  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PEDocumentID  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  MaxLateDaysPORel  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.TINType:str = obj["TINType"]
      """  TINType  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  SecondTINNotice  """  
      self.NameControl:str = obj["NameControl"]
      """  NameControl  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.NonUS:bool = obj["NonUS"]
      """  NonUS  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.INSupplierType:str = obj["INSupplierType"]
      """  INSupplierType  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PaymentReporting:bool = obj["PaymentReporting"]
      """  PaymentReporting  """  
      self.ExternalPurchasing:bool = obj["ExternalPurchasing"]
      """  ExternalPurchasing  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.Reporting1099Name:str = obj["Reporting1099Name"]
      """  Reporting1099Name  """  
      self.Reporting1099Name2:str = obj["Reporting1099Name2"]
      """  Reporting1099Name2  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.AccountNum:str = obj["AccountNum"]
      """  AccountNum  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TWGUIRegNum  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PERetentionRegime:str = obj["PERetentionRegime"]
      """  PERetentionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  INGSTComplianceRate  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      """  TINValidationStatus  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  ImporterOfRecord  """  
      self.PLAutomaticAPInvoiceNum:bool = obj["PLAutomaticAPInvoiceNum"]
      """  PLAutomaticAPInvoiceNum  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  MXDIOTTranType  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  US1099KMerchCatCode  """  
      self.MXTaxpayerType:str = obj["MXTaxpayerType"]
      """  MXTaxpayerType  """  
      self.MXLegalRepRFC:str = obj["MXLegalRepRFC"]
      """  MXLegalRepRFC  """  
      self.MXLegalRepCURP:str = obj["MXLegalRepCURP"]
      """  MXLegalRepCURP  """  
      self.MXLegalRepName:str = obj["MXLegalRepName"]
      """  MXLegalRepName  """  
      self.MXLegalRepTaxpayerType:str = obj["MXLegalRepTaxpayerType"]
      """  MXLegalRepTaxpayerType  """  
      self.US1099State:str = obj["US1099State"]
      """  US1099State  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  TaxValidationStatus  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  TaxValidationDate  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EDISupplier:bool = obj["EDISupplier"]
      """  Flag used to mark a Supplier as EDI.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DispVendorID:str = obj["DispVendorID"]
      self.LinkVendorID:str = obj["LinkVendorID"]
      """  The VendorId to link to (new or existing)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbVendorSearchTableset:
   def __init__(self, obj):
      self.GlbVendor:list[Erp_Tablesets_GlbVendorRow] = obj["GlbVendor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbVendorSearchTableset:
   def __init__(self, obj):
      self.GlbVendor:list[Erp_Tablesets_GlbVendorRow] = obj["GlbVendor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   glbVendorNum
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbVendorNum:int = obj["glbVendorNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbVendorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbVendor_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewGlbVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbVendor
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbVendor:str = obj["whereClauseGlbVendor"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["returnObj"]
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

class RefreshGlbVendorRow_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global Vendor Number  """  
      self.ds:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["ds"]
      pass

class RefreshGlbVendorRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbVendorSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbVendorSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

