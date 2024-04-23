import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APTranSearchSvc
# Description: bo/APTranSearch
           APTran records for AR/AP Invoice Tracker
           Jennifer Johnson
           07/27/04
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APTranSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APTranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTranSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches",headers=creds) as resp:
           return await resp.json()

async def post_APTranSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTranSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APTranSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APTranSearches_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTranSearch item
   Description: Calls GetByID to retrieve the APTranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APTranSearches_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APTranSearch for the service
   Description: Calls UpdateExt to update APTranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APTranSearches_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APTranSearch item
   Description: Call UpdateExt to delete APTranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTranSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/APTranSearches(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_PaymentTotals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PaymentTotals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PaymentTotals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PaymentTotalsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals",headers=creds) as resp:
           return await resp.json()

async def post_PaymentTotals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PaymentTotals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PaymentTotalsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PaymentTotalsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PaymentTotals_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PaymentTotal item
   Description: Calls GetByID to retrieve the PaymentTotal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PaymentTotal
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PaymentTotalsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PaymentTotals_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PaymentTotal for the service
   Description: Calls UpdateExt to update PaymentTotal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PaymentTotal
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PaymentTotalsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PaymentTotals_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PaymentTotal item
   Description: Call UpdateExt to delete PaymentTotal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PaymentTotal
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/PaymentTotals(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPTranSearch, whereClausePaymentTotals, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPTranSearch=" + whereClauseAPTranSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePaymentTotals=" + whereClausePaymentTotals
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(headNum, apTranNo, invoiceNum, voided, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "headNum=" + headNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "apTranNo=" + apTranNo
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "invoiceNum=" + invoiceNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "voided=" + voided

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForPO
   Description: Invokes GetRows filtering on invoices for the specified PONum
   OperationID: GetRowsForPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForReceipt
   Description: Invokes GetRows filtering on invoices for the specified Pack slip
   OperationID: GetRowsForReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KineticGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KineticGetRows
   Description: bo/APTranSearch
           GetRows to be run from Kinetic UI to also populate pymtTotals
           rather than populating in the client code.
   OperationID: KineticGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KineticGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPaymentData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPaymentData
   Description: bo/APTranSearch
           GetPaymentData to be run from Kinetic UI to populate grid and pymtTotals
           rather than populating in the client code.
   OperationID: GetPaymentData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPaymentData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPTranSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPTranSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTranSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTranSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTranSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APTranSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APTranSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APTranSearchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PaymentTotalsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PaymentTotalsRow] = obj["value"]
      pass

class Erp_Tablesets_APTranSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number of the related CheckHed.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created this APTran record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is prepayment.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  """  
      self.RefPONum:int = obj["RefPONum"]
      """  Reference Purchase Order Number for Prepayments.  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt Number (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate Number (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
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
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  Legal Number for the adjustment.  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  Transaction Document Type for the adjustment.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date  """  
      self.InvCurrSymbol:str = obj["InvCurrSymbol"]
      """  Invoice Currency Symbol  """  
      self.TranDesc:str = obj["TranDesc"]
      """  TranType Description  """  
      self.CheckAccess:bool = obj["CheckAccess"]
      """  True if user has security to see Check Payment Details  """  
      self.CheckAmt:int = obj["CheckAmt"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceDiscount:int = obj["InvoiceDiscount"]
      self.InvType:str = obj["InvType"]
      """  Either Debit Memo or Invoice or blank  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  The reference Check number paid by the Corporate for the CPay invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  """  
      self.CPayBalance:int = obj["CPayBalance"]
      """  The latest invoice balance of the CPay invoice.  """  
      self.CPayDocBalance:int = obj["CPayDocBalance"]
      """  The latest invoice balance (in Vendor currrency) of the CPay invoice.  """  
      self.CPayIMReceived:bool = obj["CPayIMReceived"]
      """  Flag to indicate if the CPay invoice got created successfully at the corporate.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number of the related CheckHed.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created this APTran record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is prepayment.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  """  
      self.RefPONum:int = obj["RefPONum"]
      """  Reference Purchase Order Number for Prepayments.  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt Number (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate Number (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
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
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  Legal Number for the adjustment.  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  Transaction Document Type for the adjustment.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  InvoiceRef  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code for transactions of type ADJ  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date  """  
      self.NOTranReason:str = obj["NOTranReason"]
      """  NOTranReason  """  
      self.PEIsDetractionPayment:bool = obj["PEIsDetractionPayment"]
      """  PEIsDetractionPayment  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.DocWhManAddAmt:int = obj["DocWhManAddAmt"]
      """  DocWhManAddAmt  """  
      self.WhManAddAmt:int = obj["WhManAddAmt"]
      """  WhManAddAmt  """  
      self.Rpt1WhManAddAmt:int = obj["Rpt1WhManAddAmt"]
      """  Rpt1WhManAddAmt  """  
      self.Rpt2WhManAddAmt:int = obj["Rpt2WhManAddAmt"]
      """  Rpt2WhManAddAmt  """  
      self.Rpt3WhManAddAmt:int = obj["Rpt3WhManAddAmt"]
      """  Rpt3WhManAddAmt  """  
      self.CheckAccess:bool = obj["CheckAccess"]
      """  True if user has security to see Check Payment Details  """  
      self.CPayBalance:int = obj["CPayBalance"]
      """  The latest invoice balance of the CPay invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  The reference Check number paid by the Corporate for the CPay invoice.  """  
      self.CPayDocBalance:int = obj["CPayDocBalance"]
      """  The latest invoice balance (in Vendor currrency) of the CPay invoice.  """  
      self.CPayIMReceived:bool = obj["CPayIMReceived"]
      """  Flag to indicate if the CPay invoice got created successfully at the corporate.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrName:str = obj["CurrName"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DocumentDesc:str = obj["DocumentDesc"]
      self.InvCurrSymbol:str = obj["InvCurrSymbol"]
      """  Invoice Currency Symbol  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceDiscount:int = obj["InvoiceDiscount"]
      self.InvType:str = obj["InvType"]
      """  Either Debit Memo or Invoice or blank  """  
      self.TranDesc:str = obj["TranDesc"]
      """  TranType Description  """  
      self.BOEInvoiceNum:str = obj["BOEInvoiceNum"]
      """  (CSF Peru) Bill of Exchange Invoice Number  """  
      self.CheckAmt:int = obj["CheckAmt"]
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.PayingSiteCode:str = obj["PayingSiteCode"]
      """  Site Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorName:str = obj["VendorName"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorBankBankName:str = obj["VendorBankBankName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PaymentTotalsRow:
   def __init__(self, obj):
      self.CashRcv:int = obj["CashRcv"]
      self.DocCashRcv:int = obj["DocCashRcv"]
      self.DocDscTaken:int = obj["DocDscTaken"]
      self.DocGainReal:int = obj["DocGainReal"]
      self.DocGainUnreal:int = obj["DocGainUnreal"]
      self.DscTaken:int = obj["DscTaken"]
      self.GainReal:int = obj["GainReal"]
      self.GainUnreal:int = obj["GainUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1CashRcv:int = obj["Rpt1CashRcv"]
      self.Rpt1DscTaken:int = obj["Rpt1DscTaken"]
      self.Rpt1GainReal:int = obj["Rpt1GainReal"]
      self.Rpt1GainUnreal:int = obj["Rpt1GainUnreal"]
      self.Rpt2CashRcv:int = obj["Rpt2CashRcv"]
      self.Rpt2DscTaken:int = obj["Rpt2DscTaken"]
      self.Rpt2GainReal:int = obj["Rpt2GainReal"]
      self.Rpt2GainUnreal:int = obj["Rpt2GainUnreal"]
      self.Rpt3CashRcv:int = obj["Rpt3CashRcv"]
      self.Rpt3DscTaken:int = obj["Rpt3DscTaken"]
      self.Rpt3GainReal:int = obj["Rpt3GainReal"]
      self.Rpt3GainUnreal:int = obj["Rpt3GainUnreal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   headNum
   apTranNo
   invoiceNum
   voided
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.voided:bool = obj["voided"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APTranSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number of the related CheckHed.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created this APTran record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is prepayment.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  """  
      self.RefPONum:int = obj["RefPONum"]
      """  Reference Purchase Order Number for Prepayments.  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt Number (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate Number (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
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
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  Legal Number for the adjustment.  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  Transaction Document Type for the adjustment.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date  """  
      self.InvCurrSymbol:str = obj["InvCurrSymbol"]
      """  Invoice Currency Symbol  """  
      self.TranDesc:str = obj["TranDesc"]
      """  TranType Description  """  
      self.CheckAccess:bool = obj["CheckAccess"]
      """  True if user has security to see Check Payment Details  """  
      self.CheckAmt:int = obj["CheckAmt"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceDiscount:int = obj["InvoiceDiscount"]
      self.InvType:str = obj["InvType"]
      """  Either Debit Memo or Invoice or blank  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  The reference Check number paid by the Corporate for the CPay invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  """  
      self.CPayBalance:int = obj["CPayBalance"]
      """  The latest invoice balance of the CPay invoice.  """  
      self.CPayDocBalance:int = obj["CPayDocBalance"]
      """  The latest invoice balance (in Vendor currrency) of the CPay invoice.  """  
      self.CPayIMReceived:bool = obj["CPayIMReceived"]
      """  Flag to indicate if the CPay invoice got created successfully at the corporate.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranSearchListTableset:
   def __init__(self, obj):
      self.APTranSearchList:list[Erp_Tablesets_APTranSearchListRow] = obj["APTranSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APTranSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranType:str = obj["TranType"]
      """  An internal flag which identifies the type of transaction. Valid types are "Pay" or "Adj".  """  
      self.HeadNum:int = obj["HeadNum"]
      """  If TranType = "Pay" or "ADJ" for a currency gain/loss  then this is a duplicate of the related CheckHed.HeadNum,  otherwise it is set to zero.  """  
      self.APTranNo:int = obj["APTranNo"]
      """  Integer assigned by the system which is used as one of the fields to uniquely identify the APTran record.  If (TranType = "Pay"  and InvoiceNum = "") or (TranType = "Adj") it is assigned a unique #  using the database sequence "APTranNo", for Void checks it is a duplicate of the related APTran.APTranNo, else it is set to zero.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number that is being paid or adjusted. This is blank in the case of paying a non-payables expense. Otherwise it DOES have to be valid in the APInvHed file.  """  
      self.Posted:bool = obj["Posted"]
      """  An internal flag which indicates if this check has been Posted.  If "NO" then it is considered as still being in the data entry mode. In which case it is still accessible by the check entry programs.  It is set to "Yes" by the group posting process. This is only applicable for TranType = "Pay".  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount in the vendor's currency. Represents the amount to be applied against the related invoice balance. In the case of payments, this amount excludes any discount, considered as gross payment. TranAmt with a positive sign REDUCES payables while negative INCREASES payables. Example, check detail payments of expenses are positive, unless they are referencing a debit memo. The logic used is that these records are subtracted from the invoice balance.  The adjustment entry program flips the signs of these fields between the user interface and the database. That is to say, the user enters a positive to increase the related invoice or debit memo or a credit to decrease but it is flip when going to/from the database.  """  
      self.DiscAmt:int = obj["DiscAmt"]
      """  Prompt Payment discount. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.DocDiscAmt:int = obj["DocDiscAmt"]
      """  Prompt Payment discount in Vendors currency. Only applicable if related to a valid APInvHed record. In which case it can be defaulted. This would carry a positive sign except in the case of void checks.  """  
      self.Description:str = obj["Description"]
      """  In the case of payment details this description is printed on the check stub. If referencing a invoice the APInvHed.Description is used as a default.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the BankAcct master that this check was drawn  against. This field is updated during the check printing process for system printed checks or entered by the user for manually printed checks. It must be entered and valid for manual checks. It is invalid if not found or BankAcct.Active = No.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number of the related CheckHed.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date. This may be the CheckDate, Void date, or adjustment date. Check dates are duplicated from the CheckHed.CheckDate during the Check printing process. Void date is entered by the user and the void check program duplicates it into each APTran record it generates for the check. Adjustment dates are directly entered by the user.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal Year that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYear during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year to each record on the TranDate  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this transaction is posted to. Updated by the check printing process for system printed checks or by the user for manually printed checks.  If entered must be valid in the Fiscal master.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Indicates if this transaction has been posted to the General Ledger.  This is set during the G/L transfer process.  """  
      self.Voided:bool = obj["Voided"]
      """   An internal flag indicating if this is a Void payment transaction.
This is set by the A/P void check program. Void payments are duplicates of their original APTran payment record with the exception of having the signs on TranAmt and DiscAmt fields flipped.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  UserID that created this APTran record.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number. The foreign key that relates the record to the Vendor master record. For TranType = "Pay" it is set equal to CheckHed.VendorNum. For TranType = "Adj" it is captured from the Vendor.VendorNum field.  """  
      self.Comment:str = obj["Comment"]
      """  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adj".  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this payment.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Sales Tax Amount.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount in the vendors currency.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RoundDiff:int = obj["RoundDiff"]
      """  Rounding difference arises when invoice in one currency are settled in another currency  """  
      self.Rpt1DiscAmt:int = obj["Rpt1DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2DiscAmt:int = obj["Rpt2DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3DiscAmt:int = obj["Rpt3DiscAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Reporting currency value of this field  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """   Fiscal Year Suffix that transaction will be posted to. For check payments this is duplicated from CheckHed.FiscalYearSuffix during check posting.
Void Check entry and adjustment entry assigns the proper fiscal year suffix to each record on the TranDate  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Tax Amount.  """  
      self.SelfAssessAmt:int = obj["SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.DocSelfAssessAmt:int = obj["DocSelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt1SelfAssessAmt:int = obj["Rpt1SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt2SelfAssessAmt:int = obj["Rpt2SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.Rpt3SelfAssessAmt:int = obj["Rpt3SelfAssessAmt"]
      """  Self Assessment Tax Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Red Storno Flag  """  
      self.PrePayment:bool = obj["PrePayment"]
      """  Indicates that this is prepayment.  """  
      self.ContractRef:str = obj["ContractRef"]
      """  Free form Reference (e.g. Contract Number or other reference specified by user) In case Ref PO is specified, default reference is 'PO: 99999', but can be changed by user.  """  
      self.ContractRefDate:str = obj["ContractRefDate"]
      """  Reference Date (e.g. Contract Date, PO Date or other related date) In case Ref PO is specified, default is PO date, and but be changed by user.  """  
      self.RefPONum:int = obj["RefPONum"]
      """  Reference Purchase Order Number for Prepayments.  """  
      self.TaxReceiptDate:str = obj["TaxReceiptDate"]
      """  Tax Receipt Date (Thailand Localization)  """  
      self.TaxReceiptNo:str = obj["TaxReceiptNo"]
      """  Tax Receipt Number (Thailand Localization)  """  
      self.WHTCertificateDate:str = obj["WHTCertificateDate"]
      """  Withholding Tax Certificate Date (Thailand Localization)  """  
      self.WHTCertificateNo:str = obj["WHTCertificateNo"]
      """  Withholding Tax Certificate Number (Thailand Localization)  """  
      self.PCashDeskID:str = obj["PCashDeskID"]
      """  Unique identifier of Petty Cash Desk  """  
      self.GainLossType:str = obj["GainLossType"]
      """  "R" for realized or "U" for unrealized Gain/Loss  """  
      self.PCashRefNum:int = obj["PCashRefNum"]
      """  Reference Number, unique identifier of Petty Cash Document  """  
      self.ReverseGL:bool = obj["ReverseGL"]
      """  Indicates if it's a reversing Gain/Loss adjustment  """  
      self.RevalueDate:str = obj["RevalueDate"]
      """  Revaluation date that generated the gain/loss record  """  
      self.RevalueBal:int = obj["RevalueBal"]
      """  Invoice Balance at the time of revaluation  """  
      self.DocRevalueBal:int = obj["DocRevalueBal"]
      """  Document currency Invoice Balance at the time of revaluation  """  
      self.Rpt1RevalueBal:int = obj["Rpt1RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt2RevalueBal:int = obj["Rpt2RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.Rpt3RevalueBal:int = obj["Rpt3RevalueBal"]
      """  Reporting currency Invoice Balance at the time of revaluation  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
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
      self.AdjLegalNumber:str = obj["AdjLegalNumber"]
      """  Legal Number for the adjustment.  """  
      self.AdjTranDocTypeID:str = obj["AdjTranDocTypeID"]
      """  Transaction Document Type for the adjustment.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.MainSite:bool = obj["MainSite"]
      """  Main Site  """  
      self.SiteCode:str = obj["SiteCode"]
      """  Site Code  """  
      self.BranchID:str = obj["BranchID"]
      """  Branch ID  """  
      self.InvoiceDate:str = obj["InvoiceDate"]
      """  Invoice Date  """  
      self.Remarks:str = obj["Remarks"]
      """  Remarks  """  
      self.AssetTypeCode:str = obj["AssetTypeCode"]
      """  Asset Type Code  """  
      self.Cash:bool = obj["Cash"]
      """  Cash  """  
      self.CreditCard:bool = obj["CreditCard"]
      """  Credit Card  """  
      self.Normal:bool = obj["Normal"]
      """  Normal  """  
      self.CardID:str = obj["CardID"]
      """  Card ID  """  
      self.CardHolderTaxID:str = obj["CardHolderTaxID"]
      """  Card Holder Tax ID  """  
      self.CardMemberName:str = obj["CardMemberName"]
      """  Card Member Name  """  
      self.Excluded:bool = obj["Excluded"]
      """  Excluded  """  
      self.Deferred:bool = obj["Deferred"]
      """  Deferred  """  
      self.NonDeductAmt:int = obj["NonDeductAmt"]
      """  Non Deductable Amount  """  
      self.NonDeductDocAmt:int = obj["NonDeductDocAmt"]
      """  Non Deductable Doc Amount  """  
      self.NonDeductRpt1Amt:int = obj["NonDeductRpt1Amt"]
      """  Non Deductable Rpt1 Amount  """  
      self.NonDeductRpt2Amt:int = obj["NonDeductRpt2Amt"]
      """  Non Deductable Rpt2 Amount  """  
      self.NonDeductRpt3Amt:int = obj["NonDeductRpt3Amt"]
      """  Non Deductable Rpt3 Amount  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UrgentPayment:bool = obj["UrgentPayment"]
      """  UrgentPayment  """  
      self.InvoiceRef:str = obj["InvoiceRef"]
      """  InvoiceRef  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code for transactions of type ADJ  """  
      self.CNCFICode:str = obj["CNCFICode"]
      """  CNCFICode  """  
      self.Gen1099Date:str = obj["Gen1099Date"]
      """  Generation 1099 Date  """  
      self.NOTranReason:str = obj["NOTranReason"]
      """  NOTranReason  """  
      self.PEIsDetractionPayment:bool = obj["PEIsDetractionPayment"]
      """  PEIsDetractionPayment  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  Code1099ID  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.DocWhManAddAmt:int = obj["DocWhManAddAmt"]
      """  DocWhManAddAmt  """  
      self.WhManAddAmt:int = obj["WhManAddAmt"]
      """  WhManAddAmt  """  
      self.Rpt1WhManAddAmt:int = obj["Rpt1WhManAddAmt"]
      """  Rpt1WhManAddAmt  """  
      self.Rpt2WhManAddAmt:int = obj["Rpt2WhManAddAmt"]
      """  Rpt2WhManAddAmt  """  
      self.Rpt3WhManAddAmt:int = obj["Rpt3WhManAddAmt"]
      """  Rpt3WhManAddAmt  """  
      self.CheckAccess:bool = obj["CheckAccess"]
      """  True if user has security to see Check Payment Details  """  
      self.CPayBalance:int = obj["CPayBalance"]
      """  The latest invoice balance of the CPay invoice.  """  
      self.CPayCheckDate:str = obj["CPayCheckDate"]
      """  The reference Check Date of the latest payment made by the Corporate for the CPay invoice.  """  
      self.CPayCheckNum:int = obj["CPayCheckNum"]
      """  The reference Check number paid by the Corporate for the CPay invoice.  """  
      self.CPayDocBalance:int = obj["CPayDocBalance"]
      """  The latest invoice balance (in Vendor currrency) of the CPay invoice.  """  
      self.CPayIMReceived:bool = obj["CPayIMReceived"]
      """  Flag to indicate if the CPay invoice got created successfully at the corporate.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyID:str = obj["CurrencyID"]
      self.CurrName:str = obj["CurrName"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DocumentDesc:str = obj["DocumentDesc"]
      self.InvCurrSymbol:str = obj["InvCurrSymbol"]
      """  Invoice Currency Symbol  """  
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceDiscount:int = obj["InvoiceDiscount"]
      self.InvType:str = obj["InvType"]
      """  Either Debit Memo or Invoice or blank  """  
      self.TranDesc:str = obj["TranDesc"]
      """  TranType Description  """  
      self.BOEInvoiceNum:str = obj["BOEInvoiceNum"]
      """  (CSF Peru) Bill of Exchange Invoice Number  """  
      self.CheckAmt:int = obj["CheckAmt"]
      self.NettingID:int = obj["NettingID"]
      """  Id of the netting transaction that generated this document.  """  
      self.PayingSiteCode:str = obj["PayingSiteCode"]
      """  Site Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorName:str = obj["VendorName"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorBankBankName:str = obj["VendorBankBankName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APTranSearchTableset:
   def __init__(self, obj):
      self.APTranSearch:list[Erp_Tablesets_APTranSearchRow] = obj["APTranSearch"]
      self.PaymentTotals:list[Erp_Tablesets_PaymentTotalsRow] = obj["PaymentTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PaymentTotalsRow:
   def __init__(self, obj):
      self.CashRcv:int = obj["CashRcv"]
      self.DocCashRcv:int = obj["DocCashRcv"]
      self.DocDscTaken:int = obj["DocDscTaken"]
      self.DocGainReal:int = obj["DocGainReal"]
      self.DocGainUnreal:int = obj["DocGainUnreal"]
      self.DscTaken:int = obj["DscTaken"]
      self.GainReal:int = obj["GainReal"]
      self.GainUnreal:int = obj["GainUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1CashRcv:int = obj["Rpt1CashRcv"]
      self.Rpt1DscTaken:int = obj["Rpt1DscTaken"]
      self.Rpt1GainReal:int = obj["Rpt1GainReal"]
      self.Rpt1GainUnreal:int = obj["Rpt1GainUnreal"]
      self.Rpt2CashRcv:int = obj["Rpt2CashRcv"]
      self.Rpt2DscTaken:int = obj["Rpt2DscTaken"]
      self.Rpt2GainReal:int = obj["Rpt2GainReal"]
      self.Rpt2GainUnreal:int = obj["Rpt2GainUnreal"]
      self.Rpt3CashRcv:int = obj["Rpt3CashRcv"]
      self.Rpt3DscTaken:int = obj["Rpt3DscTaken"]
      self.Rpt3GainReal:int = obj["Rpt3GainReal"]
      self.Rpt3GainUnreal:int = obj["Rpt3GainUnreal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAPTranSearchTableset:
   def __init__(self, obj):
      self.APTranSearch:list[Erp_Tablesets_APTranSearchRow] = obj["APTranSearch"]
      self.PaymentTotals:list[Erp_Tablesets_PaymentTotalsRow] = obj["PaymentTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   headNum
   apTranNo
   invoiceNum
   voided
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.voided:bool = obj["voided"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APTranSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPTranSearch_input:
   """ Required : 
   ds
   headNum
   apTranNo
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APTranSearchTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewAPTranSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APTranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPaymentData_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetPaymentData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
      pass

class GetRowsForPO_input:
   """ Required : 
   whereClauseAPTranSearch
   poNum
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPTranSearch:str = obj["whereClauseAPTranSearch"]
      self.poNum:int = obj["poNum"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForPO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsForReceipt_input:
   """ Required : 
   whereClauseAPTranSearch
   vendorNum
   purPoint
   packSlip
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPTranSearch:str = obj["whereClauseAPTranSearch"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.packSlip:str = obj["packSlip"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsForReceipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPTranSearch
   whereClausePaymentTotals
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPTranSearch:str = obj["whereClauseAPTranSearch"]
      self.whereClausePaymentTotals:str = obj["whereClausePaymentTotals"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
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

class KineticGetRows_input:
   """ Required : 
   whereClauseAPTranSearch
   """  
   def __init__(self, obj):
      self.whereClauseAPTranSearch:str = obj["whereClauseAPTranSearch"]
      pass

class KineticGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APTranSearchTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPTranSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPTranSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APTranSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APTranSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

