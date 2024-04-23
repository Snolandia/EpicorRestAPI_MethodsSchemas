import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COOneTimeSvc
# Description: One-Time Customer/Vendor Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COOneTimes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COOneTimes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COOneTimes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COOneTimeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/COOneTimes",headers=creds) as resp:
           return await resp.json()

async def post_COOneTimes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COOneTimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COOneTimeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COOneTimeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/COOneTimes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COOneTimes_Company_COOneTimeID(Company, COOneTimeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COOneTime item
   Description: Calls GetByID to retrieve the COOneTime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COOneTime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COOneTimeID: Desc: COOneTimeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COOneTimeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/COOneTimes(" + Company + "," + COOneTimeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COOneTimes_Company_COOneTimeID(Company, COOneTimeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COOneTime for the service
   Description: Calls UpdateExt to update COOneTime. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COOneTime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COOneTimeID: Desc: COOneTimeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COOneTimeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/COOneTimes(" + Company + "," + COOneTimeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COOneTimes_Company_COOneTimeID(Company, COOneTimeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COOneTime item
   Description: Call UpdateExt to delete COOneTime item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COOneTime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COOneTimeID: Desc: COOneTimeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/COOneTimes(" + Company + "," + COOneTimeID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COOneTimeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOOneTime, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCOOneTime=" + whereClauseCOOneTime
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coOneTimeID, epicorHeaders = None):
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
   params += "coOneTimeID=" + coOneTimeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_checkIfOneTimeHasBeenAssigned(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method checkIfOneTimeHasBeenAssigned
   Description: Check If OneTime Has Been Assigned in TaxTran, FAAddition, GLJrnDtlMnl
   OperationID: checkIfOneTimeHasBeenAssigned
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkIfOneTimeHasBeenAssigned_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkIfOneTimeHasBeenAssigned_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateSegmentValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateSegmentValue
   Description: Validates user input and create segment value for selected COA and Segment
   OperationID: CreateSegmentValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateSegmentValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSegmentValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateCheckDigit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateCheckDigit
   Description: Generating Checking Digit for Columbia
   OperationID: GenerateCheckDigit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateCheckDigit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateCheckDigit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOOneTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOOneTime
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOOneTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOOneTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOOneTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COOneTimeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COOneTimeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COOneTimeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COOneTimeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COOneTimeRow] = obj["value"]
      pass

class Erp_Tablesets_COOneTimeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CheckDigit:int = obj["CheckDigit"]
      """  CheckDigit  """  
      self.IdentificationType:str = obj["IdentificationType"]
      """  IdentificationType  """  
      self.FirstLastName:str = obj["FirstLastName"]
      """  FirstLastName  """  
      self.FirstName:str = obj["FirstName"]
      """  FirstName  """  
      self.SecondLastName:str = obj["SecondLastName"]
      """  SecondLastName  """  
      self.OtherNames:str = obj["OtherNames"]
      """  OtherNames  """  
      self.CompanyName:str = obj["CompanyName"]
      """  CompanyName  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.Phone:str = obj["Phone"]
      """  Phone  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.TownCode:str = obj["TownCode"]
      """  TownCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CIIUCode:str = obj["CIIUCode"]
      """  CIIUCode  """  
      self.CommonRegime:bool = obj["CommonRegime"]
      """  CommonRegime  """  
      self.ImportantTaxpayer:bool = obj["ImportantTaxpayer"]
      """  ImportantTaxpayer  """  
      self.SimplifiedRegime:bool = obj["SimplifiedRegime"]
      """  SimplifiedRegime  """  
      self.Nature:str = obj["Nature"]
      """  Nature  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  EmailAddress  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  CellPhoneNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COOneTimeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CheckDigit:int = obj["CheckDigit"]
      """  CheckDigit  """  
      self.IdentificationType:str = obj["IdentificationType"]
      """  IdentificationType  """  
      self.FirstLastName:str = obj["FirstLastName"]
      """  FirstLastName  """  
      self.FirstName:str = obj["FirstName"]
      """  FirstName  """  
      self.SecondLastName:str = obj["SecondLastName"]
      """  SecondLastName  """  
      self.OtherNames:str = obj["OtherNames"]
      """  OtherNames  """  
      self.CompanyName:str = obj["CompanyName"]
      """  CompanyName  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.Phone:str = obj["Phone"]
      """  Phone  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.TownCode:str = obj["TownCode"]
      """  TownCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CIIUCode:str = obj["CIIUCode"]
      """  CIIUCode  """  
      self.CommonRegime:bool = obj["CommonRegime"]
      """  CommonRegime  """  
      self.ImportantTaxpayer:bool = obj["ImportantTaxpayer"]
      """  ImportantTaxpayer  """  
      self.SimplifiedRegime:bool = obj["SimplifiedRegime"]
      """  SimplifiedRegime  """  
      self.Nature:str = obj["Nature"]
      """  Nature  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  EmailAddress  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  CellPhoneNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateSegmentValue_input:
   """ Required : 
   COACode
   segmentNbr
   segValue
   segName
   segDescr
   """  
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Selected COA  """  
      self.segmentNbr:int = obj["segmentNbr"]
      """  Selected segment  """  
      self.segValue:str = obj["segValue"]
      """  Segment value  """  
      self.segName:str = obj["segName"]
      """  Segment name  """  
      self.segDescr:str = obj["segDescr"]
      """  Segment description  """  
      pass

class CreateSegmentValue_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   coOneTimeID
   """  
   def __init__(self, obj):
      self.coOneTimeID:str = obj["coOneTimeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_COOneTimeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CheckDigit:int = obj["CheckDigit"]
      """  CheckDigit  """  
      self.IdentificationType:str = obj["IdentificationType"]
      """  IdentificationType  """  
      self.FirstLastName:str = obj["FirstLastName"]
      """  FirstLastName  """  
      self.FirstName:str = obj["FirstName"]
      """  FirstName  """  
      self.SecondLastName:str = obj["SecondLastName"]
      """  SecondLastName  """  
      self.OtherNames:str = obj["OtherNames"]
      """  OtherNames  """  
      self.CompanyName:str = obj["CompanyName"]
      """  CompanyName  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.Phone:str = obj["Phone"]
      """  Phone  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.TownCode:str = obj["TownCode"]
      """  TownCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CIIUCode:str = obj["CIIUCode"]
      """  CIIUCode  """  
      self.CommonRegime:bool = obj["CommonRegime"]
      """  CommonRegime  """  
      self.ImportantTaxpayer:bool = obj["ImportantTaxpayer"]
      """  ImportantTaxpayer  """  
      self.SimplifiedRegime:bool = obj["SimplifiedRegime"]
      """  SimplifiedRegime  """  
      self.Nature:str = obj["Nature"]
      """  Nature  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  EmailAddress  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  CellPhoneNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COOneTimeListTableset:
   def __init__(self, obj):
      self.COOneTimeList:list[Erp_Tablesets_COOneTimeListRow] = obj["COOneTimeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COOneTimeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.CheckDigit:int = obj["CheckDigit"]
      """  CheckDigit  """  
      self.IdentificationType:str = obj["IdentificationType"]
      """  IdentificationType  """  
      self.FirstLastName:str = obj["FirstLastName"]
      """  FirstLastName  """  
      self.FirstName:str = obj["FirstName"]
      """  FirstName  """  
      self.SecondLastName:str = obj["SecondLastName"]
      """  SecondLastName  """  
      self.OtherNames:str = obj["OtherNames"]
      """  OtherNames  """  
      self.CompanyName:str = obj["CompanyName"]
      """  CompanyName  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.Phone:str = obj["Phone"]
      """  Phone  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.TownCode:str = obj["TownCode"]
      """  TownCode  """  
      self.CountryCode:str = obj["CountryCode"]
      """  CountryCode  """  
      self.CIIUCode:str = obj["CIIUCode"]
      """  CIIUCode  """  
      self.CommonRegime:bool = obj["CommonRegime"]
      """  CommonRegime  """  
      self.ImportantTaxpayer:bool = obj["ImportantTaxpayer"]
      """  ImportantTaxpayer  """  
      self.SimplifiedRegime:bool = obj["SimplifiedRegime"]
      """  SimplifiedRegime  """  
      self.Nature:str = obj["Nature"]
      """  Nature  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  EmailAddress  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  CellPhoneNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COOneTimeTableset:
   def __init__(self, obj):
      self.COOneTime:list[Erp_Tablesets_COOneTimeRow] = obj["COOneTime"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCOOneTimeTableset:
   def __init__(self, obj):
      self.COOneTime:list[Erp_Tablesets_COOneTimeRow] = obj["COOneTime"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateCheckDigit_input:
   """ Required : 
   cOOneTimeID
   identificationType
   """  
   def __init__(self, obj):
      self.cOOneTimeID:str = obj["cOOneTimeID"]
      """  Columbia OneTimeID  """  
      self.identificationType:str = obj["identificationType"]
      """  Identification Type (in UI - Document type)  """  
      pass

class GenerateCheckDigit_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   coOneTimeID
   """  
   def __init__(self, obj):
      self.coOneTimeID:str = obj["coOneTimeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COOneTimeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COOneTimeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COOneTimeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COOneTimeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCOOneTime_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COOneTimeTableset] = obj["ds"]
      pass

class GetNewCOOneTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COOneTimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOOneTime
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOOneTime:str = obj["whereClauseCOOneTime"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COOneTimeTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCOOneTimeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOOneTimeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COOneTimeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COOneTimeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class checkIfOneTimeHasBeenAssigned_input:
   """ Required : 
   oneTimeID
   """  
   def __init__(self, obj):
      self.oneTimeID:str = obj["oneTimeID"]
      pass

class checkIfOneTimeHasBeenAssigned_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

