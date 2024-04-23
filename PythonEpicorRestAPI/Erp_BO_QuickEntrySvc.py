import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuickEntrySvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries",headers=creds) as resp:
           return await resp.json()

async def post_QuickEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickEntries_Company_EmpID(Company, EmpID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickEntry item
   Description: Calls GetByID to retrieve the QuickEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickEntries_Company_EmpID(Company, EmpID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickEntry for the service
   Description: Calls UpdateExt to update QuickEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpBasicRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickEntries_Company_EmpID(Company, EmpID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickEntry item
   Description: Call UpdateExt to delete QuickEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntries_Company_EmpID_QuickEntryExpenses(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuickEntryExpenses items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickEntryExpenses1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryExpenses",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntries_Company_EmpID_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickEntryExpense item
   Description: Calls GetByID to retrieve the QuickEntryExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryExpense1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntries_Company_EmpID_QuickEntryTimes(Company, EmpID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuickEntryTimes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickEntryTimes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryTimeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryTimes",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntries_Company_EmpID_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickEntryTime item
   Description: Calls GetByID to retrieve the QuickEntryTime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryTime1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntries(" + Company + "," + EmpID + ")/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntryExpenses(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickEntryExpenses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntryExpenses
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses",headers=creds) as resp:
           return await resp.json()

async def post_QuickEntryExpenses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntryExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickEntryExpense item
   Description: Calls GetByID to retrieve the QuickEntryExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickEntryExpense for the service
   Description: Calls UpdateExt to update QuickEntryExpense. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntryExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuickEntryExpenseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickEntryExpenses_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickEntryExpense item
   Description: Call UpdateExt to delete QuickEntryExpense item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntryExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryExpenses(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntryTimes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickEntryTimes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntryTimes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryTimeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes",headers=creds) as resp:
           return await resp.json()

async def post_QuickEntryTimes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntryTimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickEntryTime item
   Description: Calls GetByID to retrieve the QuickEntryTime item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntryTime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickEntryTime for the service
   Description: Calls UpdateExt to update QuickEntryTime. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntryTime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuickEntryTimeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickEntryTimes_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickEntryTime item
   Description: Call UpdateExt to delete QuickEntryTime item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntryTime
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/QuickEntryTimes(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpBasicListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEmpBasic, whereClauseQuickEntryExpense, whereClauseQuickEntryTime, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseEmpBasic=" + whereClauseEmpBasic
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuickEntryExpense=" + whereClauseQuickEntryExpense
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuickEntryTime=" + whereClauseQuickEntryTime
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empID, epicorHeaders = None):
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
   params += "empID=" + empID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIndirectCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIndirectCode
   Description: Method to call when changing the Indirect Code
   OperationID: OnChangeIndirectCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIndirectCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIndirectCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLaborType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLaborType
   Description: Method to call when changing the Labor Type
   OperationID: OnChangeLaborType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLaborType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLaborType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMiscCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMiscCode
   Description: Method to call when changing the Miscellaneous Code.
   OperationID: OnChangeMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOprSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOprSeq
   Description: Method to call when changing the Operation Sequence
   OperationID: OnChangeOprSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePaymentMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePaymentMethod
   Description: Method to call when changing the Payment Method.
   OperationID: OnChangePaymentMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePaymentMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePaymentMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePhaseID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePhaseID
   Description: Method to call when changing the Phase ID.
   OperationID: OnChangePhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeProjectID
   Description: Method to call when changing the Project ID.
   OperationID: OnChangeProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRoleCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRoleCd
   Description: This method defaults dataset fields when the RoleCd field changes.
   OperationID: OnChangeRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildRoleCodeWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildRoleCodeWhereClause
   OperationID: BuildRoleCodeWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildRoleCodeWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildRoleCodeWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EmployeeExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EmployeeExists
   OperationID: EmployeeExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EmployeeExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmployeeExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsEmpAuthToBookTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsEmpAuthToBookTime
   OperationID: IsEmpAuthToBookTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsEmpAuthToBookTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsEmpAuthToBookTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFilteredRoleCdList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFilteredRoleCdList
   Description: Returns Filtered Role Codes.
   OperationID: GetFilteredRoleCdList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFilteredRoleCdList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFilteredRoleCdList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpBasic(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpBasic
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpBasic
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpBasic_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpBasic_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickEntryExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickEntryExpense
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickEntryExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickEntryExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickEntryExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickEntryTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickEntryTime
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickEntryTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickEntryTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickEntryTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpBasicListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpBasicRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpBasicRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryExpenseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuickEntryExpenseRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryTimeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuickEntryTimeRow] = obj["value"]
      pass

class Erp_Tablesets_EmpBasicListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpBasicRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address Line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EmgPhone:str = obj["EmgPhone"]
      """  Emergency Phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.Payroll:bool = obj["Payroll"]
      """   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.EmgContact:str = obj["EmgContact"]
      """  Emergency contact name.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the Employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.CanReportQty:bool = obj["CanReportQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  """  
      self.CanOverrideJob:bool = obj["CanOverrideJob"]
      """   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  """  
      self.CanRequestMaterial:bool = obj["CanRequestMaterial"]
      """   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  """  
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  """  
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  If false the shop employee will not be allowed to book time to manufacturing jobs.  """  
      self.ContractEmp:bool = obj["ContractEmp"]
      """  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Time transactions.  """  
      self.ExpenseEntryAllowed:bool = obj["ExpenseEntryAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense transactions.  """  
      self.ExpenseVendorNum:int = obj["ExpenseVendorNum"]
      """  The Supplier Number associated to the Employee for Expense entry.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.CanEnterIndirectTime:bool = obj["CanEnterIndirectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  """  
      self.CanEnterProductionTime:bool = obj["CanEnterProductionTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  """  
      self.CanEnterProjectTime:bool = obj["CanEnterProjectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  """  
      self.CanEnterServiceTime:bool = obj["CanEnterServiceTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  """  
      self.CanEnterSetupTime:bool = obj["CanEnterSetupTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  """  
      self.TimeAutoApprove:bool = obj["TimeAutoApprove"]
      """  Time transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.ExpenseAutoApprove:bool = obj["ExpenseAutoApprove"]
      """  Expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileUserPassword:str = obj["MobileUserPassword"]
      """  Mobile Password  """  
      self.AllowIndirect:bool = obj["AllowIndirect"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  """  
      self.AllowProduction:bool = obj["AllowProduction"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  """  
      self.AllowProject:bool = obj["AllowProject"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  """  
      self.AllowService:bool = obj["AllowService"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  """  
      self.AllowSetup:bool = obj["AllowSetup"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  """  
      self.DefaultLaborTypePseudo:str = obj["DefaultLaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.DefaultTimeTypCd:str = obj["DefaultTimeTypCd"]
      """  Time Type Code  """  
      self.DefaultIndirectCode:str = obj["DefaultIndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.DefaultExpenseCode:str = obj["DefaultExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.DefaultResourceGrpID:str = obj["DefaultResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.DefaultResourceID:str = obj["DefaultResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.DefaultLaborHrs:int = obj["DefaultLaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.DefaultExpCurrencyCode:str = obj["DefaultExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.DefaultClaimCurrencyCode:str = obj["DefaultClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.DefaultPMUID:int = obj["DefaultPMUID"]
      """  The payment method of the expense.  """  
      self.DefaultTaxRegionCode:str = obj["DefaultTaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DefaultTaxIncluded:bool = obj["DefaultTaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.ExpenseAdvReqAllowed:bool = obj["ExpenseAdvReqAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense for advance requests.  """  
      self.ExpenseAdvReqWFGroupID:str = obj["ExpenseAdvReqWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense advance request transactions.  """  
      self.ExpenseAdvReqAutoApprove:bool = obj["ExpenseAdvReqAutoApprove"]
      """  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileResourceID:str = obj["MobileResourceID"]
      """  MobileResourceID  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.UserNameInJDF:str = obj["UserNameInJDF"]
      """  UserNameInJDF  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PermitScrap:bool = obj["PermitScrap"]
      """  PermitScrap  """  
      self.PermitDown:bool = obj["PermitDown"]
      """  PermitDown  """  
      self.PermitHelp:bool = obj["PermitHelp"]
      """  PermitHelp  """  
      self.PermitJobControl:bool = obj["PermitJobControl"]
      """  PermitJobControl  """  
      self.PermitNextJobControl:bool = obj["PermitNextJobControl"]
      """  PermitNextJobControl  """  
      self.PermitManualSqc:bool = obj["PermitManualSqc"]
      """  PermitManualSqc  """  
      self.PermitVariableSqc:bool = obj["PermitVariableSqc"]
      """  PermitVariableSqc  """  
      self.PermitAttributeSqc:bool = obj["PermitAttributeSqc"]
      """  PermitAttributeSqc  """  
      self.PermitMaterialLot:bool = obj["PermitMaterialLot"]
      """  PermitMaterialLot  """  
      self.PermitSetupMaterial:bool = obj["PermitSetupMaterial"]
      """  PermitSetupMaterial  """  
      self.PermitCavities:bool = obj["PermitCavities"]
      """  PermitCavities  """  
      self.PermitPercentRegrind:bool = obj["PermitPercentRegrind"]
      """  PermitPercentRegrind  """  
      self.PermitSaveProfile:bool = obj["PermitSaveProfile"]
      """  PermitSaveProfile  """  
      self.PermitCalibration:bool = obj["PermitCalibration"]
      """  PermitCalibration  """  
      self.PermitMachinePm:bool = obj["PermitMachinePm"]
      """  PermitMachinePm  """  
      self.PermitToolPm:bool = obj["PermitToolPm"]
      """  PermitToolPm  """  
      self.PermitLanguage:bool = obj["PermitLanguage"]
      """  PermitLanguage  """  
      self.PermitPreferences:bool = obj["PermitPreferences"]
      """  PermitPreferences  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisallowTimeEntry:bool = obj["DisallowTimeEntry"]
      """  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  """  
      self.PkgInboundAllowed:bool = obj["PkgInboundAllowed"]
      """  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgOutboundAllowed:bool = obj["PkgOutboundAllowed"]
      """  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgInventoryAllowed:bool = obj["PkgInventoryAllowed"]
      """  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgManufacturingAllowed:bool = obj["PkgManufacturingAllowed"]
      """  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgQualityAllowed:bool = obj["PkgQualityAllowed"]
      """  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.PkgMasterMixedPrint:bool = obj["PkgMasterMixedPrint"]
      """  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  """  
      self.PkgSuppressPrintMessages:bool = obj["PkgSuppressPrintMessages"]
      """  PkgSuppressPrintMessages  """  
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  PayrollValuesForHCM  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the employee has to be synchronized with Epicor FSA application.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.IDDocument:str = obj["IDDocument"]
      """  Identity Document  """  
      self.BirthDate:str = obj["BirthDate"]
      """  Birthdate  """  
      self.Sex:str = obj["Sex"]
      """  Sex  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.EnrollmentDate:str = obj["EnrollmentDate"]
      """  Enrollment Date  """  
      self.DepartureDate:str = obj["DepartureDate"]
      """  Departure Date  """  
      self.AlertFlag:bool = obj["AlertFlag"]
      """  Should this employee receive email alert messages.  """  
      self.DepartmentDescription:str = obj["DepartmentDescription"]
      """  Department Description  """  
      self.EnableExpenseSupplier:bool = obj["EnableExpenseSupplier"]
      """  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  """  
      self.ExpenseDescription:str = obj["ExpenseDescription"]
      """  Expense Description  """  
      self.ExpenseDisableCreate:bool = obj["ExpenseDisableCreate"]
      """  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      self.FoundPayroll:bool = obj["FoundPayroll"]
      """  Payroll record has been found so changes to many fields are disallowed.  """  
      self.FoundPayrollUserAllowed:bool = obj["FoundPayrollUserAllowed"]
      """  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  """  
      self.HCMEnabledAt:str = obj["HCMEnabledAt"]
      """  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  """  
      self.IsHCMAllowedByEmp:bool = obj["IsHCMAllowedByEmp"]
      """  External field used on Employee Entry in order to enable/disable HCM configuration  """  
      self.PayrollValuesForHCMDsp:str = obj["PayrollValuesForHCMDsp"]
      """  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  """  
      self.PerConName:str = obj["PerConName"]
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.SetShopLoad:bool = obj["SetShopLoad"]
      """  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  """  
      self.ShiftEndTime:str = obj["ShiftEndTime"]
      """  Shift end time in Hours:Minute format., used by Shop Tracker  """  
      self.ShiftStartTime:str = obj["ShiftStartTime"]
      """  Shift start time in Hours:Minutes format  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.TimeDisableCreate:bool = obj["TimeDisableCreate"]
      """  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      self.UserIDName:str = obj["UserIDName"]
      """  User ID Name  """  
      self.CalendarID:str = obj["CalendarID"]
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.TimeApprovalTasksTree:str = obj["TimeApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ExpenseApprovalTasksTree:str = obj["ExpenseApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ShiftLength:int = obj["ShiftLength"]
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.ExpenseVendorNumName:str = obj["ExpenseVendorNumName"]
      self.ExpenseVendorNumCity:str = obj["ExpenseVendorNumCity"]
      self.ExpenseVendorNumTermsCode:str = obj["ExpenseVendorNumTermsCode"]
      self.ExpenseVendorNumAddress3:str = obj["ExpenseVendorNumAddress3"]
      self.ExpenseVendorNumDefaultFOB:str = obj["ExpenseVendorNumDefaultFOB"]
      self.ExpenseVendorNumCurrencyCode:str = obj["ExpenseVendorNumCurrencyCode"]
      self.ExpenseVendorNumZIP:str = obj["ExpenseVendorNumZIP"]
      self.ExpenseVendorNumVendorID:str = obj["ExpenseVendorNumVendorID"]
      self.ExpenseVendorNumAddress2:str = obj["ExpenseVendorNumAddress2"]
      self.ExpenseVendorNumAddress1:str = obj["ExpenseVendorNumAddress1"]
      self.ExpenseVendorNumCountry:str = obj["ExpenseVendorNumCountry"]
      self.ExpenseVendorNumState:str = obj["ExpenseVendorNumState"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntryExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.IndirectExpense:bool = obj["IndirectExpense"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  """  
      self.PMUID:int = obj["PMUID"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      """  Currency Description  """  
      self.ClaimCurrencyCodeDescription:str = obj["ClaimCurrencyCodeDescription"]
      """  Claim Currency Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeExpUnitBased:bool = obj["MiscCodeExpUnitBased"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntryTimeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.LaborType:str = obj["LaborType"]
      """  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  """  
      self.JobNum:str = obj["JobNum"]
      """  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The Expense Code for the labor transaction.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The Resource Group in which the labor is performed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource that was used to do the work.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleSelectionDisabled:bool = obj["RoleSelectionDisabled"]
      self.TimeTypSelectionDisabled:bool = obj["TimeTypSelectionDisabled"]
      self.BitFlag:int = obj["BitFlag"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.TimeTypeDescription:str = obj["TimeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildRoleCodeWhereClause_input:
   """ Required : 
   iEmpID
   iProjID
   iJobNum
   iAssSeq
   iOprSeq
   """  
   def __init__(self, obj):
      self.iEmpID:str = obj["iEmpID"]
      self.iProjID:str = obj["iProjID"]
      self.iJobNum:str = obj["iJobNum"]
      self.iAssSeq:int = obj["iAssSeq"]
      self.iOprSeq:int = obj["iOprSeq"]
      pass

class BuildRoleCodeWhereClause_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EmployeeExists_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class EmployeeExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class Erp_Tablesets_EmpBasicListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpBasicListTableset:
   def __init__(self, obj):
      self.EmpBasicList:list[Erp_Tablesets_EmpBasicListRow] = obj["EmpBasicList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpBasicRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FirstName:str = obj["FirstName"]
      """  First name of employee.  """  
      self.MiddleInitial:str = obj["MiddleInitial"]
      """  Middle name of employee.  """  
      self.LastName:str = obj["LastName"]
      """  Last name of employee  """  
      self.Name:str = obj["Name"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.Address:str = obj["Address"]
      """  First Address Line  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line  """  
      self.City:str = obj["City"]
      """  City portion of address  """  
      self.State:str = obj["State"]
      """  Home State. Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of address  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.Phone:str = obj["Phone"]
      """  Home phone number  """  
      self.EmgPhone:str = obj["EmgPhone"]
      """  Emergency Phone number  """  
      self.Shift:int = obj["Shift"]
      """  Normal work shift.  Value is to be defaulted from XASyst.DefaultShift (Production/Data Collection tab in Company Configuration) when available, otherwise it is not defaulted.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate that is used for Job Costing.  """  
      self.Payroll:bool = obj["Payroll"]
      """   Indicates if this employee is should be paid through the Manufacturing System payroll module.  This does not mean they have been setup in payroll, only that they should be.
Once setup in payroll (existence of corresponding PREmpMas record) this field cannot be changed.  """  
      self.PRSetupReq:bool = obj["PRSetupReq"]
      """  An internally assigned flag that Indicates if the employee needs to be established in payroll. (Existence of PREmpMas). This flag is used to allow payroll employee maintenance view new employees created by job costing that were flagged as being "Payroll" employees.  """  
      self.EmpStatus:str = obj["EmpStatus"]
      """  Indicates the employment status. Can be A-Active, I-InActive or T-Terminated.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """   The default expense code that will be for direct labor hours reported by this employee.  This must be valid in the LabExpCd master file.
This will be used unless labor is reported where the JobHead.ExpenseCode is not blank.  """  
      self.PhotoFile:str = obj["PhotoFile"]
      """  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  """  
      self.JCDept:str = obj["JCDept"]
      """   The Job Department in which the employee works work was done. An optional field. If entered must be valid in JCDept table.
Used by data collection in the "Work Que" window to provide a default department to view.  """  
      self.EmgContact:str = obj["EmgContact"]
      """  Emergency contact name.  """  
      self.SupervisorID:str = obj["SupervisorID"]
      """   The ID of the Supervisor for the employee.  The Supervisor ID is actually the EmpID used for supervisor's PREmpMas record.
Validation: Can't be blank, if entered must be found in the PREmpMas file.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.ServTech:bool = obj["ServTech"]
      """  This person usually goes out on service calls  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the Employee.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """   Links the employee to a UserID.  This link is used by the Shop Floor Menu(SFM).  In the SFM, the user signs on with their employee id instead of a User id. This link grants the menu security authorizations of the User to the employee. It also defines the language to be used.
Note: An employee can only be related to one UserFile record. Each UserFile, can be related to many employees.  Therefore, you might set up a few generic Users per language, or based on security levels or you might set up a user for each employee. Note: Many transactions, are stamped with the UserID, thus if you use generic users you will be tracking to the individual employee.
This field is OPTIONAL. However, employee will not be allowed to login to the SFM without a being linked to a UserID.  Also, the company of the employee must be an authorized company of the user. This is validated by the finding a record in UserComp table, using EmpBasic.Company, EmpBasic.DCDUserID.  """  
      self.ProductionWorker:bool = obj["ProductionWorker"]
      """  Indicates if this employee works on the manufacturing line. This must be checked for employee to use the Shop Floor Menu production options.  """  
      self.MaterialHandler:bool = obj["MaterialHandler"]
      """  Indicates if this employee is a material handler. This must be checked for employee to use the Shop Floor Menu material handler options.  """  
      self.ShopSupervisor:bool = obj["ShopSupervisor"]
      """  Indicates if this employee is a shop supervisor. This must be checked for employee to use the Shop Floor Menu Supervisor options.  """  
      self.CanReportQty:bool = obj["CanReportQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report completed quantities.  """  
      self.CanOverrideJob:bool = obj["CanOverrideJob"]
      """   Pertains to Data Collection only.
Indicates if the job/asm/opr can be overriden when reporting completed quantity.  If NO, then they will only be allowed to report against a job/asm/opr that they are currently working on (active labordtl record ) or where the job is open and the operation is marked as "quantity only" reporting .  If YES, they can enter the quantity for any open job without first having to do a start activity function.
( See also EmpBasic.CanReportQty )  """  
      self.CanRequestMaterial:bool = obj["CanRequestMaterial"]
      """   Pertains to Data Collection/Advanced Material Management only.
Indicates if the employee is allowed make requests for materials.  """  
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report scrap quantities.  """  
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      """   Pertains to Data Collection only.
Indicates if the employee is allowed report nonconformance quantities.  """  
      self.ShipRecv:bool = obj["ShipRecv"]
      """  Indicates if this employee is a Shipping/Receiving worker. This must be checked for employee to use the Shop Floor Menu Shipping/Receiving options.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WarehouseManager:bool = obj["WarehouseManager"]
      """  A warehouse manager has the access to the Manager's Queue tab in the Material Request Queue.  """  
      self.CanOverrideAllocations:bool = obj["CanOverrideAllocations"]
      """  Employee is able to override a hard allocation against inventory and select it from another Bin during the process of picking and packing orders, as long as it is not allocated to another Sales Order, Job or Transfer Order.  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  If false the shop employee will not be allowed to book time to manufacturing jobs.  """  
      self.ContractEmp:bool = obj["ContractEmp"]
      """  True indicates that the shop employee is on contract rather than paid via the payroll. This flag is then used in the advanced billing invoice preparation process.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Resource Group ID for this employee, only allowed if the Project Billing module licensed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Resource D for this employee, only allowed if the Project Billing module licensed.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Time transactions.  """  
      self.ExpenseEntryAllowed:bool = obj["ExpenseEntryAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense transactions.  """  
      self.ExpenseVendorNum:int = obj["ExpenseVendorNum"]
      """  The Supplier Number associated to the Employee for Expense entry.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.CanEnterIndirectTime:bool = obj["CanEnterIndirectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Indirect time.  """  
      self.CanEnterProductionTime:bool = obj["CanEnterProductionTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Production time.  """  
      self.CanEnterProjectTime:bool = obj["CanEnterProjectTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Project time.  """  
      self.CanEnterServiceTime:bool = obj["CanEnterServiceTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Service time.  """  
      self.CanEnterSetupTime:bool = obj["CanEnterSetupTime"]
      """   Pertains to Time Management.
Maintains whether the employee is allowed to enter Setup time.  """  
      self.TimeAutoApprove:bool = obj["TimeAutoApprove"]
      """  Time transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.ExpenseAutoApprove:bool = obj["ExpenseAutoApprove"]
      """  Expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileUserPassword:str = obj["MobileUserPassword"]
      """  Mobile Password  """  
      self.AllowIndirect:bool = obj["AllowIndirect"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Indirect.  If True, an employee may select Indirect labor type.  If false, employee may not select Indirect labor type in Time Entry.  """  
      self.AllowProduction:bool = obj["AllowProduction"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Production.  If True, an employee may select Production labor type.  If false, employee may not select Production labor type in Time Entry.  """  
      self.AllowProject:bool = obj["AllowProject"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Project.  If True, an employee may select Project labor type.  If false, employee may not select Project labor type in Time Entry.  """  
      self.AllowService:bool = obj["AllowService"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Service.  If True, an employee may select Service labor type.  If false, employee may not select Service labor type in Time Entry.  """  
      self.AllowSetup:bool = obj["AllowSetup"]
      """  Default is True.  Determines if an employee can enter time with a labor type of Setup.  If True, an employee may select Setup labor type.  If false, employee may not select Setup labor type in Time Entry.  """  
      self.DefaultLaborTypePseudo:str = obj["DefaultLaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.DefaultTimeTypCd:str = obj["DefaultTimeTypCd"]
      """  Time Type Code  """  
      self.DefaultIndirectCode:str = obj["DefaultIndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.DefaultExpenseCode:str = obj["DefaultExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.DefaultResourceGrpID:str = obj["DefaultResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.DefaultResourceID:str = obj["DefaultResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.DefaultLaborHrs:int = obj["DefaultLaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.DefaultExpCurrencyCode:str = obj["DefaultExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.DefaultClaimCurrencyCode:str = obj["DefaultClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.DefaultPMUID:int = obj["DefaultPMUID"]
      """  The payment method of the expense.  """  
      self.DefaultTaxRegionCode:str = obj["DefaultTaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DefaultTaxIncluded:bool = obj["DefaultTaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.ExpenseAdvReqAllowed:bool = obj["ExpenseAdvReqAllowed"]
      """  This value will be true if the Employee is allowed to enter Expense for advance requests.  """  
      self.ExpenseAdvReqWFGroupID:str = obj["ExpenseAdvReqWFGroupID"]
      """  Unique identifier of the workflow group for this employee's Expense advance request transactions.  """  
      self.ExpenseAdvReqAutoApprove:bool = obj["ExpenseAdvReqAutoApprove"]
      """  Advance request expense transactions for the employee requiring employee approval logic will automatically be approved.  """  
      self.MobileResourceID:str = obj["MobileResourceID"]
      """  MobileResourceID  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.UserNameInJDF:str = obj["UserNameInJDF"]
      """  UserNameInJDF  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PermitScrap:bool = obj["PermitScrap"]
      """  PermitScrap  """  
      self.PermitDown:bool = obj["PermitDown"]
      """  PermitDown  """  
      self.PermitHelp:bool = obj["PermitHelp"]
      """  PermitHelp  """  
      self.PermitJobControl:bool = obj["PermitJobControl"]
      """  PermitJobControl  """  
      self.PermitNextJobControl:bool = obj["PermitNextJobControl"]
      """  PermitNextJobControl  """  
      self.PermitManualSqc:bool = obj["PermitManualSqc"]
      """  PermitManualSqc  """  
      self.PermitVariableSqc:bool = obj["PermitVariableSqc"]
      """  PermitVariableSqc  """  
      self.PermitAttributeSqc:bool = obj["PermitAttributeSqc"]
      """  PermitAttributeSqc  """  
      self.PermitMaterialLot:bool = obj["PermitMaterialLot"]
      """  PermitMaterialLot  """  
      self.PermitSetupMaterial:bool = obj["PermitSetupMaterial"]
      """  PermitSetupMaterial  """  
      self.PermitCavities:bool = obj["PermitCavities"]
      """  PermitCavities  """  
      self.PermitPercentRegrind:bool = obj["PermitPercentRegrind"]
      """  PermitPercentRegrind  """  
      self.PermitSaveProfile:bool = obj["PermitSaveProfile"]
      """  PermitSaveProfile  """  
      self.PermitCalibration:bool = obj["PermitCalibration"]
      """  PermitCalibration  """  
      self.PermitMachinePm:bool = obj["PermitMachinePm"]
      """  PermitMachinePm  """  
      self.PermitToolPm:bool = obj["PermitToolPm"]
      """  PermitToolPm  """  
      self.PermitLanguage:bool = obj["PermitLanguage"]
      """  PermitLanguage  """  
      self.PermitPreferences:bool = obj["PermitPreferences"]
      """  PermitPreferences  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DisallowTimeEntry:bool = obj["DisallowTimeEntry"]
      """  The purpose of the flag is to disallow an employee to enter their own time in Time and Expense Entry  """  
      self.PkgInboundAllowed:bool = obj["PkgInboundAllowed"]
      """  Indicates that an employee can execute inbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgOutboundAllowed:bool = obj["PkgOutboundAllowed"]
      """  Indicates that an employee can execute outbound related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgInventoryAllowed:bool = obj["PkgInventoryAllowed"]
      """  Indicates that an employee can execute inventory related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgManufacturingAllowed:bool = obj["PkgManufacturingAllowed"]
      """  Indicates that an employee can execute manufacturing related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.PkgQualityAllowed:bool = obj["PkgQualityAllowed"]
      """  Indicates that an employee can execute quality related transactions on the shop floor. The default for the check box is unchecked.  """  
      self.ImageID:str = obj["ImageID"]
      """  ImageID  """  
      self.PkgMasterMixedPrint:bool = obj["PkgMasterMixedPrint"]
      """  Package Control Activity setting to indicate if the employee is allowed to print during the Master and MixedMaster.  """  
      self.PkgSuppressPrintMessages:bool = obj["PkgSuppressPrintMessages"]
      """  PkgSuppressPrintMessages  """  
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  PayrollValuesForHCM  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the employee has to be synchronized with Epicor FSA application.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.IDDocument:str = obj["IDDocument"]
      """  Identity Document  """  
      self.BirthDate:str = obj["BirthDate"]
      """  Birthdate  """  
      self.Sex:str = obj["Sex"]
      """  Sex  """  
      self.Department:str = obj["Department"]
      """  Department  """  
      self.EnrollmentDate:str = obj["EnrollmentDate"]
      """  Enrollment Date  """  
      self.DepartureDate:str = obj["DepartureDate"]
      """  Departure Date  """  
      self.AlertFlag:bool = obj["AlertFlag"]
      """  Should this employee receive email alert messages.  """  
      self.DepartmentDescription:str = obj["DepartmentDescription"]
      """  Department Description  """  
      self.EnableExpenseSupplier:bool = obj["EnableExpenseSupplier"]
      """  external field for UI to use to know whether it should enable or disable the ExpenseVendorNumVendorID field.  """  
      self.ExpenseDescription:str = obj["ExpenseDescription"]
      """  Expense Description  """  
      self.ExpenseDisableCreate:bool = obj["ExpenseDisableCreate"]
      """  Indicates whether the user is allowed to create Expense transactions in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      self.FoundPayroll:bool = obj["FoundPayroll"]
      """  Payroll record has been found so changes to many fields are disallowed.  """  
      self.FoundPayrollUserAllowed:bool = obj["FoundPayrollUserAllowed"]
      """  Payroll record has been found so changes to many fields are disallowed, but the user is in the employee's payroll class so can see the labor rate field  """  
      self.HCMEnabledAt:str = obj["HCMEnabledAt"]
      """  String value which contains the validations for the HCM Integration, possible values NON(Nothing configured), HDR (Header) DTL (Detail)  """  
      self.IsHCMAllowedByEmp:bool = obj["IsHCMAllowedByEmp"]
      """  External field used on Employee Entry in order to enable/disable HCM configuration  """  
      self.PayrollValuesForHCMDsp:str = obj["PayrollValuesForHCMDsp"]
      """  Displays blank if "Allow Override Integrate Labor Pay Hours at Employee" checkbox in Site configuration is unchecked and Employee's value if checked.  """  
      self.PerConName:str = obj["PerConName"]
      self.PhotoFilePath:str = obj["PhotoFilePath"]
      """  Path to the photo file if it exists.  """  
      self.SetShopLoad:bool = obj["SetShopLoad"]
      """  Flag used to indicate that the generate fill shop capacity process needs to be run to update the ShopCap records because new records won't be added due performance.  """  
      self.ShiftEndTime:str = obj["ShiftEndTime"]
      """  Shift end time in Hours:Minute format., used by Shop Tracker  """  
      self.ShiftStartTime:str = obj["ShiftStartTime"]
      """  Shift start time in Hours:Minutes format  """  
      self.SupervisorName:str = obj["SupervisorName"]
      """  SupervisorName  """  
      self.TimeDisableCreate:bool = obj["TimeDisableCreate"]
      """  Indicates whether the user is allowed to create a Time transaction in Time and Expense Entry for another employee for which they are an Approver.  """  
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      self.UserIDName:str = obj["UserIDName"]
      """  User ID Name  """  
      self.CalendarID:str = obj["CalendarID"]
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.TimeApprovalTasksTree:str = obj["TimeApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ExpenseApprovalTasksTree:str = obj["ExpenseApprovalTasksTree"]
      """  This column used to display Time Approval Task tree in MetaUI  """  
      self.ShiftLength:int = obj["ShiftLength"]
      self.BitFlag:int = obj["BitFlag"]
      self.CompanySendToFSA:bool = obj["CompanySendToFSA"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.ExpenseVendorNumName:str = obj["ExpenseVendorNumName"]
      self.ExpenseVendorNumCity:str = obj["ExpenseVendorNumCity"]
      self.ExpenseVendorNumTermsCode:str = obj["ExpenseVendorNumTermsCode"]
      self.ExpenseVendorNumAddress3:str = obj["ExpenseVendorNumAddress3"]
      self.ExpenseVendorNumDefaultFOB:str = obj["ExpenseVendorNumDefaultFOB"]
      self.ExpenseVendorNumCurrencyCode:str = obj["ExpenseVendorNumCurrencyCode"]
      self.ExpenseVendorNumZIP:str = obj["ExpenseVendorNumZIP"]
      self.ExpenseVendorNumVendorID:str = obj["ExpenseVendorNumVendorID"]
      self.ExpenseVendorNumAddress2:str = obj["ExpenseVendorNumAddress2"]
      self.ExpenseVendorNumAddress1:str = obj["ExpenseVendorNumAddress1"]
      self.ExpenseVendorNumCountry:str = obj["ExpenseVendorNumCountry"]
      self.ExpenseVendorNumState:str = obj["ExpenseVendorNumState"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntryExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.IndirectExpense:bool = obj["IndirectExpense"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  """  
      self.PMUID:int = obj["PMUID"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CurrencyCodeDescription:str = obj["CurrencyCodeDescription"]
      """  Currency Description  """  
      self.ClaimCurrencyCodeDescription:str = obj["ClaimCurrencyCodeDescription"]
      """  Claim Currency Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeLCAmount:int = obj["MiscCodeLCAmount"]
      self.MiscCodeLCCurrencyCode:str = obj["MiscCodeLCCurrencyCode"]
      self.MiscCodeLCDisburseMethod:str = obj["MiscCodeLCDisburseMethod"]
      self.MiscCodeExpUnitBased:bool = obj["MiscCodeExpUnitBased"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntryTableset:
   def __init__(self, obj):
      self.EmpBasic:list[Erp_Tablesets_EmpBasicRow] = obj["EmpBasic"]
      self.QuickEntryExpense:list[Erp_Tablesets_QuickEntryExpenseRow] = obj["QuickEntryExpense"]
      self.QuickEntryTime:list[Erp_Tablesets_QuickEntryTimeRow] = obj["QuickEntryTime"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuickEntryTimeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.LaborType:str = obj["LaborType"]
      """  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  """  
      self.JobNum:str = obj["JobNum"]
      """  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The Expense Code for the labor transaction.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The Resource Group in which the labor is performed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource that was used to do the work.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleSelectionDisabled:bool = obj["RoleSelectionDisabled"]
      self.TimeTypSelectionDisabled:bool = obj["TimeTypSelectionDisabled"]
      self.BitFlag:int = obj["BitFlag"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.TimeTypeDescription:str = obj["TimeTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtQuickEntryTableset:
   def __init__(self, obj):
      self.EmpBasic:list[Erp_Tablesets_EmpBasicRow] = obj["EmpBasic"]
      self.QuickEntryExpense:list[Erp_Tablesets_QuickEntryExpenseRow] = obj["QuickEntryExpense"]
      self.QuickEntryTime:list[Erp_Tablesets_QuickEntryTimeRow] = obj["QuickEntryTime"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuickEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuickEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuickEntryTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFilteredRoleCdList_input:
   """ Required : 
   iEmpID
   iProjID
   iJobNum
   iAssSeq
   iOprSeq
   """  
   def __init__(self, obj):
      self.iEmpID:str = obj["iEmpID"]
      self.iProjID:str = obj["iProjID"]
      self.iJobNum:str = obj["iJobNum"]
      self.iAssSeq:int = obj["iAssSeq"]
      self.iOprSeq:int = obj["iOprSeq"]
      pass

class GetFilteredRoleCdList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpBasicListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEmpBasic_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class GetNewEmpBasic_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuickEntryExpense_input:
   """ Required : 
   ds
   empID
   quickEntryType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.quickEntryType:str = obj["quickEntryType"]
      pass

class GetNewQuickEntryExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuickEntryTime_input:
   """ Required : 
   ds
   empID
   quickEntryType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.quickEntryType:str = obj["quickEntryType"]
      pass

class GetNewQuickEntryTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEmpBasic
   whereClauseQuickEntryExpense
   whereClauseQuickEntryTime
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEmpBasic:str = obj["whereClauseEmpBasic"]
      self.whereClauseQuickEntryExpense:str = obj["whereClauseQuickEntryExpense"]
      self.whereClauseQuickEntryTime:str = obj["whereClauseQuickEntryTime"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuickEntryTableset] = obj["returnObj"]
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

class IsEmpAuthToBookTime_input:
   """ Required : 
   iEmpID
   iProjID
   """  
   def __init__(self, obj):
      self.iEmpID:str = obj["iEmpID"]
      self.iProjID:str = obj["iProjID"]
      pass

class IsEmpAuthToBookTime_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeIndirectCode_input:
   """ Required : 
   proposedIndirectCode
   ds
   """  
   def __init__(self, obj):
      self.proposedIndirectCode:str = obj["proposedIndirectCode"]
      """  The proposed Indirect Code  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangeIndirectCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLaborType_input:
   """ Required : 
   proposedLaborType
   ds
   """  
   def __init__(self, obj):
      self.proposedLaborType:str = obj["proposedLaborType"]
      """  The proposed Labor Type  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangeLaborType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMiscCode_input:
   """ Required : 
   proposedMiscCode
   ds
   """  
   def __init__(self, obj):
      self.proposedMiscCode:str = obj["proposedMiscCode"]
      """  The proposed miscellaneous code  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangeMiscCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOprSeq_input:
   """ Required : 
   proposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.proposedOprSeq:int = obj["proposedOprSeq"]
      """  The proposed Operation Sequence  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangeOprSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePaymentMethod_input:
   """ Required : 
   proposedPMUID
   ds
   """  
   def __init__(self, obj):
      self.proposedPMUID:int = obj["proposedPMUID"]
      """  The proposed pay method id  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangePaymentMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePhaseID_input:
   """ Required : 
   proposedPhaseID
   ds
   """  
   def __init__(self, obj):
      self.proposedPhaseID:str = obj["proposedPhaseID"]
      """  The proposed phase ID  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangePhaseID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeProjectID_input:
   """ Required : 
   proposedProjectID
   ds
   """  
   def __init__(self, obj):
      self.proposedProjectID:str = obj["proposedProjectID"]
      """  The proposed project ID  """  
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class OnChangeProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRoleCd_input:
   """ Required : 
   ds
   ipRoleCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      self.ipRoleCd:str = obj["ipRoleCd"]
      """  Proposed RoleCd change  """  
      pass

class OnChangeRoleCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuickEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuickEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

