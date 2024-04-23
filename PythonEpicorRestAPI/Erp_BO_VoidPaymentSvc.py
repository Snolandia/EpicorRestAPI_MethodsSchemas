import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VoidPaymentSvc
# Description: AP Void Payment Entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_VoidPayments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VoidPayments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VoidPayments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/VoidPayments",headers=creds) as resp:
           return await resp.json()

async def post_VoidPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VoidPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/VoidPayments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VoidPayments_Company_HeadNum(Company, HeadNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VoidPayment item
   Description: Calls GetByID to retrieve the VoidPayment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VoidPayment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/VoidPayments(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VoidPayments_Company_HeadNum(Company, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VoidPayment for the service
   Description: Calls UpdateExt to update VoidPayment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VoidPayment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CheckHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/VoidPayments(" + Company + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VoidPayments_Company_HeadNum(Company, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VoidPayment item
   Description: Call UpdateExt to delete VoidPayment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VoidPayment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/VoidPayments(" + Company + "," + HeadNum + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCheckHed, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCheckHed=" + whereClauseCheckHed
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(headNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidChecks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidChecks
   Description: Voids CheckHed rows contained in ds.
   OperationID: VoidChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidSelectedChecks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidSelectedChecks
   Description: Void Checks if SelectedForAction = true, return not updated ds
   OperationID: VoidSelectedChecks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidSelectedChecks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidSelectedChecks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOnScreenLoad(epicorHeaders = None):
   """  
   Summary: Invoke method CheckOnScreenLoad
   Description: This method is called only on first build of the screen.  If the GL is not
interfaced the user will get a warning asking if they'd like to continue or not.
If the user answers no or any exceptions were raised, then the screen is immediately
shut down and the user is sent back to the main menu.
   OperationID: CheckOnScreenLoad
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOnScreenLoad_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GenerateLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateLegalNumber
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GenerateLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateLegalNumberOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateLegalNumberOpts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: GenerateLegalNumberOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLegalNumberOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLegalNumberOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumbersOnClose(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumbersOnClose
   Description: This method will void legal numbers that have been generated for checks
that were not voided.  This can happen if legal numbers were generated,
but the user never actually voided the check(s).
   OperationID: VoidLegalNumbersOnClose
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumbersOnClose_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumbersOnClose_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: This method will void legal number for specific check
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetVoidDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetVoidDate
   Description: Set void date.
   OperationID: SetVoidDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetVoidDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetVoidDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeVoid(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeVoid
   OperationID: CheckBeforeVoid
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeVoid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeVoid_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateVoidedDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateVoidedDocs
   OperationID: CreateVoidedDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateVoidedDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateVoidedDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteVoidedDocs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteVoidedDocs
   Description: Deletes documents created for void check.
   OperationID: DeleteVoidedDocs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteVoidedDocs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteVoidedDocs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCheckHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCheckHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCheckHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCheckHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VoidPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CheckHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CheckHedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_CheckHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.CheckSrc:str = obj["CheckSrc"]
      """  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  employee # for payroll checks  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Check Amount. Base Currency.  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount. Document Currency.  """  
      self.ManualPrint:bool = obj["ManualPrint"]
      """  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  """  
      self.Address1:str = obj["Address1"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Zip code or Postal code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payment by electronic funds transfer.  Default from the Vendor.  """  
      self.VendorBankID:str = obj["VendorBankID"]
      """  ID of the vendor's bank.  """  
      self.VendorBankName:str = obj["VendorBankName"]
      """  Supplier Bank Name  """  
      self.VendorBankNameOnAccount:str = obj["VendorBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.VendorBankAddress1:str = obj["VendorBankAddress1"]
      """  First address line of supplier bank.  """  
      self.VendorBankAddress2:str = obj["VendorBankAddress2"]
      """  Second address line of supplier bank.  """  
      self.VendorBankAddress3:str = obj["VendorBankAddress3"]
      """  Third address line of supplier bank.  """  
      self.VendorBankCity:str = obj["VendorBankCity"]
      """  City portion of address of supplier bank.  """  
      self.VendorBankState:str = obj["VendorBankState"]
      """  Can be blank.  """  
      self.VendorBankPostalCode:str = obj["VendorBankPostalCode"]
      """  Postal Code or zip code portion of address of supplier bank.  """  
      self.VendorBankCountryNum:int = obj["VendorBankCountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.VendorBankAcctNumber:str = obj["VendorBankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.VendorBankSwiftNum:str = obj["VendorBankSwiftNum"]
      """  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.XRefCheckNum:str = obj["XRefCheckNum"]
      """  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Total amount in Bank currency  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Total entered flag  """  
      self.LockRate:int = obj["LockRate"]
      """  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to first checkhed  """  
      self.ApplyingPayment:bool = obj["ApplyingPayment"]
      """  Identifies that record is created by 'Apply Debit Memo'.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number for Apply Debit Memo Process.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NOPaymentStatus:int = obj["NOPaymentStatus"]
      """  NOPaymentStatus  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.PayLegalNumber:str = obj["PayLegalNumber"]
      """  PayLegalNumber  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.THPayerType:int = obj["THPayerType"]
      """  THPayerType  """  
      self.VoidDate:str = obj["VoidDate"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.OneTimeVendor:bool = obj["OneTimeVendor"]
      """  Indicates if payment to a One-Time Vendor  """  
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.VendorID:str = obj["VendorID"]
      """  To be used by UI for entry  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      """  Payment Total can be entered manually  """  
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      """  label <Payment Currency> -> <Bank Currency>  """  
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      """  label <Payment Currency> --> <Base Currency>  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ExchangeRateDisabled:bool = obj["ExchangeRateDisabled"]
      self.BaseExchRate:bool = obj["BaseExchRate"]
      self.DocUnappliedAmt:int = obj["DocUnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.InvType:str = obj["InvType"]
      """  It is used for Apply Debit Memo Process  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  """  
      self.HasLines:bool = obj["HasLines"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.EnableIsEnterTotal:bool = obj["EnableIsEnterTotal"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.VendorBankCountryNumDescription:str = obj["VendorBankCountryNumDescription"]
      """  Country name  """  
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
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.UrgentCheck:bool = obj["UrgentCheck"]
      """  CSF Switzerland - Indicate that Check has urgent Invoice payment  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.CheckSrc:str = obj["CheckSrc"]
      """  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  employee # for payroll checks  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Check Amount. Base Currency.  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount. Document Currency.  """  
      self.ManualPrint:bool = obj["ManualPrint"]
      """  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  """  
      self.Address1:str = obj["Address1"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Zip code or Postal code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payment by electronic funds transfer.  Default from the Vendor.  """  
      self.VendorBankID:str = obj["VendorBankID"]
      """  ID of the vendor's bank.  """  
      self.VendorBankName:str = obj["VendorBankName"]
      """  Supplier Bank Name  """  
      self.VendorBankNameOnAccount:str = obj["VendorBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.VendorBankAddress1:str = obj["VendorBankAddress1"]
      """  First address line of supplier bank.  """  
      self.VendorBankAddress2:str = obj["VendorBankAddress2"]
      """  Second address line of supplier bank.  """  
      self.VendorBankAddress3:str = obj["VendorBankAddress3"]
      """  Third address line of supplier bank.  """  
      self.VendorBankCity:str = obj["VendorBankCity"]
      """  City portion of address of supplier bank.  """  
      self.VendorBankState:str = obj["VendorBankState"]
      """  Can be blank.  """  
      self.VendorBankPostalCode:str = obj["VendorBankPostalCode"]
      """  Postal Code or zip code portion of address of supplier bank.  """  
      self.VendorBankCountryNum:int = obj["VendorBankCountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.VendorBankAcctNumber:str = obj["VendorBankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.VendorBankSwiftNum:str = obj["VendorBankSwiftNum"]
      """  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.XRefCheckNum:str = obj["XRefCheckNum"]
      """  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Total amount in Bank currency  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Total entered flag  """  
      self.LockRate:int = obj["LockRate"]
      """  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to first checkhed  """  
      self.ApplyingPayment:bool = obj["ApplyingPayment"]
      """  Identifies that record is created by 'Apply Debit Memo'.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number for Apply Debit Memo Process.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorBankIBANCode:str = obj["VendorBankIBANCode"]
      """  VendorBankIBANCode  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.NOPaymentStatus:int = obj["NOPaymentStatus"]
      """  NOPaymentStatus  """  
      self.NOPaymentDirection:str = obj["NOPaymentDirection"]
      """  NOPaymentDirection  """  
      self.NOPaymentType:str = obj["NOPaymentType"]
      """  NOPaymentType  """  
      self.NOTransferFileName:str = obj["NOTransferFileName"]
      """  Norway CSF: The name of created payment file.  """  
      self.NOBankTransRef:str = obj["NOBankTransRef"]
      """  Norway CSF: Transaction Reference Number assigned by bank.  """  
      self.BalanceUpdate:int = obj["BalanceUpdate"]
      """  BalanceUpdate  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.BOEInvoiceNum:str = obj["BOEInvoiceNum"]
      """  Bill of Exchange Invoice num this was generated from  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MsgId:str = obj["MsgId"]
      """  MsgId  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.PayLegalNumber:str = obj["PayLegalNumber"]
      """  PayLegalNumber  """  
      self.PayTranDocTypeID:str = obj["PayTranDocTypeID"]
      """  PayTranDocTypeID  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.TaxPaymInfo:str = obj["TaxPaymInfo"]
      """  TaxPaymInfo  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  VoidLegalNumber  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  VoidTranDocTypeID  """  
      self.SEGrpNum:int = obj["SEGrpNum"]
      """  SEGrpNum  """  
      self.SEReference:str = obj["SEReference"]
      """  SEReference  """  
      self.SEISGroupedPO3:bool = obj["SEISGroupedPO3"]
      """  SEISGroupedPO3  """  
      self.SEISExported:bool = obj["SEISExported"]
      """  SEISExported  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MXBankAcctNumber:str = obj["MXBankAcctNumber"]
      """  MXBankAcctNumber  """  
      self.MXBankIdentifier:str = obj["MXBankIdentifier"]
      """  MXBankIdentifier  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that payment is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.SEPAPaymentDescription:str = obj["SEPAPaymentDescription"]
      """  SEPAPaymentDescription  """  
      self.THPayerType:int = obj["THPayerType"]
      """  THPayerType  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  TH Reference Invoice Num  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  TH Reference Vendor Num  """  
      self.VoidedReason:str = obj["VoidedReason"]
      """  Text entered by the user to indicate the reason a Payment  was voided.  """  
      self.RegulatoryReportingCode:str = obj["RegulatoryReportingCode"]
      """  Regulatory Reporting Code  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.TaxPointDate:str = obj["TaxPointDate"]
      """  Tax Point Date  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.US1099KGen:bool = obj["US1099KGen"]
      """  US1099KGen  """  
      self.VendorBankBranchCode:str = obj["VendorBankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.VoidDescription:str = obj["VoidDescription"]
      """  GL Description for the Payment Voiding process  """  
      self.DMDescription:str = obj["DMDescription"]
      """  GL Description for AP - Apply Debit Memo/Prepayment  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  CSF Mexico DIOT Transaction Type  """  
      self.ChildPlant:str = obj["ChildPlant"]
      """  ChildPlant  """  
      self.BankBatchIDDsp:str = obj["BankBatchIDDsp"]
      self.BankCheckAmt:int = obj["BankCheckAmt"]
      """  Bank Check Amount  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseExchRate:bool = obj["BaseExchRate"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DocPreTaxTotal:int = obj["DocPreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in document currency.  """  
      self.DocUnappliedAmt:int = obj["DocUnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  """  
      self.DocWhldTotal:int = obj["DocWhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in document currency  """  
      self.EnableAssignLN:bool = obj["EnableAssignLN"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.EnableIsEnterTotal:bool = obj["EnableIsEnterTotal"]
      self.EnableTranDocTypeID:bool = obj["EnableTranDocTypeID"]
      self.EnableVoidLN:bool = obj["EnableVoidLN"]
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      """  Payment Total can be entered manually  """  
      self.ExchangeRateDisabled:bool = obj["ExchangeRateDisabled"]
      self.FromBankRec:bool = obj["FromBankRec"]
      """  If Payment is created from Bank Reconcilation  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.HasLines:bool = obj["HasLines"]
      self.InvType:str = obj["InvType"]
      """  It is used for Apply Debit Memo Process  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualDateChange:bool = obj["ManualDateChange"]
      """  Indicates if the Payment (check) date was chagned by the user.  """  
      self.ManualExRateChange:bool = obj["ManualExRateChange"]
      """  Indicates if Exchange rate was manually changed by the user.  """  
      self.OneTimeVendor:bool = obj["OneTimeVendor"]
      """  Indicates if payment to a One-Time Vendor  """  
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.PCReceipt:bool = obj["PCReceipt"]
      self.PreTaxTotal:int = obj["PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in base currency.  """  
      self.Rpt1PreTaxTotal:int = obj["Rpt1PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt1 currency.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt1WhldTotal:int = obj["Rpt1WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in Rpt1 currency  """  
      self.Rpt2PreTaxTotal:int = obj["Rpt2PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt2 currency.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt2WhldTotal:int = obj["Rpt2WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in Rpt2 currency  """  
      self.Rpt3PreTaxTotal:int = obj["Rpt3PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt3 currency  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt3WhldTotal:int = obj["Rpt3WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in Rpt3t currency  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.SEPAPaymentDescriptionEnabled:bool = obj["SEPAPaymentDescriptionEnabled"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.UrgentCheck:bool = obj["UrgentCheck"]
      """  CSF Switzerland - Indicate that Check has urgent Invoice payment  """  
      self.VendorID:str = obj["VendorID"]
      """  To be used by UI for entry  """  
      self.VoidDate:str = obj["VoidDate"]
      self.WhldTotal:int = obj["WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in base currency  """  
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      """  label <Payment Currency> -> <Bank Currency>  """  
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      """  label <Payment Currency> --> <Base Currency>  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.FullAddress:str = obj["FullAddress"]
      """  Full address of Voided Payment  """  
      self.CheckMiscAmt:int = obj["CheckMiscAmt"]
      """  Check Misc Amount. Base Currency.  """  
      self.DocCheckMiscAmt:int = obj["DocCheckMiscAmt"]
      """  Check Misc Amount. Document Currency.  """  
      self.DocCheckInvAmt:int = obj["DocCheckInvAmt"]
      """  Check Invoice Amount. Document Currency.  """  
      self.CheckInvAmt:int = obj["CheckInvAmt"]
      """  Check Invoice Amount. Base Currency.  """  
      self.Rpt1CheckMiscAmt:int = obj["Rpt1CheckMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckMiscAmt:int = obj["Rpt2CheckMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckMiscAmt:int = obj["Rpt3CheckMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1CheckInvAmt:int = obj["Rpt1CheckInvAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckInvAmt:int = obj["Rpt2CheckInvAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckInvAmt:int = obj["Rpt3CheckInvAmt"]
      """  Reporting currency value of this field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankBranchBankBranchCode:str = obj["BankBranchBankBranchCode"]
      self.BankBranchDescription:str = obj["BankBranchDescription"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.THRefVendorNumName:str = obj["THRefVendorNumName"]
      self.THRefVendorNumVendorID:str = obj["THRefVendorNumVendorID"]
      self.VendorBankCountryNumDescription:str = obj["VendorBankCountryNumDescription"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
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
class CheckBeforeVoid_input:
   """ Required : 
   headNum
   fromAutoBankRec
   bankAcctID
   cashBookNum
   cashBookLine
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      self.fromAutoBankRec:bool = obj["fromAutoBankRec"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashBookLine:int = obj["cashBookLine"]
      pass

class CheckBeforeVoid_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue
   """  
   def __init__(self, obj):
      self.keyValue:str = obj["keyValue"]
      """  HeadNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckOnScreenLoad_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateVoidedDocs_input:
   """ Required : 
   headNum
   fromAutoBankRec
   bankAcctID
   cashBookNum
   cashBookLine
   ds
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      self.fromAutoBankRec:bool = obj["fromAutoBankRec"]
      self.bankAcctID:str = obj["bankAcctID"]
      self.cashBookNum:int = obj["cashBookNum"]
      self.cashBookLine:int = obj["cashBookLine"]
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

class CreateVoidedDocs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteVoidedDocs_input:
   """ Required : 
   HeadNum
   ds
   """  
   def __init__(self, obj):
      self.HeadNum:int = obj["HeadNum"]
      """  CheckHed HeadNum.  """  
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

class DeleteVoidedDocs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CheckHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.CheckSrc:str = obj["CheckSrc"]
      """  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  employee # for payroll checks  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Check Amount. Base Currency.  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount. Document Currency.  """  
      self.ManualPrint:bool = obj["ManualPrint"]
      """  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  """  
      self.Address1:str = obj["Address1"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Zip code or Postal code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payment by electronic funds transfer.  Default from the Vendor.  """  
      self.VendorBankID:str = obj["VendorBankID"]
      """  ID of the vendor's bank.  """  
      self.VendorBankName:str = obj["VendorBankName"]
      """  Supplier Bank Name  """  
      self.VendorBankNameOnAccount:str = obj["VendorBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.VendorBankAddress1:str = obj["VendorBankAddress1"]
      """  First address line of supplier bank.  """  
      self.VendorBankAddress2:str = obj["VendorBankAddress2"]
      """  Second address line of supplier bank.  """  
      self.VendorBankAddress3:str = obj["VendorBankAddress3"]
      """  Third address line of supplier bank.  """  
      self.VendorBankCity:str = obj["VendorBankCity"]
      """  City portion of address of supplier bank.  """  
      self.VendorBankState:str = obj["VendorBankState"]
      """  Can be blank.  """  
      self.VendorBankPostalCode:str = obj["VendorBankPostalCode"]
      """  Postal Code or zip code portion of address of supplier bank.  """  
      self.VendorBankCountryNum:int = obj["VendorBankCountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.VendorBankAcctNumber:str = obj["VendorBankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.VendorBankSwiftNum:str = obj["VendorBankSwiftNum"]
      """  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.XRefCheckNum:str = obj["XRefCheckNum"]
      """  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Total amount in Bank currency  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Total entered flag  """  
      self.LockRate:int = obj["LockRate"]
      """  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to first checkhed  """  
      self.ApplyingPayment:bool = obj["ApplyingPayment"]
      """  Identifies that record is created by 'Apply Debit Memo'.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number for Apply Debit Memo Process.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.NOPaymentStatus:int = obj["NOPaymentStatus"]
      """  NOPaymentStatus  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.PayLegalNumber:str = obj["PayLegalNumber"]
      """  PayLegalNumber  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.THPayerType:int = obj["THPayerType"]
      """  THPayerType  """  
      self.VoidDate:str = obj["VoidDate"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.OneTimeVendor:bool = obj["OneTimeVendor"]
      """  Indicates if payment to a One-Time Vendor  """  
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.VendorID:str = obj["VendorID"]
      """  To be used by UI for entry  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      """  Payment Total can be entered manually  """  
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      """  label <Payment Currency> -> <Bank Currency>  """  
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      """  label <Payment Currency> --> <Base Currency>  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ExchangeRateDisabled:bool = obj["ExchangeRateDisabled"]
      self.BaseExchRate:bool = obj["BaseExchRate"]
      self.DocUnappliedAmt:int = obj["DocUnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.InvType:str = obj["InvType"]
      """  It is used for Apply Debit Memo Process  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  """  
      self.HasLines:bool = obj["HasLines"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.EnableIsEnterTotal:bool = obj["EnableIsEnterTotal"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.VendorBankCountryNumDescription:str = obj["VendorBankCountryNumDescription"]
      """  Country name  """  
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
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.UrgentCheck:bool = obj["UrgentCheck"]
      """  CSF Switzerland - Indicate that Check has urgent Invoice payment  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CheckHedListTableset:
   def __init__(self, obj):
      self.CheckHedList:list[Erp_Tablesets_CheckHedListRow] = obj["CheckHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CheckHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is  considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry "group" that the transaction is assigned to. All transactions belong to a "Group". It is  assigned to the record during creation using the "current group" that the user is signed into.  It can not be changed.  The GroupID is used to selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """   Check number is assigned during the check printing process for checks that are printed by the system or entered by the user for hand written checks. NOTE:  Posting of the group is not allowed if any CheckHed record exits with a zero check.
Note: As of version 5.0 electronic payments begin with 50,000,000  """  
      self.CheckDate:str = obj["CheckDate"]
      """  Check Date is assigned during the printing process for system printed checks or entered by the user for hand written checks.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.CheckSrc:str = obj["CheckSrc"]
      """  1=AP Disbursements, 2=AP Manual 3=AP User 4=PR, 5=PR Manual 6=PR User.  """  
      self.ClearedCheck:bool = obj["ClearedCheck"]
      """  Indicates the check's cleared status.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the check is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the check for.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the check (System Set).  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the check was cleared in the system (System Set).  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the check was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the check was cleared on.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """  employee # for payroll checks  """  
      self.CheckAmt:int = obj["CheckAmt"]
      """  Check Amount. Base Currency.  """  
      self.DocCheckAmt:int = obj["DocCheckAmt"]
      """  Check Amount. Document Currency.  """  
      self.ManualPrint:bool = obj["ManualPrint"]
      """  Indicates if this check is printed by the system or manually by the user. If "Yes" then the user must enter the BankAcctID,CheckNum and CheckDate otherwise these fields are not available during entry and will be updated during check printing.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created the Check. Assign by the system using the current UserID at the time the record was created.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead its assigned via selection list processing.  """  
      self.Name:str = obj["Name"]
      """  Vendors name.  """  
      self.Address1:str = obj["Address1"]
      """  First Address line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Zip code or Postal code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement) on which this transaction was cleared by the bank. This is updated via the bank reconciliation process.  This is also written to the related GLJrnDtl records.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payment by electronic funds transfer.  Default from the Vendor.  """  
      self.VendorBankID:str = obj["VendorBankID"]
      """  ID of the vendor's bank.  """  
      self.VendorBankName:str = obj["VendorBankName"]
      """  Supplier Bank Name  """  
      self.VendorBankNameOnAccount:str = obj["VendorBankNameOnAccount"]
      """  Name on the Bank Account.  """  
      self.VendorBankAddress1:str = obj["VendorBankAddress1"]
      """  First address line of supplier bank.  """  
      self.VendorBankAddress2:str = obj["VendorBankAddress2"]
      """  Second address line of supplier bank.  """  
      self.VendorBankAddress3:str = obj["VendorBankAddress3"]
      """  Third address line of supplier bank.  """  
      self.VendorBankCity:str = obj["VendorBankCity"]
      """  City portion of address of supplier bank.  """  
      self.VendorBankState:str = obj["VendorBankState"]
      """  Can be blank.  """  
      self.VendorBankPostalCode:str = obj["VendorBankPostalCode"]
      """  Postal Code or zip code portion of address of supplier bank.  """  
      self.VendorBankCountryNum:int = obj["VendorBankCountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.VendorBankAcctNumber:str = obj["VendorBankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.VendorBankSwiftNum:str = obj["VendorBankSwiftNum"]
      """  Swift number of the bank. (Data is copied from the VendBank.SwiftNum field).  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  This field identifies a line of a bankslip.  """  
      self.XRefCheckNum:str = obj["XRefCheckNum"]
      """  Cross reference check number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  """  
      self.Rpt1CheckAmt:int = obj["Rpt1CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckAmt:int = obj["Rpt2CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckAmt:int = obj["Rpt3CheckAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Total amount in Bank currency  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Total entered flag  """  
      self.LockRate:int = obj["LockRate"]
      """  0 ? System Defaultl; 1 ? Locked; 2 ? Overridden by user  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  it is true, if CheckHed.ManualPrint is false and related BankAcct.UsePendAcct is true.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice's terms definition, to be used.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to first checkhed  """  
      self.ApplyingPayment:bool = obj["ApplyingPayment"]
      """  Identifies that record is created by 'Apply Debit Memo'.  """  
      self.Plant:str = obj["Plant"]
      """  Site ID (Used Primary for Thailand Localization)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  AP Invoice Number for Apply Debit Memo Process.  """  
      self.PMUID:int = obj["PMUID"]
      """  Payment Method Unique Identifier  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.BankTranID:str = obj["BankTranID"]
      """  ID Given by the Bank assigned during matching  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.BankPaidAmt:int = obj["BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.DocBankPaidAmt:int = obj["DocBankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt1BankPaidAmt:int = obj["Rpt1BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt2BankPaidAmt:int = obj["Rpt2BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.Rpt3BankPaidAmt:int = obj["Rpt3BankPaidAmt"]
      """  Amount Bank Paid  """  
      self.BankTransDate:str = obj["BankTransDate"]
      """  Bank Transaction Date  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorBankIBANCode:str = obj["VendorBankIBANCode"]
      """  VendorBankIBANCode  """  
      self.OwnReference:str = obj["OwnReference"]
      """  OwnReference  """  
      self.NOPaymentStatus:int = obj["NOPaymentStatus"]
      """  NOPaymentStatus  """  
      self.NOPaymentDirection:str = obj["NOPaymentDirection"]
      """  NOPaymentDirection  """  
      self.NOPaymentType:str = obj["NOPaymentType"]
      """  NOPaymentType  """  
      self.NOTransferFileName:str = obj["NOTransferFileName"]
      """  Norway CSF: The name of created payment file.  """  
      self.NOBankTransRef:str = obj["NOBankTransRef"]
      """  Norway CSF: Transaction Reference Number assigned by bank.  """  
      self.BalanceUpdate:int = obj["BalanceUpdate"]
      """  BalanceUpdate  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      """  BankRecGainLoss  """  
      self.BOEInvoiceNum:str = obj["BOEInvoiceNum"]
      """  Bill of Exchange Invoice num this was generated from  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      """  DocBankRecGainLoss  """  
      self.MsgId:str = obj["MsgId"]
      """  MsgId  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.PayLegalNumber:str = obj["PayLegalNumber"]
      """  PayLegalNumber  """  
      self.PayTranDocTypeID:str = obj["PayTranDocTypeID"]
      """  PayTranDocTypeID  """  
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      """  Rpt1BankRecGainLoss  """  
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      """  Rpt2BankRecGainLoss  """  
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      """  Rpt3BankRecGainLoss  """  
      self.TaxPaymInfo:str = obj["TaxPaymInfo"]
      """  TaxPaymInfo  """  
      self.VoidLegalNumber:str = obj["VoidLegalNumber"]
      """  VoidLegalNumber  """  
      self.VoidTranDocTypeID:str = obj["VoidTranDocTypeID"]
      """  VoidTranDocTypeID  """  
      self.SEGrpNum:int = obj["SEGrpNum"]
      """  SEGrpNum  """  
      self.SEReference:str = obj["SEReference"]
      """  SEReference  """  
      self.SEISGroupedPO3:bool = obj["SEISGroupedPO3"]
      """  SEISGroupedPO3  """  
      self.SEISExported:bool = obj["SEISExported"]
      """  SEISExported  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.MXBankAcctNumber:str = obj["MXBankAcctNumber"]
      """  MXBankAcctNumber  """  
      self.MXBankIdentifier:str = obj["MXBankIdentifier"]
      """  MXBankIdentifier  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.BankBatchExcluded:bool = obj["BankBatchExcluded"]
      """  Indicates that payment is currently excluded from batch in Bank Statement Processing.  """  
      self.BankBatchSysRowID:str = obj["BankBatchSysRowID"]
      """  BankBatchSysRowID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID  """  
      self.SEPAPaymentDescription:str = obj["SEPAPaymentDescription"]
      """  SEPAPaymentDescription  """  
      self.THPayerType:int = obj["THPayerType"]
      """  THPayerType  """  
      self.THRefInvoiceNum:str = obj["THRefInvoiceNum"]
      """  TH Reference Invoice Num  """  
      self.THRefVendorNum:int = obj["THRefVendorNum"]
      """  TH Reference Vendor Num  """  
      self.VoidedReason:str = obj["VoidedReason"]
      """  Text entered by the user to indicate the reason a Payment  was voided.  """  
      self.RegulatoryReportingCode:str = obj["RegulatoryReportingCode"]
      """  Regulatory Reporting Code  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.TaxPointDate:str = obj["TaxPointDate"]
      """  Tax Point Date  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.ACHTranCode:int = obj["ACHTranCode"]
      """  ACH Transaction Code  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.US1099KGen:bool = obj["US1099KGen"]
      """  US1099KGen  """  
      self.VendorBankBranchCode:str = obj["VendorBankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.VoidDescription:str = obj["VoidDescription"]
      """  GL Description for the Payment Voiding process  """  
      self.DMDescription:str = obj["DMDescription"]
      """  GL Description for AP - Apply Debit Memo/Prepayment  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  CSF Mexico DIOT Transaction Type  """  
      self.ChildPlant:str = obj["ChildPlant"]
      """  ChildPlant  """  
      self.BankBatchIDDsp:str = obj["BankBatchIDDsp"]
      self.BankCheckAmt:int = obj["BankCheckAmt"]
      """  Bank Check Amount  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseExchRate:bool = obj["BaseExchRate"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DocPreTaxTotal:int = obj["DocPreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in document currency.  """  
      self.DocUnappliedAmt:int = obj["DocUnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.DocUnpostedBal:int = obj["DocUnpostedBal"]
      """  DocUnpostedBal of Debit Memo or Pre-Payment Invoice.  """  
      self.DocWhldTotal:int = obj["DocWhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in document currency  """  
      self.EnableAssignLN:bool = obj["EnableAssignLN"]
      self.EnableCurrency:bool = obj["EnableCurrency"]
      self.EnableIsEnterTotal:bool = obj["EnableIsEnterTotal"]
      self.EnableTranDocTypeID:bool = obj["EnableTranDocTypeID"]
      self.EnableVoidLN:bool = obj["EnableVoidLN"]
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      """  Payment Total can be entered manually  """  
      self.ExchangeRateDisabled:bool = obj["ExchangeRateDisabled"]
      self.FromBankRec:bool = obj["FromBankRec"]
      """  If Payment is created from Bank Reconcilation  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  """  
      self.HasLines:bool = obj["HasLines"]
      self.InvType:str = obj["InvType"]
      """  It is used for Apply Debit Memo Process  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.ManualDateChange:bool = obj["ManualDateChange"]
      """  Indicates if the Payment (check) date was chagned by the user.  """  
      self.ManualExRateChange:bool = obj["ManualExRateChange"]
      """  Indicates if Exchange rate was manually changed by the user.  """  
      self.OneTimeVendor:bool = obj["OneTimeVendor"]
      """  Indicates if payment to a One-Time Vendor  """  
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.PCReceipt:bool = obj["PCReceipt"]
      self.PreTaxTotal:int = obj["PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in base currency.  """  
      self.Rpt1PreTaxTotal:int = obj["Rpt1PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt1 currency.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt1WhldTotal:int = obj["Rpt1WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in Rpt1 currency  """  
      self.Rpt2PreTaxTotal:int = obj["Rpt2PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt2 currency.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt2WhldTotal:int = obj["Rpt2WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in Rpt2 currency  """  
      self.Rpt3PreTaxTotal:int = obj["Rpt3PreTaxTotal"]
      """  The total amount of tax related to Prepayment Invoice availabe for reverse in Rpt3 currency  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.Rpt3WhldTotal:int = obj["Rpt3WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in Rpt3t currency  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.SEPAPaymentDescriptionEnabled:bool = obj["SEPAPaymentDescriptionEnabled"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      """  Sum of all rounding differences of the payments for one Cash Receipt and one Check  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  It is used for Apply Debit Memo Process  """  
      self.UrgentCheck:bool = obj["UrgentCheck"]
      """  CSF Switzerland - Indicate that Check has urgent Invoice payment  """  
      self.VendorID:str = obj["VendorID"]
      """  To be used by UI for entry  """  
      self.VoidDate:str = obj["VoidDate"]
      self.WhldTotal:int = obj["WhldTotal"]
      """  Withholding taxes calcullated on applying Debit Memo in base currency  """  
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      """  label <Payment Currency> -> <Bank Currency>  """  
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      """  label <Payment Currency> --> <Base Currency>  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.FullAddress:str = obj["FullAddress"]
      """  Full address of Voided Payment  """  
      self.CheckMiscAmt:int = obj["CheckMiscAmt"]
      """  Check Misc Amount. Base Currency.  """  
      self.DocCheckMiscAmt:int = obj["DocCheckMiscAmt"]
      """  Check Misc Amount. Document Currency.  """  
      self.DocCheckInvAmt:int = obj["DocCheckInvAmt"]
      """  Check Invoice Amount. Document Currency.  """  
      self.CheckInvAmt:int = obj["CheckInvAmt"]
      """  Check Invoice Amount. Base Currency.  """  
      self.Rpt1CheckMiscAmt:int = obj["Rpt1CheckMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckMiscAmt:int = obj["Rpt2CheckMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckMiscAmt:int = obj["Rpt3CheckMiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1CheckInvAmt:int = obj["Rpt1CheckInvAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2CheckInvAmt:int = obj["Rpt2CheckInvAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3CheckInvAmt:int = obj["Rpt3CheckInvAmt"]
      """  Reporting currency value of this field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankBranchBankBranchCode:str = obj["BankBranchBankBranchCode"]
      self.BankBranchDescription:str = obj["BankBranchDescription"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.PMUIDName:str = obj["PMUIDName"]
      self.THRefVendorNumName:str = obj["THRefVendorNumName"]
      self.THRefVendorNumVendorID:str = obj["THRefVendorNumVendorID"]
      self.VendorBankCountryNumDescription:str = obj["VendorBankCountryNumDescription"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
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

class Erp_Tablesets_UpdExtVoidPaymentTableset:
   def __init__(self, obj):
      self.CheckHed:list[Erp_Tablesets_CheckHedRow] = obj["CheckHed"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VoidPaymentTableset:
   def __init__(self, obj):
      self.CheckHed:list[Erp_Tablesets_CheckHedRow] = obj["CheckHed"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateLegalNumberOpts_input:
   """ Required : 
   ds
   inHeadNum
   ipLegalNumGenOpts
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.inHeadNum:int = obj["inHeadNum"]
      """  HeadNum of current checkhed record  """  
      self.ipLegalNumGenOpts:str = obj["ipLegalNumGenOpts"]
      """  Legal Number opts  """  
      pass

class GenerateLegalNumberOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GenerateLegalNumber_input:
   """ Required : 
   ds
   inHeadNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.inHeadNum:int = obj["inHeadNum"]
      """  HeadNum of current checkhed record  """  
      pass

class GenerateLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VoidPaymentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VoidPaymentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VoidPaymentTableset] = obj["returnObj"]
      pass

class GetLegalNumGenOpts_input:
   """ Required : 
   ds
   inHeadNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.inHeadNum:int = obj["inHeadNum"]
      """  HeadNum of current checkhed record  """  
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
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
      self.returnObj:list[Erp_Tablesets_CheckHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCheckHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

class GetNewCheckHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCheckHed
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCheckHed:str = obj["whereClauseCheckHed"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VoidPaymentTableset] = obj["returnObj"]
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

class SetVoidDate_input:
   """ Required : 
   HeadNum
   VoidDate
   ds
   """  
   def __init__(self, obj):
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum.  """  
      self.VoidDate:str = obj["VoidDate"]
      """  Void date.  """  
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

class SetVoidDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVoidPaymentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVoidPaymentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidChecks_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

class VoidChecks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumber_input:
   """ Required : 
   ds
   inHeadNum
   voidReason
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.inHeadNum:int = obj["inHeadNum"]
      """  Cheks' HeadNum , if we are voiding only one LegalNumber  """  
      self.voidReason:str = obj["voidReason"]
      """  Void Reason  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumbersOnClose_input:
   """ Required : 
   ds
   autoVoidPayment
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.autoVoidPayment:bool = obj["autoVoidPayment"]
      """  True when is called from AutoVoidPaymentForm  """  
      pass

class VoidLegalNumbersOnClose_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidSelectedChecks_input:
   """ Required : 
   ds
   singleVoid
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.singleVoid:bool = obj["singleVoid"]
      """  Is voiding call from Details(for single void) or from grid(for multiple void)  """  
      pass

class VoidSelectedChecks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VoidPaymentTableset] = obj["ds"]
      self.allOK:bool = obj["allOK"]
      self.rvnJrnUID:int = obj["parameters"]
      pass

      """  output parameters  """  

