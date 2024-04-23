import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLJrnGrpSvc
# Description: Business Object for selected, updating, and posting a G/L Journal Group
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnGrps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnGrps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnGrps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnGrps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnGrps_Company_GroupID(Company, GroupID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnGrp item
   Description: Calls GetByID to retrieve the GLJrnGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnGrps_Company_GroupID(Company, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnGrp for the service
   Description: Calls UpdateExt to update GLJrnGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps(" + Company + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnGrps_Company_GroupID(Company, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnGrp item
   Description: Call UpdateExt to delete GLJrnGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnGrp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps(" + Company + "," + GroupID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLJrnGrp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLJrnGrp=" + whereClauseGLJrnGrp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, epicorHeaders = None):
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
   params += "groupID=" + groupID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBookID
   Description: Method to call when changing the Book.
   OperationID: ChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEntryMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEntryMode
   Description: Method to call when changing the Entry Mode.
   OperationID: ChangeEntryMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalPeriod
   Description: Method to call when changing the Fiscal Period.
   OperationID: ChangeFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalPeriodType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalPeriodType
   Description: Method to call when changing the Fiscal Period Type.
   OperationID: ChangeFiscalPeriodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalYear
   Description: Method to call when changing the Fiscal Year.
   OperationID: ChangeFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalYearSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalYearSuffix
   Description: Method to call when changing the Fiscal Year Suffix.
   OperationID: ChangeFiscalYearSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateType
   Description: Method to call when changing the Rate Type.
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJournalCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJournalCode
   Description: Method to call when changing the Journal Code.
   OperationID: ChangeJournalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFiscalYear
   Description: Method to call before updating the journal group. This method will check the
date that the user entered to verify it is in the current fiscal year and period.
If it is not then opMessage will be assigned with message text.  If it is
then the Fiscal Period and Year will be updated.
   OperationID: CheckFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateActiveUserID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateActiveUserID
   Description: Check current ActiveUserID and update it, if it is empty.
   OperationID: UpdateActiveUserID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateActiveUserID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateActiveUserID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDocumentIsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforePost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforePost
   OperationID: CheckBeforePost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsNeedAsyncronousPosting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsNeedAsyncronousPosting
   Description: This method returns true if it is better to use asyncronous posting because of performance.
   OperationID: IsNeedAsyncronousPosting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsNeedAsyncronousPosting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsNeedAsyncronousPosting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostGroupJournals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostGroupJournals
   Description: Method to call when posting journal for a specific group.  Posting of a group
causes the GlJrnGrp to be deleted from the database if all the records in the
group posted correctly.  It will also cause the GlJrnHed record to be deleted
after the specific journal is posted.
   OperationID: PostGroupJournals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostGroupJournals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostGroupJournals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlockGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockGroup
   Description: Method to call to unlock a group record.  This method should be called whenever
the group no longer needs to be locked.  The group no longer needs to be locked
when the journal object is closed, or when a different group is selected.
   OperationID: UnlockGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsNoLock
   Description: GetRows method with disabled ActiveUser functionality.
   OperationID: GetRowsNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnGrpNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnGrpNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsUseLockSetting(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsUseLockSetting
   Description: Returns the GLJrnGrp dataset using the automatic group lock configuration setting.
   OperationID: GetRowsUseLockSetting
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsUseLockSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUseLockSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateNoLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateNoLock
   Description: Update group without locking by ActiveUser
   OperationID: UpdateNoLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GroupUnlock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupUnlock
   Description: Clears the lock of a group, only if the user of the current session is the same as the one locking the group.
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupUnlock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupUnlock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupUnlock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GroupLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GroupLock
   Description: Locks the groupID for the current user in session only if the group is not locked already
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GroupLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnGrpRow] = obj["value"]
      pass

class Erp_Tablesets_GLJrnGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  """  
      self.JEDate:str = obj["JEDate"]
      """  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.FiscalPeriodType:str = obj["FiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if all records for this group were posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookIDDescription:str = obj["BookIDDescription"]
      """  Descripiton of Book  """  
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the book.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  """  
      self.JEDate:str = obj["JEDate"]
      """  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.FiscalPeriodType:str = obj["FiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if all records for this group were posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFiscalPeriod:str = obj["DspFiscalPeriod"]
      """  Periods List. The value will be populated in the BO logic containing Ordinary or Closing periods.  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BookModeDisabled:bool = obj["BookModeDisabled"]
      """  Indicates that Book Mode cannot be changed by user  """  
      self.DspFiscalPeriodType:str = obj["DspFiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods
S - Opening
Calculated based on the Book Selected.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      self.BookIDDescription:str = obj["BookIDDescription"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.JournalCodeAllowStatJournals:bool = obj["JournalCodeAllowStatJournals"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBookID_input:
   """ Required : 
   proposeBookID
   ds
   """  
   def __init__(self, obj):
      self.proposeBookID:str = obj["proposeBookID"]
      """  The proposed Book ID  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEntryMode_input:
   """ Required : 
   proposedBookMode
   ds
   """  
   def __init__(self, obj):
      self.proposedBookMode:str = obj["proposedBookMode"]
      """  The proposed Entry Mode  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeEntryMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalPeriodType_input:
   """ Required : 
   proposedPeriodType
   ds
   """  
   def __init__(self, obj):
      self.proposedPeriodType:str = obj["proposedPeriodType"]
      """  The proposed Fiscal Period Type  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeFiscalPeriodType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeFiscalPeriod_input:
   """ Required : 
   proposedFiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalPeriod:int = obj["proposedFiscalPeriod"]
      """  The proposed Fiscal Period  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalYearSuffix_input:
   """ Required : 
   proposedFiscalYearSuffix
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalYearSuffix:str = obj["proposedFiscalYearSuffix"]
      """  The proposed Fiscal Year Suffix  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeFiscalYearSuffix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalYear_input:
   """ Required : 
   proposedFiscalYear
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalYear:int = obj["proposedFiscalYear"]
      """  The proposed Fiscal Year  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJournalCode_input:
   """ Required : 
   proposedJournalCode
   ds
   """  
   def __init__(self, obj):
      self.proposedJournalCode:str = obj["proposedJournalCode"]
      """  The proposed Journal Code  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeJournalCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRateType_input:
   """ Required : 
   proposedRateType
   ds
   """  
   def __init__(self, obj):
      self.proposedRateType:str = obj["proposedRateType"]
      """  The proposed Rate Type  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class ChangeRateType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBeforePost_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  The group id of the group of journals to be posted  """  
      pass

class CheckBeforePost_output:
   def __init__(self, obj):
      pass

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  keyValue  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckFiscalYear_input:
   """ Required : 
   ds
   cGroupID
   cJEDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      self.cGroupID:str = obj["cGroupID"]
      """  Group Id field  """  
      self.cJEDate:str = obj["cJEDate"]
      """  JEDate proposed value  """  
      pass

class CheckFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLJrnGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  """  
      self.JEDate:str = obj["JEDate"]
      """  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.FiscalPeriodType:str = obj["FiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if all records for this group were posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFiscalPeriod:int = obj["DspFiscalPeriod"]
      """  Display Fiscal Period  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      """  Indicates the base currency for the book  """  
      self.BookIDDescription:str = obj["BookIDDescription"]
      """  Descripiton of Book  """  
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      """  Flag that indicates if correspondence accounting is set-up for the book.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      """  Journal  Description.  """  
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnGrpListTableset:
   def __init__(self, obj):
      self.GLJrnGrpList:list[Erp_Tablesets_GLJrnGrpListRow] = obj["GLJrnGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this batch.  """  
      self.ActiveUserID:str = obj["ActiveUserID"]
      """  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  """  
      self.PostErrorLog:str = obj["PostErrorLog"]
      """   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  """  
      self.JEDate:str = obj["JEDate"]
      """  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.FiscalPeriodType:str = obj["FiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  """  
      self.Posted:bool = obj["Posted"]
      """  It is true, if all records for this group were posted.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFiscalPeriod:str = obj["DspFiscalPeriod"]
      """  Periods List. The value will be populated in the BO logic containing Ordinary or Closing periods.  """  
      self.HasDetails:bool = obj["HasDetails"]
      """  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BookModeDisabled:bool = obj["BookModeDisabled"]
      """  Indicates that Book Mode cannot be changed by user  """  
      self.DspFiscalPeriodType:str = obj["DspFiscalPeriodType"]
      """   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods
S - Opening
Calculated based on the Book Selected.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BookIDCurrencyCode:str = obj["BookIDCurrencyCode"]
      self.BookIDDescription:str = obj["BookIDDescription"]
      self.BookIDCorrAccounting:bool = obj["BookIDCorrAccounting"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.JournalCodeAllowStatJournals:bool = obj["JournalCodeAllowStatJournals"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.RateGrpCodeDescription:str = obj["RateGrpCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnGrpTableset:
   def __init__(self, obj):
      self.GLJrnGrp:list[Erp_Tablesets_GLJrnGrpRow] = obj["GLJrnGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLJrnGrpTableset:
   def __init__(self, obj):
      self.GLJrnGrp:list[Erp_Tablesets_GLJrnGrpRow] = obj["GLJrnGrp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJrnGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLJrnGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLJrnGrpTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLJrnGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLJrnGrpNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class GetNewGLJrnGrpNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnGrp_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class GetNewGLJrnGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsNoLock_input:
   """ Required : 
   whereClauseGLJrnGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLJrnGrp:str = obj["whereClauseGLJrnGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsNoLock_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJrnGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsUseLockSetting_input:
   """ Required : 
   whereClauseGLJrnGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLJrnGrp:str = obj["whereClauseGLJrnGrp"]
      """  GLJrnGrp where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsUseLockSetting_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJrnGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLJrnGrp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLJrnGrp:str = obj["whereClauseGLJrnGrp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLJrnGrpTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GroupLock_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID to lock  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class GroupLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GroupUnlock_input:
   """ Required : 
   groupID
   ds
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID.  """  
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class GroupUnlock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
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

class IsNeedAsyncronousPosting_input:
   """ Required : 
   groupID
   maxCountOfLines
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  GroupID  """  
      self.maxCountOfLines:int = obj["maxCountOfLines"]
      """  recommended maximum count of lines  """  
      pass

class IsNeedAsyncronousPosting_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class PostGroupJournals_input:
   """ Required : 
   postGroupID
   """  
   def __init__(self, obj):
      self.postGroupID:str = obj["postGroupID"]
      """  The group id of the group of journals to be posted  """  
      pass

class PostGroupJournals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.NotAllPostedMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UnlockGroup_input:
   """ Required : 
   inGroupID
   """  
   def __init__(self, obj):
      self.inGroupID:str = obj["inGroupID"]
      """  The group id of the group record to unlock  """  
      pass

class UnlockGroup_output:
   def __init__(self, obj):
      pass

class UpdateActiveUserID_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      """  Group ID  """  
      pass

class UpdateActiveUserID_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLJrnGrpTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLJrnGrpTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateNoLock_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class UpdateNoLock_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLJrnGrpTableset] = obj["ds"]
      pass

      """  output parameters  """  

