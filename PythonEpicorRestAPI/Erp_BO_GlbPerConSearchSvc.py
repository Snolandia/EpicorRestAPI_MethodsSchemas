import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GlbPerConSearchSvc
# Description: GlbPerCon search object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GlbPerConSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GlbPerConSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbPerConSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPerConRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches",headers=creds) as resp:
           return await resp.json()

async def post_GlbPerConSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbPerConSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbPerConRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GlbPerConRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GlbPerConSearches_Company_GlbCompany_GlbPerConID(Company, GlbCompany, GlbPerConID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GlbPerConSearch item
   Description: Calls GetByID to retrieve the GlbPerConSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbPerConSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbPerConID: Desc: GlbPerConID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GlbPerConRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches(" + Company + "," + GlbCompany + "," + GlbPerConID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GlbPerConSearches_Company_GlbCompany_GlbPerConID(Company, GlbCompany, GlbPerConID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GlbPerConSearch for the service
   Description: Calls UpdateExt to update GlbPerConSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbPerConSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbPerConID: Desc: GlbPerConID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbPerConRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches(" + Company + "," + GlbCompany + "," + GlbPerConID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GlbPerConSearches_Company_GlbCompany_GlbPerConID(Company, GlbCompany, GlbPerConID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GlbPerConSearch item
   Description: Call UpdateExt to delete GlbPerConSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbPerConSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param GlbPerConID: Desc: GlbPerConID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/GlbPerConSearches(" + Company + "," + GlbCompany + "," + GlbPerConID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbPerConListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGlbPerCon, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGlbPerCon=" + whereClauseGlbPerCon
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, glbPerConID, epicorHeaders = None):
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
   params += "glbPerConID=" + glbPerConID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGlbPerCon(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGlbPerCon
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbPerCon
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GlbPerConSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbPerConListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbPerConRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbPerConRow] = obj["value"]
      pass

class Erp_Tablesets_GlbPerConListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
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
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPerConID:int = obj["GlbPerConID"]
      """  The Owner's PerConID field identifies the PerCon and is used as the primary key.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPerConID:int = obj["OldPerConID"]
      """  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GlbName:str = obj["GlbName"]
      """  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.LinkPerConID:int = obj["LinkPerConID"]
      self.LinkName:str = obj["LinkName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPerConRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
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
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPerConID:int = obj["GlbPerConID"]
      """  The Owner's PerConID field identifies the PerCon and is used as the primary key.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPerConID:int = obj["OldPerConID"]
      """  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GlbName:str = obj["GlbName"]
      """  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.LinkName:str = obj["LinkName"]
      self.LinkPerConID:int = obj["LinkPerConID"]
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
   glbPerConID
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbPerConID:int = obj["glbPerConID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GlbPerConListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
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
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPerConID:int = obj["GlbPerConID"]
      """  The Owner's PerConID field identifies the PerCon and is used as the primary key.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPerConID:int = obj["OldPerConID"]
      """  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GlbName:str = obj["GlbName"]
      """  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.LinkPerConID:int = obj["LinkPerConID"]
      self.LinkName:str = obj["LinkName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPerConListTableset:
   def __init__(self, obj):
      self.GlbPerConList:list[Erp_Tablesets_GlbPerConListRow] = obj["GlbPerConList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbPerConRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.FirstName:str = obj["FirstName"]
      """  Contact's first name.  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Contact's middle name.  """  
      self.LastName:str = obj["LastName"]
      """  Contact's last name.  """  
      self.PRName:str = obj["PRName"]
      """  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contact's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contact's pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contact's home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contact's alternate phone number.  """  
      self.Prefix:str = obj["Prefix"]
      """  Contact's prefix.  """  
      self.Suffix:str = obj["Suffix"]
      """  Contact's suffix.  """  
      self.Initials:str = obj["Initials"]
      """  Contact's initials.  """  
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
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.CorpName:str = obj["CorpName"]
      """  The company name of the contact's mailing address. (See Address1 for additional information).  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  Contact's title.  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name of the person this contact reports to.  """  
      self.PRLastName:str = obj["PRLastName"]
      """  Contact's payroll last name.  """  
      self.PRFirstName:str = obj["PRFirstName"]
      """  Contact's payroll first name.  """  
      self.PRMiddleName:str = obj["PRMiddleName"]
      """  Contact's payroll middle name.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  The System User ID.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbPerConID:int = obj["GlbPerConID"]
      """  The Owner's PerConID field identifies the PerCon and is used as the primary key.  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldPerConID:int = obj["OldPerConID"]
      """  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  """  
      self.GlobalPerCon:bool = obj["GlobalPerCon"]
      """  Marks the PerCon as a global PerCon, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.GlbName:str = obj["GlbName"]
      """  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  """  
      self.HCMLinked:bool = obj["HCMLinked"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the PerCon is Global (master or linked)  """  
      self.LinkName:str = obj["LinkName"]
      self.LinkPerConID:int = obj["LinkPerConID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbPerConSearchTableset:
   def __init__(self, obj):
      self.GlbPerCon:list[Erp_Tablesets_GlbPerConRow] = obj["GlbPerCon"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGlbPerConSearchTableset:
   def __init__(self, obj):
      self.GlbPerCon:list[Erp_Tablesets_GlbPerConRow] = obj["GlbPerCon"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   glbPerConID
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.glbPerConID:int = obj["glbPerConID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbPerConListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGlbPerCon_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewGlbPerCon_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGlbPerCon
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGlbPerCon:str = obj["whereClauseGlbPerCon"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGlbPerConSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGlbPerConSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbPerConSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

