import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReminderLetterSvc
# Description: Reminder Letter Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ReminderLetters(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReminderLetters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReminderLetters
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReminderLetterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters",headers=creds) as resp:
           return await resp.json()

async def post_ReminderLetters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReminderLetters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ReminderLetterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ReminderLetterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReminderLetters_Company_LetterNum(Company, LetterNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReminderLetter item
   Description: Calls GetByID to retrieve the ReminderLetter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReminderLetter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ReminderLetterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters(" + Company + "," + LetterNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReminderLetters_Company_LetterNum(Company, LetterNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReminderLetter for the service
   Description: Calls UpdateExt to update ReminderLetter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReminderLetter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ReminderLetterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters(" + Company + "," + LetterNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReminderLetters_Company_LetterNum(Company, LetterNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReminderLetter item
   Description: Call UpdateExt to delete ReminderLetter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReminderLetter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters(" + Company + "," + LetterNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReminderLetters_Company_LetterNum_InvcReminders(Company, LetterNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InvcReminders items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InvcReminders1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcReminderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters(" + Company + "," + LetterNum + ")/InvcReminders",headers=creds) as resp:
           return await resp.json()

async def get_ReminderLetters_Company_LetterNum_InvcReminders_Company_LetterNum_InvoiceNum(Company, LetterNum, InvoiceNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcReminder item
   Description: Calls GetByID to retrieve the InvcReminder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcReminder1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcReminderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/ReminderLetters(" + Company + "," + LetterNum + ")/InvcReminders(" + Company + "," + LetterNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_InvcReminders(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InvcReminders items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcReminders
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcReminderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/InvcReminders",headers=creds) as resp:
           return await resp.json()

async def post_InvcReminders(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcReminders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcReminderRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InvcReminderRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/InvcReminders", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InvcReminders_Company_LetterNum_InvoiceNum(Company, LetterNum, InvoiceNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InvcReminder item
   Description: Calls GetByID to retrieve the InvcReminder item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcReminder
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InvcReminderRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/InvcReminders(" + Company + "," + LetterNum + "," + InvoiceNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InvcReminders_Company_LetterNum_InvoiceNum(Company, LetterNum, InvoiceNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InvcReminder for the service
   Description: Calls UpdateExt to update InvcReminder. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcReminder
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcReminderRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/InvcReminders(" + Company + "," + LetterNum + "," + InvoiceNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InvcReminders_Company_LetterNum_InvoiceNum(Company, LetterNum, InvoiceNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InvcReminder item
   Description: Call UpdateExt to delete InvcReminder item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcReminder
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LetterNum: Desc: LetterNum   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/InvcReminders(" + Company + "," + LetterNum + "," + InvoiceNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReminderLetterListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseReminderLetter, whereClauseInvcReminder, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseReminderLetter=" + whereClauseReminderLetter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInvcReminder=" + whereClauseInvcReminder
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(letterNum, epicorHeaders = None):
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
   params += "letterNum=" + letterNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePrintedLetters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePrintedLetters
   Description: Validate there is at least one printed letter.
   OperationID: ValidatePrintedLetters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePrintedLetters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePrintedLetters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateReminderInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateReminderInvoices
   Description: Create finance charge invoices.
   OperationID: CreateReminderInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateReminderInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateReminderInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateISRCodeLineAmountPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateISRCodeLineAmountPart
   Description: Generate ISR code line's amount part
   OperationID: GenerateISRCodeLineAmountPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateISRCodeLineAmountPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateISRCodeLineAmountPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateReminderLetters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateReminderLetters
   Description: Generate reminder letters according to a specific date and customers
   OperationID: GenerateReminderLetters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateReminderLetters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateReminderLetters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompanySetup(epicorHeaders = None):
   """  
   Summary: Invoke method GetCompanySetup
   Description: Returns the "Combined with Reminder Letter" company setting
   OperationID: GetCompanySetup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompanySetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_PostReminders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostReminders
   Description: This method posts reminder letters to the DB.
   OperationID: PostReminders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostReminders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostReminders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePrintReminders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePrintReminders
   Description: Put temp records into DB, so that they can be updated in case of successfull printing.
   OperationID: PrePrintReminders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePrintReminders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePrintReminders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshLetters(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshLetters
   Description: Get Printed field value for all generated letters.
   OperationID: RefreshLetters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshLetters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshLetters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReminderLetter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReminderLetter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReminderLetter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReminderLetter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReminderLetter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInvcReminder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInvcReminder
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcReminder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInvcReminder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcReminder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReminderLetterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcReminderRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InvcReminderRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReminderLetterListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReminderLetterListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReminderLetterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReminderLetterRow] = obj["value"]
      pass

class Erp_Tablesets_InvcReminderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Unique Invoice number  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Reminder Group Code  """  
      self.Sequence:int = obj["Sequence"]
      """  Reminder Sequence  """  
      self.GenDate:str = obj["GenDate"]
      """  The date when the letter was generated.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the invoice.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  InvoiceType  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LetterNum:int = obj["LetterNum"]
      """  Unique Letter Num.  """  
      self.FinChargeAmt:int = obj["FinChargeAmt"]
      """  Financial charge amount  """  
      self.Payments:int = obj["Payments"]
      """  Number of Payments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.FinChargeCode:str = obj["FinChargeCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReminderLetterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Printed:bool = obj["Printed"]
      """  Printed flag  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Group Code  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the reminder letter to the Customer master file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency of all overdur invoices (each letter can only contain invoiced with the same document currency).  """  
      self.OverdueInvNum:int = obj["OverdueInvNum"]
      """  Total number of invoices included in the reminder letter.  """  
      self.OverdueAmt:int = obj["OverdueAmt"]
      """  Total overdue amount in base currency.  """  
      self.FinChargeAmt:int = obj["FinChargeAmt"]
      """  Total finance charges for included invoices.  """  
      self.LetterNum:int = obj["LetterNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustID:str = obj["CustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReminderLetterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Printed:bool = obj["Printed"]
      """  Printed flag  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Group Code  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the reminder letter to the Customer master file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency of all overdur invoices (each letter can only contain invoiced with the same document currency).  """  
      self.OverdueInvNum:int = obj["OverdueInvNum"]
      """  Total number of invoices included in the reminder letter.  """  
      self.OverdueAmt:int = obj["OverdueAmt"]
      """  Total overdue amount in base currency.  """  
      self.FinChargeAmt:int = obj["FinChargeAmt"]
      """  Total finance charges for included invoices.  """  
      self.LetterNum:int = obj["LetterNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CHISRRefNum:str = obj["CHISRRefNum"]
      """  CHISRRefNum  """  
      self.CustID:str = obj["CustID"]
      self.CHISRCodeGenFailed:bool = obj["CHISRCodeGenFailed"]
      """  CustomerID should be highlighted if ISR Code generation failed (CSF Switzerland)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CreateReminderInvoices_input:
   """ Required : 
   ds
   ipAsOfDate
   ipCustomerList
   ipGroupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  As of Date  """  
      self.ipCustomerList:str = obj["ipCustomerList"]
      """  Customer List  """  
      self.ipGroupID:str = obj["ipGroupID"]
      """  Invoice Group  """  
      pass

class CreateReminderInvoices_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   letterNum
   """  
   def __init__(self, obj):
      self.letterNum:int = obj["letterNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_InvcReminderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Unique Invoice number  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Reminder Group Code  """  
      self.Sequence:int = obj["Sequence"]
      """  Reminder Sequence  """  
      self.GenDate:str = obj["GenDate"]
      """  The date when the letter was generated.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the invoice.  """  
      self.InvoiceType:str = obj["InvoiceType"]
      """  InvoiceType  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice date is duplicated from the InvcGrp record.  """  
      self.DueDate:str = obj["DueDate"]
      """  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      """  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Current outstanding balance. Carries a true sign. (Credit memos are negative).  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.LetterNum:int = obj["LetterNum"]
      """  Unique Letter Num.  """  
      self.FinChargeAmt:int = obj["FinChargeAmt"]
      """  Financial charge amount  """  
      self.Payments:int = obj["Payments"]
      """  Number of Payments  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      self.CustID:str = obj["CustID"]
      self.FinChargeCode:str = obj["FinChargeCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReminderLetterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Printed:bool = obj["Printed"]
      """  Printed flag  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Group Code  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the reminder letter to the Customer master file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency of all overdur invoices (each letter can only contain invoiced with the same document currency).  """  
      self.OverdueInvNum:int = obj["OverdueInvNum"]
      """  Total number of invoices included in the reminder letter.  """  
      self.OverdueAmt:int = obj["OverdueAmt"]
      """  Total overdue amount in base currency.  """  
      self.FinChargeAmt:int = obj["FinChargeAmt"]
      """  Total finance charges for included invoices.  """  
      self.LetterNum:int = obj["LetterNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustID:str = obj["CustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReminderLetterListTableset:
   def __init__(self, obj):
      self.ReminderLetterList:list[Erp_Tablesets_ReminderLetterListRow] = obj["ReminderLetterList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReminderLetterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Printed:bool = obj["Printed"]
      """  Printed flag  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Group Code  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.CustNum:int = obj["CustNum"]
      """  The CustNum field is the internal # that is used to link the reminder letter to the Customer master file.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency of all overdur invoices (each letter can only contain invoiced with the same document currency).  """  
      self.OverdueInvNum:int = obj["OverdueInvNum"]
      """  Total number of invoices included in the reminder letter.  """  
      self.OverdueAmt:int = obj["OverdueAmt"]
      """  Total overdue amount in base currency.  """  
      self.FinChargeAmt:int = obj["FinChargeAmt"]
      """  Total finance charges for included invoices.  """  
      self.LetterNum:int = obj["LetterNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHISRCodeLine:str = obj["CHISRCodeLine"]
      """  CHISRCodeLine  """  
      self.CHISRRefNum:str = obj["CHISRRefNum"]
      """  CHISRRefNum  """  
      self.CustID:str = obj["CustID"]
      self.CHISRCodeGenFailed:bool = obj["CHISRCodeGenFailed"]
      """  CustomerID should be highlighted if ISR Code generation failed (CSF Switzerland)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReminderLetterTableset:
   def __init__(self, obj):
      self.ReminderLetter:list[Erp_Tablesets_ReminderLetterRow] = obj["ReminderLetter"]
      self.InvcReminder:list[Erp_Tablesets_InvcReminderRow] = obj["InvcReminder"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtReminderLetterTableset:
   def __init__(self, obj):
      self.ReminderLetter:list[Erp_Tablesets_ReminderLetterRow] = obj["ReminderLetter"]
      self.InvcReminder:list[Erp_Tablesets_InvcReminderRow] = obj["InvcReminder"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateISRCodeLineAmountPart_input:
   """ Required : 
   ipCurrencyCode
   ipAmount
   """  
   def __init__(self, obj):
      self.ipCurrencyCode:str = obj["ipCurrencyCode"]
      """  Currency code  """  
      self.ipAmount:int = obj["ipAmount"]
      """  Overdue amount  """  
      pass

class GenerateISRCodeLineAmountPart_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  ISR code line's amount part.  """  
      pass

class GenerateReminderLetters_input:
   """ Required : 
   ipCustomerList
   ipAsOfDate
   """  
   def __init__(self, obj):
      self.ipCustomerList:str = obj["ipCustomerList"]
      """  Customer's list  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  Cutoff date to generate letters  """  
      pass

class GenerateReminderLetters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReminderLetterTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.sMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   letterNum
   """  
   def __init__(self, obj):
      self.letterNum:int = obj["letterNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReminderLetterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReminderLetterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReminderLetterTableset] = obj["returnObj"]
      pass

class GetCompanySetup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCombined:bool = obj["opCombined"]
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
      self.returnObj:list[Erp_Tablesets_ReminderLetterListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInvcReminder_input:
   """ Required : 
   ds
   letterNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      self.letterNum:int = obj["letterNum"]
      pass

class GetNewInvcReminder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReminderLetter_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

class GetNewReminderLetter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseReminderLetter
   whereClauseInvcReminder
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseReminderLetter:str = obj["whereClauseReminderLetter"]
      self.whereClauseInvcReminder:str = obj["whereClauseInvcReminder"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReminderLetterTableset] = obj["returnObj"]
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

class PostReminders_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

class PostReminders_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PrePrintReminders_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

class PrePrintReminders_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshLetters_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

class RefreshLetters_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReminderLetterTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReminderLetterTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePrintedLetters_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

class ValidatePrintedLetters_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if there is at least one printed letter, false otherwise.  """  
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReminderLetterTableset] = obj["ds"]
      pass

      """  output parameters  """  

