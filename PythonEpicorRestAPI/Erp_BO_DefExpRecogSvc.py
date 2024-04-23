import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DefExpRecogSvc
# Description: DefExpRecogSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DefExpRecogs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DefExpRecogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DefExpRecogs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DefExpRecogTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/DefExpRecogs",headers=creds) as resp:
           return await resp.json()

async def post_DefExpRecogs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DefExpRecogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DefExpRecogTaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DefExpRecogTaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/DefExpRecogs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DefExpRecogs_Company_TaskUID_TaskLine(Company, TaskUID, TaskLine, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DefExpRecog item
   Description: Calls GetByID to retrieve the DefExpRecog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DefExpRecog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskUID: Desc: TaskUID   Required: True   Allow empty value : True
      :param TaskLine: Desc: TaskLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DefExpRecogTaskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/DefExpRecogs(" + Company + "," + TaskUID + "," + TaskLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DefExpRecogs_Company_TaskUID_TaskLine(Company, TaskUID, TaskLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DefExpRecog for the service
   Description: Calls UpdateExt to update DefExpRecog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DefExpRecog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskUID: Desc: TaskUID   Required: True   Allow empty value : True
      :param TaskLine: Desc: TaskLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DefExpRecogTaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/DefExpRecogs(" + Company + "," + TaskUID + "," + TaskLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DefExpRecogs_Company_TaskUID_TaskLine(Company, TaskUID, TaskLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DefExpRecog item
   Description: Call UpdateExt to delete DefExpRecog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DefExpRecog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TaskUID: Desc: TaskUID   Required: True   Allow empty value : True
      :param TaskLine: Desc: TaskLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/DefExpRecogs(" + Company + "," + TaskUID + "," + TaskLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DefExpRecogTaskListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDefExpRecogTask, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseDefExpRecogTask=" + whereClauseDefExpRecogTask
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(taskUID, taskLine, epicorHeaders = None):
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
   params += "taskUID=" + taskUID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "taskLine=" + taskLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_SubmitSilentMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitSilentMode
   Description: Build Recognition Task in Silent Mode
   OperationID: SubmitSilentMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitSilentMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSilentMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildEditListTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildEditListTask
   Description: Build copy of Recognition Tasks batch for Edit List report
   OperationID: BuildEditListTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildEditListTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildEditListTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizations
   Description: Selects Amortization Lines to be processed
   OperationID: GetAmortizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizationsWithTotal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizationsWithTotal
   Description: Selects Amortization Lines to be processed
   OperationID: GetAmortizationsWithTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationsWithTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationsWithTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAmortizationTotal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAmortizationTotal
   Description: This method calculates the amortization total based on records in the GetAmortization tableset
   OperationID: GetAmortizationTotal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAmortizationTotal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAmortizationTotal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteTaskLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteTaskLines
   Description: Delete Task Lines by ID
   OperationID: DeleteTaskLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteTaskLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTaskLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumbers
   Description: Assign Legal Numbers to Amortization lines
   OperationID: AssignLegalNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumbers
   Description: Void Legal Numbers on Amortization lines
   OperationID: VoidLegalNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDefExpRecogTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDefExpRecogTask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDefExpRecogTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDefExpRecogTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDefExpRecogTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DefExpRecogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DefExpRecogTaskListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DefExpRecogTaskListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DefExpRecogTaskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DefExpRecogTaskRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_DefExpRecogTaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaskUID:str = obj["TaskUID"]
      """  TaskUID  """  
      self.TaskLine:int = obj["TaskLine"]
      """  TaskLine  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  RelatedToFile  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DefExpRecogTaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaskUID:str = obj["TaskUID"]
      """  TaskUID  """  
      self.TaskLine:int = obj["TaskLine"]
      """  TaskLine  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  RelatedToFile  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AmortAmt:int = obj["AmortAmt"]
      self.DocAmortAmount:int = obj["DocAmortAmount"]
      self.DocDate:str = obj["DocDate"]
      self.EntityName:str = obj["EntityName"]
      self.EntityNum:str = obj["EntityNum"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.LineNum:int = obj["LineNum"]
      self.Reference:str = obj["Reference"]
      self.AmortDate:str = obj["AmortDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumbers_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class AssignLegalNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class BuildEditListTask_input:
   """ Required : 
   ipVendList
   ipInvList
   ipGLJrnList
   ipAmortCodeList
   ipApplyDate
   ipScope
   ds
   """  
   def __init__(self, obj):
      self.ipVendList:str = obj["ipVendList"]
      """  Filter by Vendors  """  
      self.ipInvList:str = obj["ipInvList"]
      """  Filter by AP Invoice Numbers  """  
      self.ipGLJrnList:str = obj["ipGLJrnList"]
      """  Filter by GL Journal Numbers  """  
      self.ipAmortCodeList:str = obj["ipAmortCodeList"]
      """  Filter by Amortization Codes  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  As of Date  """  
      self.ipScope:str = obj["ipScope"]
      """  AP/GL/BO(both)  """  
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class BuildEditListTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opTaskGuid:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   taskUID
   taskLine
   """  
   def __init__(self, obj):
      self.taskUID:str = obj["taskUID"]
      self.taskLine:int = obj["taskLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteTaskLines_input:
   """ Required : 
   taskUID
   """  
   def __init__(self, obj):
      self.taskUID:str = obj["taskUID"]
      """  Task ID  """  
      pass

class DeleteTaskLines_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DefExpRecogListTableset:
   def __init__(self, obj):
      self.DefExpRecogTaskList:list[Erp_Tablesets_DefExpRecogTaskListRow] = obj["DefExpRecogTaskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DefExpRecogTableset:
   def __init__(self, obj):
      self.DefExpRecogTask:list[Erp_Tablesets_DefExpRecogTaskRow] = obj["DefExpRecogTask"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DefExpRecogTaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaskUID:str = obj["TaskUID"]
      """  TaskUID  """  
      self.TaskLine:int = obj["TaskLine"]
      """  TaskLine  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  RelatedToFile  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DefExpRecogTaskRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TaskUID:str = obj["TaskUID"]
      """  TaskUID  """  
      self.TaskLine:int = obj["TaskLine"]
      """  TaskLine  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  RelatedToFile  """  
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AmortAmt:int = obj["AmortAmt"]
      self.DocAmortAmount:int = obj["DocAmortAmount"]
      self.DocDate:str = obj["DocDate"]
      self.EntityName:str = obj["EntityName"]
      self.EntityNum:str = obj["EntityNum"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.LineNum:int = obj["LineNum"]
      self.Reference:str = obj["Reference"]
      self.AmortDate:str = obj["AmortDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDefExpRecogTableset:
   def __init__(self, obj):
      self.DefExpRecogTask:list[Erp_Tablesets_DefExpRecogTaskRow] = obj["DefExpRecogTask"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAmortizationTotal_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class GetAmortizationTotal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.amortizationTotal:int = obj["parameters"]
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAmortizationsWithTotal_input:
   """ Required : 
   ipGuid
   ipVendList
   ipInvList
   ipGLJrnList
   ipAmortCodeList
   ipApplyDate
   ipScope
   ds
   """  
   def __init__(self, obj):
      self.ipGuid:str = obj["ipGuid"]
      """  Task GUID  """  
      self.ipVendList:str = obj["ipVendList"]
      """  Filter by Vendors  """  
      self.ipInvList:str = obj["ipInvList"]
      """  Filter by AP Invoice Numbers  """  
      self.ipGLJrnList:str = obj["ipGLJrnList"]
      """  Filter by GL Journal Numbers  """  
      self.ipAmortCodeList:str = obj["ipAmortCodeList"]
      """  Filter by Amortization Codes  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  As of Date  """  
      self.ipScope:str = obj["ipScope"]
      """  AP/GL/BO(both)  """  
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class GetAmortizationsWithTotal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalAmortization:int = obj["parameters"]
      self.baseCurrencyCode:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAmortizations_input:
   """ Required : 
   ipGuid
   ipVendList
   ipInvList
   ipGLJrnList
   ipAmortCodeList
   ipApplyDate
   ipScope
   ds
   """  
   def __init__(self, obj):
      self.ipGuid:str = obj["ipGuid"]
      """  Task GUID  """  
      self.ipVendList:str = obj["ipVendList"]
      """  Filter by Vendors  """  
      self.ipInvList:str = obj["ipInvList"]
      """  Filter by AP Invoice Numbers  """  
      self.ipGLJrnList:str = obj["ipGLJrnList"]
      """  Filter by GL Journal Numbers  """  
      self.ipAmortCodeList:str = obj["ipAmortCodeList"]
      """  Filter by Amortization Codes  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  As of Date  """  
      self.ipScope:str = obj["ipScope"]
      """  AP/GL/BO(both)  """  
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class GetAmortizations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   taskUID
   taskLine
   """  
   def __init__(self, obj):
      self.taskUID:str = obj["taskUID"]
      self.taskLine:int = obj["taskLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DefExpRecogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DefExpRecogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DefExpRecogTableset] = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ds
   ipTranDocTypeID
   ipTranDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.ipTranDate:str = obj["ipTranDate"]
      """  Transaction Date  """  
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      self.opRequiresUserInput:bool = obj["opRequiresUserInput"]
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
      self.returnObj:list[Erp_Tablesets_DefExpRecogListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDefExpRecogTask_input:
   """ Required : 
   ds
   taskUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      self.taskUID:str = obj["taskUID"]
      pass

class GetNewDefExpRecogTask_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDefExpRecogTask
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDefExpRecogTask:str = obj["whereClauseDefExpRecogTask"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DefExpRecogTableset] = obj["returnObj"]
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

class SubmitSilentMode_input:
   """ Required : 
   ipGuid
   ipVendList
   ipInvList
   ipGLJrnList
   ipAmortCodeList
   ipApplyDate
   ipScope
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipGuid:str = obj["ipGuid"]
      """  Task GUID  """  
      self.ipVendList:str = obj["ipVendList"]
      """  Filter by Vendors  """  
      self.ipInvList:str = obj["ipInvList"]
      """  Filter by AP Invoice Numbers  """  
      self.ipGLJrnList:str = obj["ipGLJrnList"]
      """  Filter by GL Journal Numbers  """  
      self.ipAmortCodeList:str = obj["ipAmortCodeList"]
      """  Filter by Amortization Codes  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  As of Date  """  
      self.ipScope:str = obj["ipScope"]
      """  AP/GL/BO(both)  """  
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class SubmitSilentMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDefExpRecogTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDefExpRecogTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumbers_input:
   """ Required : 
   ipVoidingReason
   ds
   """  
   def __init__(self, obj):
      self.ipVoidingReason:str = obj["ipVoidingReason"]
      """  Voiding Reason  """  
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

class VoidLegalNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DefExpRecogTableset] = obj["ds"]
      pass

      """  output parameters  """  

