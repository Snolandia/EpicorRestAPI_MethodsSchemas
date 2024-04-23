import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APLOCSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APLOCs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APLOCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APLOCs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs",headers=creds) as resp:
           return await resp.json()

async def post_APLOCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APLOCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APLOCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APLOCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APLOCs_Company_LCID(Company, LCID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APLOC item
   Description: Calls GetByID to retrieve the APLOC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APLOC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APLOCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APLOCs_Company_LCID(Company, LCID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APLOC for the service
   Description: Calls UpdateExt to update APLOC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APLOC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APLOCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APLOCs_Company_LCID(Company, LCID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APLOC item
   Description: Call UpdateExt to delete APLOC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APLOC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APLOCs_Company_LCID_APLOCAttches(Company, LCID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APLOCAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APLOCAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")/APLOCAttches",headers=creds) as resp:
           return await resp.json()

async def get_APLOCs_Company_LCID_APLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APLOCAttch item
   Description: Calls GetByID to retrieve the APLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APLOCAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCs(" + Company + "," + LCID + ")/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APLOCAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APLOCAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APLOCAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches",headers=creds) as resp:
           return await resp.json()

async def post_APLOCAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APLOCAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APLOCAttch item
   Description: Calls GetByID to retrieve the APLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APLOCAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APLOCAttch for the service
   Description: Calls UpdateExt to update APLOCAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APLOCAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APLOCAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APLOCAttch item
   Description: Call UpdateExt to delete APLOCAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APLOCAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/APLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APLOCListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPLOC, whereClauseAPLOCAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAPLOC=" + whereClauseAPLOC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPLOCAttch=" + whereClauseAPLOCAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(lcID, epicorHeaders = None):
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
   params += "lcID=" + lcID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyCode
   Description: Called when the CurrencyCode field has been changed.
   OperationID: ChangeCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeIssueDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeIssueDate
   Description: Called when the IssueDate field has been changed.
   OperationID: ChangeIssueDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeIssueDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeIssueDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDocLCValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDocLCValue
   Description: Called when the DocLCValue field has been changed.
   OperationID: ChangeDocLCValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDocLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDocLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExchangeRate
   Description: Called when the ExchangeRate field has been changed.
   OperationID: ChangeExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUseExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUseExchangeRate
   Description: Called when the Use ExchangeRate field has been changed.
   OperationID: ChangeUseExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUseExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUseExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPLOCInvc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPLOCInvc
   Description: This method will retrieve all the information related to AP Invoices
   OperationID: GetAPLOCInvc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCInvc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCInvc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPLOCPO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPLOCPO
   Description: This method will retrieve all the information related to Purchase Orders.
   OperationID: GetAPLOCPO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCPO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCPO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfCurrencyCode
   Description: Called when the CurrencyCode field is changing.
   OperationID: OnChangeOfCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfFromDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfFromDate
   Description: Called when changing the FromDate field.
   OperationID: OnChangeOfFromDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFromDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFromDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfUseExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfUseExchangeRate
   Description: Called when changing the FromDate field.
   OperationID: OnChangeOfUseExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfUseExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfUseExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLCValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLCValue
   Description: Called when changing the LCValue field.
   OperationID: OnChangeOfLCValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfToDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfToDate
   Description: Called when changing the ToDate field.
   OperationID: OnChangeOfToDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfToDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfToDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankAcctID
   Description: Called when changing the BankAcctId field.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPLOC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPLOC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPLOC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPLOCAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPLOCAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPLOCAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPLOCAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPLOCAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APLOCAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APLOCListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APLOCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APLOCRow] = obj["value"]
      pass

class Erp_Tablesets_APLOCAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LCID:str = obj["LCID"]
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

class Erp_Tablesets_APLOCListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcct ID.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Letter of Credit Value for report currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Letter of Credit Value for report currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Letter of Credit Value for report currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Letter of Credit Currency code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate.  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Indicates a locked exchange rate.  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill to customer.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Letter of Credit Terms.  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true, no more commitments to this Letter of Credit.  """  
      self.InactiveReason:str = obj["InactiveReason"]
      """  Reason Letter of Credit was marked Inactive (entered by user).  """  
      self.Closed:bool = obj["Closed"]
      """  If true, Letter of Credit is closed.  """  
      self.FOB:str = obj["FOB"]
      """  Optional.  """  
      self.IssuanceType:str = obj["IssuanceType"]
      """  Free form text.  """  
      self.PackListCopies:str = obj["PackListCopies"]
      """  Free form text.  """  
      self.PlaceOfLoading:str = obj["PlaceOfLoading"]
      """  Free form text.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text comments.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier.  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.VendorID:str = obj["VendorID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.InUse:bool = obj["InUse"]
      self.CumInValue:int = obj["CumInValue"]
      """  Cumulative Invoice Value  """  
      self.OutPOValue:int = obj["OutPOValue"]
      """  Outstanding PO Value  """  
      self.RemLCValue:int = obj["RemLCValue"]
      """  Remaining LC Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.DocCumInValue:int = obj["DocCumInValue"]
      self.Rpt1CumInValue:int = obj["Rpt1CumInValue"]
      self.Rpt2CumInValue:int = obj["Rpt2CumInValue"]
      self.Rpt3CumInValue:int = obj["Rpt3CumInValue"]
      self.DocRemLCValue:int = obj["DocRemLCValue"]
      self.Rpt1RemLCValue:int = obj["Rpt1RemLCValue"]
      self.Rpt2RemLCValue:int = obj["Rpt2RemLCValue"]
      self.Rpt3RemLCValue:int = obj["Rpt3RemLCValue"]
      self.DocOutPOValue:int = obj["DocOutPOValue"]
      self.Rpt1OutPOValue:int = obj["Rpt1OutPOValue"]
      self.Rpt2OutPOValue:int = obj["Rpt2OutPOValue"]
      self.Rpt3OutPOValue:int = obj["Rpt3OutPOValue"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.APTermsDescription:str = obj["APTermsDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APLOCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcct ID.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Letter of Credit Value for report currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Letter of Credit Value for report currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Letter of Credit Value for report currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Letter of Credit Currency code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate.  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Indicates a locked exchange rate.  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill to customer.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Letter of Credit Terms.  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true, no more commitments to this Letter of Credit.  """  
      self.InactiveReason:str = obj["InactiveReason"]
      """  Reason Letter of Credit was marked Inactive (entered by user).  """  
      self.Closed:bool = obj["Closed"]
      """  If true, Letter of Credit is closed.  """  
      self.FOB:str = obj["FOB"]
      """  Optional.  """  
      self.IssuanceType:str = obj["IssuanceType"]
      """  Free form text.  """  
      self.PackListCopies:str = obj["PackListCopies"]
      """  Free form text.  """  
      self.PlaceOfLoading:str = obj["PlaceOfLoading"]
      """  Free form text.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text comments.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier.  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.VendorID:str = obj["VendorID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.InUse:bool = obj["InUse"]
      self.CumInValue:int = obj["CumInValue"]
      """  Cumulative Invoice Value  """  
      self.OutPOValue:int = obj["OutPOValue"]
      """  Outstanding PO Value  """  
      self.RemLCValue:int = obj["RemLCValue"]
      """  Remaining LC Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.DocCumInValue:int = obj["DocCumInValue"]
      self.Rpt1CumInValue:int = obj["Rpt1CumInValue"]
      self.Rpt2CumInValue:int = obj["Rpt2CumInValue"]
      self.Rpt3CumInValue:int = obj["Rpt3CumInValue"]
      self.DocRemLCValue:int = obj["DocRemLCValue"]
      self.Rpt1RemLCValue:int = obj["Rpt1RemLCValue"]
      self.Rpt2RemLCValue:int = obj["Rpt2RemLCValue"]
      self.Rpt3RemLCValue:int = obj["Rpt3RemLCValue"]
      self.DocOutPOValue:int = obj["DocOutPOValue"]
      self.Rpt1OutPOValue:int = obj["Rpt1OutPOValue"]
      self.Rpt2OutPOValue:int = obj["Rpt2OutPOValue"]
      self.Rpt3OutPOValue:int = obj["Rpt3OutPOValue"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      """  Use to choose which Exchange Rate will be use either Letter of Credit's or current.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.APTermsDescription:str = obj["APTermsDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.CurrencyCodeBaseCurr:bool = obj["CurrencyCodeBaseCurr"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCurrencyCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class ChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDocLCValue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class ChangeDocLCValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExchangeRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class ChangeExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeIssueDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class ChangeIssueDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUseExchangeRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class ChangeUseExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   lcID
   """  
   def __init__(self, obj):
      self.lcID:str = obj["lcID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APLOCAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LCID:str = obj["LCID"]
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

class Erp_Tablesets_APLOCInvcRow:
   def __init__(self, obj):
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Field required for the grid of APLOCTracker Invoices.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.OpenPayable:bool = obj["OpenPayable"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyName:str = obj["CurrencyName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APLOCListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcct ID.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Letter of Credit Value for report currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Letter of Credit Value for report currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Letter of Credit Value for report currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Letter of Credit Currency code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate.  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Indicates a locked exchange rate.  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill to customer.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Letter of Credit Terms.  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true, no more commitments to this Letter of Credit.  """  
      self.InactiveReason:str = obj["InactiveReason"]
      """  Reason Letter of Credit was marked Inactive (entered by user).  """  
      self.Closed:bool = obj["Closed"]
      """  If true, Letter of Credit is closed.  """  
      self.FOB:str = obj["FOB"]
      """  Optional.  """  
      self.IssuanceType:str = obj["IssuanceType"]
      """  Free form text.  """  
      self.PackListCopies:str = obj["PackListCopies"]
      """  Free form text.  """  
      self.PlaceOfLoading:str = obj["PlaceOfLoading"]
      """  Free form text.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text comments.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier.  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.VendorID:str = obj["VendorID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.InUse:bool = obj["InUse"]
      self.CumInValue:int = obj["CumInValue"]
      """  Cumulative Invoice Value  """  
      self.OutPOValue:int = obj["OutPOValue"]
      """  Outstanding PO Value  """  
      self.RemLCValue:int = obj["RemLCValue"]
      """  Remaining LC Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.DocCumInValue:int = obj["DocCumInValue"]
      self.Rpt1CumInValue:int = obj["Rpt1CumInValue"]
      self.Rpt2CumInValue:int = obj["Rpt2CumInValue"]
      self.Rpt3CumInValue:int = obj["Rpt3CumInValue"]
      self.DocRemLCValue:int = obj["DocRemLCValue"]
      self.Rpt1RemLCValue:int = obj["Rpt1RemLCValue"]
      self.Rpt2RemLCValue:int = obj["Rpt2RemLCValue"]
      self.Rpt3RemLCValue:int = obj["Rpt3RemLCValue"]
      self.DocOutPOValue:int = obj["DocOutPOValue"]
      self.Rpt1OutPOValue:int = obj["Rpt1OutPOValue"]
      self.Rpt2OutPOValue:int = obj["Rpt2OutPOValue"]
      self.Rpt3OutPOValue:int = obj["Rpt3OutPOValue"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.APTermsDescription:str = obj["APTermsDescription"]
      """  Full description of terms....this is printed on purchase orders. Can't be blank.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APLOCListTableset:
   def __init__(self, obj):
      self.APLOCList:list[Erp_Tablesets_APLOCListRow] = obj["APLOCList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APLOCPORow:
   def __init__(self, obj):
      self.OpenOrder:bool = obj["OpenOrder"]
      self.PONum:int = obj["PONum"]
      """  Temp Table required by the APLOCTracker Dataset  """  
      self.OutstdValue:int = obj["OutstdValue"]
      """  the value of open unreceived goods + value of received but unmatched to invoice goods.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyName:str = obj["CurrencyName"]
      """  Currency Name  """  
      self.DocOutstdValue:int = obj["DocOutstdValue"]
      self.Rpt1OutstdValue:int = obj["Rpt1OutstdValue"]
      self.Rpt2OutstdValue:int = obj["Rpt2OutstdValue"]
      self.Rpt3OutstdValue:int = obj["Rpt3OutstdValue"]
      self.TotalOrder:int = obj["TotalOrder"]
      """  Total Order form PO  """  
      self.DocTotalOrder:int = obj["DocTotalOrder"]
      self.Rpt1TotalOrder:int = obj["Rpt1TotalOrder"]
      """  Total Order form PO  """  
      self.Rpt2TotalOrder:int = obj["Rpt2TotalOrder"]
      """  Total Order form PO  """  
      self.Rpt3TotalOrder:int = obj["Rpt3TotalOrder"]
      """  Total Order form PO  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APLOCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcct ID.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable, instead it is assigned from the Vendor.VendorNum using VendorID to find the Vendor record.  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Letter of Credit Value for report currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Letter of Credit Value for report currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Letter of Credit Value for report currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Letter of Credit Currency code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate.  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Indicates a locked exchange rate.  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill to customer.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Letter of Credit Terms.  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Determines whether shipments linked to the Letter of Credit needs to be shipped complete.  """  
      self.Inactive:bool = obj["Inactive"]
      """  If true, no more commitments to this Letter of Credit.  """  
      self.InactiveReason:str = obj["InactiveReason"]
      """  Reason Letter of Credit was marked Inactive (entered by user).  """  
      self.Closed:bool = obj["Closed"]
      """  If true, Letter of Credit is closed.  """  
      self.FOB:str = obj["FOB"]
      """  Optional.  """  
      self.IssuanceType:str = obj["IssuanceType"]
      """  Free form text.  """  
      self.PackListCopies:str = obj["PackListCopies"]
      """  Free form text.  """  
      self.PlaceOfLoading:str = obj["PlaceOfLoading"]
      """  Free form text.  """  
      self.Comment:str = obj["Comment"]
      """  Free form text comments.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier.  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.VendorID:str = obj["VendorID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.InUse:bool = obj["InUse"]
      self.CumInValue:int = obj["CumInValue"]
      """  Cumulative Invoice Value  """  
      self.OutPOValue:int = obj["OutPOValue"]
      """  Outstanding PO Value  """  
      self.RemLCValue:int = obj["RemLCValue"]
      """  Remaining LC Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoice Balance  """  
      self.DocCumInValue:int = obj["DocCumInValue"]
      self.Rpt1CumInValue:int = obj["Rpt1CumInValue"]
      self.Rpt2CumInValue:int = obj["Rpt2CumInValue"]
      self.Rpt3CumInValue:int = obj["Rpt3CumInValue"]
      self.DocRemLCValue:int = obj["DocRemLCValue"]
      self.Rpt1RemLCValue:int = obj["Rpt1RemLCValue"]
      self.Rpt2RemLCValue:int = obj["Rpt2RemLCValue"]
      self.Rpt3RemLCValue:int = obj["Rpt3RemLCValue"]
      self.DocOutPOValue:int = obj["DocOutPOValue"]
      self.Rpt1OutPOValue:int = obj["Rpt1OutPOValue"]
      self.Rpt2OutPOValue:int = obj["Rpt2OutPOValue"]
      self.Rpt3OutPOValue:int = obj["Rpt3OutPOValue"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      """  Use to choose which Exchange Rate will be use either Letter of Credit's or current.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.APTermsDescription:str = obj["APTermsDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.CurrencyCodeBaseCurr:bool = obj["CurrencyCodeBaseCurr"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorName:str = obj["VendorName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APLOCTableset:
   def __init__(self, obj):
      self.APLOC:list[Erp_Tablesets_APLOCRow] = obj["APLOC"]
      self.APLOCAttch:list[Erp_Tablesets_APLOCAttchRow] = obj["APLOCAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APLOCTrackerTableset:
   def __init__(self, obj):
      self.APLOCInvc:list[Erp_Tablesets_APLOCInvcRow] = obj["APLOCInvc"]
      self.APLOCPO:list[Erp_Tablesets_APLOCPORow] = obj["APLOCPO"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAPLOCTableset:
   def __init__(self, obj):
      self.APLOC:list[Erp_Tablesets_APLOCRow] = obj["APLOC"]
      self.APLOCAttch:list[Erp_Tablesets_APLOCAttchRow] = obj["APLOCAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAPLOCInvc_input:
   """ Required : 
   aplocid
   ds
   """  
   def __init__(self, obj):
      self.aplocid:str = obj["aplocid"]
      """  AP Letters Of Credit ID  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class GetAPLOCInvc_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APLOCTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAPLOCPO_input:
   """ Required : 
   aplocid
   ds
   """  
   def __init__(self, obj):
      self.aplocid:str = obj["aplocid"]
      """  AP Letters Of Credit ID  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class GetAPLOCPO_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APLOCTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   lcID
   """  
   def __init__(self, obj):
      self.lcID:str = obj["lcID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APLOCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APLOCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APLOCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APLOCListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPLOCAttch_input:
   """ Required : 
   ds
   lcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      self.lcID:str = obj["lcID"]
      pass

class GetNewAPLOCAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPLOC_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class GetNewAPLOC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPLOC
   whereClauseAPLOCAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPLOC:str = obj["whereClauseAPLOC"]
      self.whereClauseAPLOCAttch:str = obj["whereClauseAPLOCAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APLOCTableset] = obj["returnObj"]
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

class OnChangeBankAcctID_input:
   """ Required : 
   pcBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  The proposed value of BankAcctID.  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class OnChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfCurrencyCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class OnChangeOfCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfFromDate_input:
   """ Required : 
   proposedFromDate
   ds
   """  
   def __init__(self, obj):
      self.proposedFromDate:str = obj["proposedFromDate"]
      """  Proposed From Date  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class OnChangeOfFromDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLCValue_input:
   """ Required : 
   proposedLCValue
   ds
   """  
   def __init__(self, obj):
      self.proposedLCValue:int = obj["proposedLCValue"]
      """  Proposed LCValue  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class OnChangeOfLCValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfToDate_input:
   """ Required : 
   proposedToDate
   ds
   """  
   def __init__(self, obj):
      self.proposedToDate:str = obj["proposedToDate"]
      """  Proposed To Date  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class OnChangeOfToDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfUseExchangeRate_input:
   """ Required : 
   proposedFromUseExchangeRate
   ds
   """  
   def __init__(self, obj):
      self.proposedFromUseExchangeRate:str = obj["proposedFromUseExchangeRate"]
      """  Proposed From Date  """  
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class OnChangeOfUseExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPLOCTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPLOCTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

