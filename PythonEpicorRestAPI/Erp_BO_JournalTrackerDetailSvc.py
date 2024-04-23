import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.JournalTrackerDetailSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_JournalTrackerDetails(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get JournalTrackerDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JournalTrackerDetails
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails",headers=creds) as resp:
           return await resp.json()

async def post_JournalTrackerDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JournalTrackerDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the JournalTrackerDetail item
   Description: Calls GetByID to retrieve the JournalTrackerDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JournalTrackerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update JournalTrackerDetail for the service
   Description: Calls UpdateExt to update JournalTrackerDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JournalTrackerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete JournalTrackerDetail item
   Description: Call UpdateExt to delete JournalTrackerDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JournalTrackerDetail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_GLJrnDtlAttches(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLJrnDtlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLJrnDtlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")/GLJrnDtlAttches",headers=creds) as resp:
           return await resp.json()

async def get_JournalTrackerDetails_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/JournalTrackerDetails(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + ")/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlAttch item
   Description: Calls GetByID to retrieve the GLJrnDtlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlAttch for the service
   Description: Calls UpdateExt to update GLJrnDtlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlAttches_Company_BookID_FiscalYear_FiscalYearSuffix_JournalCode_JournalNum_JournalLine_DrawingSeq(Company, BookID, FiscalYear, FiscalYearSuffix, JournalCode, JournalNum, JournalLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlAttch item
   Description: Call UpdateExt to delete GLJrnDtlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BookID: Desc: BookID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param JournalNum: Desc: JournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlAttches(" + Company + "," + BookID + "," + FiscalYear + "," + FiscalYearSuffix + "," + JournalCode + "," + JournalNum + "," + JournalLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJournalTrackers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJournalTrackers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJournalTrackers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJournalTrackerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers",headers=creds) as resp:
           return await resp.json()

async def post_GLJournalTrackers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJournalTrackers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJournalTrackerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJournalTrackerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJournalTrackers_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJournalTracker item
   Description: Calls GetByID to retrieve the GLJournalTracker item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJournalTracker
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJournalTrackerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJournalTrackers_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJournalTracker for the service
   Description: Calls UpdateExt to update GLJournalTracker. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJournalTracker
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJournalTrackerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJournalTrackers_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJournalTracker item
   Description: Call UpdateExt to delete GLJournalTracker item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJournalTracker
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJournalTrackers(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlDEASches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLJrnDtlMnlDEASches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnDtlMnlDEASches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlMnlDEASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches",headers=creds) as resp:
           return await resp.json()

async def post_GLJrnDtlMnlDEASches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnDtlMnlDEASches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, GLBookID, JournalCode, GLJournalNum, JournalLine, AmortSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item
   Description: Calls GetByID to retrieve the GLJrnDtlMnlDEASch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnDtlMnlDEASch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, GLBookID, JournalCode, GLJournalNum, JournalLine, AmortSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLJrnDtlMnlDEASch for the service
   Description: Calls UpdateExt to update GLJrnDtlMnlDEASch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnDtlMnlDEASch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnDtlMnlDEASchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLJrnDtlMnlDEASches_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_GLBookID_JournalCode_GLJournalNum_JournalLine_AmortSeq(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, GLBookID, JournalCode, GLJournalNum, JournalLine, AmortSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLJrnDtlMnlDEASch item
   Description: Call UpdateExt to delete GLJrnDtlMnlDEASch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnDtlMnlDEASch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param GLBookID: Desc: GLBookID   Required: True   Allow empty value : True
      :param JournalCode: Desc: JournalCode   Required: True   Allow empty value : True
      :param GLJournalNum: Desc: GLJournalNum   Required: True
      :param JournalLine: Desc: JournalLine   Required: True
      :param AmortSeq: Desc: AmortSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/GLJrnDtlMnlDEASches(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + GLBookID + "," + JournalCode + "," + GLJournalNum + "," + JournalLine + "," + AmortSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TranGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TranGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TranGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs",headers=creds) as resp:
           return await resp.json()

async def post_TranGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TranGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TranGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TranGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TranGLCs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TranGLC item
   Description: Calls GetByID to retrieve the TranGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TranGLC
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TranGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TranGLCs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TranGLC for the service
   Description: Calls UpdateExt to update TranGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TranGLC
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TranGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TranGLCs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TranGLC item
   Description: Call UpdateExt to delete TranGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TranGLC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/TranGLCs(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLJrnDtl, whereClauseGLJrnDtlAttch, whereClauseGLJournalTracker, whereClauseGLJrnDtlMnlDEASch, whereClauseTranGLC, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseGLJrnDtl=" + whereClauseGLJrnDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnDtlAttch=" + whereClauseGLJrnDtlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJournalTracker=" + whereClauseGLJournalTracker
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLJrnDtlMnlDEASch=" + whereClauseGLJrnDtlMnlDEASch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTranGLC=" + whereClauseTranGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bookID, fiscalYear, fiscalYearSuffix, journalCode, journalNum, journalLine, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "journalLine=" + journalLine

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_LoadGLJournalTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LoadGLJournalTracker
   Description: Creates the initial GLTrackerView record
   OperationID: LoadGLJournalTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LoadGLJournalTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadGLJournalTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJournalDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournalDetail
   Description: Filter journals by Journal Code and Journal Number.
   OperationID: GetJournalDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournalDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJournalDetailByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournalDetailByID
   Description: Invokes GetJournalDetail using the values passed in
   OperationID: GetJournalDetailByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournalDetailByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalDetailByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranGLCHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranGLCHead
   Description: This method replaces the standard GetRows method
   OperationID: GetTranGLCHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranGLCHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranGLCHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranGLCHeadSite(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranGLCHeadSite
   Description: This method replaces the standard GetRows method
   OperationID: GetTranGLCHeadSite
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranGLCHeadSite_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranGLCHeadSite_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLJrnDtlMnlDEASch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLJrnDtlMnlDEASch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnDtlMnlDEASch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnDtlMnlDEASch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTranGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTranGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTranGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTranGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTranGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.JournalTrackerDetailSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJournalTrackerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJournalTrackerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLJrnDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TranGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TranGLCRow] = obj["value"]
      pass

class Erp_Tablesets_GLJournalTrackerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.GLBookDesc:str = obj["GLBookDesc"]
      self.TotDebit:int = obj["TotDebit"]
      self.TotCredit:int = obj["TotCredit"]
      self.JournalCodeDesc:str = obj["JournalCodeDesc"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyCodeDesc:str = obj["CurrencyCodeDesc"]
      self.Balance:int = obj["Balance"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  AmortSeq  """  
      self.SchFiscalCalendarID:str = obj["SchFiscalCalendarID"]
      """  SchFiscalCalendarID  """  
      self.SchFiscalYear:int = obj["SchFiscalYear"]
      """  SchFiscalYear  """  
      self.SchFiscalYearSuffix:str = obj["SchFiscalYearSuffix"]
      """  SchFiscalYearSuffix  """  
      self.SchFiscalPeriod:int = obj["SchFiscalPeriod"]
      """  SchFiscalPeriod  """  
      self.AmortDate:str = obj["AmortDate"]
      """  AmortDate  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  AmortPercent  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  AmortAmt  """  
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      """  DocAmortAmt  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  PostedDate  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  Rpt1AmortAmt  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Document currency  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  Rpt2AmortAmt  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  Rpt3AmortAmt  """  
      self.GLBookID:str = obj["GLBookID"]
      """  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  """  
      self.GLJournalNum:int = obj["GLJournalNum"]
      """  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  """  
      self.DispAmortAmt:int = obj["DispAmortAmt"]
      """  DispAmortAmt  """  
      self.DispDocAmortAmt:int = obj["DispDocAmortAmt"]
      """  DispDocAmortAmt  """  
      self.HasReverseLines:bool = obj["HasReverseLines"]
      """  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  Account Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.COOneTimeDesc:str = obj["COOneTimeDesc"]
      """   Colombia Loc field            
This field is used as external calculated only.  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """   Colombia Loc field.           
This field is used as external calculated only.  """  
      self.DEACodeDesc:str = obj["DEACodeDesc"]
      """  DEA Code  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEA End Date  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEA Start Date  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  Deferred Expense  """  
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.ExtRefAcctChart:str = obj["ExtRefAcctChart"]
      self.ExtRefAcctDept:str = obj["ExtRefAcctDept"]
      self.ExtRefAcctDiv:str = obj["ExtRefAcctDiv"]
      self.ExtRefCodeStatus:str = obj["ExtRefCodeStatus"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.HeaderCommentText:str = obj["HeaderCommentText"]
      """  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  """  
      self.LineReference:str = obj["LineReference"]
      """  Manual GL Journal Line Reference.  """  
      self.LineReferenceHolder:str = obj["LineReferenceHolder"]
      """  Manual GL Journal Line Reference Holder.  """  
      self.LineReferenceHolderName:str = obj["LineReferenceHolderName"]
      """  Manual GL Journal Line Reference Holder Name.  """  
      self.LineReferenceType:str = obj["LineReferenceType"]
      """  Manual GL Journal Line Reference Type.  """  
      self.MovementNum:int = obj["MovementNum"]
      self.OrigApplyDate:str = obj["OrigApplyDate"]
      """  Apply Date of the Original Transaction  """  
      self.OrigJrnlLine:int = obj["OrigJrnlLine"]
      """  Journal line of the original transaction that was reversed.  """  
      self.OrigJrnlNbr:int = obj["OrigJrnlNbr"]
      """  Journal number of the original transaction that was reversed.  """  
      self.OrigJrnlYear:int = obj["OrigJrnlYear"]
      """  Fiscal year of the original transaction that was reversed.  """  
      self.OrigJrnlYearSuffix:str = obj["OrigJrnlYearSuffix"]
      """  Fiscal year suffix of the original transaction that was reversed.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.RevApplyDate:str = obj["RevApplyDate"]
      """  Apply date of the reversing transaction  """  
      self.RevJrnlLine:int = obj["RevJrnlLine"]
      """  Journal line of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlNbr:int = obj["RevJrnlNbr"]
      """  Journal number of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYear:int = obj["RevJrnlYear"]
      """  Fiscal year of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYearSuffix:str = obj["RevJrnlYearSuffix"]
      """  Fiscal year suffix of the latest journal entry made to reverse a transaction.  """  
      self.StatAmount:int = obj["StatAmount"]
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BookCurrencySymbol:str = obj["BookCurrencySymbol"]
      self.EntityDescription:str = obj["EntityDescription"]
      """  Description of the entity the journal detail is for  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAccount:str = obj["GLAccountGLAccount"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.SrcGLAccountGLShortAcct:str = obj["SrcGLAccountGLShortAcct"]
      self.SrcGLAccountAccountDesc:str = obj["SrcGLAccountAccountDesc"]
      self.SrcGLAccountGLAcctDisp:str = obj["SrcGLAccountGLAcctDisp"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TranGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.APTranNo:int = obj["APTranNo"]
      """  AP Tran Number  """  
      self.APTranVoided:bool = obj["APTranVoided"]
      """  Indicates if the AP Transaction is voided  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankGroupID:str = obj["BankGroupID"]
      """  Bank Group ID  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Tran Number  """  
      self.BankTranVoided:bool = obj["BankTranVoided"]
      """  Indicates if the Bank Transaction has been voided  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.CashHeadNum:int = obj["CashHeadNum"]
      """  Cash Head Number  """  
      self.CashHedGroup:str = obj["CashHedGroup"]
      """  Cash Head Group ID  """  
      self.CashInvRef:int = obj["CashInvRef"]
      """  Cash Detail Invoice Reference  """  
      self.CheckHeadNum:int = obj["CheckHeadNum"]
      """  Chead Head Number  """  
      self.CheckHedVoided:bool = obj["CheckHedVoided"]
      """  Indicates if the Check Header has been voided.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Container ID  """  
      self.DocumentText:str = obj["DocumentText"]
      self.DocumentType:str = obj["DocumentType"]
      self.Key1Label:str = obj["Key1Label"]
      """  Used to display a context sensitive label for Key1.  This data is set on the server side and is translateable.  """  
      self.Key2Label:str = obj["Key2Label"]
      """  Used to display a context sensitive label for Key2.  This data is set on the server side and is translateable.  """  
      self.Key3Label:str = obj["Key3Label"]
      """  Used to display a context sensitive label for Key3.  This data is set on the server side and is translateable.  """  
      self.Key4Label:str = obj["Key4Label"]
      """  Used to display a context sensitive label for Key4.  This data is set on the server side and is translateable.  """  
      self.Key5Label:str = obj["Key5Label"]
      """  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  """  
      self.Key6Label:str = obj["Key6Label"]
      """  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  """  
      self.Packslip:str = obj["Packslip"]
      """  Purchase order receipt pack slip number  """  
      self.POLine:int = obj["POLine"]
      """  Purchase Order Line Number  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order Number  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.RateCodeDesc:str = obj["RateCodeDesc"]
      self.StatAmount:int = obj["StatAmount"]
      self.SupplierName:str = obj["SupplierName"]
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  The Taxable Amount if the current TranGLc record is related to the InvcTax or APInvTax tables.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.TaxCode:str = obj["TaxCode"]
      self.TaxCodeDesc:str = obj["TaxCodeDesc"]
      self.TaxRatePercent:int = obj["TaxRatePercent"]
      """  The percent of the rate if current TranGLC record is related to the InvcTax or APInvTax tables  """  
      self.APHeadNum:int = obj["APHeadNum"]
      """  AP Tran head Number  """  
      self.HideKey2:bool = obj["HideKey2"]
      self.HideKey3:bool = obj["HideKey3"]
      self.HideKey4:bool = obj["HideKey4"]
      self.HideKey5:bool = obj["HideKey5"]
      self.HideKey6:bool = obj["HideKey6"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.FiscalCalendarDescription:str = obj["FiscalCalendarDescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.InvoiceLineLineDesc:str = obj["InvoiceLineLineDesc"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
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
   journalLine
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLJournalTrackerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.GLBookDesc:str = obj["GLBookDesc"]
      self.TotDebit:int = obj["TotDebit"]
      self.TotCredit:int = obj["TotCredit"]
      self.JournalCodeDesc:str = obj["JournalCodeDesc"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyCodeDesc:str = obj["CurrencyCodeDesc"]
      self.Balance:int = obj["Balance"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  MXFiscalFolio  """  
      self.MXRFC:str = obj["MXRFC"]
      """  MXRFC  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BookID:str = obj["BookID"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.JournalCode:str = obj["JournalCode"]
      self.JournalNum:int = obj["JournalNum"]
      self.JournalLine:int = obj["JournalLine"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlListTableset:
   def __init__(self, obj):
      self.GLJrnDtlList:list[Erp_Tablesets_GLJrnDtlListRow] = obj["GLJrnDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLJrnDtlMnlDEASchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  FiscalCalendarID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode  """  
      self.JournalNum:int = obj["JournalNum"]
      """  JournalNum  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine  """  
      self.AmortSeq:int = obj["AmortSeq"]
      """  AmortSeq  """  
      self.SchFiscalCalendarID:str = obj["SchFiscalCalendarID"]
      """  SchFiscalCalendarID  """  
      self.SchFiscalYear:int = obj["SchFiscalYear"]
      """  SchFiscalYear  """  
      self.SchFiscalYearSuffix:str = obj["SchFiscalYearSuffix"]
      """  SchFiscalYearSuffix  """  
      self.SchFiscalPeriod:int = obj["SchFiscalPeriod"]
      """  SchFiscalPeriod  """  
      self.AmortDate:str = obj["AmortDate"]
      """  AmortDate  """  
      self.AmortPercent:int = obj["AmortPercent"]
      """  AmortPercent  """  
      self.AmortAmt:int = obj["AmortAmt"]
      """  AmortAmt  """  
      self.DocAmortAmt:int = obj["DocAmortAmt"]
      """  DocAmortAmt  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.PostedDate:str = obj["PostedDate"]
      """  PostedDate  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  LegalNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1AmortAmt:int = obj["Rpt1AmortAmt"]
      """  Rpt1AmortAmt  """  
      self.GroupID:str = obj["GroupID"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Document currency  """  
      self.Rpt2AmortAmt:int = obj["Rpt2AmortAmt"]
      """  Rpt2AmortAmt  """  
      self.Rpt3AmortAmt:int = obj["Rpt3AmortAmt"]
      """  Rpt3AmortAmt  """  
      self.GLBookID:str = obj["GLBookID"]
      """  Used for Tracker only for records from GLJournalEntry. BookID in GLJrnDtl. The same as BookID field value for Single-book mode.  """  
      self.GLJournalNum:int = obj["GLJournalNum"]
      """  Used for Tracker only for records from GLJournalEntry. Journal Number in GLJrnDtl. The same as JournalNum field value for Single-book mode.  """  
      self.DispAmortAmt:int = obj["DispAmortAmt"]
      """  DispAmortAmt  """  
      self.DispDocAmortAmt:int = obj["DispDocAmortAmt"]
      """  DispDocAmortAmt  """  
      self.HasReverseLines:bool = obj["HasReverseLines"]
      """  Indicates if this recognized Deferred Expense Amortization transaction has reverse lines  """  
      self.CurrencyCodeAcct:str = obj["CurrencyCodeAcct"]
      """  Account Currency  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLJrnDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Number that is assigned by the system. The Journal number is a way of relating the detail entries into a group that would normally balance.  The system assigns this number by finding  the journalnum of the last record for the fiscal year and adding one.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  A system assigned number to which is used along with the company, FiscalYear and JournalNum to uniquely identify the record.  System determines number by reading last record for a specific Company/FiscalYear/JournalNum combination and adding 1.  """  
      self.Description:str = obj["Description"]
      """  Describes the journal transaction. Defaulted from GLJrnHed in journal entry program.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.GroupID:str = obj["GroupID"]
      """  The data entry Group that the journal entry is assigned to. This field is not directly maintainable, it is assigned by the entry program using the GroupID of the "current" group that the user is working with.  It is used as a selection criteria during the posting process.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  User ID that posted this translation.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates if this entry has been posted to the G/L master balance files. Unposted entries are excluded from all G/L reports.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctId of the BankAcct master that this check was drawn  against.  """  
      self.CheckNum:int = obj["CheckNum"]
      """  Check number.  """  
      self.CRHeadNum:int = obj["CRHeadNum"]
      """  Cash Receipts reference field.  """  
      self.Reverse:bool = obj["Reverse"]
      """  Indicates that the transaction is a reversing entry created during the journal entry post for GLJrnHed transactions when flagged as Reverse = YES.  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Transaction Number.  Used when a transaction is a direct transfer from one bank account to another.  """  
      self.BankSlip:str = obj["BankSlip"]
      """   The identifier of the Bank Slip document (bank statement).  The user enters a bank slip during the reconciliation process.  This is then written into the related GLJrnDtl records.
Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.ExtRefType:str = obj["ExtRefType"]
      """  Multi-Company G/L Reference Type from the external company.  This is used by the Multi-Company Journal.  """  
      self.ExtRefCode:str = obj["ExtRefCode"]
      """  Multi-Company G/L Reference Code from the external company.  This is used by the Multi-Company Journal.  """  
      self.GlbJournalNum:int = obj["GlbJournalNum"]
      """  The Journal Number assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalLine:int = obj["GlbJournalLine"]
      """  The Journal Line assigned at the destination or target company when this Multi-Company Journal is created.  """  
      self.GlbJournalCode:str = obj["GlbJournalCode"]
      """  Journal Code used by the Multi-Company Journal when it gets created at the target external company.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor number.  Used by Multi-Company Journal.  """  
      self.GlbAPInvoiceNum:str = obj["GlbAPInvoiceNum"]
      """  Global AP Invoice identifier.  Used by Multi-Company Journal.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  Flag to indicate that a separate journal entry will be created at the target company for the Multi-Company G/L Account entered in this journal line.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to a Multi-Company Journal.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal line entry.  Defaults from GLJrnHed.CommentText.  """  
      self.GlbCompanyID:str = obj["GlbCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.GlbFiscalYear:int = obj["GlbFiscalYear"]
      """  The fiscal year for this journal transaction header from the external company. Assigned from GLJrnGrp.FiscalYear.  """  
      self.GlbFiscalPeriod:int = obj["GlbFiscalPeriod"]
      """  Fiscal period from the external company that this journal entry applies to.  """  
      self.GlbGroupID:str = obj["GlbGroupID"]
      """  The data entry Group from the external company that the journal entry is assigned to.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  External Segment Value 2  """  
      self.ExtSegValue3:str = obj["ExtSegValue3"]
      """  External Segment Value 3  """  
      self.ExtSegValue4:str = obj["ExtSegValue4"]
      """  External Segment Value 4  """  
      self.ExtSegValue5:str = obj["ExtSegValue5"]
      """  External Segment Value 5  """  
      self.ExtSegValue6:str = obj["ExtSegValue6"]
      """  External Segment Value 6  """  
      self.ExtSegValue7:str = obj["ExtSegValue7"]
      """  External Segment Value 7  """  
      self.ExtSegValue8:str = obj["ExtSegValue8"]
      """  External Segment Value 8  """  
      self.ExtSegValue9:str = obj["ExtSegValue9"]
      """  External Segment Value 9  """  
      self.ExtSegValue10:str = obj["ExtSegValue10"]
      """  External Segment Value 10  """  
      self.ExtSegValue11:str = obj["ExtSegValue11"]
      """  External Segment Value 11  """  
      self.ExtSegValue12:str = obj["ExtSegValue12"]
      """  External Segment Value 12  """  
      self.ExtSegValue13:str = obj["ExtSegValue13"]
      """  External Segment Value 13  """  
      self.ExtSegValue14:str = obj["ExtSegValue14"]
      """  External Segment Value 14  """  
      self.ExtSegValue15:str = obj["ExtSegValue15"]
      """  External Segment Value 15  """  
      self.ExtSegValue16:str = obj["ExtSegValue16"]
      """  External Segment Value 16  """  
      self.ExtSegValue17:str = obj["ExtSegValue17"]
      """  External Segment Value 17  """  
      self.ExtSegValue18:str = obj["ExtSegValue18"]
      """  External Segment Value 18  """  
      self.ExtSegValue19:str = obj["ExtSegValue19"]
      """  External Segment Value 19  """  
      self.ExtSegValue20:str = obj["ExtSegValue20"]
      """  External Segment Value 20  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of source document  """  
      self.PerBalFlag:bool = obj["PerBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.TBFlag:bool = obj["TBFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.DailyBalFlag:bool = obj["DailyBalFlag"]
      """  Indicates if this record has been processed by the balance logic.  Yes - the record has been processed.  No - the record needs to be processed.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GlbFiscalYearSuffix:str = obj["GlbFiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.GlbFiscalCalendarID:str = obj["GlbFiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IntermediateProc:bool = obj["IntermediateProc"]
      """  Identifies the journal entry as one processed by consolidation posting mode where the data transfer is immediate and an intermediate book is used.  """  
      self.GenID:int = obj["GenID"]
      """  Internal system calculated sequence number not inteneded for external use.  """  
      self.SrcCompany:str = obj["SrcCompany"]
      """  Source Company Identifier.  Identifies the company where this GLJrnDtl originated from.  """  
      self.SrcBook:str = obj["SrcBook"]
      """  Unique Book Identifier  This is the book that is being consolidated into a target book.  """  
      self.SrcGLAccount:str = obj["SrcGLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the internal segment separator.  This is the unique identifier for the GL Account and is stored in physical segment number sequence with the vertical bar as its separator.  This field is not intended for end user display.  It is used internally as a unique identifier.  The display format GL Account is found in table GLAcctDisp.  """  
      self.SrcJrnlCode:str = obj["SrcJrnlCode"]
      """  Source Journal Code  """  
      self.SrcJournalNum:int = obj["SrcJournalNum"]
      """  Source Journal Number  """  
      self.SrcJournalLine:int = obj["SrcJournalLine"]
      """  Source Journal Line  """  
      self.SrcType:str = obj["SrcType"]
      """   P = derived from Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equas ABTUID which was created during posting  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  This field shows Debit value of transaction  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  This field shows Credit value of transaction  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  This field shows Debit value of transaction recalculated from DebitAmount according to Currency of mentioned Book  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  This field shows Credit value of transaction recalculated from CreditAmount according to Currency of mentioned Book  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.BalanceAcct:str = obj["BalanceAcct"]
      """  This is the resolved balance account the period balance, currency balance and/or daily balance records were written under for this GL Journal Detail GL Account.  """  
      self.TrialAcct:str = obj["TrialAcct"]
      """  This is the resolved balance account the trial balance records were written under for this GL Journal Detail GL Account.  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp that affected this GLJrnDtl.  """  
      self.BatchID:str = obj["BatchID"]
      """  Identifies the allocation batch this journal entry was processed under.  """  
      self.AllocID:str = obj["AllocID"]
      """  This is the allocation id that processed this journal entry.  """  
      self.RunNbr:int = obj["RunNbr"]
      """  The allocation run number is a unique sequential number that identifies which run of an allocation batch this journal entry was created under.  """  
      self.AllocRunNbr:int = obj["AllocRunNbr"]
      """  Intended for internal use only.  Updated by the Advanced Allocations Engine.  This identifies the last allocation run number that used this GLJrnDtl as a source record.  """  
      self.AllocTgtNbr:int = obj["AllocTgtNbr"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.AllocTgtSeq:int = obj["AllocTgtSeq"]
      """  Internal next number sequence used to keep the records unique.  Not intended for display or use by the end user.  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA Code  """  
      self.MatchCode:str = obj["MatchCode"]
      """  MatchCode is used to match two or more journal detail records together.  """  
      self.MatchDate:str = obj["MatchDate"]
      """  MatchDate is set when the journal detail record is matched to other journal detail records.  """  
      self.Reconciled:bool = obj["Reconciled"]
      """  Indicates whether or not the transaction has been flagged as reconciled.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.PaymentNumber:str = obj["PaymentNumber"]
      """  PaymentNumber  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Sequence:int = obj["Sequence"]
      """  Journal Sequence Number  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.COOneTimeDesc:str = obj["COOneTimeDesc"]
      """   Colombia Loc field            
This field is used as external calculated only.  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """   Colombia Loc field.           
This field is used as external calculated only.  """  
      self.DEACodeDesc:str = obj["DEACodeDesc"]
      """  DEA Code  """  
      self.DEAEndDate:str = obj["DEAEndDate"]
      """  DEA End Date  """  
      self.DEAStartDate:str = obj["DEAStartDate"]
      """  DEA Start Date  """  
      self.DeferredExp:bool = obj["DeferredExp"]
      """  Deferred Expense  """  
      self.Distributed:int = obj["Distributed"]
      """  DEA Distributed Amount  """  
      self.DocDistributed:int = obj["DocDistributed"]
      """  DEA Distributed Amount in Doc Currency  """  
      self.DocExpense:int = obj["DocExpense"]
      """  DEA Expense Amount in Doc Currency  """  
      self.DocRecognized:int = obj["DocRecognized"]
      """  DEA Recognized Amount in Doc Currency  """  
      self.DocRemaining:int = obj["DocRemaining"]
      """  DEA Remaining Amount in Doc Currency  """  
      self.DocUnrecognized:int = obj["DocUnrecognized"]
      """  DEA Unrecognized Amount in Doc Currency  """  
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      """  Flag to indicate if the MultiCompany check box needs to be enabled.  """  
      self.Expense:int = obj["Expense"]
      """  DEA Expense Amount  """  
      self.ExtRefAcctChart:str = obj["ExtRefAcctChart"]
      self.ExtRefAcctDept:str = obj["ExtRefAcctDept"]
      self.ExtRefAcctDiv:str = obj["ExtRefAcctDiv"]
      self.ExtRefCodeStatus:str = obj["ExtRefCodeStatus"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.HeaderCommentText:str = obj["HeaderCommentText"]
      """  External field used in Journal Tracker and Chart tracker. Journal Comments tab.  """  
      self.LineReference:str = obj["LineReference"]
      """  Manual GL Journal Line Reference.  """  
      self.LineReferenceHolder:str = obj["LineReferenceHolder"]
      """  Manual GL Journal Line Reference Holder.  """  
      self.LineReferenceHolderName:str = obj["LineReferenceHolderName"]
      """  Manual GL Journal Line Reference Holder Name.  """  
      self.LineReferenceType:str = obj["LineReferenceType"]
      """  Manual GL Journal Line Reference Type.  """  
      self.MovementNum:int = obj["MovementNum"]
      self.OrigApplyDate:str = obj["OrigApplyDate"]
      """  Apply Date of the Original Transaction  """  
      self.OrigJrnlLine:int = obj["OrigJrnlLine"]
      """  Journal line of the original transaction that was reversed.  """  
      self.OrigJrnlNbr:int = obj["OrigJrnlNbr"]
      """  Journal number of the original transaction that was reversed.  """  
      self.OrigJrnlYear:int = obj["OrigJrnlYear"]
      """  Fiscal year of the original transaction that was reversed.  """  
      self.OrigJrnlYearSuffix:str = obj["OrigJrnlYearSuffix"]
      """  Fiscal year suffix of the original transaction that was reversed.  """  
      self.Recognized:int = obj["Recognized"]
      """  DEA Recognized Amount  """  
      self.RefAcctChart:str = obj["RefAcctChart"]
      self.RefAcctDept:str = obj["RefAcctDept"]
      self.RefAcctDiv:str = obj["RefAcctDiv"]
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Remaining:int = obj["Remaining"]
      """  DEA Remaining Amount  """  
      self.RevApplyDate:str = obj["RevApplyDate"]
      """  Apply date of the reversing transaction  """  
      self.RevJrnlLine:int = obj["RevJrnlLine"]
      """  Journal line of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlNbr:int = obj["RevJrnlNbr"]
      """  Journal number of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYear:int = obj["RevJrnlYear"]
      """  Fiscal year of the latest journal entry made to reverse a transaction.  """  
      self.RevJrnlYearSuffix:str = obj["RevJrnlYearSuffix"]
      """  Fiscal year suffix of the latest journal entry made to reverse a transaction.  """  
      self.StatAmount:int = obj["StatAmount"]
      self.TotCredit:int = obj["TotCredit"]
      self.TotDebit:int = obj["TotDebit"]
      self.Unrecognized:int = obj["Unrecognized"]
      """  DEA Unrecognized Amount  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BookCurrencySymbol:str = obj["BookCurrencySymbol"]
      self.EntityDescription:str = obj["EntityDescription"]
      """  Description of the entity the journal detail is for  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAccount:str = obj["GLAccountGLAccount"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.SrcGLAccountGLShortAcct:str = obj["SrcGLAccountGLShortAcct"]
      self.SrcGLAccountAccountDesc:str = obj["SrcGLAccountAccountDesc"]
      self.SrcGLAccountGLAcctDisp:str = obj["SrcGLAccountGLAcctDisp"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JournalTrackerDetailTableset:
   def __init__(self, obj):
      self.GLJrnDtl:list[Erp_Tablesets_GLJrnDtlRow] = obj["GLJrnDtl"]
      self.GLJrnDtlAttch:list[Erp_Tablesets_GLJrnDtlAttchRow] = obj["GLJrnDtlAttch"]
      self.GLJournalTracker:list[Erp_Tablesets_GLJournalTrackerRow] = obj["GLJournalTracker"]
      self.GLJrnDtlMnlDEASch:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["GLJrnDtlMnlDEASch"]
      self.TranGLC:list[Erp_Tablesets_TranGLCRow] = obj["TranGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TranGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.APTranNo:int = obj["APTranNo"]
      """  AP Tran Number  """  
      self.APTranVoided:bool = obj["APTranVoided"]
      """  Indicates if the AP Transaction is voided  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankGroupID:str = obj["BankGroupID"]
      """  Bank Group ID  """  
      self.BankTranNum:int = obj["BankTranNum"]
      """  Bank Tran Number  """  
      self.BankTranVoided:bool = obj["BankTranVoided"]
      """  Indicates if the Bank Transaction has been voided  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.CashHeadNum:int = obj["CashHeadNum"]
      """  Cash Head Number  """  
      self.CashHedGroup:str = obj["CashHedGroup"]
      """  Cash Head Group ID  """  
      self.CashInvRef:int = obj["CashInvRef"]
      """  Cash Detail Invoice Reference  """  
      self.CheckHeadNum:int = obj["CheckHeadNum"]
      """  Chead Head Number  """  
      self.CheckHedVoided:bool = obj["CheckHedVoided"]
      """  Indicates if the Check Header has been voided.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Container ID  """  
      self.DocumentText:str = obj["DocumentText"]
      self.DocumentType:str = obj["DocumentType"]
      self.Key1Label:str = obj["Key1Label"]
      """  Used to display a context sensitive label for Key1.  This data is set on the server side and is translateable.  """  
      self.Key2Label:str = obj["Key2Label"]
      """  Used to display a context sensitive label for Key2.  This data is set on the server side and is translateable.  """  
      self.Key3Label:str = obj["Key3Label"]
      """  Used to display a context sensitive label for Key3.  This data is set on the server side and is translateable.  """  
      self.Key4Label:str = obj["Key4Label"]
      """  Used to display a context sensitive label for Key4.  This data is set on the server side and is translateable.  """  
      self.Key5Label:str = obj["Key5Label"]
      """  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  """  
      self.Key6Label:str = obj["Key6Label"]
      """  Used to display a context sensitive label for Key6.  This data is set on the server side and is translateable.  """  
      self.Packslip:str = obj["Packslip"]
      """  Purchase order receipt pack slip number  """  
      self.POLine:int = obj["POLine"]
      """  Purchase Order Line Number  """  
      self.PONum:int = obj["PONum"]
      """  Purchase Order Number  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.RateCodeDesc:str = obj["RateCodeDesc"]
      self.StatAmount:int = obj["StatAmount"]
      self.SupplierName:str = obj["SupplierName"]
      self.TaxableAmt:int = obj["TaxableAmt"]
      """  The Taxable Amount if the current TranGLc record is related to the InvcTax or APInvTax tables.  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.TaxCode:str = obj["TaxCode"]
      self.TaxCodeDesc:str = obj["TaxCodeDesc"]
      self.TaxRatePercent:int = obj["TaxRatePercent"]
      """  The percent of the rate if current TranGLC record is related to the InvcTax or APInvTax tables  """  
      self.APHeadNum:int = obj["APHeadNum"]
      """  AP Tran head Number  """  
      self.HideKey2:bool = obj["HideKey2"]
      self.HideKey3:bool = obj["HideKey3"]
      self.HideKey4:bool = obj["HideKey4"]
      self.HideKey5:bool = obj["HideKey5"]
      self.HideKey6:bool = obj["HideKey6"]
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.FiscalCalendarDescription:str = obj["FiscalCalendarDescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.InvoiceLineLineDesc:str = obj["InvoiceLineLineDesc"]
      self.InvoiceNumTermsCode:str = obj["InvoiceNumTermsCode"]
      self.InvoiceNumCardMemberName:str = obj["InvoiceNumCardMemberName"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtJournalTrackerDetailTableset:
   def __init__(self, obj):
      self.GLJrnDtl:list[Erp_Tablesets_GLJrnDtlRow] = obj["GLJrnDtl"]
      self.GLJrnDtlAttch:list[Erp_Tablesets_GLJrnDtlAttchRow] = obj["GLJrnDtlAttch"]
      self.GLJournalTracker:list[Erp_Tablesets_GLJournalTrackerRow] = obj["GLJournalTracker"]
      self.GLJrnDtlMnlDEASch:list[Erp_Tablesets_GLJrnDtlMnlDEASchRow] = obj["GLJrnDtlMnlDEASch"]
      self.TranGLC:list[Erp_Tablesets_TranGLCRow] = obj["TranGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   journalLine
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
      pass

class GetJournalDetailByID_input:
   """ Required : 
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      pass

class GetJournalDetailByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
      pass

class GetJournalDetail_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

class GetJournalDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_GLJrnDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlAttch_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   journalLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetNewGLJrnDtlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtlMnlDEASch_input:
   """ Required : 
   ds
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   glBookID
   journalCode
   glJournalNum
   journalLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.glBookID:str = obj["glBookID"]
      self.journalCode:str = obj["journalCode"]
      self.glJournalNum:int = obj["glJournalNum"]
      self.journalLine:int = obj["journalLine"]
      pass

class GetNewGLJrnDtlMnlDEASch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLJrnDtl_input:
   """ Required : 
   ds
   bookID
   fiscalYear
   fiscalYearSuffix
   journalCode
   journalNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.journalCode:str = obj["journalCode"]
      self.journalNum:int = obj["journalNum"]
      pass

class GetNewGLJrnDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTranGLC_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

class GetNewTranGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLJrnDtl
   whereClauseGLJrnDtlAttch
   whereClauseGLJournalTracker
   whereClauseGLJrnDtlMnlDEASch
   whereClauseTranGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLJrnDtl:str = obj["whereClauseGLJrnDtl"]
      self.whereClauseGLJrnDtlAttch:str = obj["whereClauseGLJrnDtlAttch"]
      self.whereClauseGLJournalTracker:str = obj["whereClauseGLJournalTracker"]
      self.whereClauseGLJrnDtlMnlDEASch:str = obj["whereClauseGLJrnDtlMnlDEASch"]
      self.whereClauseTranGLC:str = obj["whereClauseTranGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTranGLCHeadSite_input:
   """ Required : 
   vJournalCode
   vBookID
   vTaxCode
   vSiteList
   """  
   def __init__(self, obj):
      self.vJournalCode:str = obj["vJournalCode"]
      """  Journal Code  """  
      self.vBookID:str = obj["vBookID"]
      """  Book ID  """  
      self.vTaxCode:str = obj["vTaxCode"]
      """  Tax Code  """  
      self.vSiteList:str = obj["vSiteList"]
      """  Selected Sites  """  
      pass

class GetTranGLCHeadSite_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
      pass

class GetTranGLCHead_input:
   """ Required : 
   vJournalCode
   vBookID
   vTaxCode
   """  
   def __init__(self, obj):
      self.vJournalCode:str = obj["vJournalCode"]
      """  Journal Code  """  
      self.vBookID:str = obj["vBookID"]
      """  Book ID  """  
      self.vTaxCode:str = obj["vTaxCode"]
      """  Tax Code  """  
      pass

class GetTranGLCHead_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["returnObj"]
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

class LoadGLJournalTracker_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

class LoadGLJournalTracker_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJournalTrackerDetailTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtJournalTrackerDetailTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_JournalTrackerDetailTableset] = obj["ds"]
      pass

      """  output parameters  """  

