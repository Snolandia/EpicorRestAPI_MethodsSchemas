import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WHTPaymentSvc
# Description: Withholding Tax Payment Report BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_WHTPayments(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WHTPayments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WHTPayments
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments",headers=creds) as resp:
           return await resp.json()

async def post_WHTPayments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WHTPayments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WHTPayments_Company_ReportID(Company, ReportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WHTPayment item
   Description: Calls GetByID to retrieve the WHTPayment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPayment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WHTPayments_Company_ReportID(Company, ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WHTPayment for the service
   Description: Calls UpdateExt to update WHTPayment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WHTPayment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WHTPaymentHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WHTPayments_Company_ReportID(Company, ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WHTPayment item
   Description: Call UpdateExt to delete WHTPayment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WHTPayment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WHTPayments_Company_ReportID_WHTPaymentDtls(Company, ReportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WHTPaymentDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WHTPaymentDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")/WHTPaymentDtls",headers=creds) as resp:
           return await resp.json()

async def get_WHTPayments_Company_ReportID_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company, ReportID, TranDate, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WHTPaymentDtl item
   Description: Calls GetByID to retrieve the WHTPaymentDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPayments(" + Company + "," + ReportID + ")/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_WHTPaymentDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WHTPaymentDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WHTPaymentDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls",headers=creds) as resp:
           return await resp.json()

async def post_WHTPaymentDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WHTPaymentDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company, ReportID, TranDate, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WHTPaymentDtl item
   Description: Calls GetByID to retrieve the WHTPaymentDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WHTPaymentDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company, ReportID, TranDate, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WHTPaymentDtl for the service
   Description: Calls UpdateExt to update WHTPaymentDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WHTPaymentDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WHTPaymentDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WHTPaymentDtls_Company_ReportID_TranDate_TranNum(Company, ReportID, TranDate, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WHTPaymentDtl item
   Description: Call UpdateExt to delete WHTPaymentDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WHTPaymentDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param TranDate: Desc: TranDate   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/WHTPaymentDtls(" + Company + "," + ReportID + "," + TranDate + "," + TranNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WHTPaymentHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWHTPaymentHead, whereClauseWHTPaymentDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseWHTPaymentHead=" + whereClauseWHTPaymentHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWHTPaymentDtl=" + whereClauseWHTPaymentDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankAcctID
   Description: Call this method when the user changes the Bank Account.
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTaxCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTaxCode
   Description: Call this method when the user changes the Tax Code.
   OperationID: OnChangeTaxCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTaxCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTaxCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWHTaxRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWHTaxRecords
   Description: This method get Withholding Tax Records for specific period
   OperationID: GetWHTaxRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWHTaxRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWHTaxRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveUnPaidWHTaxRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveUnPaidWHTaxRecords
   Description: This method remove UnPaid Withholding Tax Records from the report
   OperationID: RemoveUnPaidWHTaxRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveUnPaidWHTaxRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveUnPaidWHTaxRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveSelectedWHTaxRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveSelectedWHTaxRecords
   Description: This method remove selected Withholding Tax Records from the report
   OperationID: RemoveSelectedWHTaxRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveSelectedWHTaxRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSelectedWHTaxRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWHTPaymentAPInvData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWHTPaymentAPInvData
   Description: Get submitted withholding tax reports linked to specific AP Invoice.
   OperationID: GetWHTPaymentAPInvData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWHTPaymentAPInvData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWHTPaymentAPInvData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWHTPaymentHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWHTPaymentHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWHTPaymentHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWHTPaymentHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWHTPaymentHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWHTPaymentDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWHTPaymentDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWHTPaymentDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWHTPaymentDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWHTPaymentDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WHTPaymentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WHTPaymentDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WHTPaymentHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WHTPaymentHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WHTPaymentHeadRow] = obj["value"]
      pass

class Erp_Tablesets_WHTPaymentDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate from Erp.TaxTran table.  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum from Erp.TaxTran table.  """  
      self.IsPaid:bool = obj["IsPaid"]
      """  Whether the tax line is paid to government.  """  
      self.Notes:str = obj["Notes"]
      """  Tax Line comment.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user who added the line to report.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of adding.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  The last user who changed the report line.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date and time of last changing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsInvoice:bool = obj["IsInvoice"]
      """  Transaction belongs to Invoice.  """  
      self.IsDM:bool = obj["IsDM"]
      """  Transaction belongs to Debit Memo.  """  
      self.IsCM:bool = obj["IsCM"]
      """  Transaction belongs to Credit Memo.  """  
      self.IsCorrection:bool = obj["IsCorrection"]
      """  Transaction belongs to Correction Invoice.  """  
      self.IsPayment:bool = obj["IsPayment"]
      """  Transaction belongs to Payment.  """  
      self.PartyID:str = obj["PartyID"]
      """  Customer/Supplier ID.  """  
      self.PartyName:str = obj["PartyName"]
      """  Customer/Supplier Name.  """  
      self.PartyPAN:str = obj["PartyPAN"]
      """  Customer/Supplier PAN Number.  """  
      self.PartyTaxEntityType:str = obj["PartyTaxEntityType"]
      """  Customer/Supplier Tax Entity Type.  """  
      self.DocumentNum:str = obj["DocumentNum"]
      """  Invoice/Payment Number.  """  
      self.DocumentDate:str = obj["DocumentDate"]
      """  Invoice/Payment Date.  """  
      self.DocumentDescription:str = obj["DocumentDescription"]
      """  Invoice/Payment Description.  """  
      self.DocumentLN:str = obj["DocumentLN"]
      """  Invoice/Payment Legal Number.  """  
      self.DocumentAmt:int = obj["DocumentAmt"]
      """  Invoice/Payment Document Amount.  """  
      self.DocumentTypeName:str = obj["DocumentTypeName"]
      """  Document type name.  """  
      self.BoENumber:str = obj["BoENumber"]
      """  Invoice Pre-Payment check number.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Transaction Apply Date.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Transaction Tax Point Date.  """  
      self.TaxRatePercent:int = obj["TaxRatePercent"]
      """  Transaction Tax Rate Percent.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Transaction Taxable Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Transaction Tax Amount.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Transaction Tax Liability Code.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Transaction Tax Liability Description.  """  
      self.TaxTypeCode:str = obj["TaxTypeCode"]
      """  Transaction Tax Type ID.  """  
      self.TaxTypeDescription:str = obj["TaxTypeDescription"]
      """  Transaction Tax Type Description.  """  
      self.TaxTextCode:str = obj["TaxTextCode"]
      """  Transaction Tax Type Legal Text Code.  """  
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      """  Transaction Tax Type Legal Text.  """  
      self.TaxRptCatCode:str = obj["TaxRptCatCode"]
      """  Transaction Tax Type Report Category Code.  """  
      self.TaxRptCatDescription:str = obj["TaxRptCatDescription"]
      """  Transaction Tax Type Report Category Description.  """  
      self.Selected:bool = obj["Selected"]
      """  Transaction selected.  """  
      self.PartyNum:int = obj["PartyNum"]
      """  Customer/Supplier Number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WHTPaymentHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start date of the report period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the report period.  """  
      self.Description:str = obj["Description"]
      """  Report Description.  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Report date.  """  
      self.Module:str = obj["Module"]
      """  Module AR or AP.  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Tax Entity Type.  """  
      self.WHTPaymentAmount:int = obj["WHTPaymentAmount"]
      """  The amount of WHT paid to the government.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.ReceiptNumber:str = obj["ReceiptNumber"]
      """  Bank receipt number.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Bank receipt date.  """  
      self.BankTranRefNum:str = obj["BankTranRefNum"]
      """  Bank transaction reference number (BSR Code).  """  
      self.PaymentDate:str = obj["PaymentDate"]
      """  Report payment date.  """  
      self.ChequeNumber:str = obj["ChequeNumber"]
      """  Cheque Number  """  
      self.ChequeDate:str = obj["ChequeDate"]
      """  Cheque or ECS Date  """  
      self.AdditionalTranRef:str = obj["AdditionalTranRef"]
      """  Additional transaction reference (ECS).  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the report.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  The date and time of submitting.  """  
      self.ReportStatus:int = obj["ReportStatus"]
      """  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  """  
      self.LatePaymentCharge:int = obj["LatePaymentCharge"]
      """  The charge paid for late filing of the tax returns.  """  
      self.NatureOfRemittance:str = obj["NatureOfRemittance"]
      """  Nature of Remittance.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax Type ID.  """  
      self.SubmitReportID:str = obj["SubmitReportID"]
      """  Submitted Report ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user who created the report.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  The last user who changed the report.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date and time of last changing.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PenaltyAmount:int = obj["PenaltyAmount"]
      """  Penalty amount.  """  
      self.IsSubmitted:bool = obj["IsSubmitted"]
      """  Report was submitted or not.  """  
      self.IsClosed:bool = obj["IsClosed"]
      """  Report is closed for changing or not.  """  
      self.IsReady:bool = obj["IsReady"]
      """  Mark report to ready for submitting.  """  
      self.TotalPaymentAmt:int = obj["TotalPaymentAmt"]
      """  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WHTPaymentHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start date of the report period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the report period.  """  
      self.Description:str = obj["Description"]
      """  Report Description.  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Report date.  """  
      self.Module:str = obj["Module"]
      """  Module AR or AP.  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Tax Entity Type.  """  
      self.WHTPaymentAmount:int = obj["WHTPaymentAmount"]
      """  The amount of WHT paid to the government.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.ReceiptNumber:str = obj["ReceiptNumber"]
      """  Bank receipt number.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Bank receipt date.  """  
      self.BankTranRefNum:str = obj["BankTranRefNum"]
      """  Bank transaction reference number (BSR Code).  """  
      self.PaymentDate:str = obj["PaymentDate"]
      """  Report payment date.  """  
      self.ChequeNumber:str = obj["ChequeNumber"]
      """  Cheque Number  """  
      self.ChequeDate:str = obj["ChequeDate"]
      """  Cheque or ECS Date  """  
      self.AdditionalTranRef:str = obj["AdditionalTranRef"]
      """  Additional transaction reference (ECS).  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the report.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  The date and time of submitting.  """  
      self.ReportStatus:int = obj["ReportStatus"]
      """  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  """  
      self.Notes:str = obj["Notes"]
      """  Report comment.  """  
      self.LatePaymentCharge:int = obj["LatePaymentCharge"]
      """  The charge paid for late filing of the tax returns.  """  
      self.NatureOfRemittance:str = obj["NatureOfRemittance"]
      """  Nature of Remittance.  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Customer filter.  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Supplier filter.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax Type ID.  """  
      self.TaxLiabilityList:str = obj["TaxLiabilityList"]
      """  Tax Liability filter.  """  
      self.SubmitReportID:str = obj["SubmitReportID"]
      """  Submitted Report ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user who created the report.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  The last user who changed the report.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date and time of last changing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PenaltyAmount:int = obj["PenaltyAmount"]
      """  Penalty amount.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency Symbol of base Currency.  """  
      self.BookID:str = obj["BookID"]
      """  Main Book ID.  """  
      self.IsClosed:bool = obj["IsClosed"]
      """  Report is closed for changing or not.  """  
      self.IsReady:bool = obj["IsReady"]
      """  Mark report to ready for submitting.  """  
      self.IsSubmitted:bool = obj["IsSubmitted"]
      """  Report was submitted or not.  """  
      self.LineTotalAmt:int = obj["LineTotalAmt"]
      """  Report Lines total amount.  """  
      self.SelectAll:bool = obj["SelectAll"]
      """  Select/Deselect all detail rows.  """  
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      """  Tax Type description.  """  
      self.TotalPaymentAmt:int = obj["TotalPaymentAmt"]
      """  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  """  
      self.BaseCurrCode:str = obj["BaseCurrCode"]
      """  Currency Code of base Currency.  """  
      self.BaseCurrID:str = obj["BaseCurrID"]
      """  Currency ID of base Currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtWHTPaymentTableset:
   def __init__(self, obj):
      self.WHTPaymentHead:list[Erp_Tablesets_WHTPaymentHeadRow] = obj["WHTPaymentHead"]
      self.WHTPaymentDtl:list[Erp_Tablesets_WHTPaymentDtlRow] = obj["WHTPaymentDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WHTPaymentDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.TranDate:str = obj["TranDate"]
      """  TranDate from Erp.TaxTran table.  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum from Erp.TaxTran table.  """  
      self.IsPaid:bool = obj["IsPaid"]
      """  Whether the tax line is paid to government.  """  
      self.Notes:str = obj["Notes"]
      """  Tax Line comment.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user who added the line to report.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of adding.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  The last user who changed the report line.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date and time of last changing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsInvoice:bool = obj["IsInvoice"]
      """  Transaction belongs to Invoice.  """  
      self.IsDM:bool = obj["IsDM"]
      """  Transaction belongs to Debit Memo.  """  
      self.IsCM:bool = obj["IsCM"]
      """  Transaction belongs to Credit Memo.  """  
      self.IsCorrection:bool = obj["IsCorrection"]
      """  Transaction belongs to Correction Invoice.  """  
      self.IsPayment:bool = obj["IsPayment"]
      """  Transaction belongs to Payment.  """  
      self.PartyID:str = obj["PartyID"]
      """  Customer/Supplier ID.  """  
      self.PartyName:str = obj["PartyName"]
      """  Customer/Supplier Name.  """  
      self.PartyPAN:str = obj["PartyPAN"]
      """  Customer/Supplier PAN Number.  """  
      self.PartyTaxEntityType:str = obj["PartyTaxEntityType"]
      """  Customer/Supplier Tax Entity Type.  """  
      self.DocumentNum:str = obj["DocumentNum"]
      """  Invoice/Payment Number.  """  
      self.DocumentDate:str = obj["DocumentDate"]
      """  Invoice/Payment Date.  """  
      self.DocumentDescription:str = obj["DocumentDescription"]
      """  Invoice/Payment Description.  """  
      self.DocumentLN:str = obj["DocumentLN"]
      """  Invoice/Payment Legal Number.  """  
      self.DocumentAmt:int = obj["DocumentAmt"]
      """  Invoice/Payment Document Amount.  """  
      self.DocumentTypeName:str = obj["DocumentTypeName"]
      """  Document type name.  """  
      self.BoENumber:str = obj["BoENumber"]
      """  Invoice Pre-Payment check number.  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Transaction Apply Date.  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Transaction Tax Point Date.  """  
      self.TaxRatePercent:int = obj["TaxRatePercent"]
      """  Transaction Tax Rate Percent.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Transaction Taxable Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Transaction Tax Amount.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Transaction Tax Liability Code.  """  
      self.TaxRegionDescription:str = obj["TaxRegionDescription"]
      """  Transaction Tax Liability Description.  """  
      self.TaxTypeCode:str = obj["TaxTypeCode"]
      """  Transaction Tax Type ID.  """  
      self.TaxTypeDescription:str = obj["TaxTypeDescription"]
      """  Transaction Tax Type Description.  """  
      self.TaxTextCode:str = obj["TaxTextCode"]
      """  Transaction Tax Type Legal Text Code.  """  
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      """  Transaction Tax Type Legal Text.  """  
      self.TaxRptCatCode:str = obj["TaxRptCatCode"]
      """  Transaction Tax Type Report Category Code.  """  
      self.TaxRptCatDescription:str = obj["TaxRptCatDescription"]
      """  Transaction Tax Type Report Category Description.  """  
      self.Selected:bool = obj["Selected"]
      """  Transaction selected.  """  
      self.PartyNum:int = obj["PartyNum"]
      """  Customer/Supplier Number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WHTPaymentHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start date of the report period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the report period.  """  
      self.Description:str = obj["Description"]
      """  Report Description.  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Report date.  """  
      self.Module:str = obj["Module"]
      """  Module AR or AP.  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Tax Entity Type.  """  
      self.WHTPaymentAmount:int = obj["WHTPaymentAmount"]
      """  The amount of WHT paid to the government.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.ReceiptNumber:str = obj["ReceiptNumber"]
      """  Bank receipt number.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Bank receipt date.  """  
      self.BankTranRefNum:str = obj["BankTranRefNum"]
      """  Bank transaction reference number (BSR Code).  """  
      self.PaymentDate:str = obj["PaymentDate"]
      """  Report payment date.  """  
      self.ChequeNumber:str = obj["ChequeNumber"]
      """  Cheque Number  """  
      self.ChequeDate:str = obj["ChequeDate"]
      """  Cheque or ECS Date  """  
      self.AdditionalTranRef:str = obj["AdditionalTranRef"]
      """  Additional transaction reference (ECS).  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the report.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  The date and time of submitting.  """  
      self.ReportStatus:int = obj["ReportStatus"]
      """  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  """  
      self.LatePaymentCharge:int = obj["LatePaymentCharge"]
      """  The charge paid for late filing of the tax returns.  """  
      self.NatureOfRemittance:str = obj["NatureOfRemittance"]
      """  Nature of Remittance.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax Type ID.  """  
      self.SubmitReportID:str = obj["SubmitReportID"]
      """  Submitted Report ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user who created the report.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  The last user who changed the report.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date and time of last changing.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PenaltyAmount:int = obj["PenaltyAmount"]
      """  Penalty amount.  """  
      self.IsSubmitted:bool = obj["IsSubmitted"]
      """  Report was submitted or not.  """  
      self.IsClosed:bool = obj["IsClosed"]
      """  Report is closed for changing or not.  """  
      self.IsReady:bool = obj["IsReady"]
      """  Mark report to ready for submitting.  """  
      self.TotalPaymentAmt:int = obj["TotalPaymentAmt"]
      """  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WHTPaymentHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start date of the report period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the report period.  """  
      self.Description:str = obj["Description"]
      """  Report Description.  """  
      self.ReportDate:str = obj["ReportDate"]
      """  Report date.  """  
      self.Module:str = obj["Module"]
      """  Module AR or AP.  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Tax Entity Type.  """  
      self.WHTPaymentAmount:int = obj["WHTPaymentAmount"]
      """  The amount of WHT paid to the government.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.ReceiptNumber:str = obj["ReceiptNumber"]
      """  Bank receipt number.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Bank receipt date.  """  
      self.BankTranRefNum:str = obj["BankTranRefNum"]
      """  Bank transaction reference number (BSR Code).  """  
      self.PaymentDate:str = obj["PaymentDate"]
      """  Report payment date.  """  
      self.ChequeNumber:str = obj["ChequeNumber"]
      """  Cheque Number  """  
      self.ChequeDate:str = obj["ChequeDate"]
      """  Cheque or ECS Date  """  
      self.AdditionalTranRef:str = obj["AdditionalTranRef"]
      """  Additional transaction reference (ECS).  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the report.  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  The date and time of submitting.  """  
      self.ReportStatus:int = obj["ReportStatus"]
      """  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  """  
      self.Notes:str = obj["Notes"]
      """  Report comment.  """  
      self.LatePaymentCharge:int = obj["LatePaymentCharge"]
      """  The charge paid for late filing of the tax returns.  """  
      self.NatureOfRemittance:str = obj["NatureOfRemittance"]
      """  Nature of Remittance.  """  
      self.CustomerList:str = obj["CustomerList"]
      """  Customer filter.  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Supplier filter.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax Type ID.  """  
      self.TaxLiabilityList:str = obj["TaxLiabilityList"]
      """  Tax Liability filter.  """  
      self.SubmitReportID:str = obj["SubmitReportID"]
      """  Submitted Report ID.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user who created the report.  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  The date and time of creating.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  The last user who changed the report.  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  The date and time of last changing.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PenaltyAmount:int = obj["PenaltyAmount"]
      """  Penalty amount.  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      """  Currency Symbol of base Currency.  """  
      self.BookID:str = obj["BookID"]
      """  Main Book ID.  """  
      self.IsClosed:bool = obj["IsClosed"]
      """  Report is closed for changing or not.  """  
      self.IsReady:bool = obj["IsReady"]
      """  Mark report to ready for submitting.  """  
      self.IsSubmitted:bool = obj["IsSubmitted"]
      """  Report was submitted or not.  """  
      self.LineTotalAmt:int = obj["LineTotalAmt"]
      """  Report Lines total amount.  """  
      self.SelectAll:bool = obj["SelectAll"]
      """  Select/Deselect all detail rows.  """  
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      """  Tax Type description.  """  
      self.TotalPaymentAmt:int = obj["TotalPaymentAmt"]
      """  Total payment amount (sum of WHTPaymentAmount, LatePaymentCharge, PenaltyAmount)  """  
      self.BaseCurrCode:str = obj["BaseCurrCode"]
      """  Currency Code of base Currency.  """  
      self.BaseCurrID:str = obj["BaseCurrID"]
      """  Currency ID of base Currency.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WHTPaymentInvDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  WHT Report ID.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start date of the report period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the report period.  """  
      self.Description:str = obj["Description"]
      """  Report Description.  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  Tax Entity Type.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account.  """  
      self.ReceiptNumber:str = obj["ReceiptNumber"]
      """  Bank receipt number.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Bank receipt date.  """  
      self.BankTranRefNum:str = obj["BankTranRefNum"]
      """  Bank transaction reference number (BSR Code).  """  
      self.PaymentDate:str = obj["PaymentDate"]
      """  Report payment date.  """  
      self.ChequeNumber:str = obj["ChequeNumber"]
      """  Cheque Number  """  
      self.ChequeDate:str = obj["ChequeDate"]
      """  Cheque or ECS Date  """  
      self.AdditionalTranRef:str = obj["AdditionalTranRef"]
      """  Additional transaction reference (ECS).  """  
      self.ReportStatus:int = obj["ReportStatus"]
      """  Report Status (0 - Created; 1 - Ready; 2 - Submitted; 3 - Closed)  """  
      self.NatureOfRemittance:str = obj["NatureOfRemittance"]
      """  Nature of Remittance.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Tax Type ID.  """  
      self.SubmitReportID:str = obj["SubmitReportID"]
      """  Submitted Report ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  Transaction Taxable Amount.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Transaction Tax Amount.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WHTPaymentInvDtlTableset:
   def __init__(self, obj):
      self.WHTPaymentInvDtl:list[Erp_Tablesets_WHTPaymentInvDtlRow] = obj["WHTPaymentInvDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WHTPaymentListTableset:
   def __init__(self, obj):
      self.WHTPaymentHeadList:list[Erp_Tablesets_WHTPaymentHeadListRow] = obj["WHTPaymentHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WHTPaymentTableset:
   def __init__(self, obj):
      self.WHTPaymentHead:list[Erp_Tablesets_WHTPaymentHeadRow] = obj["WHTPaymentHead"]
      self.WHTPaymentDtl:list[Erp_Tablesets_WHTPaymentDtlRow] = obj["WHTPaymentDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WHTPaymentListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewWHTPaymentDtl_input:
   """ Required : 
   ds
   reportID
   tranDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.tranDate:str = obj["tranDate"]
      pass

class GetNewWHTPaymentDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWHTPaymentHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class GetNewWHTPaymentHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWHTPaymentHead
   whereClauseWHTPaymentDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWHTPaymentHead:str = obj["whereClauseWHTPaymentHead"]
      self.whereClauseWHTPaymentDtl:str = obj["whereClauseWHTPaymentDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetWHTPaymentAPInvData_input:
   """ Required : 
   vendorNum
   invoiceNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  The Vendor Number  """  
      self.invoiceNum:str = obj["invoiceNum"]
      """  The AP Invoice Number  """  
      pass

class GetWHTPaymentAPInvData_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WHTPaymentInvDtlTableset] = obj["returnObj"]
      pass

class GetWHTaxRecords_input:
   """ Required : 
   reportID
   ds
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  WHT Report ID  """  
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class GetWHTaxRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
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

class OnChangeBankAcctID_input:
   """ Required : 
   bankAcctID
   ds
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  The proposed value of BankAcctID  """  
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class OnChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTaxCode_input:
   """ Required : 
   taxCode
   ds
   """  
   def __init__(self, obj):
      self.taxCode:str = obj["taxCode"]
      """  The proposed value of TaxCode  """  
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class OnChangeTaxCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemoveSelectedWHTaxRecords_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class RemoveSelectedWHTaxRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
      pass

class RemoveUnPaidWHTaxRecords_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class RemoveUnPaidWHTaxRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WHTPaymentTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWHTPaymentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWHTPaymentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WHTPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

