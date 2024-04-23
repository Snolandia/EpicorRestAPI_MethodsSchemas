import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CNGLJrnAttachmentsSvc
# Description: CN GL Journal Attachments Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CNGLJrnAttachments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNGLJrnAttachments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNGLJrnAttachments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNGLJrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachments",headers=creds) as resp:
           return await resp.json()

async def post_CNGLJrnAttachments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNGLJrnAttachments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNGLJrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNGLJrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNGLJrnAttachments_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNGLJrnAttachment item
   Description: Calls GetByID to retrieve the CNGLJrnAttachment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNGLJrnAttachment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNGLJrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachments(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNGLJrnAttachments_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNGLJrnAttachment for the service
   Description: Calls UpdateExt to update CNGLJrnAttachment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNGLJrnAttachment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNGLJrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachments(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNGLJrnAttachments_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_FiscalCalendarID(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, FiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNGLJrnAttachment item
   Description: Call UpdateExt to delete CNGLJrnAttachment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNGLJrnAttachment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachments(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + FiscalCalendarID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CNGLJrnAttachParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CNGLJrnAttachParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CNGLJrnAttachParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNGLJrnAttachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachParams",headers=creds) as resp:
           return await resp.json()

async def post_CNGLJrnAttachParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CNGLJrnAttachParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CNGLJrnAttachParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CNGLJrnAttachParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CNGLJrnAttachParams_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CNGLJrnAttachParam item
   Description: Calls GetByID to retrieve the CNGLJrnAttachParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CNGLJrnAttachParam
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CNGLJrnAttachParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachParams(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CNGLJrnAttachParams_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CNGLJrnAttachParam for the service
   Description: Calls UpdateExt to update CNGLJrnAttachParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CNGLJrnAttachParam
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CNGLJrnAttachParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachParams(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CNGLJrnAttachParams_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CNGLJrnAttachParam item
   Description: Call UpdateExt to delete CNGLJrnAttachParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CNGLJrnAttachParam
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/CNGLJrnAttachParams(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CNGLJrnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCNGLJrn, whereClauseCNGLJrnAttachParam, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCNGLJrn=" + whereClauseCNGLJrn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCNGLJrnAttachParam=" + whereClauseCNGLJrnAttachParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bookID, fiscalYear, fiscalYearSuffix, journalCode, journalNum, fiscalCalendarID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "bookID=" + bookID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYear=" + fiscalYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYearSuffix=" + fiscalYearSuffix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "journalCode=" + journalCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "journalNum=" + journalNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalCalendarID=" + fiscalCalendarID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSelParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSelParams
   Description: Gets new selection parameters row
   OperationID: GetNewSelParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSelParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSelParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfBookID
   Description: Change Book ID
   OperationID: OnChangeOfBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateParams
   Description: Validate parameters before Refresh
   OperationID: ValidateParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJournalsList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournalsList
   Description: Gets Journals List according to selection parameters
   OperationID: GetJournalsList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournalsList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalsList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCNGLJrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCNGLJrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCNGLJrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCNGLJrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCNGLJrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CNGLJrnAttachmentsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNGLJrnAttachParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNGLJrnAttachParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNGLJrnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNGLJrnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CNGLJrnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CNGLJrnRow] = obj["value"]
      pass

class Erp_Tablesets_CNGLJrnAttachParamRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.EndPeriod:int = obj["EndPeriod"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCodeList:str = obj["JournalCodeList"]
      self.StartPeriod:int = obj["StartPeriod"]
      self.WithEmptyAttachNum:bool = obj["WithEmptyAttachNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNGLJrnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.AttachCount:int = obj["AttachCount"]
      """  AttachCount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNGLJrnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.AttachCount:int = obj["AttachCount"]
      """  AttachCount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Description:str = obj["Description"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.PostedDate:str = obj["PostedDate"]
      self.SourceModule:str = obj["SourceModule"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CNGLJrnAttachParamRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.EndPeriod:int = obj["EndPeriod"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCodeList:str = obj["JournalCodeList"]
      self.StartPeriod:int = obj["StartPeriod"]
      self.WithEmptyAttachNum:bool = obj["WithEmptyAttachNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNGLJrnAttachmentsTableset:
   def __init__(self, obj):
      self.CNGLJrn:list[Erp_Tablesets_CNGLJrnRow] = obj["CNGLJrn"]
      self.CNGLJrnAttachParam:list[Erp_Tablesets_CNGLJrnAttachParamRow] = obj["CNGLJrnAttachParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNGLJrnListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.AttachCount:int = obj["AttachCount"]
      """  AttachCount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CNGLJrnListTableset:
   def __init__(self, obj):
      self.CNGLJrnList:list[Erp_Tablesets_CNGLJrnListRow] = obj["CNGLJrnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CNGLJrnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.AttachCount:int = obj["AttachCount"]
      """  AttachCount  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Description:str = obj["Description"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.PostedDate:str = obj["PostedDate"]
      self.SourceModule:str = obj["SourceModule"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCNGLJrnAttachmentsTableset:
   def __init__(self, obj):
      self.CNGLJrn:list[Erp_Tablesets_CNGLJrnRow] = obj["CNGLJrn"]
      self.CNGLJrnAttachParam:list[Erp_Tablesets_CNGLJrnAttachParamRow] = obj["CNGLJrnAttachParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   fiscalCalendarID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["returnObj"]
      pass

class GetJournalsList_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

class GetJournalsList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_CNGLJrnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCNGLJrn_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      pass

class GetNewCNGLJrn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSelParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

class GetNewSelParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCNGLJrn
   whereClauseCNGLJrnAttachParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCNGLJrn:str = obj["whereClauseCNGLJrn"]
      self.whereClauseCNGLJrnAttachParam:str = obj["whereClauseCNGLJrnAttachParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["returnObj"]
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

class OnChangeOfBookID_input:
   """ Required : 
   newGLBookID
   ds
   """  
   def __init__(self, obj):
      self.newGLBookID:str = obj["newGLBookID"]
      """  New BookID value  """  
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

class OnChangeOfBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNGLJrnAttachmentsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCNGLJrnAttachmentsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

class ValidateParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CNGLJrnAttachmentsTableset] = obj["ds"]
      pass

      """  output parameters  """  

