import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VendCntSearchSvc
# Description: Vendor Contact Search Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VendCntSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendCntSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCntSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/VendCntSearches",headers=creds) as resp:
           return await resp.json()

async def post_VendCntSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCntSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/VendCntSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendCntSearches_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCntSearch item
   Description: Calls GetByID to retrieve the VendCntSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/VendCntSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendCntSearches_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendCntSearch for the service
   Description: Calls UpdateExt to update VendCntSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCntSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/VendCntSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendCntSearches_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendCntSearch item
   Description: Call UpdateExt to delete VendCntSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCntSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/VendCntSearches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVendCnt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseVendCnt=" + whereClauseVendCnt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, purPoint, conNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "conNum=" + conNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendCntSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendCntListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendCntRow] = obj["value"]
      pass

class Erp_Tablesets_VendCntListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      """  The name of the person contact.  """  
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
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      """  A description of the role.  """  
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
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      """  The name of the person contact.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
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
   conNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.conNum:int = obj["conNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtVendCntSearchTableset:
   def __init__(self, obj):
      self.VendCnt:list[Erp_Tablesets_VendCntRow] = obj["VendCnt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendCntListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      """  The name of the person contact.  """  
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
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      """  A description of the role.  """  
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
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntListTableset:
   def __init__(self, obj):
      self.VendCntList:list[Erp_Tablesets_VendCntListRow] = obj["VendCntList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      """  The name of the person contact.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntSearchTableset:
   def __init__(self, obj):
      self.VendCnt:list[Erp_Tablesets_VendCntRow] = obj["VendCnt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   vendorNum
   purPoint
   conNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.conNum:int = obj["conNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendCntSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendCntSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendCntSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendCntListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewVendCnt_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendCntSearchTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewVendCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendCntSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVendCnt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendCnt:str = obj["whereClauseVendCnt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendCntSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtVendCntSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendCntSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendCntSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendCntSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

