import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MaterialQueueSvc
# Description: Here are some brief notes regarding how to accomplish in Sonoma
the features found in the v6.10 Vantage program Material Request Queue.
            
1) The three tab folders each show Material Queue (MtlQueue) records.
1a) The Unselected tab dataset rows can be obtained with a call to
MaterialQueue.GetRows(), whereClauseMtlQueue = 'ttMtlQueue.SelectedByEmpID = ""'
            
1b) The My Selections tab dataset rows can be obtained with a call to
MaterialQueue.GetRows(), whereClauseMtlQueue = 'ttMtlQueue.SelectedByEmpID = {currentEmpId}'
            
1c) The Others Selections tab dataset rows can be obtained with a call to
MaterialQueue.GetRows(), whereClauseMtlQueue = 'ttMtlQueue.SelectedByEmpID < > ""
and ttMtlQueue.SelectedByEmpID < > {currentEmpId}'
2) The Select button should merely write the currentEmpId into ttMtlQueue.SelectedByEmpID
and then call MaterialQueue.Update().
            
3) The Deselect button should merely clear the ttMtlQueue.SelectedByEmpID and
then call MaterialQueue.Update().
            
4) The Delete button should merely call MaterialQueue.DeleteById().
            
5) The button with the bar-code image on it should call the MtlTag print routine.
I don't know what object and method(s) are involved, but there are many examples
throughout Sonoma.
            
6) The Process button is more complicated.  First, check the value of
ttMtlQueue.OkToProcess.  If that is false, disable the button.
Otherwise, you will need to look to ttMtlQueue.TranType to determine what
application to pop up for user entry:
When ttMtlQueue.TranType is MFG-STK, MFG-WIP or SVG-STK, you need to run
the Receipts From Manufacturing program.
When ttMtlQueue.TranType is anything else, you need to run
the Move Material program.
I think there is substantial work involved in setting up these calls--they
each use different datasets.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MaterialQueues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MaterialQueues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MaterialQueues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues",headers=creds) as resp:
           return await resp.json()

async def post_MaterialQueues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MaterialQueues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MaterialQueues_Company_MtlQueueSeq(Company, MtlQueueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MaterialQueue item
   Description: Calls GetByID to retrieve the MaterialQueue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MaterialQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MaterialQueues_Company_MtlQueueSeq(Company, MtlQueueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MaterialQueue for the service
   Description: Calls UpdateExt to update MaterialQueue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MaterialQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MtlQueueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues(" + Company + "," + MtlQueueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MaterialQueues_Company_MtlQueueSeq(Company, MtlQueueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MaterialQueue item
   Description: Call UpdateExt to delete MaterialQueue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MaterialQueue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MtlQueueSeq: Desc: MtlQueueSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/MaterialQueues(" + Company + "," + MtlQueueSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MtlQueueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMtlQueue, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMtlQueue=" + whereClauseMtlQueue
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(mtlQueueSeq, epicorHeaders = None):
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
   params += "mtlQueueSeq=" + mtlQueueSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AutoSelectTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AutoSelectTransactions
   Description: Retrieve material queue entry by company and by employee.
   OperationID: AutoSelectTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AutoSelectTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoSelectTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlQueueByTranID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlQueueByTranID
   Description: Retrieve material queue entry by company and by mtlQueueSeq.
   OperationID: GetMtlQueueByTranID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueueByTranID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueByTranID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockUnLockMtlQueForEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockUnLockMtlQueForEmpID
   Description: Purpose:     Called by handheld (where Employee ID is entered and available on client)
Notes:
<param name="ipTranStatus">Transaction status</param><param name="ipMtlQueueSeq">Material Queue Sequence</param><param name="ipEmpID">Employee ID</param><param name="ds">The MaterialQueueDataSet.</param>
   OperationID: LockUnLockMtlQueForEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockUnLockMtlQueForEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockUnLockMtlQueForEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockUnLockMtlQue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockUnLockMtlQue
   Description: Purpose:     Called from the full client (where Employee ID has not been entered; must use ID associated with login)
Notes:
<param name="ipTranStatus">Transaction status</param><param name="ipMtlQueueSeq">Material Queue Sequence</param><param name="ds">The MaterialQueueDataSet.</param>
   OperationID: LockUnLockMtlQue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockUnLockMtlQue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockUnLockMtlQue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultFilterSettings(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultFilterSettings
   Description: Returns the PlantConfCtrl filter settings for the current company / plant
   OperationID: GetDefaultFilterSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFilterSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UnlockAutoSelectTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlockAutoSelectTransactions
   Description: UnLockAutoSelectTransactions.
   OperationID: UnlockAutoSelectTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlockAutoSelectTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockAutoSelectTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SortQueueByPriority(epicorHeaders = None):
   """  
   Summary: Invoke method SortQueueByPriority
   Description: Return a flag to know if the records will be sorted by the PlantConfCtrl.SortQueuebyPriority filed
   OperationID: SortQueueByPriority
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SortQueueByPriority_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_VerifyMtlQueueExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyMtlQueueExists
   Description: VerifyMtlQueueExists - Returns true if MtlQueue still exists
   OperationID: VerifyMtlQueueExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyMtlQueueExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyMtlQueueExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsCustom(delimitedFilterString, recordsPerPage, pageNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: GetRowsCustom
   OperationID: Get_GetRowsCustom
      :param delimitedFilterString: Desc: Format is [FieldName]Value~[FieldName]Value~   Required: True   Allow empty value : True
      :param recordsPerPage: Desc: Records per page or 0 for all rows   Required: True
      :param pageNum: Desc: Page number defaults to page 1 if not specified   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "delimitedFilterString=" + delimitedFilterString
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "recordsPerPage=" + recordsPerPage
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageNum=" + pageNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsCustomParams(whereClause, fromDate, toDate, fromWhse, toWhse, tranType, selectedByEmpID, excludeTransStatus, onlySelectedByEmp, onlyUnselected, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomParams
   Description: GetRowsCustomParams
   OperationID: Get_GetRowsCustomParams
      :param whereClause: Desc: Where Clause   Required: True   Allow empty value : True
      :param fromDate: Desc: From Date   Required: True   Allow empty value : True
      :param toDate: Desc: To Date   Required: True   Allow empty value : True
      :param fromWhse: Desc: From Warehouse   Required: True   Allow empty value : True
      :param toWhse: Desc: To Warehouse   Required: True   Allow empty value : True
      :param tranType: Desc: TranType   Required: True   Allow empty value : True
      :param selectedByEmpID: Desc: Select by emp ID   Required: True   Allow empty value : True
      :param excludeTransStatus: Desc: Exclude tran status   Required: True   Allow empty value : True
      :param onlySelectedByEmp: Desc: Only return rows selected by employee   Required: True
      :param onlyUnselected: Desc: Only sreturn rows not selected by any employee   Required: True
      :param pageSize: Desc: Page Size   Required: True
      :param absolutePage: Desc: Absolute Page   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomParams_output
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
   params += "fromDate=" + fromDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "toDate=" + toDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fromWhse=" + fromWhse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "toWhse=" + toWhse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranType=" + tranType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "selectedByEmpID=" + selectedByEmpID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "excludeTransStatus=" + excludeTransStatus
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "onlySelectedByEmp=" + onlySelectedByEmp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "onlyUnselected=" + onlyUnselected
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPCIDPrintParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPCIDPrintParams
   Description: GetPCIDPrintParams - returns the number of labels, and report style information for the mtl queue PCID print
   OperationID: GetPCIDPrintParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCIDPrintParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCIDPrintParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPkgControlIDGenParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlIDGenParams
   OperationID: GetPkgControlIDGenParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlIDGenParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlIDGenParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetParametersForMtlTags(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetParametersForMtlTags
   Description: Returns the string required to call the Print Mtl Tags UI
   OperationID: GetParametersForMtlTags
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParametersForMtlTags_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParametersForMtlTags_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedMtlQueueList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedMtlQueueList
   Description: Returns a delimited list of selected material queue records
   OperationID: GetSelectedMtlQueueList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedMtlQueueList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedMtlQueueList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDeleteConfirmationMessage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeleteConfirmationMessage
   Description: Returns a delete message that includes the list of MtlQueue records to be deleted
   OperationID: GetDeleteConfirmationMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeleteConfirmationMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeleteConfirmationMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultToDate(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultToDate
   Description: Returns the default to date
   OperationID: GetDefaultToDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultToDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewMtlQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMtlQueue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MaterialQueueSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MtlQueueListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MtlQueueRow] = obj["value"]
      pass

class Erp_Tablesets_MtlQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
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
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AutoSelectTransactions_input:
   """ Required : 
   ipEmpID
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee ID  """  
      pass

class AutoSelectTransactions_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   mtlQueueSeq
   """  
   def __init__(self, obj):
      self.mtlQueueSeq:int = obj["mtlQueueSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MaterialQueueTableset:
   def __init__(self, obj):
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MtlQueueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
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
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      """  Warehouse Group Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MtlQueueListTableset:
   def __init__(self, obj):
      self.MtlQueueList:list[Erp_Tablesets_MtlQueueListRow] = obj["MtlQueueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MtlQueueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time(seconds since midnight) when transaction was created.  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  Number assigned by the system to uniquely identify the record.  Created by using the database sequence "MtlQueueSeq".  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of item in the container.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity  """  
      self.TranType:str = obj["TranType"]
      """   Internal flag to indicate the type of transaction that this request is for.  This will control which functions are invoked for processing.
The same codes as in PartTran are used.  However, there are some additional codes also. 
They are; GET-WIP,  RTN-WIP, RTN-MTL, PUT-MTL, PUT-WIP, PICK-SO, PICK-JOB, PICK-TFO, BIN-REPLENISH, BIN-CONSOLIDATE, PICK-SO-XDOCK, PICK-JOB-XDOCK, PICK-TFO-XDOCK  """  
      self.ReferencePrefix:str = obj["ReferencePrefix"]
      """   Used as a translatable prefix for the Reference field.
For example for a purchase receipt of stock it has "PS", (Packing Slip). For display purposes this is field is translated, then concatenated with the value in the Refernce field. 
Other values are "Job",  """  
      self.Reference:str = obj["Reference"]
      """  Contains a reference about the request. May contain Job/Asm/Seq, WrkCtr,  Packing Slip #,  Sales Order, etc...depending on the TranType.  """  
      self.RequestedByEmpID:str = obj["RequestedByEmpID"]
      """  Employee ID that made the request.  """  
      self.SelectedByEmpID:str = obj["SelectedByEmpID"]
      """  Employee ID that has selected this record from the queue for processing.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that the request is related to.  This allows sorting by Job, which provides the user a method of working on all the requests for a specific job.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Job Assembly Sequence.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl)  or "O" = Job Operation (JobOper).  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of the related specific material or operation record.  For WIP parts it's the operation sequence that created the part. For raw materials it's the related JobMtl.MtlSeq.  """  
      self.FromWhse:str = obj["FromWhse"]
      """  Warehouse Code where item is to be found. For example a Get Raw Material request of a stocked part  would be the warehouse  the requirement was allocated against (JobMtl.WareHouseCode).  A "Move of a WIP part" will contain the Warehouse defined by the WrkCenter.PutWhse...  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  Warehouse bin where item is to be found. For example a Get Raw Material request of a stocked part  would be the Primary Bin of the part/warehouse, if no primary bin, then the first Bin in the warehouse which contains this part, else blank.  A "Move of a WIP part" will contain the bin defined by the WrkCenter.PutBin...  """  
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse where item should be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputWhse).  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Warehouse bin where item is to be moved to. For example, on a Get Raw Material request  it would be the "input" warehouse of the workcenter on the operation to which the material is related (WrkCenter.InputBin).  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      """  Assembly sequence of the operation that completed quantity of the job operation  will be moved to.  """  
      self.NextJobSeq:int = obj["NextJobSeq"]
      """  Sequence of the operation that completed quantity of the job operation will be moved to.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the this request is needed by.  Defaults, to current system date.  """  
      self.NeedByTime:int = obj["NeedByTime"]
      """  Time (seconds since midnight) that request is need by.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor number of the related purchase receipt (RcvDtl).  Company,VendorNum, PurPoint, PackSlip,Packline are used to provide the link to the related RcvDtl record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point id of the related purchase receipt (RcvDtl).  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip # of the related RcvDtl.  """  
      self.PackLine:int = obj["PackLine"]
      """  Vendors Packing Slip line  # of the related RcvDtl.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   Order number job is making parts for. (See JobProd.OrderNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

OrderNum pertains only to "make to order" requirements.  
Provides relationship to the JobProd for "make to order" requirements.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Related Sales order line number.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Related sales order release number.  """  
      self.TargetJobNum:str = obj["TargetJobNum"]
      """   Job that this job is making parts for. (See JobProd.TargetJobNum).
A job can have 3 types of production demand requirement;
 1. Make to Order
 2. Make to Job
 3. Make to Stock.
As job complete quantity is reported the system suggests where it should be moved to.
It does this in the following order;
 1. Shipping area for make to order requirements
 2. Staging area of related operatations work center for make to job requirements
 3. Warehouse for make to stock requirements. 

TargetJobNum pertains only to "make to job" requirements.  
Provides relationship to the JobProd for "make to Job" requirements.  """  
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      """  Assembly Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      """  Material Sequence of the JobMtl record that is making the production demand. (See "TargetJobNum")  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  A description of the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Internal unit of measure.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order # that the receipt is for. Only applicable for receipt of Purchase Order transactions.  """  
      self.POLine:int = obj["POLine"]
      """  The PO line # which is being received. Only applicable for PO receipt transactions.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # which is being received.  """  
      self.Visible:bool = obj["Visible"]
      """  Indicates if this MtlQueue is visible to the user on the Material Queue browse.  Set based on the users response to make a "move  request" when reporting quantities.  Set to true visible), if a move request is made.  This was implemented to keep track of labor quantity reported without making a move request.  The move request will then reflect the total quantity to move instead of what was reported on the labor transaction that requested the move.  Regardless of making a "Move Request" labor quantity reporting always creates/updates a MtlQueue record.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMAReceipt number of the related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMADisp number of the related RMADisp record.  """  
      self.NCTranID:int = obj["NCTranID"]
      """  The related NonConf.TranID number. Used to link the MtlQueue table to the NonConf table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the part.  """  
      self.Lock:bool = obj["Lock"]
      """  Indicates this record has been locked by a Advanced Shipping user and is not available for processing by any other user.  """  
      self.QueueID:str = obj["QueueID"]
      """  Used by Advanced Shipping to designate which queue this record is in.  Advanced Shipping queues can prioritize and process records.  """  
      self.QueuePickSeq:int = obj["QueuePickSeq"]
      """  Sequence of this record within an Advanced Shipping Queue.  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  This is an internal sequence number for grouping MtlQueue records.  """  
      self.WhseGroupCode:str = obj["WhseGroupCode"]
      """  Warehouse Group that was assigned to this transaction.  """  
      self.TranStatus:str = obj["TranStatus"]
      """   The status of the transaction of the material.  Valid values:
MGMT-LOCK - Manager locked, RELEASED - Released, HOLD - On Hold, USER-LOCK - Locked for a user, ORDER-HOLD - On Hold for Order Based Picking, QUALITY-HOLD - On Hold for Quality Control, and PICK-PACK - Three step allocation Pick-Pack Method  """  
      self.WaveNum:int = obj["WaveNum"]
      """  The Wave that was assigned during the allocation process.  """  
      self.Priority:int = obj["Priority"]
      """  Transaction Priority.  Valid values are 1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.TranSource:str = obj["TranSource"]
      """  Transaction Source  """  
      self.LastMgrChangeEmpID:str = obj["LastMgrChangeEmpID"]
      """  When the TranStatus, AssignedToEmpID or Priority are modified, this value is updated with the ID of the Manager making the change.  """  
      self.AssignedToEmpID:str = obj["AssignedToEmpID"]
      """  Employee ID that was selected by the Warehouse Manager to process record from the queue.  """  
      self.TargetTFOrdNum:str = obj["TargetTFOrdNum"]
      """  Transfer Order for which Demand is being satisfied.  """  
      self.TargetTFOrdLine:int = obj["TargetTFOrdLine"]
      """  Transfer Order Line for which Demand is being satisfied.  """  
      self.PackStation:str = obj["PackStation"]
      """  Unique identifier of the WorkStations.  Valid values are existing Work Stations that are setup as a Pack Station.  """  
      self.DistributionType:str = obj["DistributionType"]
      """  Distribution Type.  Valid values:  PICKPACK or HANDHELD.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.LastUsedPCID:str = obj["LastUsedPCID"]
      """  Last Used PCID on the selected line.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  The PCID from which the material movement will occur.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  The PCID to which the material movement will occur.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      """  AttributeValueSeq  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.CustID:str = obj["CustID"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.DisableTO:bool = obj["DisableTO"]
      """  Indicates whether Transfer Order Selector Flag should be disabled.  """  
      self.FromInv:bool = obj["FromInv"]
      """  From Inventory Selector Flag  """  
      self.FromJob:bool = obj["FromJob"]
      """  From Manufacturing Selector Flag  """  
      self.FromPO:bool = obj["FromPO"]
      """  From Purchasing Selector Flag  """  
      self.FromTO:bool = obj["FromTO"]
      """  From Transfer Order Selector Flag  """  
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FSAServiceOrderNumber:int = obj["FSAServiceOrderNumber"]
      """  Service Order Number from FSA. Only available in FSA Request Workbench.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource Num from FSA. Only available in FSA Request Workbench.  """  
      self.HoldStatus:bool = obj["HoldStatus"]
      self.LeadTime:int = obj["LeadTime"]
      self.MaxMfgLotSize:int = obj["MaxMfgLotSize"]
      self.MfgLeadTime:int = obj["MfgLeadTime"]
      self.MinMfgLotSize:int = obj["MinMfgLotSize"]
      self.NeedByTimeDisp:str = obj["NeedByTimeDisp"]
      self.NonStock:bool = obj["NonStock"]
      self.OkToProcess:bool = obj["OkToProcess"]
      """  Holds the result of checking sub-menu security.  NO indicates the current user does not have permission to carry out the indicated TranType.  """  
      self.OnHandQtySite:int = obj["OnHandQtySite"]
      self.OnHandQtyWhse:int = obj["OnHandQtyWhse"]
      self.PlantName:str = obj["PlantName"]
      self.PrimWhseCode:str = obj["PrimWhseCode"]
      self.PrimWhseDesc:str = obj["PrimWhseDesc"]
      self.RequestedByEmpName:str = obj["RequestedByEmpName"]
      self.RequestError:bool = obj["RequestError"]
      """  Indicates whether an error occured in processing.  """  
      self.RequestMsg:str = obj["RequestMsg"]
      """  Message used to return status information after processing.  """  
      self.SameWhseGroupEmp:bool = obj["SameWhseGroupEmp"]
      """  Is this material queue row part of the employees warehouse group  """  
      self.SelectedByEmpName:str = obj["SelectedByEmpName"]
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  Used by user to select rows for mass processing  """  
      self.ShipToCity:str = obj["ShipToCity"]
      self.ShipToCountry:str = obj["ShipToCountry"]
      self.ShipToName:str = obj["ShipToName"]
      """  Customer Ship To Name  """  
      self.ShipToNum:str = obj["ShipToNum"]
      self.ShipToState:str = obj["ShipToState"]
      self.ShipToZIP:str = obj["ShipToZIP"]
      self.SortByPriority:int = obj["SortByPriority"]
      """  Sort priority from highest to lowest (1,2,3,4,5,6,7,8,9,0)  """  
      self.SourceTypeDesc:str = obj["SourceTypeDesc"]
      """  Transfer, Sales Kit, Manufactured or Purchased.  """  
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.TransferLeadTime:int = obj["TransferLeadTime"]
      self.TransferPlant:str = obj["TransferPlant"]
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """  Readable tran type (used in Replenishment Workbench)  """  
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.WaveRelated:bool = obj["WaveRelated"]
      """  Value is true if this mtlqueue record is related to a wave. False if it is not.  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  Customer Sales Territory Region Code  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumVendorID_:str = obj["VendorNumVendorID_"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName_:str = obj["VendorNumName_"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.WarehouseGroupCodeWhseGroupDesc:str = obj["WarehouseGroupCodeWhseGroupDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlIDGeneratorRow:
   def __init__(self, obj):
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """   This field will be like the field on the PCID Generate screen that is called from the Material Queue STK-SHP transaction.  The search button will allow searching & Selecting an Active Package Control ID Configuration having Label Print Controlled = False.
When a value is entered or selected, if the Package Code field is empty then the Package Code field should get populated with the Package Code on the selected control ID configuration  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package code  """  
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  Package code description  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.NumberToGenerate:int = obj["NumberToGenerate"]
      self.TypeDescription:str = obj["TypeDescription"]
      self.PrintName:str = obj["PrintName"]
      """  Printer name  """  
      self.Description:str = obj["Description"]
      self.NumberOfLabelsToPrint:int = obj["NumberOfLabelsToPrint"]
      self.PrinterID:str = obj["PrinterID"]
      self.GenerateStagePCIDs:bool = obj["GenerateStagePCIDs"]
      self.CheckAllowMixedParts:bool = obj["CheckAllowMixedParts"]
      self.CheckAllowMixedUOMs:bool = obj["CheckAllowMixedUOMs"]
      self.CheckAllowMixedLots:bool = obj["CheckAllowMixedLots"]
      self.CheckAllowMultipleSerialNumsPerPCID:bool = obj["CheckAllowMultipleSerialNumsPerPCID"]
      self.PrintLabels:bool = obj["PrintLabels"]
      self.PkgControlType:str = obj["PkgControlType"]
      self.PartNum:str = obj["PartNum"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   pulated with all the Warehouses owned or shared with the current site.  The Search will allow searching & selecting any Warehouse owned or shared with the current site.  Users can also enter a Warehouse ID
When a Warehouse is Entered/Selected, the Printer field should be populated with the Default Printer for the Warehouse  """  
      self.HHForm:bool = obj["HHForm"]
      self.PCIDSGenerated:str = obj["PCIDSGenerated"]
      self.DisableScreen:bool = obj["DisableScreen"]
      self.Plant:str = obj["Plant"]
      self.DisableWarehouse:bool = obj["DisableWarehouse"]
      """  Disable Warehouse in the PCID Generator screen if true as sometimes we require to pass in and force the warehouse to not be modified,  """  
      self.SuppressPrintLabels:bool = obj["SuppressPrintLabels"]
      self.DisableNumberToGenerate:bool = obj["DisableNumberToGenerate"]
      self.StyleNum:int = obj["StyleNum"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.DisableNumLblsRptStyle:bool = obj["DisableNumLblsRptStyle"]
      self.PkgControlOutboundContainer:bool = obj["PkgControlOutboundContainer"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlIDGeneratorTableset:
   def __init__(self, obj):
      self.PkgControlIDGenerator:list[Erp_Tablesets_PkgControlIDGeneratorRow] = obj["PkgControlIDGenerator"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtMaterialQueueTableset:
   def __init__(self, obj):
      self.MtlQueue:list[Erp_Tablesets_MtlQueueRow] = obj["MtlQueue"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   mtlQueueSeq
   """  
   def __init__(self, obj):
      self.mtlQueueSeq:int = obj["mtlQueueSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
      pass

class GetDefaultFilterSettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mtlQueueMaxRowsToReturn:int = obj["parameters"]
      self.mtlQueueEndDaysOffset:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultToDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultToDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDeleteConfirmationMessage_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

class GetDeleteConfirmationMessage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      self.deleteConfirmationMessage:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_MtlQueueListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMtlQueueByTranID_input:
   """ Required : 
   ipMtlQueueSeq
   """  
   def __init__(self, obj):
      self.ipMtlQueueSeq:str = obj["ipMtlQueueSeq"]
      """  Material Queue Sequence  """  
      pass

class GetMtlQueueByTranID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
      pass

class GetNewMtlQueue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

class GetNewMtlQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPCIDPrintParams_input:
   """ Required : 
   ipCompany
   ipPartNum
   ipPCID
   ipOrderNum
   ipOrderLine
   ipOrderRelNum
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      """  input company  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  input part number  """  
      self.ipPCID:str = obj["ipPCID"]
      """  input pcid  """  
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  input order number  """  
      self.ipOrderLine:int = obj["ipOrderLine"]
      """  input order line  """  
      self.ipOrderRelNum:int = obj["ipOrderRelNum"]
      """  input order line  """  
      pass

class GetPCIDPrintParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNumLabelsToPrint:int = obj["parameters"]
      self.opPromptForReportStyle:bool = obj["opPromptForReportStyle"]
      self.opStyleNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetParametersForMtlTags_input:
   """ Required : 
   mtlQueueSysRowID
   """  
   def __init__(self, obj):
      self.mtlQueueSysRowID:str = obj["mtlQueueSysRowID"]
      pass

class GetParametersForMtlTags_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mtlTagParameter:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPkgControlIDGenParams_input:
   """ Required : 
   pkgControlIDCode
   partNum
   warehouseCode
   isHHForm
   """  
   def __init__(self, obj):
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.isHHForm:bool = obj["isHHForm"]
      pass

class GetPkgControlIDGenParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDGeneratorTableset] = obj["returnObj"]
      pass

class GetRowsCustomParams_input:
   """ Required : 
   whereClause
   fromDate
   toDate
   fromWhse
   toWhse
   tranType
   selectedByEmpID
   excludeTransStatus
   onlySelectedByEmp
   onlyUnselected
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where Clause  """  
      self.fromDate:str = obj["fromDate"]
      """  From Date  """  
      self.toDate:str = obj["toDate"]
      """  To Date  """  
      self.fromWhse:str = obj["fromWhse"]
      """  From Warehouse  """  
      self.toWhse:str = obj["toWhse"]
      """  To Warehouse  """  
      self.tranType:str = obj["tranType"]
      """  TranType  """  
      self.selectedByEmpID:str = obj["selectedByEmpID"]
      """  Select by emp ID  """  
      self.excludeTransStatus:str = obj["excludeTransStatus"]
      """  Exclude tran status  """  
      self.onlySelectedByEmp:bool = obj["onlySelectedByEmp"]
      """  Only return rows selected by employee  """  
      self.onlyUnselected:bool = obj["onlyUnselected"]
      """  Only sreturn rows not selected by any employee  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute Page  """  
      pass

class GetRowsCustomParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   delimitedFilterString
   recordsPerPage
   pageNum
   """  
   def __init__(self, obj):
      self.delimitedFilterString:str = obj["delimitedFilterString"]
      """  Format is [FieldName]Value~[FieldName]Value~  """  
      self.recordsPerPage:int = obj["recordsPerPage"]
      """  Records per page or 0 for all rows  """  
      self.pageNum:int = obj["pageNum"]
      """  Page number defaults to page 1 if not specified  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.rowCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMtlQueue
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMtlQueue:str = obj["whereClauseMtlQueue"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MaterialQueueTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectedMtlQueueList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

class GetSelectedMtlQueueList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      self.mtlQueueSelectedList:str = obj["parameters"]
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

class LockUnLockMtlQueForEmpID_input:
   """ Required : 
   ipTranStatus
   ipMtlQueueSeq
   ipEmpID
   ds
   """  
   def __init__(self, obj):
      self.ipTranStatus:str = obj["ipTranStatus"]
      self.ipMtlQueueSeq:int = obj["ipMtlQueueSeq"]
      self.ipEmpID:str = obj["ipEmpID"]
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

class LockUnLockMtlQueForEmpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LockUnLockMtlQue_input:
   """ Required : 
   ipTranStatus
   ipMtlQueueSeq
   ds
   """  
   def __init__(self, obj):
      self.ipTranStatus:str = obj["ipTranStatus"]
      self.ipMtlQueueSeq:int = obj["ipMtlQueueSeq"]
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

class LockUnLockMtlQue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SortQueueByPriority_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  QueuePriority  """  
      pass

class UnlockAutoSelectTransactions_input:
   """ Required : 
   ipEmpID
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee ID  """  
      pass

class UnlockAutoSelectTransactions_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMaterialQueueTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMaterialQueueTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MaterialQueueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VerifyMtlQueueExists_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class VerifyMtlQueueExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

