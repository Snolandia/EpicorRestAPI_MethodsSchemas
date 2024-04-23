import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CreditCardProcSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CreditCardProcs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditCardProcs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditCardProcs
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs",headers=creds) as resp:
           return await resp.json()

async def post_CreditCardProcs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditCardProcs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditCardProcs_Company(Company, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditCardProc item
   Description: Calls GetByID to retrieve the CreditCardProc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditCardProc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditCardProcs_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditCardProc for the service
   Description: Calls UpdateExt to update CreditCardProc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditCardProc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditCardProcRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditCardProcs_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditCardProc item
   Description: Call UpdateExt to delete CreditCardProc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditCardProc
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditCardProcs_Company_CreditCardProcessors(Company, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CreditCardProcessors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CreditCardProcessors1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcessorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")/CreditCardProcessors",headers=creds) as resp:
           return await resp.json()

async def get_CreditCardProcs_Company_CreditCardProcessors_Company_ProcessorNum(Company, ProcessorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditCardProcessor item
   Description: Calls GetByID to retrieve the CreditCardProcessor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditCardProcessor1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessorNum: Desc: ProcessorNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcs(" + Company + ")/CreditCardProcessors(" + Company + "," + ProcessorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_CreditCardProcessors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CreditCardProcessors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditCardProcessors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcessorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors",headers=creds) as resp:
           return await resp.json()

async def post_CreditCardProcessors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditCardProcessors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CreditCardProcessors_Company_ProcessorNum(Company, ProcessorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CreditCardProcessor item
   Description: Calls GetByID to retrieve the CreditCardProcessor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditCardProcessor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessorNum: Desc: ProcessorNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors(" + Company + "," + ProcessorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CreditCardProcessors_Company_ProcessorNum(Company, ProcessorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CreditCardProcessor for the service
   Description: Calls UpdateExt to update CreditCardProcessor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditCardProcessor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessorNum: Desc: ProcessorNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CreditCardProcessorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors(" + Company + "," + ProcessorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CreditCardProcessors_Company_ProcessorNum(Company, ProcessorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CreditCardProcessor item
   Description: Call UpdateExt to delete CreditCardProcessor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditCardProcessor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProcessorNum: Desc: ProcessorNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/CreditCardProcessors(" + Company + "," + ProcessorNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CreditCardProcListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCreditCardProc, whereClauseCreditCardProcessor, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCreditCardProc=" + whereClauseCreditCardProc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCreditCardProcessor=" + whereClauseCreditCardProcessor
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeProcessor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeProcessor
   Description: This method validates the Processor ID
   OperationID: OnChangeProcessor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProcessor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProcessor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HasPendingAuthorizations(epicorHeaders = None):
   """  
   Summary: Invoke method HasPendingAuthorizations
   Description: Returns if there is any authorization, unused, succeeded transaction.
   OperationID: HasPendingAuthorizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasPendingAuthorizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_HasProcessorPendingAuthorizations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HasProcessorPendingAuthorizations
   Description: Returns if there is any unused success authorization for the processor.
   OperationID: HasProcessorPendingAuthorizations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HasProcessorPendingAuthorizations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasProcessorPendingAuthorizations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCreditCardProc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCreditCardProc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditCardProc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditCardProc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditCardProc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCreditCardProcessor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCreditCardProcessor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCreditCardProcessor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCreditCardProcessor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCreditCardProcessor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CreditCardProcSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditCardProcListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditCardProcRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CreditCardProcessorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CreditCardProcessorRow] = obj["value"]
      pass

class Erp_Tablesets_CreditCardProcListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcInterfaceCode:str = obj["ProcInterfaceCode"]
      """  Processor Interface code  """  
      self.ProcInterfaceDesc:str = obj["ProcInterfaceDesc"]
      """  Processor Interface Description  """  
      self.HostAddress:str = obj["HostAddress"]
      """  Host Address  """  
      self.HostPort:int = obj["HostPort"]
      """  Host Port number  """  
      self.TimeOut:int = obj["TimeOut"]
      """  Time Out  """  
      self.Verbosity:str = obj["Verbosity"]
      """  L = Low, M = Medium  """  
      self.ProxyAddress:str = obj["ProxyAddress"]
      """  Proxy Address  """  
      self.ProxyPort:int = obj["ProxyPort"]
      """  Proxy Port number  """  
      self.ProxyLogon:str = obj["ProxyLogon"]
      """  Proxy Logon  """  
      self.ProxyPwd:str = obj["ProxyPwd"]
      """  Proxy Password  """  
      self.AllowDepPay:bool = obj["AllowDepPay"]
      """  Allow Deposit Payments on Sales Orders  """  
      self.FailDepToSalesTrans:bool = obj["FailDepToSalesTrans"]
      """  Failed DEPOSIT becomes SALE transaction  """  
      self.FailStopsShip:bool = obj["FailStopsShip"]
      """  Credit card failure stops shipment  """  
      self.ReauthRemaining:bool = obj["ReauthRemaining"]
      """  Reauthorize remaining balance on back order  """  
      self.DaysToRetainInfo:int = obj["DaysToRetainInfo"]
      """  Number of days to retain credit card information  """  
      self.ReauthBeforePick:bool = obj["ReauthBeforePick"]
      """  Reauthorize before picking  """  
      self.ReauthAfterDays:int = obj["ReauthAfterDays"]
      """  Reauthorize credit card after number of days as passed  """  
      self.ReauthAbove:int = obj["ReauthAbove"]
      """  Reauthorize if Above value  """  
      self.UseCSC:bool = obj["UseCSC"]
      """  Validate using CSC Code  """  
      self.IgnoreCSCFail:bool = obj["IgnoreCSCFail"]
      """  Ignore CSC validation failure  """  
      self.UseAVS:bool = obj["UseAVS"]
      """  Use Address + Zip to verify credit card  """  
      self.IgnoreAVSFail:bool = obj["IgnoreAVSFail"]
      """  Ignore address validation failure  """  
      self.IsTest:bool = obj["IsTest"]
      """  Indicates if the credit card transactions will be logged.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditCardProcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcInterfaceCode:str = obj["ProcInterfaceCode"]
      """  Processor Interface code  """  
      self.ProcInterfaceDesc:str = obj["ProcInterfaceDesc"]
      """  Processor Interface Description  """  
      self.HostAddress:str = obj["HostAddress"]
      """  Host Address  """  
      self.HostPort:int = obj["HostPort"]
      """  Host Port number  """  
      self.TimeOut:int = obj["TimeOut"]
      """  Time Out  """  
      self.Verbosity:str = obj["Verbosity"]
      """  L = Low, M = Medium  """  
      self.ProxyAddress:str = obj["ProxyAddress"]
      """  Proxy Address  """  
      self.ProxyPort:int = obj["ProxyPort"]
      """  Proxy Port number  """  
      self.ProxyLogon:str = obj["ProxyLogon"]
      """  Proxy Logon  """  
      self.ProxyPwd:str = obj["ProxyPwd"]
      """  Proxy Password  """  
      self.AllowDepPay:bool = obj["AllowDepPay"]
      """  Allow Deposit Payments on Sales Orders  """  
      self.FailDepToSalesTrans:bool = obj["FailDepToSalesTrans"]
      """  Failed DEPOSIT becomes SALE transaction  """  
      self.FailStopsShip:bool = obj["FailStopsShip"]
      """  Credit card failure stops shipment  """  
      self.ReauthRemaining:bool = obj["ReauthRemaining"]
      """  Reauthorize remaining balance on back order  """  
      self.DaysToRetainInfo:int = obj["DaysToRetainInfo"]
      """  Number of days to retain credit card information  """  
      self.ReauthBeforePick:bool = obj["ReauthBeforePick"]
      """  Reauthorize before picking  """  
      self.ReauthAfterDays:int = obj["ReauthAfterDays"]
      """  Reauthorize credit card after number of days as passed  """  
      self.ReauthAbove:int = obj["ReauthAbove"]
      """  Reauthorize if Above value  """  
      self.UseCSC:bool = obj["UseCSC"]
      """  Validate using CSC Code  """  
      self.IgnoreCSCFail:bool = obj["IgnoreCSCFail"]
      """  Ignore CSC validation failure  """  
      self.UseAVS:bool = obj["UseAVS"]
      """  Use Address + Zip to verify credit card  """  
      self.IgnoreAVSFail:bool = obj["IgnoreAVSFail"]
      """  Ignore address validation failure  """  
      self.IsTest:bool = obj["IsTest"]
      """  Indicates if the credit card transactions will be logged.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.IsTraining:bool = obj["IsTraining"]
      """  Indicates if the credit card setup will be using a testing Paygate instance for transactions. Force requests to use Paygate test url: paygate-test1.eaglesoa.com.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditCardProcessorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.Processor:str = obj["Processor"]
      """  Processor  """  
      self.ProcessorDesc:str = obj["ProcessorDesc"]
      """  ProcessorDesc  """  
      self.Partner:str = obj["Partner"]
      """  Partner  """  
      self.PartnerUser:str = obj["PartnerUser"]
      """  PartnerUser  """  
      self.PartnerVendor:str = obj["PartnerVendor"]
      """  PartnerVendor  """  
      self.PartnerPwd:str = obj["PartnerPwd"]
      """  PartnerPwd  """  
      self.TPPID:str = obj["TPPID"]
      """  TPPID  """  
      self.FDMSGroupID:str = obj["FDMSGroupID"]
      """  FDMSGroupID  """  
      self.FDMSCustomerID:str = obj["FDMSCustomerID"]
      """  FDMSCustomerID  """  
      self.FDMSPhoneNum:str = obj["FDMSPhoneNum"]
      """  FDMSPhoneNum  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerPwdMasked:str = obj["PartnerPwdMasked"]
      """  Credit Card Masked password field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CreditCardProcListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcInterfaceCode:str = obj["ProcInterfaceCode"]
      """  Processor Interface code  """  
      self.ProcInterfaceDesc:str = obj["ProcInterfaceDesc"]
      """  Processor Interface Description  """  
      self.HostAddress:str = obj["HostAddress"]
      """  Host Address  """  
      self.HostPort:int = obj["HostPort"]
      """  Host Port number  """  
      self.TimeOut:int = obj["TimeOut"]
      """  Time Out  """  
      self.Verbosity:str = obj["Verbosity"]
      """  L = Low, M = Medium  """  
      self.ProxyAddress:str = obj["ProxyAddress"]
      """  Proxy Address  """  
      self.ProxyPort:int = obj["ProxyPort"]
      """  Proxy Port number  """  
      self.ProxyLogon:str = obj["ProxyLogon"]
      """  Proxy Logon  """  
      self.ProxyPwd:str = obj["ProxyPwd"]
      """  Proxy Password  """  
      self.AllowDepPay:bool = obj["AllowDepPay"]
      """  Allow Deposit Payments on Sales Orders  """  
      self.FailDepToSalesTrans:bool = obj["FailDepToSalesTrans"]
      """  Failed DEPOSIT becomes SALE transaction  """  
      self.FailStopsShip:bool = obj["FailStopsShip"]
      """  Credit card failure stops shipment  """  
      self.ReauthRemaining:bool = obj["ReauthRemaining"]
      """  Reauthorize remaining balance on back order  """  
      self.DaysToRetainInfo:int = obj["DaysToRetainInfo"]
      """  Number of days to retain credit card information  """  
      self.ReauthBeforePick:bool = obj["ReauthBeforePick"]
      """  Reauthorize before picking  """  
      self.ReauthAfterDays:int = obj["ReauthAfterDays"]
      """  Reauthorize credit card after number of days as passed  """  
      self.ReauthAbove:int = obj["ReauthAbove"]
      """  Reauthorize if Above value  """  
      self.UseCSC:bool = obj["UseCSC"]
      """  Validate using CSC Code  """  
      self.IgnoreCSCFail:bool = obj["IgnoreCSCFail"]
      """  Ignore CSC validation failure  """  
      self.UseAVS:bool = obj["UseAVS"]
      """  Use Address + Zip to verify credit card  """  
      self.IgnoreAVSFail:bool = obj["IgnoreAVSFail"]
      """  Ignore address validation failure  """  
      self.IsTest:bool = obj["IsTest"]
      """  Indicates if the credit card transactions will be logged.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditCardProcListTableset:
   def __init__(self, obj):
      self.CreditCardProcList:list[Erp_Tablesets_CreditCardProcListRow] = obj["CreditCardProcList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CreditCardProcRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProcInterfaceCode:str = obj["ProcInterfaceCode"]
      """  Processor Interface code  """  
      self.ProcInterfaceDesc:str = obj["ProcInterfaceDesc"]
      """  Processor Interface Description  """  
      self.HostAddress:str = obj["HostAddress"]
      """  Host Address  """  
      self.HostPort:int = obj["HostPort"]
      """  Host Port number  """  
      self.TimeOut:int = obj["TimeOut"]
      """  Time Out  """  
      self.Verbosity:str = obj["Verbosity"]
      """  L = Low, M = Medium  """  
      self.ProxyAddress:str = obj["ProxyAddress"]
      """  Proxy Address  """  
      self.ProxyPort:int = obj["ProxyPort"]
      """  Proxy Port number  """  
      self.ProxyLogon:str = obj["ProxyLogon"]
      """  Proxy Logon  """  
      self.ProxyPwd:str = obj["ProxyPwd"]
      """  Proxy Password  """  
      self.AllowDepPay:bool = obj["AllowDepPay"]
      """  Allow Deposit Payments on Sales Orders  """  
      self.FailDepToSalesTrans:bool = obj["FailDepToSalesTrans"]
      """  Failed DEPOSIT becomes SALE transaction  """  
      self.FailStopsShip:bool = obj["FailStopsShip"]
      """  Credit card failure stops shipment  """  
      self.ReauthRemaining:bool = obj["ReauthRemaining"]
      """  Reauthorize remaining balance on back order  """  
      self.DaysToRetainInfo:int = obj["DaysToRetainInfo"]
      """  Number of days to retain credit card information  """  
      self.ReauthBeforePick:bool = obj["ReauthBeforePick"]
      """  Reauthorize before picking  """  
      self.ReauthAfterDays:int = obj["ReauthAfterDays"]
      """  Reauthorize credit card after number of days as passed  """  
      self.ReauthAbove:int = obj["ReauthAbove"]
      """  Reauthorize if Above value  """  
      self.UseCSC:bool = obj["UseCSC"]
      """  Validate using CSC Code  """  
      self.IgnoreCSCFail:bool = obj["IgnoreCSCFail"]
      """  Ignore CSC validation failure  """  
      self.UseAVS:bool = obj["UseAVS"]
      """  Use Address + Zip to verify credit card  """  
      self.IgnoreAVSFail:bool = obj["IgnoreAVSFail"]
      """  Ignore address validation failure  """  
      self.IsTest:bool = obj["IsTest"]
      """  Indicates if the credit card transactions will be logged.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PayGateHostAddress:str = obj["PayGateHostAddress"]
      """  Host Address for the Paygate Hosted Token Service.  """  
      self.PayGateNameSpace:str = obj["PayGateNameSpace"]
      """  NameSpace for the Paygate Hosted Token Service.  """  
      self.PayGatePublicKey:str = obj["PayGatePublicKey"]
      """  Public Key for the Paygate Hosted Token Service EWA component.  """  
      self.IsTraining:bool = obj["IsTraining"]
      """  Indicates if the credit card setup will be using a testing Paygate instance for transactions. Force requests to use Paygate test url: paygate-test1.eaglesoa.com.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CreditCardProcTableset:
   def __init__(self, obj):
      self.CreditCardProc:list[Erp_Tablesets_CreditCardProcRow] = obj["CreditCardProc"]
      self.CreditCardProcessor:list[Erp_Tablesets_CreditCardProcessorRow] = obj["CreditCardProcessor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CreditCardProcessorRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ProcessorNum:int = obj["ProcessorNum"]
      """  ProcessorNum  """  
      self.Processor:str = obj["Processor"]
      """  Processor  """  
      self.ProcessorDesc:str = obj["ProcessorDesc"]
      """  ProcessorDesc  """  
      self.Partner:str = obj["Partner"]
      """  Partner  """  
      self.PartnerUser:str = obj["PartnerUser"]
      """  PartnerUser  """  
      self.PartnerVendor:str = obj["PartnerVendor"]
      """  PartnerVendor  """  
      self.PartnerPwd:str = obj["PartnerPwd"]
      """  PartnerPwd  """  
      self.TPPID:str = obj["TPPID"]
      """  TPPID  """  
      self.FDMSGroupID:str = obj["FDMSGroupID"]
      """  FDMSGroupID  """  
      self.FDMSCustomerID:str = obj["FDMSCustomerID"]
      """  FDMSCustomerID  """  
      self.FDMSPhoneNum:str = obj["FDMSPhoneNum"]
      """  FDMSPhoneNum  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerPwdMasked:str = obj["PartnerPwdMasked"]
      """  Credit Card Masked password field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCreditCardProcTableset:
   def __init__(self, obj):
      self.CreditCardProc:list[Erp_Tablesets_CreditCardProcRow] = obj["CreditCardProc"]
      self.CreditCardProcessor:list[Erp_Tablesets_CreditCardProcessorRow] = obj["CreditCardProcessor"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditCardProcTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditCardProcTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditCardProcTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CreditCardProcListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCreditCardProc_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

class GetNewCreditCardProc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCreditCardProcessor_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

class GetNewCreditCardProcessor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCreditCardProc
   whereClauseCreditCardProcessor
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCreditCardProc:str = obj["whereClauseCreditCardProc"]
      self.whereClauseCreditCardProcessor:str = obj["whereClauseCreditCardProcessor"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CreditCardProcTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class HasPendingAuthorizations_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class HasProcessorPendingAuthorizations_input:
   """ Required : 
   processor
   """  
   def __init__(self, obj):
      self.processor:str = obj["processor"]
      pass

class HasProcessorPendingAuthorizations_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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

class OnChangeProcessor_input:
   """ Required : 
   procInterfaceCode
   ds
   """  
   def __init__(self, obj):
      self.procInterfaceCode:str = obj["procInterfaceCode"]
      """  New Process interface code  """  
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

class OnChangeProcessor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCreditCardProcTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCreditCardProcTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CreditCardProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

