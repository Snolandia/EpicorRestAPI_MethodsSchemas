import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ApplyDebitMemoSvc
# Description: Apply Debit Memo entry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ApplyDebitMemoes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ApplyDebitMemoes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ApplyDebitMemoes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CheckHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes",headers=creds) as resp:
           return await resp.json()

async def post_ApplyDebitMemoes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ApplyDebitMemoes
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ApplyDebitMemoes_Company_HeadNum(Company, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ApplyDebitMemo item
   Description: Calls GetByID to retrieve the ApplyDebitMemo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ApplyDebitMemo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ApplyDebitMemoes_Company_HeadNum(Company, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ApplyDebitMemo for the service
   Description: Calls UpdateExt to update ApplyDebitMemo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ApplyDebitMemo
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ApplyDebitMemoes_Company_HeadNum(Company, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ApplyDebitMemo item
   Description: Call UpdateExt to delete ApplyDebitMemo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ApplyDebitMemo
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ApplyDebitMemoes_Company_HeadNum_APTrans(Company, HeadNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")/APTrans",headers=creds) as resp:
           return await resp.json()

async def get_ApplyDebitMemoes_Company_HeadNum_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTran item
   Description: Calls GetByID to retrieve the APTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTran1
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/ApplyDebitMemoes(" + Company + "," + HeadNum + ")/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def get_APTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans",headers=creds) as resp:
           return await resp.json()

async def post_APTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APTran item
   Description: Calls GetByID to retrieve the APTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APTran
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APTran for the service
   Description: Calls UpdateExt to update APTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param APTranNo: Desc: APTranNo   Required: True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param Voided: Desc: Voided   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APTrans_Company_HeadNum_APTranNo_InvoiceNum_Voided(Company, HeadNum, APTranNo, InvoiceNum, Voided, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APTran item
   Description: Call UpdateExt to delete APTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APTran
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/APTrans(" + Company + "," + HeadNum + "," + APTranNo + "," + InvoiceNum + "," + Voided + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCheckHed, whereClauseAPTran, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPTran=" + whereClauseAPTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ApplyDebitMemo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method _ApplyDebitMemo
   Description: This method needs to be run as the last method as the user leaves the CheckHed record.
It validates that the entire memo has been applied and creates the required GL records
If the entire memo has not been applied, then an exception will be raised and the user
cannot leave the record until it all has been applied.
   OperationID: _ApplyDebitMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/_ApplyDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_ApplyDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BeforeApplyDebitMemo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BeforeApplyDebitMemo
   Description: Method performs actions needed before sending the CheckHed to the posting engine
Checks Withholding Taxes
Creates additional APTran records
Performs Tax Calculation and Allocation
This method does not call the posting engine
   OperationID: BeforeApplyDebitMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BeforeApplyDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeApplyDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAmtToApply(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAmtToApply
   Description: This method is used to validate/update the dataset when the DocPaymentTotal is udpated
   OperationID: ChangeAmtToApply
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAmtToApply_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAmtToApply_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlInvoice
   Description: This method is called when the APTran InvoiceNum field is modified
   OperationID: ChangeDtlInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckExchangeRate
   Description: This method is called when the APTran InvoiceNum field is modified
   OperationID: CheckExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDtlTranAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDtlTranAmt
   Description: This method is run when the DocTranAmt field is modified
   OperationID: ChangeDtlTranAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDtlTranAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDtlTranAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeHedInvoice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeHedInvoice
   Description: This method is used when no Invoice Number is specified in the GetNewCheckHedInv function
This will validate the invoice number provided and if valid, will default CheckHed fields
to the values in the Invoice
   OperationID: ChangeHedInvoice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeHedInvoice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeHedInvoice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTranDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTranDate
   Description: This method is run when the Transaction date is changed to update the fiscal period fields
   OperationID: ChangeTranDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendor
   Description: Call this method when the user enters the ttCheckHed.VendorID
   OperationID: ChangeVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOnScreenLoad(epicorHeaders = None):
   """  
   Summary: Invoke method CheckOnScreenLoad
   Description: This method is called first thing when opening the screen.  It checks to see if
the G/L is interfaced and if the Fiscal Period is valid.  If the G/L is not interfaced,
a question asking if the user wants to continue will be returned.  If the user answers no,
then they are returned to the main menu.  If the Fiscal Period is invalid, an exception
will be raised and the user should be returned to the main menu.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckPrevApplication(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPrevApplication
   Description: This method is used when no Invoice Number is specified in the GetNewCheckHedInv function
This will validate the invoice number provided and if valid, will default CheckHed fields
to the values in the Invoice
   OperationID: CheckPrevApplication
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPrevApplication_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPrevApplication_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteCheckDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteCheckDetails
   Description: This method needs to be run as the last method if the user chooses not to
Apply Debit Memo but wants to leave the CheckHed record to create a new one
or closes/exits the ApplyDebitMemo UI screen.
This will delete the appropriate CheckHed and APTran records and update the
related APInvHed to reflect the appropriate invoice balance.
   OperationID: DeleteCheckDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteCheckDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCheckDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCheckHedInv(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCheckHedInv
   Description: This method replaces the standard GetNewCheckHed method.  Requires a Debit Memo Invoice
   OperationID: GetNewCheckHedInv
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCheckHedInv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCheckHedInv_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetReadyToCalc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReadyToCalc
   Description: Purpose: CALCULATE VANTAGE\TAX CONNECT TAX CALCULATIONS
UI NEEDS TO CALL A SAVE BEFORE CALLING THIS PROCEDURE
Parameters:  none
Notes:
<param name="ipHeadNum">ipHeadNum </param><param name="ipAPTranNo">ipAPTranNo </param><param name="ipCalcAll">ipCalcAll</param><param name="ds">ApplyDebitMemo dataset</param>
   OperationID: SetReadyToCalc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReadyToCalc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReadyToCalc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ApplyDebitMemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APTranRow] = obj["value"]
      pass

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

class Erp_Tablesets_APTranRow:
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
      self.BaseAdjustAmt:int = obj["BaseAdjustAmt"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseSelfAssessedTax:int = obj["BaseSelfAssessedTax"]
      self.ChangeExchangeRateResponse:str = obj["ChangeExchangeRateResponse"]
      """  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CopyRate:bool = obj["CopyRate"]
      """  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  The flag to indicate if this payment line is realted to Correction invoice with negative amount  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyGainLoss:int = obj["CurrencyGainLoss"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from APInvHed  """  
      self.CurrSymbolCurrDesc:str = obj["CurrSymbolCurrDesc"]
      self.CurrSymbolCurrName:str = obj["CurrSymbolCurrName"]
      self.CurrSymbolCurrSymbol:str = obj["CurrSymbolCurrSymbol"]
      self.CurrSymbolDocumentDesc:str = obj["CurrSymbolDocumentDesc"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DiscountAvailable:bool = obj["DiscountAvailable"]
      self.DiscountDate:str = obj["DiscountDate"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  The display gl account.  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocBaseSelfAssessedTax:int = obj["DocBaseSelfAssessedTax"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocExpenseAmount:int = obj["DocExpenseAmount"]
      self.DocGainLossAmt:int = obj["DocGainLossAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.DocNetAmount:int = obj["DocNetAmount"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.DocSelfAssessedTax:int = obj["DocSelfAssessedTax"]
      self.DocUnPostedBal:int = obj["DocUnPostedBal"]
      self.DocWithHoldTax:int = obj["DocWithHoldTax"]
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then Copy Rate checkbox is Read Only  """  
      self.DueDate:str = obj["DueDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.ExpenseAmount:int = obj["ExpenseAmount"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.GroupID:str = obj["GroupID"]
      self.InitUrgentPayment:bool = obj["InitUrgentPayment"]
      """  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  """  
      self.InvExchangeRate:int = obj["InvExchangeRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.isDiscountforDebitM:bool = obj["isDiscountforDebitM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.LockRate:bool = obj["LockRate"]
      self.MiscPayment:bool = obj["MiscPayment"]
      self.NetAmount:int = obj["NetAmount"]
      self.NewBalance:int = obj["NewBalance"]
      self.PaymentDesc:str = obj["PaymentDesc"]
      """  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Print 1099  """  
      self.RateGroupDescription:str = obj["RateGroupDescription"]
      self.RefCodeEnabled:bool = obj["RefCodeEnabled"]
      self.RefCodeList:str = obj["RefCodeList"]
      """  Delimited list of possible Ref codes.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoice balance before adjustment in Rpt1 currency  """  
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoice balance before adjustment in Rpt2 currency  """  
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Report balance before adjustment in rpt3 currency  """  
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.SelfAssessedTax:int = obj["SelfAssessedTax"]
      self.TaxableTransaction:bool = obj["TaxableTransaction"]
      """  Indicates if tax records are created and posted for AP Invoice adjustment  """  
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UnPostedBal:int = obj["UnPostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.WithHoldTax:int = obj["WithHoldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AmtToAP:int = obj["AmtToAP"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.InvoiceLegalNumber:str = obj["InvoiceLegalNumber"]
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      self.isPrecalcTax:bool = obj["isPrecalcTax"]
      """  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  """  
      self.PrepayApld:bool = obj["PrepayApld"]
      """  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      """  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class BeforeApplyDebitMemo_input:
   """ Required : 
   inHeadNum
   """  
   def __init__(self, obj):
      self.inHeadNum:int = obj["inHeadNum"]
      """  CheckHead.HeadNum  """  
      pass

class BeforeApplyDebitMemo_output:
   def __init__(self, obj):
      pass

class ChangeAmtToApply_input:
   """ Required : 
   paymentAmt
   ds
   """  
   def __init__(self, obj):
      self.paymentAmt:int = obj["paymentAmt"]
      """  Proposed value change to the DocPaymentTotal field  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class ChangeAmtToApply_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlInvoice_input:
   """ Required : 
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:str = obj["invoiceNum"]
      """  Proposed Invoice Number  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class ChangeDtlInvoice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDtlTranAmt_input:
   """ Required : 
   docTranAmt
   ds
   """  
   def __init__(self, obj):
      self.docTranAmt:int = obj["docTranAmt"]
      """  Proposed amount  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class ChangeDtlTranAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeHedInvoice_input:
   """ Required : 
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.invoiceNum:str = obj["invoiceNum"]
      """  proposed Invoice Number  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class ChangeHedInvoice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTranDate_input:
   """ Required : 
   tranDate
   ds
   """  
   def __init__(self, obj):
      self.tranDate:str = obj["tranDate"]
      """  Proposed Transaction Date  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class ChangeTranDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendor_input:
   """ Required : 
   pcVendorID
   ds
   """  
   def __init__(self, obj):
      self.pcVendorID:str = obj["pcVendorID"]
      """  Vendor ID - character code for Vendor  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class ChangeVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckDocumentIsLocked_input:
   """ Required : 
   keyValue1
   keyValue2
   """  
   def __init__(self, obj):
      self.keyValue1:str = obj["keyValue1"]
      """  VendorNum  """  
      self.keyValue2:str = obj["keyValue2"]
      """  InvoiceNum  """  
      pass

class CheckDocumentIsLocked_output:
   def __init__(self, obj):
      pass

class CheckExchangeRate_input:
   """ Required : 
   headNum
   vendorNum
   invoiceNum
   currSymbol
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      """  CheckHed HeadNum  """  
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.invoiceNum:str = obj["invoiceNum"]
      """  Proposed Invoice Number  """  
      self.currSymbol:str = obj["currSymbol"]
      """  Currency Symbol  """  
      pass

class CheckExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOnScreenLoad_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vQuestion:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPrevApplication_input:
   """ Required : 
   invoiceNum
   ipVendorNum
   """  
   def __init__(self, obj):
      self.invoiceNum:str = obj["invoiceNum"]
      """  proposed Invoice Number  """  
      self.ipVendorNum:int = obj["ipVendorNum"]
      """  proposed Vendor Number  """  
      pass

class CheckPrevApplication_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.prevFound:bool = obj["prevFound"]
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

class DeleteCheckDetails_input:
   """ Required : 
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  CheckHed.HeadNum  """  
      pass

class DeleteCheckDetails_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APTranRow:
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
      self.BaseAdjustAmt:int = obj["BaseAdjustAmt"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency.CurrSymbol for BASE  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseSelfAssessedTax:int = obj["BaseSelfAssessedTax"]
      self.ChangeExchangeRateResponse:str = obj["ChangeExchangeRateResponse"]
      """  Yes and No considered valid response.  All other values including blank treated as question was not posed to the user.  """  
      self.CNCFICodeDescription:str = obj["CNCFICodeDescription"]
      self.CopyRate:bool = obj["CopyRate"]
      """  If Copy Rate is true then original AP Invoice exchange rates are used when Adjustmet is applied and no currency gain/loss are calculated  """  
      self.CorrectionInv:bool = obj["CorrectionInv"]
      """  The flag to indicate if this payment line is realted to Correction invoice with negative amount  """  
      self.CPayLinked:bool = obj["CPayLinked"]
      """  Indicates if the related invoice is linked to a Central Payment invoice  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.CurrencyGainLoss:int = obj["CurrencyGainLoss"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  Currency.CurrSymbol from APInvHed  """  
      self.CurrSymbolCurrDesc:str = obj["CurrSymbolCurrDesc"]
      self.CurrSymbolCurrName:str = obj["CurrSymbolCurrName"]
      self.CurrSymbolCurrSymbol:str = obj["CurrSymbolCurrSymbol"]
      self.CurrSymbolDocumentDesc:str = obj["CurrSymbolDocumentDesc"]
      self.DebitMemo:bool = obj["DebitMemo"]
      self.DisableFieldsForPCashDoc:bool = obj["DisableFieldsForPCashDoc"]
      self.DiscountAvailable:bool = obj["DiscountAvailable"]
      self.DiscountDate:str = obj["DiscountDate"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  The display gl account.  """  
      self.DispTranAmt:int = obj["DispTranAmt"]
      self.DocBaseSelfAssessedTax:int = obj["DocBaseSelfAssessedTax"]
      self.DocDispTranAmt:int = obj["DocDispTranAmt"]
      self.DocExpenseAmount:int = obj["DocExpenseAmount"]
      self.DocGainLossAmt:int = obj["DocGainLossAmt"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.DocNetAmount:int = obj["DocNetAmount"]
      self.DocNewBalance:int = obj["DocNewBalance"]
      self.DocSelfAssessedTax:int = obj["DocSelfAssessedTax"]
      self.DocUnPostedBal:int = obj["DocUnPostedBal"]
      self.DocWithHoldTax:int = obj["DocWithHoldTax"]
      self.DsblCopyRate:bool = obj["DsblCopyRate"]
      """  If this flag is true then Copy Rate checkbox is Read Only  """  
      self.DueDate:str = obj["DueDate"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.ExpenseAmount:int = obj["ExpenseAmount"]
      self.FullyPaid:bool = obj["FullyPaid"]
      """  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  """  
      self.GainLossAmt:int = obj["GainLossAmt"]
      self.GlbCompany:str = obj["GlbCompany"]
      """  This is the source Company of the Central Payment linked invoice  """  
      self.GroupID:str = obj["GroupID"]
      self.InitUrgentPayment:bool = obj["InitUrgentPayment"]
      """  CSF Switzerland - Initial value for Urgent Invoice Payment flag.  """  
      self.InvExchangeRate:int = obj["InvExchangeRate"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.isDiscountforDebitM:bool = obj["isDiscountforDebitM"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.LockRate:bool = obj["LockRate"]
      self.MiscPayment:bool = obj["MiscPayment"]
      self.NetAmount:int = obj["NetAmount"]
      self.NewBalance:int = obj["NewBalance"]
      self.PaymentDesc:str = obj["PaymentDesc"]
      """  This field equals "Invoice" for Invoice payment, and "Misc" for Miscelleneous payment. This field  is used as label in tree.  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Print 1099  """  
      self.RateGroupDescription:str = obj["RateGroupDescription"]
      self.RefCodeEnabled:bool = obj["RefCodeEnabled"]
      self.RefCodeList:str = obj["RefCodeList"]
      """  Delimited list of possible Ref codes.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      """  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  """  
      self.Rpt1DispTranAmt:int = obj["Rpt1DispTranAmt"]
      self.Rpt1GainLossAmt:int = obj["Rpt1GainLossAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoice balance before adjustment in Rpt1 currency  """  
      self.Rpt1NewBalance:int = obj["Rpt1NewBalance"]
      self.Rpt2DispTranAmt:int = obj["Rpt2DispTranAmt"]
      self.Rpt2GainLossAmt:int = obj["Rpt2GainLossAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoice balance before adjustment in Rpt2 currency  """  
      self.Rpt2NewBalance:int = obj["Rpt2NewBalance"]
      self.Rpt3DispTranAmt:int = obj["Rpt3DispTranAmt"]
      self.Rpt3GainLossAmt:int = obj["Rpt3GainLossAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Report balance before adjustment in rpt3 currency  """  
      self.Rpt3NewBalance:int = obj["Rpt3NewBalance"]
      self.SelfAssessedTax:int = obj["SelfAssessedTax"]
      self.TaxableTransaction:bool = obj["TaxableTransaction"]
      """  Indicates if tax records are created and posted for AP Invoice adjustment  """  
      self.TaxLinesExist:bool = obj["TaxLinesExist"]
      self.TermsCode:str = obj["TermsCode"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.UnPostedBal:int = obj["UnPostedBal"]
      """  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  """  
      self.WithHoldTax:int = obj["WithHoldTax"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.AmtToAP:int = obj["AmtToAP"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.InvoiceLegalNumber:str = obj["InvoiceLegalNumber"]
      self.PLInvoiceReference:str = obj["PLInvoiceReference"]
      self.isPrecalcTax:bool = obj["isPrecalcTax"]
      """  The internal flag to indicate if Tax Liability assigned to the invoice being paid has Witholding taxes with Payment timing (WH taxes will be precalculated)  """  
      self.PrepayApld:bool = obj["PrepayApld"]
      """  The flag to indicate if the invoice being paid (applied)in Payment Entry/Invoice Payment is AP Invoice created for Misc. Payment / Prepayment by the system.  """  
      self.ManualTaxAdj:bool = obj["ManualTaxAdj"]
      """  The flag related to Misc. payment to indicate if Tax records created per Tax Liability assigned to Misc. payment are adjusted,  deleted,  or any tax records were added by the user  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ApplyDebitMemoTableset:
   def __init__(self, obj):
      self.CheckHed:list[Erp_Tablesets_CheckHedRow] = obj["CheckHed"]
      self.APTran:list[Erp_Tablesets_APTranRow] = obj["APTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_UpdExtApplyDebitMemoTableset:
   def __init__(self, obj):
      self.CheckHed:list[Erp_Tablesets_CheckHedRow] = obj["CheckHed"]
      self.APTran:list[Erp_Tablesets_APTranRow] = obj["APTran"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CheckHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPTran_input:
   """ Required : 
   ds
   headNum
   apTranNo
   invoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      self.headNum:int = obj["headNum"]
      self.apTranNo:int = obj["apTranNo"]
      self.invoiceNum:str = obj["invoiceNum"]
      pass

class GetNewAPTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCheckHedInv_input:
   """ Required : 
   vendorNum
   invoiceNum
   ds
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.invoiceNum:str = obj["invoiceNum"]
      """  Invoice Number  """  
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class GetNewCheckHedInv_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCheckHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class GetNewCheckHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCheckHed
   whereClauseAPTran
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCheckHed:str = obj["whereClauseCheckHed"]
      self.whereClauseAPTran:str = obj["whereClauseAPTran"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["returnObj"]
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

class SetReadyToCalc_input:
   """ Required : 
   ipHeadNum
   ipAPTranNo
   ipCalcAll
   ds
   """  
   def __init__(self, obj):
      self.ipHeadNum:int = obj["ipHeadNum"]
      self.ipAPTranNo:int = obj["ipAPTranNo"]
      self.ipCalcAll:bool = obj["ipCalcAll"]
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class SetReadyToCalc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtApplyDebitMemoTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtApplyDebitMemoTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ApplyDebitMemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class _ApplyDebitMemo_input:
   """ Required : 
   inHeadNum
   """  
   def __init__(self, obj):
      self.inHeadNum:int = obj["inHeadNum"]
      """  CheckHead.HeadNum  """  
      pass

class _ApplyDebitMemo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outRevJrnUID:int = obj["parameters"]
      self.peMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

