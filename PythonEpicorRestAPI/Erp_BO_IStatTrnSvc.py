import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IStatTrnSvc
# Description: IStatTrn business object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IStatTrns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IStatTrns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IStatTrns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IStatTrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns",headers=creds) as resp:
           return await resp.json()

async def post_IStatTrns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IStatTrns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IStatTrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.IStatTrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IStatTrns_Company_SourceModule_InvoiceNum_InvoiceLine_VendorNum_MemoFlag_SeqNum(Company, SourceModule, InvoiceNum, InvoiceLine, VendorNum, MemoFlag, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IStatTrn item
   Description: Calls GetByID to retrieve the IStatTrn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IStatTrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param MemoFlag: Desc: MemoFlag   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IStatTrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns(" + Company + "," + SourceModule + "," + InvoiceNum + "," + InvoiceLine + "," + VendorNum + "," + MemoFlag + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IStatTrns_Company_SourceModule_InvoiceNum_InvoiceLine_VendorNum_MemoFlag_SeqNum(Company, SourceModule, InvoiceNum, InvoiceLine, VendorNum, MemoFlag, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IStatTrn for the service
   Description: Calls UpdateExt to update IStatTrn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IStatTrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param MemoFlag: Desc: MemoFlag   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.IStatTrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns(" + Company + "," + SourceModule + "," + InvoiceNum + "," + InvoiceLine + "," + VendorNum + "," + MemoFlag + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IStatTrns_Company_SourceModule_InvoiceNum_InvoiceLine_VendorNum_MemoFlag_SeqNum(Company, SourceModule, InvoiceNum, InvoiceLine, VendorNum, MemoFlag, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IStatTrn item
   Description: Call UpdateExt to delete IStatTrn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IStatTrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SourceModule: Desc: SourceModule   Required: True   Allow empty value : True
      :param InvoiceNum: Desc: InvoiceNum   Required: True   Allow empty value : True
      :param InvoiceLine: Desc: InvoiceLine   Required: True
      :param VendorNum: Desc: VendorNum   Required: True
      :param MemoFlag: Desc: MemoFlag   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/IStatTrns(" + Company + "," + SourceModule + "," + InvoiceNum + "," + InvoiceLine + "," + VendorNum + "," + MemoFlag + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IStatTrnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIStatTrn, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseIStatTrn=" + whereClauseIStatTrn
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sourceModule, invoiceNum, invoiceLine, vendorNum, memoFlag, seqNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
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
   params += "sourceModule=" + sourceModule
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
   params += "invoiceLine=" + invoiceLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vendorNum=" + vendorNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "memoFlag=" + memoFlag
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "seqNum=" + seqNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ExportParamValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportParamValidation
   Description: Method to call to get validate the IStatTrnExportParam record for the generic or Iris export.
May return a warning message to inform the user that there are unposted entries
outside the fiscal period/date range or that there aren't any posted entries in
the given fiscal period/date range.  This is informational only and does not prevent
the user from continuing.
   OperationID: ExportParamValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportParamValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportParamValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FilterGetRowsRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FilterGetRowsRecords
   Description: Method to filter records after GetRows based on given parameters.
   OperationID: FilterGetRowsRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FilterGetRowsRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FilterGetRowsRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFlowList(epicorHeaders = None):
   """  
   Summary: Invoke method GetFlowList
   Description: Method to call to get the Flow List
for the Generic Export.
   OperationID: GetFlowList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFlowList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetIStatTrnExportParamGeneric(epicorHeaders = None):
   """  
   Summary: Invoke method GetIStatTrnExportParamGeneric
   Description: Method to call to get an IStatTrnExportParam record to obtain export parameters
for the Generic Export.
   OperationID: GetIStatTrnExportParamGeneric
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIStatTrnExportParamGeneric_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetIStatTrnExportParamIris(epicorHeaders = None):
   """  
   Summary: Invoke method GetIStatTrnExportParamIris
   Description: Method to call to get an IStatTrnExportParam record to obtain export parameters
for the Iris Export.
   OperationID: GetIStatTrnExportParamIris
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIStatTrnExportParamIris_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNextRefNum(epicorHeaders = None):
   """  
   Summary: Invoke method GetNextRefNum
   Description: This methods generates the next available reference number from the IStatTrn table.
   OperationID: GetNextRefNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextRefNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRowsFiltered(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsFiltered
   Description: Returns IStatTrn records Filtered by advanced parameters.
   OperationID: GetRowsFiltered
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsFiltered_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsFiltered_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsCommCodeExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsCommCodeExist
   Description: Returns message string in case CommCode is not exist
   OperationID: IsCommCodeExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsCommCodeExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsCommCodeExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofCommCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofCommCode
   Description: This methods should be called to validate the new commodity code entered by
the user.
   OperationID: OnChangeofCommCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofCommCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofCommCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofTransDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofTransDate
   Description: This methods should be called to validate the new Transaction date entered by
the user.
   OperationID: OnChangeofTransDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofTransDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofTransDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeofInvCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeofInvCurrencyCode
   Description: This methods should be called to validate the new currency code entered by
the user.
   OperationID: OnChangeofInvCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeofInvCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofInvCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessExport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessExport
   Description: Method to call to perform the export process for the generic or Iris export.
Returns a dataset containing all the records that are to be exported.
   OperationID: ProcessExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SortByData(epicorHeaders = None):
   """  
   Summary: Invoke method SortByData
   Description: Return a list of the export sort by options.  Only needs to be called for generic exports.
   OperationID: SortByData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SortByData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateRefNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRefNum
   Description: This method will validate that the reference number entered not through a search
will be a valid Reference number for the entered Intrastat transaction.
   OperationID: ValidateRefNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRefNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRefNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefExists
   Description: Validate the entered reference number does not exists.
   OperationID: RefExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIStatTrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIStatTrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIStatTrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIStatTrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIStatTrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IStatTrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IStatTrnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IStatTrnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IStatTrnRow] = obj["value"]
      pass

class Erp_Tablesets_IStatTrnListRow:
   def __init__(self, obj):
      self.Flow:str = obj["Flow"]
      """  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  """  
      self.Period:str = obj["Period"]
      """  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.Amount:int = obj["Amount"]
      """  Value of transported goods excluding taxes but including miscellaneous charges.  """  
      self.Terms:str = obj["Terms"]
      """  Delivery terms.  """  
      self.TransactionType:str = obj["TransactionType"]
      """  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.ISCountryCode:str = obj["ISCountryCode"]
      """  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  """  
      self.ISShipViaCode:str = obj["ISShipViaCode"]
      """  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border.  """  
      self.FlowSpec:str = obj["FlowSpec"]
      """  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  Currency indicator. Primarily used to cover the transitional period for the Euro.  """  
      self.Description:str = obj["Description"]
      """  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  """  
      self.SuppUnits:int = obj["SuppUnits"]
      """  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted Flag  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvDtl record.  """  
      self.MemoFlag:bool = obj["MemoFlag"]
      """   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "ShipVia" table.  """  
      self.FOB:str = obj["FOB"]
      """  The code for the FOB policy.  """  
      self.TaxID:str = obj["TaxID"]
      """  Optional field used to record the customer/vendor State Tax Identification number.  """  
      self.InvAmount:int = obj["InvAmount"]
      """  Value of transported goods excluding taxes and miscellaneous charges.  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.NotReported:bool = obj["NotReported"]
      """  Not Reported Flag  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StampID:str = obj["StampID"]
      """  Free form stamp to indicate the record has been reported to the authorities.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ManualEntry:bool = obj["ManualEntry"]
      self.CustIDSuppID:str = obj["CustIDSuppID"]
      """  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  """  
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      """  Full description of the Commodity Code.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
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
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IStatTrnRow:
   def __init__(self, obj):
      self.Flow:str = obj["Flow"]
      """  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  """  
      self.Period:str = obj["Period"]
      """  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.Amount:int = obj["Amount"]
      """  Value of transported goods excluding taxes but including miscellaneous charges.  """  
      self.Terms:str = obj["Terms"]
      """  Delivery terms.  """  
      self.TransactionType:str = obj["TransactionType"]
      """  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.ISCountryCode:str = obj["ISCountryCode"]
      """  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  """  
      self.ISShipViaCode:str = obj["ISShipViaCode"]
      """  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border.  """  
      self.FlowSpec:str = obj["FlowSpec"]
      """  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  Currency indicator. Primarily used to cover the transitional period for the Euro.  """  
      self.Description:str = obj["Description"]
      """  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  """  
      self.SuppUnits:int = obj["SuppUnits"]
      """  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted Flag  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvDtl record.  """  
      self.MemoFlag:bool = obj["MemoFlag"]
      """   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "ShipVia" table.  """  
      self.FOB:str = obj["FOB"]
      """  The code for the FOB policy.  """  
      self.TaxID:str = obj["TaxID"]
      """  Optional field used to record the customer/vendor State Tax Identification number.  """  
      self.InvAmount:int = obj["InvAmount"]
      """  Value of transported goods excluding taxes and miscellaneous charges.  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.NotReported:bool = obj["NotReported"]
      """  Not Reported Flag  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StampID:str = obj["StampID"]
      """  Free form stamp to indicate the record has been reported to the authorities.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.TaricCode:str = obj["TaricCode"]
      """  European Union integrated tariff.  """  
      self.EUPreference:str = obj["EUPreference"]
      """  European Union preference.  """  
      self.ExtraTrade:bool = obj["ExtraTrade"]
      """  Extra trade transaction indicator.  """  
      self.CommodityFlow:str = obj["CommodityFlow"]
      """  Commodity flow refers to the nature of a (cross-border) movement of goods.  """  
      self.CustomsProcedure:str = obj["CustomsProcedure"]
      """  Indicates which requested procedure and preceding procedure applies to the customs declaration.  """  
      self.ISCustomsDeclCountry:str = obj["ISCustomsDeclCountry"]
      """  The country where the customs declaration was filed, where the license for this procedure was issued by customs.  """  
      self.ISEUBorderCrossingCountry:str = obj["ISEUBorderCrossingCountry"]
      """  The EU Country from which the goods were dispatched for export, or to which the goods are ultimately destined for import.  """  
      self.IntraEUTransportMode:str = obj["IntraEUTransportMode"]
      """  The mode of transport refers to the mode of transport within the EU.  """  
      self.ContainerShip:bool = obj["ContainerShip"]
      """  Indicates whether or not there is transport by container.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Value of transported goods in invoice currency excluding taxes but including miscellaneous charges.  """  
      self.DocInvAmount:int = obj["DocInvAmount"]
      """  Value of transported goods  in invoice currency excluding taxes and miscellaneous charges.  """  
      self.InvCurrencyCode:str = obj["InvCurrencyCode"]
      """  A unique code that identifies the invoice currency.  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EUThirdParty  """  
      self.CountryDescr:str = obj["CountryDescr"]
      """  Country description  """  
      self.CountryOfOriginDescr:str = obj["CountryOfOriginDescr"]
      """  Description of country of origin  """  
      self.CustIDSuppID:str = obj["CustIDSuppID"]
      """  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  """  
      self.CustSuppName:str = obj["CustSuppName"]
      self.DelivTermsDescr:str = obj["DelivTermsDescr"]
      """  Delivery Terms description  """  
      self.EntrPointDescr:str = obj["EntrPointDescr"]
      """  Entry Point description  """  
      self.Generate2Line:bool = obj["Generate2Line"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.ManualEntry:bool = obj["ManualEntry"]
      self.ModeOfTransportDescr:str = obj["ModeOfTransportDescr"]
      """  Mode of Transport description  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RegionDescr:str = obj["RegionDescr"]
      """  Region description  """  
      self.ReportID:str = obj["ReportID"]
      self.SpecDescr:str = obj["SpecDescr"]
      """  Spec description  """  
      self.TranTypeDescr:str = obj["TranTypeDescr"]
      """  Transaction Type description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeSuppUnitsUOM:str = obj["CommodityCodeSuppUnitsUOM"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.InvCurrencyCurrDesc:str = obj["InvCurrencyCurrDesc"]
      self.InvCurrencyCurrSymbol:str = obj["InvCurrencyCurrSymbol"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sourceModule
   invoiceNum
   invoiceLine
   vendorNum
   memoFlag
   seqNum
   """  
   def __init__(self, obj):
      self.sourceModule:str = obj["sourceModule"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.vendorNum:int = obj["vendorNum"]
      self.memoFlag:bool = obj["memoFlag"]
      self.seqNum:int = obj["seqNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_IStatTrnExportParamRow:
   def __init__(self, obj):
      self.ExportType:str = obj["ExportType"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.FilterFlow:str = obj["FilterFlow"]
      self.SortOption:str = obj["SortOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IStatTrnExportParamTableset:
   def __init__(self, obj):
      self.IStatTrnExportParam:list[Erp_Tablesets_IStatTrnExportParamRow] = obj["IStatTrnExportParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IStatTrnExportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created Intrastat transaction.  This is assigned by the system. 
Values can be; AR, AP.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvDtl record.  """  
      self.MemoFlag:bool = obj["MemoFlag"]
      """  Indicates the type of document.  """  
      self.ExportType:str = obj["ExportType"]
      self.ExportData:str = obj["ExportData"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IStatTrnExportTableset:
   def __init__(self, obj):
      self.IStatTrnExport:list[Erp_Tablesets_IStatTrnExportRow] = obj["IStatTrnExport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IStatTrnListRow:
   def __init__(self, obj):
      self.Flow:str = obj["Flow"]
      """  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  """  
      self.Period:str = obj["Period"]
      """  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.Amount:int = obj["Amount"]
      """  Value of transported goods excluding taxes but including miscellaneous charges.  """  
      self.Terms:str = obj["Terms"]
      """  Delivery terms.  """  
      self.TransactionType:str = obj["TransactionType"]
      """  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.ISCountryCode:str = obj["ISCountryCode"]
      """  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  """  
      self.ISShipViaCode:str = obj["ISShipViaCode"]
      """  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border.  """  
      self.FlowSpec:str = obj["FlowSpec"]
      """  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  Currency indicator. Primarily used to cover the transitional period for the Euro.  """  
      self.Description:str = obj["Description"]
      """  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  """  
      self.SuppUnits:int = obj["SuppUnits"]
      """  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted Flag  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvDtl record.  """  
      self.MemoFlag:bool = obj["MemoFlag"]
      """   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "ShipVia" table.  """  
      self.FOB:str = obj["FOB"]
      """  The code for the FOB policy.  """  
      self.TaxID:str = obj["TaxID"]
      """  Optional field used to record the customer/vendor State Tax Identification number.  """  
      self.InvAmount:int = obj["InvAmount"]
      """  Value of transported goods excluding taxes and miscellaneous charges.  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.NotReported:bool = obj["NotReported"]
      """  Not Reported Flag  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StampID:str = obj["StampID"]
      """  Free form stamp to indicate the record has been reported to the authorities.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ManualEntry:bool = obj["ManualEntry"]
      self.CustIDSuppID:str = obj["CustIDSuppID"]
      """  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  """  
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      """  Full description of the Commodity Code.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      """  A short description that can be used to explain what this invoice is for. Ex: Rent, Auto Lease Payment.  This description is defaulted into the APTran.Description field when payments are made against the invoice.  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
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
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IStatTrnListTableset:
   def __init__(self, obj):
      self.IStatTrnList:list[Erp_Tablesets_IStatTrnListRow] = obj["IStatTrnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IStatTrnRow:
   def __init__(self, obj):
      self.Flow:str = obj["Flow"]
      """  Indicates whether the transaction is an "Arrival" (receipt) or "Dispatch" (shipment) of goods.  """  
      self.Period:str = obj["Period"]
      """  Depending on the ISSyst.PeriodFormat settings, this field contains the period in which this transaction was executed.  """  
      self.CommodityCode:str = obj["CommodityCode"]
      """  Harmonized System goods classification code. The Commodity Code field must be valid in the ICommCode (formerly called IStatGrp) master file.  """  
      self.Amount:int = obj["Amount"]
      """  Value of transported goods excluding taxes but including miscellaneous charges.  """  
      self.Terms:str = obj["Terms"]
      """  Delivery terms.  """  
      self.TransactionType:str = obj["TransactionType"]
      """  Indicates the purpose of the transaction: Change of ownership, goods for subcontract job...  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.ISCountryCode:str = obj["ISCountryCode"]
      """  Country of Consignment/Destination. This field contains the Intrastat Code from the Country table.  """  
      self.ISShipViaCode:str = obj["ISShipViaCode"]
      """  Intrastat code for method of transportation. The value comes from the IStatCode field from the ShipVia record.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border.  """  
      self.FlowSpec:str = obj["FlowSpec"]
      """  Indicates if there is a non-standard type of transaction. (for example, goods imported and immediately exported again)  """  
      self.ISCurrency:str = obj["ISCurrency"]
      """  Currency indicator. Primarily used to cover the transitional period for the Euro.  """  
      self.Description:str = obj["Description"]
      """  Description of the Commodity Code or the Detail line depending on the value of the ISSyst.DescType field.  """  
      self.SuppUnits:int = obj["SuppUnits"]
      """  When the RequiresUM field in the IStatGrp is set, this field contains the quantity part for the UM for this Commodity Code.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created Intrastat transaction.  This is assigned by the system.
Values can be; AR, AP or M (Manual Entry)  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  A/P or A/R invoice  that this Intrastat transaction is associated with. This along with InvoiceLine provides a relationship to the A/P or A/R Invoice Detail  (APInvDtl/InvcDtl)  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice line of the APInvDtl/InvcDtl record  to which this Intrastat transaction record is related to.  """  
      self.Posted:bool = obj["Posted"]
      """  Posted Flag  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum duplicated from the corresponding APInvDtl record.  """  
      self.MemoFlag:bool = obj["MemoFlag"]
      """   Indicates the type of document.  Yes = Credit/Debit Memo No = Regular AR/AP Invoice. This value can't be changed after the record has been created.
Credit/Debit memos affect the way amounts are displayed in theIntrastat reports. They will always be stored with a positive sign but will be displayed as a negative.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "ShipVia" table.  """  
      self.FOB:str = obj["FOB"]
      """  The code for the FOB policy.  """  
      self.TaxID:str = obj["TaxID"]
      """  Optional field used to record the customer/vendor State Tax Identification number.  """  
      self.InvAmount:int = obj["InvAmount"]
      """  Value of transported goods excluding taxes and miscellaneous charges.  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.NotReported:bool = obj["NotReported"]
      """  Not Reported Flag  """  
      self.ISRegion:str = obj["ISRegion"]
      """  Intrastat Region  """  
      self.ISOrigCountry:str = obj["ISOrigCountry"]
      """  This field contains the Intrastat Country of Origin Code from the Country table.  """  
      self.IntCommCode:str = obj["IntCommCode"]
      """  Intrastat goods classification code following the Intrastat Classification Nomenclature (ICN).  """  
      self.StampID:str = obj["StampID"]
      """  Free form stamp to indicate the record has been reported to the authorities.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CommentText:str = obj["CommentText"]
      """  CommentText  """  
      self.TaricCode:str = obj["TaricCode"]
      """  European Union integrated tariff.  """  
      self.EUPreference:str = obj["EUPreference"]
      """  European Union preference.  """  
      self.ExtraTrade:bool = obj["ExtraTrade"]
      """  Extra trade transaction indicator.  """  
      self.CommodityFlow:str = obj["CommodityFlow"]
      """  Commodity flow refers to the nature of a (cross-border) movement of goods.  """  
      self.CustomsProcedure:str = obj["CustomsProcedure"]
      """  Indicates which requested procedure and preceding procedure applies to the customs declaration.  """  
      self.ISCustomsDeclCountry:str = obj["ISCustomsDeclCountry"]
      """  The country where the customs declaration was filed, where the license for this procedure was issued by customs.  """  
      self.ISEUBorderCrossingCountry:str = obj["ISEUBorderCrossingCountry"]
      """  The EU Country from which the goods were dispatched for export, or to which the goods are ultimately destined for import.  """  
      self.IntraEUTransportMode:str = obj["IntraEUTransportMode"]
      """  The mode of transport refers to the mode of transport within the EU.  """  
      self.ContainerShip:bool = obj["ContainerShip"]
      """  Indicates whether or not there is transport by container.  """  
      self.DocAmount:int = obj["DocAmount"]
      """  Value of transported goods in invoice currency excluding taxes but including miscellaneous charges.  """  
      self.DocInvAmount:int = obj["DocInvAmount"]
      """  Value of transported goods  in invoice currency excluding taxes and miscellaneous charges.  """  
      self.InvCurrencyCode:str = obj["InvCurrencyCode"]
      """  A unique code that identifies the invoice currency.  """  
      self.EUThirdParty:bool = obj["EUThirdParty"]
      """  EUThirdParty  """  
      self.CountryDescr:str = obj["CountryDescr"]
      """  Country description  """  
      self.CountryOfOriginDescr:str = obj["CountryOfOriginDescr"]
      """  Description of country of origin  """  
      self.CustIDSuppID:str = obj["CustIDSuppID"]
      """  When it is an AR Invoice this will represent the Customer ID, and when it is from AP Invoice this will represent the Supplier ID.  """  
      self.CustSuppName:str = obj["CustSuppName"]
      self.DelivTermsDescr:str = obj["DelivTermsDescr"]
      """  Delivery Terms description  """  
      self.EntrPointDescr:str = obj["EntrPointDescr"]
      """  Entry Point description  """  
      self.Generate2Line:bool = obj["Generate2Line"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.ManualEntry:bool = obj["ManualEntry"]
      self.ModeOfTransportDescr:str = obj["ModeOfTransportDescr"]
      """  Mode of Transport description  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.RegionDescr:str = obj["RegionDescr"]
      """  Region description  """  
      self.ReportID:str = obj["ReportID"]
      self.SpecDescr:str = obj["SpecDescr"]
      """  Spec description  """  
      self.TranTypeDescr:str = obj["TranTypeDescr"]
      """  Transaction Type description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CommodityCodeSuppUnitsUOM:str = obj["CommodityCodeSuppUnitsUOM"]
      self.CommodityCodeDescription:str = obj["CommodityCodeDescription"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.InvCurrencyCurrDesc:str = obj["InvCurrencyCurrDesc"]
      self.InvCurrencyCurrSymbol:str = obj["InvCurrencyCurrSymbol"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IStatTrnTableset:
   def __init__(self, obj):
      self.IStatTrn:list[Erp_Tablesets_IStatTrnRow] = obj["IStatTrn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtIStatTrnTableset:
   def __init__(self, obj):
      self.IStatTrn:list[Erp_Tablesets_IStatTrnRow] = obj["IStatTrn"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportParamValidation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnExportParamTableset] = obj["ds"]
      pass

class ExportParamValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnExportParamTableset] = obj["ds"]
      self.warningText:str = obj["parameters"]
      pass

      """  output parameters  """  

class FilterGetRowsRecords_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class FilterGetRowsRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   sourceModule
   invoiceNum
   invoiceLine
   vendorNum
   memoFlag
   seqNum
   """  
   def __init__(self, obj):
      self.sourceModule:str = obj["sourceModule"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.vendorNum:int = obj["vendorNum"]
      self.memoFlag:bool = obj["memoFlag"]
      self.seqNum:int = obj["seqNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IStatTrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IStatTrnTableset] = obj["returnObj"]
      pass

class GetFlowList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Intrastat Flow List  """  
      pass

class GetIStatTrnExportParamGeneric_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnExportParamTableset] = obj["returnObj"]
      pass

class GetIStatTrnExportParamIris_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnExportParamTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IStatTrnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIStatTrn_input:
   """ Required : 
   ds
   sourceModule
   invoiceNum
   invoiceLine
   vendorNum
   memoFlag
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      self.sourceModule:str = obj["sourceModule"]
      self.invoiceNum:str = obj["invoiceNum"]
      self.invoiceLine:int = obj["invoiceLine"]
      self.vendorNum:int = obj["vendorNum"]
      self.memoFlag:bool = obj["memoFlag"]
      pass

class GetNewIStatTrn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNextRefNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNextRefNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsFiltered_input:
   """ Required : 
   whereClauseIStatTrn
   whereClauseCustSuplNum
   whereClauseLegalNumber
   whereClauseIncludeExcluded
   whereClauseIncludeReported
   whereClauseReportIDFrom
   whereClauseReportIDTo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIStatTrn:str = obj["whereClauseIStatTrn"]
      """  Base Whereclause for IStatTrn table.  """  
      self.whereClauseCustSuplNum:int = obj["whereClauseCustSuplNum"]
      """  Cust Num / Supl Num  """  
      self.whereClauseLegalNumber:str = obj["whereClauseLegalNumber"]
      """  Legal Number  """  
      self.whereClauseIncludeExcluded:bool = obj["whereClauseIncludeExcluded"]
      """  If True - selection should include all items which do not have exclude flag  """  
      self.whereClauseIncludeReported:str = obj["whereClauseIncludeReported"]
      """  No – only not reported, Yes – both reported and not reported, Only reported – only reported  """  
      self.whereClauseReportIDFrom:str = obj["whereClauseReportIDFrom"]
      """  Min Report ID  """  
      self.whereClauseReportIDTo:str = obj["whereClauseReportIDTo"]
      """  Max Report ID  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsFiltered_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseIStatTrn
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIStatTrn:str = obj["whereClauseIStatTrn"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnTableset] = obj["returnObj"]
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

class IsCommCodeExist_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

class IsCommCodeExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vErrMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofCommCode_input:
   """ Required : 
   cCommCode
   ds
   """  
   def __init__(self, obj):
      self.cCommCode:str = obj["cCommCode"]
      """  New Commodity Code.  """  
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

class OnChangeofCommCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cErrMessage:str = obj["parameters"]
      self.cOldCommCode:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofInvCurrencyCode_input:
   """ Required : 
   newInvCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.newInvCurrencyCode:str = obj["newInvCurrencyCode"]
      """  New Currency Code.  """  
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

class OnChangeofInvCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeofTransDate_input:
   """ Required : 
   newTransDate
   ds
   """  
   def __init__(self, obj):
      self.newTransDate:str = obj["newTransDate"]
      """  New Apply Date.  """  
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

class OnChangeofTransDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessExport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnExportParamTableset] = obj["ds"]
      pass

class ProcessExport_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IStatTrnExportTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnExportParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefExists_input:
   """ Required : 
   refNum
   """  
   def __init__(self, obj):
      self.refNum:str = obj["refNum"]
      """  Entered reference number  """  
      pass

class RefExists_output:
   def __init__(self, obj):
      pass

class SortByData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cSortByList:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIStatTrnTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIStatTrnTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IStatTrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateRefNum_input:
   """ Required : 
   ipRefNum
   """  
   def __init__(self, obj):
      self.ipRefNum:str = obj["ipRefNum"]
      """  The entered reference number.  """  
      pass

class ValidateRefNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vErrMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

