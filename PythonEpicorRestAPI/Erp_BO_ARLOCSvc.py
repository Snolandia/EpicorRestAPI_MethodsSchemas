import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARLOCSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ARLOCs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARLOCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARLOCs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs",headers=creds) as resp:
           return await resp.json()

async def post_ARLOCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARLOCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARLOCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARLOCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARLOCs_Company_LCID(Company, LCID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARLOC item
   Description: Calls GetByID to retrieve the ARLOC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARLOC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARLOCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARLOCs_Company_LCID(Company, LCID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARLOC for the service
   Description: Calls UpdateExt to update ARLOC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARLOC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARLOCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARLOCs_Company_LCID(Company, LCID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARLOC item
   Description: Call UpdateExt to delete ARLOC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARLOC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARLOCs_Company_LCID_ARLOCAttches(Company, LCID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARLOCAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARLOCAttches1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")/ARLOCAttches",headers=creds) as resp:
           return await resp.json()

async def get_ARLOCs_Company_LCID_ARLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARLOCAttch item
   Description: Calls GetByID to retrieve the ARLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARLOCAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCs(" + Company + "," + LCID + ")/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARLOCAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARLOCAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARLOCAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches",headers=creds) as resp:
           return await resp.json()

async def post_ARLOCAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARLOCAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARLOCAttch item
   Description: Calls GetByID to retrieve the ARLOCAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARLOCAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARLOCAttch for the service
   Description: Calls UpdateExt to update ARLOCAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARLOCAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LCID: Desc: LCID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARLOCAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARLOCAttches_Company_LCID_DrawingSeq(Company, LCID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARLOCAttch item
   Description: Call UpdateExt to delete ARLOCAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARLOCAttch
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/ARLOCAttches(" + Company + "," + LCID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARLOCListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseARLOC, whereClauseARLOCAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseARLOC=" + whereClauseARLOC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARLOCAttch=" + whereClauseARLOCAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBTCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBTCustID
   Description: This method returns the Bill To customer info.
   OperationID: ChangeBTCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBTCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBTCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARLOCInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARLOCInvoices
   Description: This method will retrieve all the information related to AR Invoices.
   OperationID: GetARLOCInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARLOCInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARLOCInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARLOCSOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARLOCSOrders
   Description: This method will retrieve all the information related to Sales Orders.
   OperationID: GetARLOCSOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARLOCSOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARLOCSOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailBTList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailBTList
   Description: This procedure returns a list of Alternate Bill To Customer for a Customer.
   OperationID: GetAvailBTList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailBTList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailBTList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfDocLCValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfDocLCValue
   Description: Called when changing the DocLCValue field.
   OperationID: OnChangeOfDocLCValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfDocLCValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfDocLCValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARLOC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARLOC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARLOC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARLOCAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARLOCAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARLOCAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARLOCAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARLOCAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARLOCSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARLOCAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARLOCListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARLOCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARLOCRow] = obj["value"]
      pass

class Erp_Tablesets_ARLOCAttchRow:
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

class Erp_Tablesets_ARLOCListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Exchange Rate Lock flag  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.GuarantorName:str = obj["GuarantorName"]
      """  Name of the Letter of Credit Guarantor.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Ship Complete flag  """  
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
      self.Type:str = obj["Type"]
      """  LC = Letter of Credit, ECG = Export Credit Guarantee  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.InUse:bool = obj["InUse"]
      """  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  """  
      self.OpenLCCredit:int = obj["OpenLCCredit"]
      self.OpenOrderValue:int = obj["OpenOrderValue"]
      self.CumInvoices:int = obj["CumInvoices"]
      self.DocCumInvoices:int = obj["DocCumInvoices"]
      """  Cumulative Invoices  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.DocOpenLCCredit:int = obj["DocOpenLCCredit"]
      """  Open LC Credit  """  
      self.DocOpenOrderValue:int = obj["DocOpenOrderValue"]
      """  Open Order Value  """  
      self.DocPaidInvoiceValue:int = obj["DocPaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.DocTotalOrderValue:int = obj["DocTotalOrderValue"]
      """  Total Order Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.PaidInvoiceValue:int = obj["PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt1CumInvoices:int = obj["Rpt1CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt2CumInvoices:int = obj["Rpt2CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt3CumInvoices:int = obj["Rpt3CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1OpenLCCredit:int = obj["Rpt1OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenLCCredit:int = obj["Rpt2OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt3OpenLCCredit:int = obj["Rpt3OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenOrderValue:int = obj["Rpt2OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1OpenOrderValue:int = obj["Rpt1OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt3OpenOrderValue:int = obj["Rpt3OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1PaidInvoiceValue:int = obj["Rpt1PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt2PaidInvoiceValue:int = obj["Rpt2PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt3PaidInvoiceValue:int = obj["Rpt3PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt1TotalOrderValue:int = obj["Rpt1TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt2TotalOrderValue:int = obj["Rpt2TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt3TotalOrderValue:int = obj["Rpt3TotalOrderValue"]
      """  Total Order Value  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.BTCustNumName:str = obj["BTCustNumName"]
      """  The full name of the customer.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.CumInvoicesCurrent:int = obj["CumInvoicesCurrent"]
      self.LCValueCurrent:int = obj["LCValueCurrent"]
      """  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  """  
      self.OpenLCCreditCurrent:int = obj["OpenLCCreditCurrent"]
      self.OpenOrderValueCurrent:int = obj["OpenOrderValueCurrent"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      self.InvoiceBalCurrent:int = obj["InvoiceBalCurrent"]
      """  Invoices Balance converted from document cuurency using current (today) exchange rate  """  
      self.PaidInvoiceValueCurrent:int = obj["PaidInvoiceValueCurrent"]
      """  Paid Invoice Value in base currency converted from the amount in doc currency using current (now) exchange rate  """  
      self.TotalOrderValueCurrent:int = obj["TotalOrderValueCurrent"]
      """  Total Order value converted from amount in doc currency using current (now) exchange rate  """  
      self.Rpt1LCValueCurrent:int = obj["Rpt1LCValueCurrent"]
      """  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt2LCValueCurrent:int = obj["Rpt2LCValueCurrent"]
      """  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt3LCValueCurrent:int = obj["Rpt3LCValueCurrent"]
      """  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Exchange Rate Lock flag  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.GuarantorName:str = obj["GuarantorName"]
      """  Name of the Letter of Credit Guarantor.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Ship Complete flag  """  
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
      self.Type:str = obj["Type"]
      """  LC = Letter of Credit, ECG = Export Credit Guarantee  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.InUse:bool = obj["InUse"]
      """  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  """  
      self.OpenLCCredit:int = obj["OpenLCCredit"]
      self.OpenOrderValue:int = obj["OpenOrderValue"]
      self.CumInvoices:int = obj["CumInvoices"]
      self.DocCumInvoices:int = obj["DocCumInvoices"]
      """  Cumulative Invoices  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.DocOpenLCCredit:int = obj["DocOpenLCCredit"]
      """  Open LC Credit  """  
      self.DocOpenOrderValue:int = obj["DocOpenOrderValue"]
      """  Open Order Value  """  
      self.DocPaidInvoiceValue:int = obj["DocPaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.DocTotalOrderValue:int = obj["DocTotalOrderValue"]
      """  Total Order Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.PaidInvoiceValue:int = obj["PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt1CumInvoices:int = obj["Rpt1CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt2CumInvoices:int = obj["Rpt2CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt3CumInvoices:int = obj["Rpt3CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1OpenLCCredit:int = obj["Rpt1OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenLCCredit:int = obj["Rpt2OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt3OpenLCCredit:int = obj["Rpt3OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenOrderValue:int = obj["Rpt2OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1OpenOrderValue:int = obj["Rpt1OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt3OpenOrderValue:int = obj["Rpt3OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1PaidInvoiceValue:int = obj["Rpt1PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt2PaidInvoiceValue:int = obj["Rpt2PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt3PaidInvoiceValue:int = obj["Rpt3PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt1TotalOrderValue:int = obj["Rpt1TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt2TotalOrderValue:int = obj["Rpt2TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt3TotalOrderValue:int = obj["Rpt3TotalOrderValue"]
      """  Total Order Value  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.Currency:str = obj["Currency"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      self.LCValueCurrent:int = obj["LCValueCurrent"]
      """  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  """  
      self.OpenLCCreditCurrent:int = obj["OpenLCCreditCurrent"]
      """  Open LOC Credit in base currency converted from Open LOC Credit in Document currency using current (today) exchange rate  """  
      self.OpenOrderValueCurrent:int = obj["OpenOrderValueCurrent"]
      """  Open Order Value in base currency converted from the amount in document currency using the current (now) exchange rate  """  
      self.CumInvoicesCurrent:int = obj["CumInvoicesCurrent"]
      self.InvoiceBalCurrent:int = obj["InvoiceBalCurrent"]
      """  Invoices Balance converted from document cuurency using current (today) exchange rate  """  
      self.PaidInvoiceValueCurrent:int = obj["PaidInvoiceValueCurrent"]
      """  Paid Invoice Value in base currency converted from amount in doc currency using the current (now) exchange rate  """  
      self.TotalOrderValueCurrent:int = obj["TotalOrderValueCurrent"]
      """  Total Order value converted from amount in doc currency using current (now) exchange rate  """  
      self.Rpt1LCValueCurrent:int = obj["Rpt1LCValueCurrent"]
      """  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt2LCValueCurrent:int = obj["Rpt2LCValueCurrent"]
      """  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt3LCValueCurrent:int = obj["Rpt3LCValueCurrent"]
      """  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      self.BTCustNumName:str = obj["BTCustNumName"]
      self.CurrencyCodeBaseCurr:bool = obj["CurrencyCodeBaseCurr"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBTCustID_input:
   """ Required : 
   newBillToCustID
   ds
   """  
   def __init__(self, obj):
      self.newBillToCustID:str = obj["newBillToCustID"]
      """  Proposed bill to custid  """  
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class ChangeBTCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCurrencyCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class ChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDocLCValue_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class ChangeDocLCValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExchangeRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class ChangeExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeIssueDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class ChangeIssueDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
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

class Erp_Tablesets_ARLOCAttchRow:
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

class Erp_Tablesets_ARLOCInvcRow:
   def __init__(self, obj):
      self.ApplyDate:str = obj["ApplyDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyName:str = obj["CurrencyName"]
      self.DocInvoiceAmt:int = obj["DocInvoiceAmt"]
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      self.InvoiceAmt:int = obj["InvoiceAmt"]
      self.InvoiceBal:int = obj["InvoiceBal"]
      self.InvoiceDate:str = obj["InvoiceDate"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.OpenInvoice:bool = obj["OpenInvoice"]
      self.OrderNum:int = obj["OrderNum"]
      self.PONum:str = obj["PONum"]
      self.Rpt1InvoiceAmt:int = obj["Rpt1InvoiceAmt"]
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      self.Rpt2InvoiceAmt:int = obj["Rpt2InvoiceAmt"]
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      self.Rpt3InvoiceAmt:int = obj["Rpt3InvoiceAmt"]
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Exchange Rate Lock flag  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.GuarantorName:str = obj["GuarantorName"]
      """  Name of the Letter of Credit Guarantor.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Ship Complete flag  """  
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
      self.Type:str = obj["Type"]
      """  LC = Letter of Credit, ECG = Export Credit Guarantee  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.InUse:bool = obj["InUse"]
      """  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  """  
      self.OpenLCCredit:int = obj["OpenLCCredit"]
      self.OpenOrderValue:int = obj["OpenOrderValue"]
      self.CumInvoices:int = obj["CumInvoices"]
      self.DocCumInvoices:int = obj["DocCumInvoices"]
      """  Cumulative Invoices  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.DocOpenLCCredit:int = obj["DocOpenLCCredit"]
      """  Open LC Credit  """  
      self.DocOpenOrderValue:int = obj["DocOpenOrderValue"]
      """  Open Order Value  """  
      self.DocPaidInvoiceValue:int = obj["DocPaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.DocTotalOrderValue:int = obj["DocTotalOrderValue"]
      """  Total Order Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.PaidInvoiceValue:int = obj["PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt1CumInvoices:int = obj["Rpt1CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt2CumInvoices:int = obj["Rpt2CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt3CumInvoices:int = obj["Rpt3CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1OpenLCCredit:int = obj["Rpt1OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenLCCredit:int = obj["Rpt2OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt3OpenLCCredit:int = obj["Rpt3OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenOrderValue:int = obj["Rpt2OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1OpenOrderValue:int = obj["Rpt1OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt3OpenOrderValue:int = obj["Rpt3OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1PaidInvoiceValue:int = obj["Rpt1PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt2PaidInvoiceValue:int = obj["Rpt2PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt3PaidInvoiceValue:int = obj["Rpt3PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt1TotalOrderValue:int = obj["Rpt1TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt2TotalOrderValue:int = obj["Rpt2TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt3TotalOrderValue:int = obj["Rpt3TotalOrderValue"]
      """  Total Order Value  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.BTCustNumName:str = obj["BTCustNumName"]
      """  The full name of the customer.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      """  Full description of the FOB Code.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      """  Full description of the terms which prints on sales orders and invoices.  """  
      self.CumInvoicesCurrent:int = obj["CumInvoicesCurrent"]
      self.LCValueCurrent:int = obj["LCValueCurrent"]
      """  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  """  
      self.OpenLCCreditCurrent:int = obj["OpenLCCreditCurrent"]
      self.OpenOrderValueCurrent:int = obj["OpenOrderValueCurrent"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      self.InvoiceBalCurrent:int = obj["InvoiceBalCurrent"]
      """  Invoices Balance converted from document cuurency using current (today) exchange rate  """  
      self.PaidInvoiceValueCurrent:int = obj["PaidInvoiceValueCurrent"]
      """  Paid Invoice Value in base currency converted from the amount in doc currency using current (now) exchange rate  """  
      self.TotalOrderValueCurrent:int = obj["TotalOrderValueCurrent"]
      """  Total Order value converted from amount in doc currency using current (now) exchange rate  """  
      self.Rpt1LCValueCurrent:int = obj["Rpt1LCValueCurrent"]
      """  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt2LCValueCurrent:int = obj["Rpt2LCValueCurrent"]
      """  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt3LCValueCurrent:int = obj["Rpt3LCValueCurrent"]
      """  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCListTableset:
   def __init__(self, obj):
      self.ARLOCList:list[Erp_Tablesets_ARLOCListRow] = obj["ARLOCList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARLOCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LCID:str = obj["LCID"]
      """  Letter of Credit ID.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.LCValue:int = obj["LCValue"]
      """  Monetary value of the Letter of Credit.  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 1.  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 2.  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Monetary value of the Letter of Credit. Report Currency 3.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.RateLocked:bool = obj["RateLocked"]
      """  Exchange Rate Lock flag  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Date that Letter of Credit was issued.  """  
      self.FromDate:str = obj["FromDate"]
      """  Valid From date.  """  
      self.ToDate:str = obj["ToDate"]
      """  Valid To date.  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description.  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.GuarantorName:str = obj["GuarantorName"]
      """  Name of the Letter of Credit Guarantor.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Terms code  """  
      self.ShipComplete:bool = obj["ShipComplete"]
      """  Ship Complete flag  """  
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
      self.Type:str = obj["Type"]
      """  LC = Letter of Credit, ECG = Export Credit Guarantee  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Monetary value of the Letter of Credit in bank's currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      """  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  """  
      self.BTCustID:str = obj["BTCustID"]
      """  Bill To Customer ID  """  
      self.BaseCurrencyID:str = obj["BaseCurrencyID"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.InUse:bool = obj["InUse"]
      """  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  """  
      self.OpenLCCredit:int = obj["OpenLCCredit"]
      self.OpenOrderValue:int = obj["OpenOrderValue"]
      self.CumInvoices:int = obj["CumInvoices"]
      self.DocCumInvoices:int = obj["DocCumInvoices"]
      """  Cumulative Invoices  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.DocOpenLCCredit:int = obj["DocOpenLCCredit"]
      """  Open LC Credit  """  
      self.DocOpenOrderValue:int = obj["DocOpenOrderValue"]
      """  Open Order Value  """  
      self.DocPaidInvoiceValue:int = obj["DocPaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.DocTotalOrderValue:int = obj["DocTotalOrderValue"]
      """  Total Order Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.PaidInvoiceValue:int = obj["PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.TotalOrderValue:int = obj["TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt1CumInvoices:int = obj["Rpt1CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt2CumInvoices:int = obj["Rpt2CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt3CumInvoices:int = obj["Rpt3CumInvoices"]
      """  Cumulative Invoices  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1OpenLCCredit:int = obj["Rpt1OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenLCCredit:int = obj["Rpt2OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt3OpenLCCredit:int = obj["Rpt3OpenLCCredit"]
      """  Open LC Credit  """  
      self.Rpt2OpenOrderValue:int = obj["Rpt2OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1OpenOrderValue:int = obj["Rpt1OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt3OpenOrderValue:int = obj["Rpt3OpenOrderValue"]
      """  Open Order Value  """  
      self.Rpt1PaidInvoiceValue:int = obj["Rpt1PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt2PaidInvoiceValue:int = obj["Rpt2PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt3PaidInvoiceValue:int = obj["Rpt3PaidInvoiceValue"]
      """  Paid Invoice Value  """  
      self.Rpt1TotalOrderValue:int = obj["Rpt1TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt2TotalOrderValue:int = obj["Rpt2TotalOrderValue"]
      """  Total Order Value  """  
      self.Rpt3TotalOrderValue:int = obj["Rpt3TotalOrderValue"]
      """  Total Order Value  """  
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.Currency:str = obj["Currency"]
      self.UseExchangeRate:str = obj["UseExchangeRate"]
      self.LCValueCurrent:int = obj["LCValueCurrent"]
      """  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  """  
      self.OpenLCCreditCurrent:int = obj["OpenLCCreditCurrent"]
      """  Open LOC Credit in base currency converted from Open LOC Credit in Document currency using current (today) exchange rate  """  
      self.OpenOrderValueCurrent:int = obj["OpenOrderValueCurrent"]
      """  Open Order Value in base currency converted from the amount in document currency using the current (now) exchange rate  """  
      self.CumInvoicesCurrent:int = obj["CumInvoicesCurrent"]
      self.InvoiceBalCurrent:int = obj["InvoiceBalCurrent"]
      """  Invoices Balance converted from document cuurency using current (today) exchange rate  """  
      self.PaidInvoiceValueCurrent:int = obj["PaidInvoiceValueCurrent"]
      """  Paid Invoice Value in base currency converted from amount in doc currency using the current (now) exchange rate  """  
      self.TotalOrderValueCurrent:int = obj["TotalOrderValueCurrent"]
      """  Total Order value converted from amount in doc currency using current (now) exchange rate  """  
      self.Rpt1LCValueCurrent:int = obj["Rpt1LCValueCurrent"]
      """  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt2LCValueCurrent:int = obj["Rpt2LCValueCurrent"]
      """  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  """  
      self.Rpt3LCValueCurrent:int = obj["Rpt3LCValueCurrent"]
      """  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BTCustNumBTName:str = obj["BTCustNumBTName"]
      self.BTCustNumCustID:str = obj["BTCustNumCustID"]
      self.BTCustNumName:str = obj["BTCustNumName"]
      self.CurrencyCodeBaseCurr:bool = obj["CurrencyCodeBaseCurr"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCSORow:
   def __init__(self, obj):
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CurrencyName:str = obj["CurrencyName"]
      self.DocOutSOValue:int = obj["DocOutSOValue"]
      self.OpenOrder:bool = obj["OpenOrder"]
      self.OrderDate:str = obj["OrderDate"]
      self.OrderNum:int = obj["OrderNum"]
      self.OutSOValue:int = obj["OutSOValue"]
      self.PoNum:str = obj["PoNum"]
      self.Rpt1OutSOValue:int = obj["Rpt1OutSOValue"]
      self.Rpt2OutSOValue:int = obj["Rpt2OutSOValue"]
      self.Rpt3OutSOValue:int = obj["Rpt3OutSOValue"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARLOCTableset:
   def __init__(self, obj):
      self.ARLOC:list[Erp_Tablesets_ARLOCRow] = obj["ARLOC"]
      self.ARLOCAttch:list[Erp_Tablesets_ARLOCAttchRow] = obj["ARLOCAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARLOCTrackerTableset:
   def __init__(self, obj):
      self.ARLOCInvc:list[Erp_Tablesets_ARLOCInvcRow] = obj["ARLOCInvc"]
      self.ARLOCSO:list[Erp_Tablesets_ARLOCSORow] = obj["ARLOCSO"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtARLOCTableset:
   def __init__(self, obj):
      self.ARLOC:list[Erp_Tablesets_ARLOCRow] = obj["ARLOC"]
      self.ARLOCAttch:list[Erp_Tablesets_ARLOCAttchRow] = obj["ARLOCAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetARLOCInvoices_input:
   """ Required : 
   arlocid
   """  
   def __init__(self, obj):
      self.arlocid:str = obj["arlocid"]
      """  AR Letters Of Credit ID  """  
      pass

class GetARLOCInvoices_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARLOCTrackerTableset] = obj["returnObj"]
      pass

class GetARLOCSOrders_input:
   """ Required : 
   arlocid
   """  
   def __init__(self, obj):
      self.arlocid:str = obj["arlocid"]
      """  AR Letters Of Credit ID  """  
      pass

class GetARLOCSOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARLOCTrackerTableset] = obj["returnObj"]
      pass

class GetAvailBTList_input:
   """ Required : 
   pcCurComp
   piCustNum
   pcCustID
   """  
   def __init__(self, obj):
      self.pcCurComp:str = obj["pcCurComp"]
      """  Current Company  """  
      self.piCustNum:int = obj["piCustNum"]
      """  Customer Number  """  
      self.pcCustID:str = obj["pcCustID"]
      """  Customer ID  """  
      pass

class GetAvailBTList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cBillToList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_ARLOCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARLOCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARLOCTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARLOCListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewARLOCAttch_input:
   """ Required : 
   ds
   lcID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      self.lcID:str = obj["lcID"]
      pass

class GetNewARLOCAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARLOC_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class GetNewARLOC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseARLOC
   whereClauseARLOCAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseARLOC:str = obj["whereClauseARLOC"]
      self.whereClauseARLOCAttch:str = obj["whereClauseARLOCAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARLOCTableset] = obj["returnObj"]
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

class OnChangeOfDocLCValue_input:
   """ Required : 
   proposedLCValue
   ds
   """  
   def __init__(self, obj):
      self.proposedLCValue:int = obj["proposedLCValue"]
      """  Proposed From Date  """  
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class OnChangeOfDocLCValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class OnChangeOfFromDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class OnChangeOfToDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARLOCTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARLOCTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARLOCTableset] = obj["ds"]
      pass

      """  output parameters  """  

