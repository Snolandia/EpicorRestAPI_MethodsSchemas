import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.CompanySvc
# Description: Company service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Companies(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Companies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Companies
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies",headers=creds) as resp:
           return await resp.json()

async def post_Companies(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Companies
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.CompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.CompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Companies_Company1(Company1, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Company item
   Description: Calls GetByID to retrieve the Company item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Company
      :param Company1: Desc: Company1   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.CompanyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies(" + Company1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Companies_Company1(Company1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Company for the service
   Description: Calls UpdateExt to update Company. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Company
      :param Company1: Desc: Company1   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.CompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies(" + Company1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Companies_Company1(Company1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Company item
   Description: Call UpdateExt to delete Company item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Company
      :param Company1: Desc: Company1   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/Companies(" + Company1 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CompanyListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCompany, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCompany=" + whereClauseCompany
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "company=" + company

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_VerifySSRSConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifySSRSConnection
   Description: Verify SQL connections for SSRS DB
   OperationID: VerifySSRSConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifySSRSConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifySSRSConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDBNameList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDBNameList
   Description: Gets a list of SSRS DB
   OperationID: GetDBNameList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDBNameList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDBNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSystemTimeZoneList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSystemTimeZoneList
   Description: This method returns a list of Microsoft Time Zone Index Values and their corresponding display name
   OperationID: GetSystemTimeZoneList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemTimeZoneList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetPackageProcessList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackageProcessList
   Description: Gets the package process list from Service Connect.
   OperationID: GetPackageProcessList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackageProcessList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageProcessList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateLogoImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateLogoImage
   Description: Updates the current company logo image (returned as Base-64 encoded string in LogoImageContent but not saved in database)
and deletes the file in the user import folder.
   OperationID: UpdateLogoImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateLogoImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLogoImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CompanySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_CompanyListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_CompanyRow] = obj["value"]
      pass

class Ice_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.Company1:str = obj["Company1"]
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State  """  
      self.Zip:str = obj["Zip"]
      """  Zip  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  PhoneNum  """  
      self.FaxNum:str = obj["FaxNum"]
      """  FaxNum  """  
      self.MfgSys:str = obj["MfgSys"]
      """  MfgSys  """  
      self.MetadataPath:str = obj["MetadataPath"]
      """  Defines the directory location used by this company to receive metadata.  """  
      self.WinWebURL:str = obj["WinWebURL"]
      """  Web Access URL for this company  """  
      self.TrackSysActivity:bool = obj["TrackSysActivity"]
      """  Track System Activity flag  """  
      self.TrackPersonalizationChg:bool = obj["TrackPersonalizationChg"]
      """  Track Personalization changes flag  """  
      self.ReportTypePref:str = obj["ReportTypePref"]
      """  Type of report  """  
      self.MobileURL:str = obj["MobileURL"]
      """  URL for Mobile client  """  
      self.MobileMetaPath:str = obj["MobileMetaPath"]
      """  Metadatapath for Mobile Client  """  
      self.WorkstationMethod:str = obj["WorkstationMethod"]
      """  Workstation Method  """  
      self.EntSearchURL:str = obj["EntSearchURL"]
      """  Enterprise Search URL  """  
      self.GlobalEntSearch:bool = obj["GlobalEntSearch"]
      """  GlobalEntSearch  """  
      self.SCServer:str = obj["SCServer"]
      """  SCServer  """  
      self.SCUserID:str = obj["SCUserID"]
      """  SCUserID  """  
      self.SCPassword:str = obj["SCPassword"]
      """  SCPassword  """  
      self.UBAQWFPackage:str = obj["UBAQWFPackage"]
      """  UBAQWFPackage  """  
      self.InstallationID:str = obj["InstallationID"]
      """  InstallationID  """  
      self.CountryGroupCode:str = obj["CountryGroupCode"]
      """  CountryGroupCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CountryCodeID:str = obj["CountryCodeID"]
      """  CountryCodeID  """  
      self.DefaultLabelsPrinter:str = obj["DefaultLabelsPrinter"]
      """  DefaultLabelsPrinter  """  
      self.DefaultReportsPrinter:str = obj["DefaultReportsPrinter"]
      """  DefaultReportsPrinter  """  
      self.HelpURI:str = obj["HelpURI"]
      """  HelpURI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SSRSBaseURL:str = obj["SSRSBaseURL"]
      """  SSRSBaseURL  """  
      self.SSRSDatabaseServerName:str = obj["SSRSDatabaseServerName"]
      """  SSRSDatabaseServerName  """  
      self.SSRSAuthenticationType:str = obj["SSRSAuthenticationType"]
      """  SSRSAuthenticationType  """  
      self.SSRSDatabaseUser:str = obj["SSRSDatabaseUser"]
      """  SSRSDatabaseUser  """  
      self.SSRSDatabaseUserPassword:str = obj["SSRSDatabaseUserPassword"]
      """  SSRSDatabaseUserPassword  """  
      self.SSRSDatabaseName:str = obj["SSRSDatabaseName"]
      """  SSRSDatabaseName  """  
      self.SSRSOverrideDefaults:bool = obj["SSRSOverrideDefaults"]
      """  SSRSOverrideDefaults  """  
      self.SSRSPrintOptions:str = obj["SSRSPrintOptions"]
      """  SSRSPrintOptions  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  TimeZoneID  """  
      self.DefaultLayoutID:str = obj["DefaultLayoutID"]
      """  DefaultLayoutID  """  
      self.ODBCUserID:str = obj["ODBCUserID"]
      """  ODBCUserID  """  
      self.ODBCPassword:str = obj["ODBCPassword"]
      """  ODBCPassword  """  
      self.EpicorEducationURL:str = obj["EpicorEducationURL"]
      """  EpicorEducationURL  """  
      self.EpicorHelpURL:str = obj["EpicorHelpURL"]
      """  EpicorHelpURL  """  
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.GridsUseBaseCurrencyInfo:bool = obj["GridsUseBaseCurrencyInfo"]
      """  GridsUseBaseCurrencyInfo  """  
      self.EDDURL:str = obj["EDDURL"]
      """  EDDURL  """  
      self.EdiProcessing:str = obj["EdiProcessing"]
      """  EdiProcessing  """  
      self.ReportLoggingLevel:str = obj["ReportLoggingLevel"]
      """  ReportLoggingLevel  """  
      self.ImportAPIMaxDOP:int = obj["ImportAPIMaxDOP"]
      """  ImportAPIMaxDOP  """  
      self.TelemetryOptIn:bool = obj["TelemetryOptIn"]
      """  TelemetryOptIn  """  
      self.TelemetryOptOutReason:str = obj["TelemetryOptOutReason"]
      """  TelemetryOptOutReason  """  
      self.ImportPurgeInterval:int = obj["ImportPurgeInterval"]
      """  ImportPurgeInterval  """  
      self.ImportMaxFileSize:int = obj["ImportMaxFileSize"]
      """  ImportMaxFileSize  """  
      self.TelemetryKey:str = obj["TelemetryKey"]
      """  TelemetryKey  """  
      self.DefaultHomepageLayoutID:str = obj["DefaultHomepageLayoutID"]
      """  DefaultHomepageLayoutID  """  
      self.IsLive:bool = obj["IsLive"]
      """  IsLive  """  
      self.KineticColor:str = obj["KineticColor"]
      """  KineticColor  """  
      self.DefaultPaperSize:str = obj["DefaultPaperSize"]
      """  DefaultPaperSize  """  
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  NomenclatureID  """  
      self.GlobalEducationURL:bool = obj["GlobalEducationURL"]
      self.GlobalHelpURL:bool = obj["GlobalHelpURL"]
      """  Indicates whether or not the education courses URL is global or just for this specific company.  """  
      self.ODBCPasswordMasked:str = obj["ODBCPasswordMasked"]
      self.AllowEdgeAgentUserInstall:bool = obj["AllowEdgeAgentUserInstall"]
      """  Indicates if the end user can download the Edge Agent installer via the Kinetic client.  """  
      self.LogoFileName:str = obj["LogoFileName"]
      """  The company logo file name, stored in a server shared folder.  """  
      self.LogoImageContent:str = obj["LogoImageContent"]
      """  The logo image content as Base-64 string.  """  
      self.KineticCssColor:str = obj["KineticCssColor"]
      """  Kinetic color - in CSS format, i.e: rgba(255, 255, 255, 0)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   company
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_CompanyTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_CompanyTableset] = obj["returnObj"]
      pass

class GetDBNameList_input:
   """ Required : 
   SQLAuthtype
   SQLServer
   DBUser
   DBPassword
   """  
   def __init__(self, obj):
      self.SQLAuthtype:str = obj["SQLAuthtype"]
      self.SQLServer:str = obj["SQLServer"]
      self.DBUser:str = obj["DBUser"]
      self.DBPassword:str = obj["DBPassword"]
      pass

class GetDBNameList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
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
      self.returnObj:list[Ice_Tablesets_CompanyListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_CompanyTableset] = obj["ds"]
      pass

class GetNewCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackageProcessList_input:
   """ Required : 
   server
   userName
   password
   """  
   def __init__(self, obj):
      self.server:str = obj["server"]
      """  the Epicor Service Connect server  """  
      self.userName:str = obj["userName"]
      """  the Epicor Service Connect username  """  
      self.password:str = obj["password"]
      """  the Epicor Service Connect password  """  
      pass

class GetPackageProcessList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_Company_Contracts_PackageInfo] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseCompany
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCompany:str = obj["whereClauseCompany"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CompanyTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSystemTimeZoneList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Ice_BO_Company_Contracts_PackageInfo:
   def __init__(self, obj):
      self.Name:str = obj["Name"]
      self.Processes:str = obj["Processes"]
      pass

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

class Ice_Tablesets_CompanyListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CompanyListTableset:
   def __init__(self, obj):
      self.CompanyList:list[Ice_Tablesets_CompanyListRow] = obj["CompanyList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_CompanyRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Name:str = obj["Name"]
      """  Company Name  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State  """  
      self.Zip:str = obj["Zip"]
      """  Zip  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  PhoneNum  """  
      self.FaxNum:str = obj["FaxNum"]
      """  FaxNum  """  
      self.MfgSys:str = obj["MfgSys"]
      """  MfgSys  """  
      self.MetadataPath:str = obj["MetadataPath"]
      """  Defines the directory location used by this company to receive metadata.  """  
      self.WinWebURL:str = obj["WinWebURL"]
      """  Web Access URL for this company  """  
      self.TrackSysActivity:bool = obj["TrackSysActivity"]
      """  Track System Activity flag  """  
      self.TrackPersonalizationChg:bool = obj["TrackPersonalizationChg"]
      """  Track Personalization changes flag  """  
      self.ReportTypePref:str = obj["ReportTypePref"]
      """  Type of report  """  
      self.MobileURL:str = obj["MobileURL"]
      """  URL for Mobile client  """  
      self.MobileMetaPath:str = obj["MobileMetaPath"]
      """  Metadatapath for Mobile Client  """  
      self.WorkstationMethod:str = obj["WorkstationMethod"]
      """  Workstation Method  """  
      self.EntSearchURL:str = obj["EntSearchURL"]
      """  Enterprise Search URL  """  
      self.GlobalEntSearch:bool = obj["GlobalEntSearch"]
      """  GlobalEntSearch  """  
      self.SCServer:str = obj["SCServer"]
      """  SCServer  """  
      self.SCUserID:str = obj["SCUserID"]
      """  SCUserID  """  
      self.SCPassword:str = obj["SCPassword"]
      """  SCPassword  """  
      self.UBAQWFPackage:str = obj["UBAQWFPackage"]
      """  UBAQWFPackage  """  
      self.InstallationID:str = obj["InstallationID"]
      """  InstallationID  """  
      self.CountryGroupCode:str = obj["CountryGroupCode"]
      """  CountryGroupCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CountryCodeID:str = obj["CountryCodeID"]
      """  CountryCodeID  """  
      self.DefaultLabelsPrinter:str = obj["DefaultLabelsPrinter"]
      """  DefaultLabelsPrinter  """  
      self.DefaultReportsPrinter:str = obj["DefaultReportsPrinter"]
      """  DefaultReportsPrinter  """  
      self.HelpURI:str = obj["HelpURI"]
      """  HelpURI  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SSRSBaseURL:str = obj["SSRSBaseURL"]
      """  SSRSBaseURL  """  
      self.SSRSDatabaseServerName:str = obj["SSRSDatabaseServerName"]
      """  SSRSDatabaseServerName  """  
      self.SSRSAuthenticationType:str = obj["SSRSAuthenticationType"]
      """  SSRSAuthenticationType  """  
      self.SSRSDatabaseUser:str = obj["SSRSDatabaseUser"]
      """  SSRSDatabaseUser  """  
      self.SSRSDatabaseUserPassword:str = obj["SSRSDatabaseUserPassword"]
      """  SSRSDatabaseUserPassword  """  
      self.SSRSDatabaseName:str = obj["SSRSDatabaseName"]
      """  SSRSDatabaseName  """  
      self.SSRSOverrideDefaults:bool = obj["SSRSOverrideDefaults"]
      """  SSRSOverrideDefaults  """  
      self.SSRSPrintOptions:str = obj["SSRSPrintOptions"]
      """  SSRSPrintOptions  """  
      self.TimeZoneID:str = obj["TimeZoneID"]
      """  TimeZoneID  """  
      self.DefaultLayoutID:str = obj["DefaultLayoutID"]
      """  DefaultLayoutID  """  
      self.ODBCUserID:str = obj["ODBCUserID"]
      """  ODBCUserID  """  
      self.ODBCPassword:str = obj["ODBCPassword"]
      """  ODBCPassword  """  
      self.EpicorEducationURL:str = obj["EpicorEducationURL"]
      """  EpicorEducationURL  """  
      self.EpicorHelpURL:str = obj["EpicorHelpURL"]
      """  EpicorHelpURL  """  
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.GridsUseBaseCurrencyInfo:bool = obj["GridsUseBaseCurrencyInfo"]
      """  GridsUseBaseCurrencyInfo  """  
      self.EDDURL:str = obj["EDDURL"]
      """  EDDURL  """  
      self.EdiProcessing:str = obj["EdiProcessing"]
      """  EdiProcessing  """  
      self.ReportLoggingLevel:str = obj["ReportLoggingLevel"]
      """  ReportLoggingLevel  """  
      self.ImportAPIMaxDOP:int = obj["ImportAPIMaxDOP"]
      """  ImportAPIMaxDOP  """  
      self.TelemetryOptIn:bool = obj["TelemetryOptIn"]
      """  TelemetryOptIn  """  
      self.TelemetryOptOutReason:str = obj["TelemetryOptOutReason"]
      """  TelemetryOptOutReason  """  
      self.ImportPurgeInterval:int = obj["ImportPurgeInterval"]
      """  ImportPurgeInterval  """  
      self.ImportMaxFileSize:int = obj["ImportMaxFileSize"]
      """  ImportMaxFileSize  """  
      self.TelemetryKey:str = obj["TelemetryKey"]
      """  TelemetryKey  """  
      self.DefaultHomepageLayoutID:str = obj["DefaultHomepageLayoutID"]
      """  DefaultHomepageLayoutID  """  
      self.IsLive:bool = obj["IsLive"]
      """  IsLive  """  
      self.KineticColor:str = obj["KineticColor"]
      """  KineticColor  """  
      self.DefaultPaperSize:str = obj["DefaultPaperSize"]
      """  DefaultPaperSize  """  
      self.NomenclatureID:str = obj["NomenclatureID"]
      """  NomenclatureID  """  
      self.GlobalEducationURL:bool = obj["GlobalEducationURL"]
      self.GlobalHelpURL:bool = obj["GlobalHelpURL"]
      """  Indicates whether or not the education courses URL is global or just for this specific company.  """  
      self.ODBCPasswordMasked:str = obj["ODBCPasswordMasked"]
      self.AllowEdgeAgentUserInstall:bool = obj["AllowEdgeAgentUserInstall"]
      """  Indicates if the end user can download the Edge Agent installer via the Kinetic client.  """  
      self.LogoFileName:str = obj["LogoFileName"]
      """  The company logo file name, stored in a server shared folder.  """  
      self.LogoImageContent:str = obj["LogoImageContent"]
      """  The logo image content as Base-64 string.  """  
      self.KineticCssColor:str = obj["KineticCssColor"]
      """  Kinetic color - in CSS format, i.e: rgba(255, 255, 255, 0)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CompanyTableset:
   def __init__(self, obj):
      self.Company:list[Ice_Tablesets_CompanyRow] = obj["Company"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtCompanyTableset:
   def __init__(self, obj):
      self.Company:list[Ice_Tablesets_CompanyRow] = obj["Company"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtCompanyTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtCompanyTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateLogoImage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_CompanyTableset] = obj["ds"]
      pass

class UpdateLogoImage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_CompanyTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_CompanyTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VerifySSRSConnection_input:
   """ Required : 
   SQLAuthtype
   SQLServer
   SQLDBName
   DBUser
   DBPassword
   """  
   def __init__(self, obj):
      self.SQLAuthtype:str = obj["SQLAuthtype"]
      self.SQLServer:str = obj["SQLServer"]
      self.SQLDBName:str = obj["SQLDBName"]
      self.DBUser:str = obj["DBUser"]
      self.DBPassword:str = obj["DBPassword"]
      pass

class VerifySSRSConnection_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

