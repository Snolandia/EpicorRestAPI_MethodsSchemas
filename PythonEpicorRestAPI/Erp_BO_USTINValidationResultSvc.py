import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.USTINValidationResultSvc
# Description: BO.USTINValidationResult
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationResults(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get USTINValidationResults items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidationResults
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationResultRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults",headers=creds) as resp:
           return await resp.json()

async def post_USTINValidationResults(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidationResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationResultRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationResultRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationResults_Company_TINValidationResultID(Company, TINValidationResultID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationResult item
   Description: Calls GetByID to retrieve the USTINValidationResult item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationResult
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationResultRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults(" + Company + "," + TINValidationResultID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_USTINValidationResults_Company_TINValidationResultID(Company, TINValidationResultID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update USTINValidationResult for the service
   Description: Calls UpdateExt to update USTINValidationResult. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidationResult
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationResultRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults(" + Company + "," + TINValidationResultID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_USTINValidationResults_Company_TINValidationResultID(Company, TINValidationResultID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete USTINValidationResult item
   Description: Call UpdateExt to delete USTINValidationResult item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidationResult
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults(" + Company + "," + TINValidationResultID + ")",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationResults_Company_TINValidationResultID_USTINValidationResultAttches(Company, TINValidationResultID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get USTINValidationResultAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_USTINValidationResultAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationResultAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults(" + Company + "," + TINValidationResultID + ")/USTINValidationResultAttches",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationResults_Company_TINValidationResultID_USTINValidationResultAttches_Company_TINValidationResultID_DrawingSeq(Company, TINValidationResultID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationResultAttch item
   Description: Calls GetByID to retrieve the USTINValidationResultAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationResultAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationResultAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResults(" + Company + "," + TINValidationResultID + ")/USTINValidationResultAttches(" + Company + "," + TINValidationResultID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationResultAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get USTINValidationResultAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_USTINValidationResultAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationResultAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResultAttches",headers=creds) as resp:
           return await resp.json()

async def post_USTINValidationResultAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_USTINValidationResultAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.USTINValidationResultAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.USTINValidationResultAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResultAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_USTINValidationResultAttches_Company_TINValidationResultID_DrawingSeq(Company, TINValidationResultID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the USTINValidationResultAttch item
   Description: Calls GetByID to retrieve the USTINValidationResultAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_USTINValidationResultAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.USTINValidationResultAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResultAttches(" + Company + "," + TINValidationResultID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_USTINValidationResultAttches_Company_TINValidationResultID_DrawingSeq(Company, TINValidationResultID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update USTINValidationResultAttch for the service
   Description: Calls UpdateExt to update USTINValidationResultAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_USTINValidationResultAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.USTINValidationResultAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResultAttches(" + Company + "," + TINValidationResultID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_USTINValidationResultAttches_Company_TINValidationResultID_DrawingSeq(Company, TINValidationResultID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete USTINValidationResultAttch item
   Description: Call UpdateExt to delete USTINValidationResultAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_USTINValidationResultAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TINValidationResultID: Desc: TINValidationResultID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/USTINValidationResultAttches(" + Company + "," + TINValidationResultID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.USTINValidationResultListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUSTINValidationResult, whereClauseUSTINValidationResultAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseUSTINValidationResult=" + whereClauseUSTINValidationResult
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseUSTINValidationResultAttch=" + whereClauseUSTINValidationResultAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tiNValidationResultID, epicorHeaders = None):
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
   params += "tiNValidationResultID=" + tiNValidationResultID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ImportResult(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportResult
   Description: Import File
   OperationID: ImportResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportResult_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTINValidationDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTINValidationDescription
   Description: Get Description of TIN Validation
   OperationID: GetTINValidationDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTINValidationDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTINValidationDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUSTINValidationResult(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUSTINValidationResult
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidationResult
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidationResult_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidationResult_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUSTINValidationResultAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUSTINValidationResultAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUSTINValidationResultAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUSTINValidationResultAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUSTINValidationResultAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.USTINValidationResultSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationResultAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationResultAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationResultListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationResultListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_USTINValidationResultRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_USTINValidationResultRow] = obj["value"]
      pass

class Erp_Tablesets_USTINValidationResultAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TINValidationResultID:str = obj["TINValidationResultID"]
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

class Erp_Tablesets_USTINValidationResultListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationResultID:str = obj["TINValidationResultID"]
      """  TIN Validation Result Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation Code  """  
      self.ImportFile:str = obj["ImportFile"]
      """  Import File  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationResultID:str = obj["TINValidationResultID"]
      """  TIN Validation Result Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation Code  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.ImportFile:str = obj["ImportFile"]
      """  Import File  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportSummary:str = obj["ImportSummary"]
      """  Import Summary  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TINValidationDescription:str = obj["TINValidationDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tiNValidationResultID
   """  
   def __init__(self, obj):
      self.tiNValidationResultID:str = obj["tiNValidationResultID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_USTINValidationResultAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TINValidationResultID:str = obj["TINValidationResultID"]
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

class Erp_Tablesets_USTINValidationResultListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationResultID:str = obj["TINValidationResultID"]
      """  TIN Validation Result Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation Code  """  
      self.ImportFile:str = obj["ImportFile"]
      """  Import File  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationResultListTableset:
   def __init__(self, obj):
      self.USTINValidationResultList:list[Erp_Tablesets_USTINValidationResultListRow] = obj["USTINValidationResultList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_USTINValidationResultRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TINValidationResultID:str = obj["TINValidationResultID"]
      """  TIN Validation Result Code  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.TINValidationID:str = obj["TINValidationID"]
      """  TIN Validation Code  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.ImportFile:str = obj["ImportFile"]
      """  Import File  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportSummary:str = obj["ImportSummary"]
      """  Import Summary  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.TINValidationDescription:str = obj["TINValidationDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_USTINValidationResultTableset:
   def __init__(self, obj):
      self.USTINValidationResult:list[Erp_Tablesets_USTINValidationResultRow] = obj["USTINValidationResult"]
      self.USTINValidationResultAttch:list[Erp_Tablesets_USTINValidationResultAttchRow] = obj["USTINValidationResultAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtUSTINValidationResultTableset:
   def __init__(self, obj):
      self.USTINValidationResult:list[Erp_Tablesets_USTINValidationResultRow] = obj["USTINValidationResult"]
      self.USTINValidationResultAttch:list[Erp_Tablesets_USTINValidationResultAttchRow] = obj["USTINValidationResultAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   tiNValidationResultID
   """  
   def __init__(self, obj):
      self.tiNValidationResultID:str = obj["tiNValidationResultID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_USTINValidationResultTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_USTINValidationResultTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_USTINValidationResultTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_USTINValidationResultListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUSTINValidationResultAttch_input:
   """ Required : 
   ds
   tiNValidationResultID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationResultTableset] = obj["ds"]
      self.tiNValidationResultID:str = obj["tiNValidationResultID"]
      pass

class GetNewUSTINValidationResultAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationResultTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewUSTINValidationResult_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationResultTableset] = obj["ds"]
      pass

class GetNewUSTINValidationResult_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationResultTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUSTINValidationResult
   whereClauseUSTINValidationResultAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUSTINValidationResult:str = obj["whereClauseUSTINValidationResult"]
      self.whereClauseUSTINValidationResultAttch:str = obj["whereClauseUSTINValidationResultAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_USTINValidationResultTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTINValidationDescription_input:
   """ Required : 
   tinValidationResultID
   tinValidationID
   """  
   def __init__(self, obj):
      self.tinValidationResultID:str = obj["tinValidationResultID"]
      self.tinValidationID:str = obj["tinValidationID"]
      pass

class GetTINValidationDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.description:str = obj["parameters"]
      self.yesNoMessage:str = obj["parameters"]
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

class ImportResult_input:
   """ Required : 
   tinValidationResultID
   eftHeadUID
   importFileName
   """  
   def __init__(self, obj):
      self.tinValidationResultID:str = obj["tinValidationResultID"]
      self.eftHeadUID:int = obj["eftHeadUID"]
      self.importFileName:str = obj["importFileName"]
      pass

class ImportResult_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUSTINValidationResultTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUSTINValidationResultTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationResultTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_USTINValidationResultTableset] = obj["ds"]
      pass

      """  output parameters  """  

