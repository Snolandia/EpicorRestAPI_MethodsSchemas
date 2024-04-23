import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TransferOrderEntrySvc
# Description: Creates Transfer Orders
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TransferOrderEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TransferOrderEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransferOrderEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries",headers=creds) as resp:
           return await resp.json()

async def post_TransferOrderEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransferOrderEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFOrdHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TransferOrderEntries_Company_TFOrdNum(Company, TFOrdNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TransferOrderEntry item
   Description: Calls GetByID to retrieve the TransferOrderEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransferOrderEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFOrdHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TransferOrderEntries_Company_TFOrdNum(Company, TFOrdNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TransferOrderEntry for the service
   Description: Calls UpdateExt to update TransferOrderEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransferOrderEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TransferOrderEntries_Company_TFOrdNum(Company, TFOrdNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TransferOrderEntry item
   Description: Call UpdateExt to delete TransferOrderEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransferOrderEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransferOrderEntries_Company_TFOrdNum_TFOrdDtls(Company, TFOrdNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFOrdDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFOrdDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdDtls",headers=creds) as resp:
           return await resp.json()

async def get_TransferOrderEntries_Company_TFOrdNum_TFOrdDtls_Company_TFLineNum(Company, TFOrdNum, TFLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFOrdDtl item
   Description: Calls GetByID to retrieve the TFOrdDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdDtls(" + Company + "," + TFLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransferOrderEntries_Company_TFOrdNum_TFOrdHedAttches(Company, TFOrdNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFOrdHedAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFOrdHedAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdHedAttches",headers=creds) as resp:
           return await resp.json()

async def get_TransferOrderEntries_Company_TFOrdNum_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company, TFOrdNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFOrdHedAttch item
   Description: Calls GetByID to retrieve the TFOrdHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdHedAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TransferOrderEntries(" + Company + "," + TFOrdNum + ")/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFOrdDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFOrdDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFOrdDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls",headers=creds) as resp:
           return await resp.json()

async def post_TFOrdDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFOrdDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFOrdDtls_Company_TFLineNum(Company, TFLineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFOrdDtl item
   Description: Calls GetByID to retrieve the TFOrdDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls(" + Company + "," + TFLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFOrdDtls_Company_TFLineNum(Company, TFLineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFOrdDtl for the service
   Description: Calls UpdateExt to update TFOrdDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFOrdDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls(" + Company + "," + TFLineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFOrdDtls_Company_TFLineNum(Company, TFLineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFOrdDtl item
   Description: Call UpdateExt to delete TFOrdDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFOrdDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFLineNum: Desc: TFLineNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdDtls(" + Company + "," + TFLineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFOrdHedAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFOrdHedAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFOrdHedAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches",headers=creds) as resp:
           return await resp.json()

async def post_TFOrdHedAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFOrdHedAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company, TFOrdNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFOrdHedAttch item
   Description: Calls GetByID to retrieve the TFOrdHedAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFOrdHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company, TFOrdNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFOrdHedAttch for the service
   Description: Calls UpdateExt to update TFOrdHedAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFOrdHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFOrdHedAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFOrdHedAttches_Company_TFOrdNum_DrawingSeq(Company, TFOrdNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFOrdHedAttch item
   Description: Call UpdateExt to delete TFOrdHedAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFOrdHedAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TFOrdNum: Desc: TFOrdNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/TFOrdHedAttches(" + Company + "," + TFOrdNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFOrdHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTFOrdHed, whereClauseTFOrdHedAttch, whereClauseTFOrdDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseTFOrdHed=" + whereClauseTFOrdHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFOrdHedAttch=" + whereClauseTFOrdHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tfOrdNum, epicorHeaders = None):
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
   params += "tfOrdNum=" + tfOrdNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromPlant
   Description: Sets the transfer ship via code base on fromplant
   OperationID: ChangeFromPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeShipVia(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeShipVia
   Description: Sets the transfer degtail ship via code from the header
   OperationID: ChangeShipVia
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeShipVia_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeShipVia_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTransferContractID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTransferContractID
   Description: Sets warehouse defaults when transfer Planning Contract or transfer link to contract are changed
   OperationID: ChangeTransferContractID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTransferContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSellingQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSellingQty
   Description: This method is to be called when the Selling Quantity field changes
   OperationID: ChangeSellingQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSellingQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSellingQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSellingQtyUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSellingQtyUOM
   Description: This method is to be called when the Selling Quantity UOM field changes
   OperationID: ChangeSellingQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSellingQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSellingQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFOrdDtlOrdNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFOrdDtlOrdNum
   Description: This method is to override the standard GetNewTFOrdDtl method since TFOrdDtl needs to
be passed in and that is no longer the primary key.
   OperationID: GetNewTFOrdDtlOrdNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdDtlOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdDtlOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustom
   Description: Custom GetList method. Retrieves records based on a delimited list
of Contract Numbers.
   OperationID: GetRowsCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsCustomPlantsWC(whereClauseTFOrdHed, whereClauseTFOrdHedAttch, whereClauseTFOrdDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomPlantsWC
   Description: Calls the GetRowsCustomPlants method, but this method allow the use of whereClauses for each DataView
<param name="whereClauseTFOrdHed">TFOrdHed WhereClause </param><param name="whereClauseTFOrdHedAttch">TFOrdHedAttch WhereClause </param><param name="whereClauseTFOrdDtl">TFOrdDtl WhereClause </param><param name="pageSize">The pageSize </param><param name="absolutePage">The absolutePage </param><param name="morePages">The morePages</param>
   OperationID: Get_GetRowsCustomPlantsWC
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomPlantsWC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFOrdHed=" + whereClauseTFOrdHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFOrdHedAttch=" + whereClauseTFOrdHedAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFOrdDtl=" + whereClauseTFOrdDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCustomPlants(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCustomPlants
   Description: Custom GetRows method. Retrieves records based on user
authorized plants.
   OperationID: GetRowsCustomPlants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCustomPlants_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCustomPlants_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransferShipDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransferShipDate
   Description: Sets the transfer ship date base on fromplant, toplant, and needbydate.
It's calculated using the needby date and subtracting the transfers days
held in the PltTranDef Table.
   OperationID: GetTransferShipDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferShipDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferShipDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: This method is to be called when the Part Number field changes
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePartAllocQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePartAllocQueue
   Description: Update the fulfillment queue with the lines on this transfer order.
   OperationID: UpdatePartAllocQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePartAllocQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePartAllocQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeUpdate
   Description: Checks before performing the transfer order update
   OperationID: CheckBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFOrdHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFOrdHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFOrdHedAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFOrdHedAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdHedAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdHedAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdHedAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFOrdDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFOrdDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFOrdDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFOrdDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFOrdDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransferOrderEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFOrdDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFOrdHedAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFOrdHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFOrdHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFOrdHedRow] = obj["value"]
      pass

class Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.TransferContractID:str = obj["TransferContractID"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  """  
      self.TransferLinkToContract:bool = obj["TransferLinkToContract"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the transfer order line should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order line is ready to be fulfilled.  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.BinNum:str = obj["BinNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.DUM:str = obj["DUM"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.Packages:int = obj["Packages"]
      self.PCID:str = obj["PCID"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      self.Selected:bool = obj["Selected"]
      self.StagingBinDesc:str = obj["StagingBinDesc"]
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.Weight:int = obj["Weight"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this release is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartDescTrackInventoryAttributes:bool = obj["PartDescTrackInventoryAttributes"]
      self.PartDescAttrClassID:str = obj["PartDescAttrClassID"]
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      self.PartDescIUM:str = obj["PartDescIUM"]
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      self.PartDescTrackInventoryByRevision:bool = obj["PartDescTrackInventoryByRevision"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TFOrdNum:str = obj["TFOrdNum"]
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

class Erp_Tablesets_TFOrdHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTo information defined for this release should be used.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time ShipTo Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time ShipTo first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time ShipTo second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time ShipTo third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portionof the One Time ShipTo address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or provine portion of the One Time ShipTo address.  """  
      self.OTSZip:str = obj["OTSZip"]
      """  The zip or postal code portion of the One Time ShipTo address.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time ShipTo contact name.  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax Number for the One Time ShipTo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.RequestDate:str = obj["RequestDate"]
      self.EntryPersonName:str = obj["EntryPersonName"]
      """  User Name  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTo information defined for this release should be used.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time ShipTo Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time ShipTo first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time ShipTo second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time ShipTo third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portionof the One Time ShipTo address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or provine portion of the One Time ShipTo address.  """  
      self.OTSZip:str = obj["OTSZip"]
      """  The zip or postal code portion of the One Time ShipTo address.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time ShipTo contact name.  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax Number for the One Time ShipTo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order is ready to be fulfilled.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.RequestDate:str = obj["RequestDate"]
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.UpdateDtlRecords:bool = obj["UpdateDtlRecords"]
      """  Flag to indicate if details need to be refreshed after changing the header.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EntryPersonName:str = obj["EntryPersonName"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeFromPlant_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class ChangeFromPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSellingQtyUOM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class ChangeSellingQtyUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSellingQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class ChangeSellingQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeShipVia_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class ChangeShipVia_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTransferContractID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class ChangeTransferContractID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBeforeUpdate_input:
   """ Required : 
   viewName
   ds
   """  
   def __init__(self, obj):
      self.viewName:str = obj["viewName"]
      """  View name  """  
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class CheckBeforeUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.tfOrdHedChangedMsgText:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   tfOrdNum
   """  
   def __init__(self, obj):
      self.tfOrdNum:str = obj["tfOrdNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TFOrdDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  Will be blank unless a header is tied to the table  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrdNum make up the unique key to  link to the TFOrdHed table. The system generates this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.OrderFirm:bool = obj["OrderFirm"]
      """  Indicates an Unfirm Transfer Order.  Similar to JobFirm  """  
      self.RequestDate:str = obj["RequestDate"]
      """  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.ManualOrder:bool = obj["ManualOrder"]
      """  Indicates if the Order was created through MRP or by UI Entry.  If Manual and Unfirm, MRP will not delete the Order  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job number of the job supplying the parts for this record (FromSite)  """  
      self.DemandJobNum:str = obj["DemandJobNum"]
      """  Job number of the job demand for the parts on this record (ToSite)  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Received Quantity  """  
      self.AdditionalQty:int = obj["AdditionalQty"]
      """  Additional quantity beyond the initial requirement to be transferred  """  
      self.FirmDate:str = obj["FirmDate"]
      """  Date transfer suggestion went firm  """  
      self.FirmUser:str = obj["FirmUser"]
      """  User who made the transfer suggestion firm  """  
      self.DemandAsmSeq:int = obj["DemandAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.DemandMtlSeq:int = obj["DemandMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.SupplyAsmSeq:int = obj["SupplyAsmSeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.SupplyMtlSeq:int = obj["SupplyMtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  """  
      self.StockTrans:bool = obj["StockTrans"]
      """  Indicates if this requirement/receipt affects stock.  """  
      self.OurStockQtyUOM:str = obj["OurStockQtyUOM"]
      """   Unit of Measure code of the order quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQtyUOM:str = obj["SellingQtyUOM"]
      """   Unit of Measure code of the selling quantity
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.SellingQty:int = obj["SellingQty"]
      """  Selling Quantity  """  
      self.SellingShippedQty:int = obj["SellingShippedQty"]
      """  Selling Shipped Quantity  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  Indicates if the transfer order line is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  """  
      self.StagingWarehouseCode:str = obj["StagingWarehouseCode"]
      """  The transfer order "Staging" warehouse for the transfer order line.  Defaults from the system default warehouse (Site.DefTFOrdPickWhse).  """  
      self.StagingBinNum:str = obj["StagingBinNum"]
      """  The transfer order "Staging" bin for the transfer order line.  Defaults from the system default bin (Site.DefTFOrdPickBin).  """  
      self.PickError:str = obj["PickError"]
      """   A non blank character indicates that the transfer order line could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  LinkToContract  """  
      self.TransferContractID:str = obj["TransferContractID"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferContractID field is designed to select a new planning contract valid for the plant that supplies the demand. ContractID field keeps the ContractID valid for the demand plant.  """  
      self.TransferLinkToContract:bool = obj["TransferLinkToContract"]
      """  Transfer Orders are multi plant while Planning Contracts are plant specific. TransferLinkToContract field is designed to work for TransferContractID valid for the plant that suppies the demand. LinkToContract works for ContractID field valid for the demand plant.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartAllocQueueAction:str = obj["PartAllocQueueAction"]
      """  Indicates if the transfer order line should be added or removed from the fulfillment queue.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order line is ready to be fulfilled.  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      self.BinNum:str = obj["BinNum"]
      self.DimCode:str = obj["DimCode"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  DimCodeDimCodeDescription  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockQty * DimConvFactor  """  
      self.DUM:str = obj["DUM"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  Inventory UOM that the Transfer Order Detail is allocated against.  """  
      self.LineStatus:str = obj["LineStatus"]
      """  Descriptive Text of OpenLine Field  """  
      self.LotNum:str = obj["LotNum"]
      self.Packages:int = obj["Packages"]
      self.PCID:str = obj["PCID"]
      self.PkgClass:str = obj["PkgClass"]
      self.PkgClassDescription:str = obj["PkgClassDescription"]
      """  PkgClassDescription  """  
      self.PkgCode:str = obj["PkgCode"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      """  PkgCodeDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      self.Selected:bool = obj["Selected"]
      self.StagingBinDesc:str = obj["StagingBinDesc"]
      self.ThisOrderInvtyQty:int = obj["ThisOrderInvtyQty"]
      """  This order inventory quantity  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.TotNetWeight:int = obj["TotNetWeight"]
      self.Weight:int = obj["Weight"]
      self.CreateOrder:bool = obj["CreateOrder"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  Error Status Display  """  
      self.InPartAllocQueue:bool = obj["InPartAllocQueue"]
      """  True if this release is in the fulfillment queue.  """  
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PartDescTrackInventoryAttributes:bool = obj["PartDescTrackInventoryAttributes"]
      self.PartDescAttrClassID:str = obj["PartDescAttrClassID"]
      self.PartDescPricePerCode:str = obj["PartDescPricePerCode"]
      self.PartDescTrackSerialNum:bool = obj["PartDescTrackSerialNum"]
      self.PartDescPartDescription:str = obj["PartDescPartDescription"]
      self.PartDescTrackDimension:bool = obj["PartDescTrackDimension"]
      self.PartDescSalesUM:str = obj["PartDescSalesUM"]
      self.PartDescIUM:str = obj["PartDescIUM"]
      self.PartDescSellingFactor:int = obj["PartDescSellingFactor"]
      self.PartDescTrackLots:bool = obj["PartDescTrackLots"]
      self.PartDescTrackInventoryByRevision:bool = obj["PartDescTrackInventoryByRevision"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.StageWhseCodeDescription:str = obj["StageWhseCodeDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdHedAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TFOrdNum:str = obj["TFOrdNum"]
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

class Erp_Tablesets_TFOrdHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTo information defined for this release should be used.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time ShipTo Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time ShipTo first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time ShipTo second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time ShipTo third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portionof the One Time ShipTo address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or provine portion of the One Time ShipTo address.  """  
      self.OTSZip:str = obj["OTSZip"]
      """  The zip or postal code portion of the One Time ShipTo address.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time ShipTo contact name.  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax Number for the One Time ShipTo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.RequestDate:str = obj["RequestDate"]
      self.EntryPersonName:str = obj["EntryPersonName"]
      """  User Name  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFOrdHedListTableset:
   def __init__(self, obj):
      self.TFOrdHedList:list[Erp_Tablesets_TFOrdHedListRow] = obj["TFOrdHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TFOrdHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.OpenOrder:bool = obj["OpenOrder"]
      """  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  """  
      self.OrderDate:str = obj["OrderDate"]
      """  Mandatory entry and must be valid. Default as the system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  """  
      self.PickListComment:str = obj["PickListComment"]
      """  Contains picking  comments about the overall order. These will be printed on the picking lists.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTo information defined for this release should be used.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time ShipTo Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time ShipTo first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time ShipTo second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time ShipTo third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portionof the One Time ShipTo address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or provine portion of the One Time ShipTo address.  """  
      self.OTSZip:str = obj["OTSZip"]
      """  The zip or postal code portion of the One Time ShipTo address.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time ShipTo contact name.  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo.  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax Number for the One Time ShipTo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the transfer order is ready to be fulfilled.  """  
      self.ToPlantDesc:str = obj["ToPlantDesc"]
      self.FromPlantDesc:str = obj["FromPlantDesc"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.RequestDate:str = obj["RequestDate"]
      self.ShowFulfillmentQueueActions:bool = obj["ShowFulfillmentQueueActions"]
      """  Show Fulfillment Queue Actions  """  
      self.UpdateDtlRecords:bool = obj["UpdateDtlRecords"]
      """  Flag to indicate if details need to be refreshed after changing the header.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.EntryPersonName:str = obj["EntryPersonName"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TransferOrderEntryTableset:
   def __init__(self, obj):
      self.TFOrdHed:list[Erp_Tablesets_TFOrdHedRow] = obj["TFOrdHed"]
      self.TFOrdHedAttch:list[Erp_Tablesets_TFOrdHedAttchRow] = obj["TFOrdHedAttch"]
      self.TFOrdDtl:list[Erp_Tablesets_TFOrdDtlRow] = obj["TFOrdDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTransferOrderEntryTableset:
   def __init__(self, obj):
      self.TFOrdHed:list[Erp_Tablesets_TFOrdHedRow] = obj["TFOrdHed"]
      self.TFOrdHedAttch:list[Erp_Tablesets_TFOrdHedAttchRow] = obj["TFOrdHedAttch"]
      self.TFOrdDtl:list[Erp_Tablesets_TFOrdDtlRow] = obj["TFOrdDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   tfOrdNum
   """  
   def __init__(self, obj):
      self.tfOrdNum:str = obj["tfOrdNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   TransferOrderList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.TransferOrderList:str = obj["TransferOrderList"]
      """  The Transfer Order List  """  
      self.pageSize:int = obj["pageSize"]
      """  The pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePage  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TFOrdHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_TFOrdHedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTFOrdDtlOrdNum_input:
   """ Required : 
   ds
   TFOrdNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Number  """  
      pass

class GetNewTFOrdDtlOrdNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFOrdDtl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class GetNewTFOrdDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFOrdHedAttch_input:
   """ Required : 
   ds
   tfOrdNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      self.tfOrdNum:str = obj["tfOrdNum"]
      pass

class GetNewTFOrdHedAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFOrdHed_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class GetNewTFOrdHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsCustomPlantsWC_input:
   """ Required : 
   whereClauseTFOrdHed
   whereClauseTFOrdHedAttch
   whereClauseTFOrdDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTFOrdHed:str = obj["whereClauseTFOrdHed"]
      self.whereClauseTFOrdHedAttch:str = obj["whereClauseTFOrdHedAttch"]
      self.whereClauseTFOrdDtl:str = obj["whereClauseTFOrdDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsCustomPlantsWC_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustomPlants_input:
   """ Required : 
   TransferOrderList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.TransferOrderList:str = obj["TransferOrderList"]
      """  The Transfer Order number list  """  
      self.pageSize:int = obj["pageSize"]
      """  The pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePage  """  
      pass

class GetRowsCustomPlants_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsCustom_input:
   """ Required : 
   TransferOrderList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.TransferOrderList:str = obj["TransferOrderList"]
      """  The Transfer Order number list  """  
      self.pageSize:int = obj["pageSize"]
      """  The pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolutePage  """  
      pass

class GetRowsCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTFOrdHed
   whereClauseTFOrdHedAttch
   whereClauseTFOrdDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTFOrdHed:str = obj["whereClauseTFOrdHed"]
      self.whereClauseTFOrdHedAttch:str = obj["whereClauseTFOrdHedAttch"]
      self.whereClauseTFOrdDtl:str = obj["whereClauseTFOrdDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTransferShipDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class GetTransferShipDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
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

class OnChangePartNum_input:
   """ Required : 
   partNum
   ds
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransferOrderEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransferOrderEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePartAllocQueue_input:
   """ Required : 
   tfOrdNum
   action
   """  
   def __init__(self, obj):
      self.tfOrdNum:str = obj["tfOrdNum"]
      """  The transfer order number  """  
      self.action:str = obj["action"]
      """  The fulfillment queue action to take ("SEND" or "REMOVE")  """  
      pass

class UpdatePartAllocQueue_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["returnObj"]
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransferOrderEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

