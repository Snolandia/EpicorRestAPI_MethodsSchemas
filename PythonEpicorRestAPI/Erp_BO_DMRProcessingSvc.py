import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DMRProcessingSvc
# Description: DMR Processing Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DMRProcessings(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DMRProcessings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRProcessings
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings",headers=creds) as resp:
           return await resp.json()

async def post_DMRProcessings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRProcessings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DMRProcessings_Company_DMRNum(Company, DMRNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRProcessing item
   Description: Calls GetByID to retrieve the DMRProcessing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRProcessing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DMRProcessings_Company_DMRNum(Company, DMRNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DMRProcessing for the service
   Description: Calls UpdateExt to update DMRProcessing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRProcessing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DMRProcessings_Company_DMRNum(Company, DMRNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DMRProcessing item
   Description: Call UpdateExt to delete DMRProcessing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRProcessing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DMRProcessings_Company_DMRNum_DMRActns(Company, DMRNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DMRActns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DMRActns1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRActns",headers=creds) as resp:
           return await resp.json()

async def get_DMRProcessings_Company_DMRNum_DMRActns_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRActn item
   Description: Calls GetByID to retrieve the DMRActn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRActn1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DMRProcessings_Company_DMRNum_DMRHeadAttches(Company, DMRNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DMRHeadAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DMRHeadAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRHeadAttches",headers=creds) as resp:
           return await resp.json()

async def get_DMRProcessings_Company_DMRNum_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company, DMRNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRHeadAttch item
   Description: Calls GetByID to retrieve the DMRHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRHeadAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRProcessings(" + Company + "," + DMRNum + ")/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DMRActns(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DMRActns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRActns
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRActnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns",headers=creds) as resp:
           return await resp.json()

async def post_DMRActns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRActns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DMRActns_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRActn item
   Description: Calls GetByID to retrieve the DMRActn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRActn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DMRActns_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DMRActn for the service
   Description: Calls UpdateExt to update DMRActn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRActn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRActnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DMRActns_Company_DMRNum_ActionNum(Company, DMRNum, ActionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DMRActn item
   Description: Call UpdateExt to delete DMRActn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRActn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param ActionNum: Desc: ActionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRActns(" + Company + "," + DMRNum + "," + ActionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DMRHeadAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DMRHeadAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DMRHeadAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches",headers=creds) as resp:
           return await resp.json()

async def post_DMRHeadAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DMRHeadAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company, DMRNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DMRHeadAttch item
   Description: Calls GetByID to retrieve the DMRHeadAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DMRHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company, DMRNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DMRHeadAttch for the service
   Description: Calls UpdateExt to update DMRHeadAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DMRHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DMRHeadAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DMRHeadAttches_Company_DMRNum_DrawingSeq(Company, DMRNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DMRHeadAttch item
   Description: Call UpdateExt to delete DMRHeadAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DMRHeadAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DMRNum: Desc: DMRNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/DMRHeadAttches(" + Company + "," + DMRNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DMRHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDMRHead, whereClauseDMRHeadAttch, whereClauseDMRActn, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseDMRHead=" + whereClauseDMRHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDMRHeadAttch=" + whereClauseDMRHeadAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDMRActn=" + whereClauseDMRActn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(dmRNum, epicorHeaders = None):
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
   params += "dmRNum=" + dmRNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyCode
   Description: This method recalculates the exchange rate and base price when the currency code changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeExchangeRate
   Description: This method recalculates the base price when the exchange rate changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobAsmSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobAsmSeq
   Description: This method initializes the job material sequence and accepted quantity
when the Job Assembly Sequence changes.
   OperationID: ChangeJobAsmSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobAsmSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobAsmSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobMtlSeq
   Description: This method initializes the IssuedComplete check box and defaults Warehouse
and Bin (if necessary) when the Job Material Sequence changes.
   OperationID: ChangeJobMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobNum
   Description: This method initializes the job assembly/material sequences, accepted quantity
and the comment text when the Job Number changes.
   OperationID: ChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackingSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackingSlip
   Description: This method retrieves information related to the packing slip where this material was originally received.
   OperationID: ChangePackingSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackingSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackingSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePackingSlipLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePackingSlipLine
   Description: This method retrieves information related to the packing slip where this material was originally received.
   OperationID: ChangePackingSlipLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePackingSlipLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePackingSlipLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRefInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRefInvoiceNum
   Description: This method validates Ref Invoice Number.
   OperationID: ChangeRefInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRefInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRefInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCID
   Description: Validates that PCID exists
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResolution(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResolution
   Description: This method check if there is an Invoice for the PONum/line.
   OperationID: OnChangeResolution
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResolution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResolution_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeStkWhs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeStkWhs
   Description: This method initializes the serial tracking data when the Accept to Stock
warehoues changes, because a warehouse change might mean a "to" plant change
which can affect serial process under some circumstances.
Updates values of warehouse and primary bin (if any)
   OperationID: ChangeStkWhs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeStkWhs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeStkWhs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnitCredit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnitCredit
   Description: This method recalculates the base price when the doc price changes or recalculates
the doc price when the base price changes.  The CurrencySwitch flag in DMRActn is used to
determine which value to calculate.
   OperationID: ChangeUnitCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnitCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnitCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarehouse
   Description: This method will load the bin number only if one bin exists for the selected warehouse.
   OperationID: ChangeWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIssueComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIssueComplete
   Description: This method returns text of a message to be asked of the user when changing the
issue complete flag for Accepting to Job Materials.  The purpose of the question
is to verify the user wants to continue with the change.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckIssueComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIssueComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIssueComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckJobMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckJobMtlSeq
   Description: This method returns a message for the user if the job material selected is already issued
complete. The user would then have the option to continue with the selected
job material or change the material sequence.
   OperationID: CheckJobMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckJobMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckJobMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlanningContractBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlanningContractBin
   Description: Method to check Contract bin.
   OperationID: CheckPlanningContractBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlanningContractBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlanningContractBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOperationComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOperationComplete
   Description: This method returns text of a message to be asked of the user when changing the
operation complete flag for Accepting to Job Operations.  The purpose of the question
is to verify the user wants to continue with the change.
If the user answers yes, the change can occur; otherwise the change shouldn't occur.
   OperationID: CheckOperationComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOperationComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOperationComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRejectDisabled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRejectDisabled
   Description: This method returns the DMR Action Debit Memo created by this rejection.
   OperationID: CheckRejectDisabled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRejectDisabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRejectDisabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDebitMemoNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDebitMemoNum
   Description: This method fills the DebitMemoNum from database.
   OperationID: UpdateDebitMemoNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDebitMemoNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDebitMemoNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomUpdate
   OperationID: CustomUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultIssueComplete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultIssueComplete
   Description: This method defaults the appropriate value for the Issue Complete check box
whenever the quantity to be accepted to Job Material changes. Also defaults
the appropiate value for the Operation Complete check box whenever the quantity
to be accepted to Job Operation changes.
   OperationID: DefaultIssueComplete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultIssueComplete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultIssueComplete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCNCustomsDeclarationBillLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCNCustomsDeclarationBillLine
   Description: Purpose:  Check Declaration Bill Line
Parameters:
<param name="bBeforeUpdate">if True - method is called before updating</param><param name="sMessage">Warning</param><param name="ds"></param>
   OperationID: CheckCNCustomsDeclarationBillLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCNCustomsDeclarationBillLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContactInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContactInfo
   Description: This method updates the default Contact information when the ConNum field changes.
   OperationID: GetContactInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContactInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContactInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base CurrencyCode
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDMRHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDMRHistory
   Description: Get DMR history
   OperationID: GetDMRHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDMRHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDMRHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActnAcceptMTL(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActnAcceptMTL
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Material to Job Material) is created.  This method requires the DMR Number
as input parameter.  In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptMTL
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptMTL_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptMTL_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActnAcceptOPR(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActnAcceptOPR
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Material to Job Operation) is created.  This method requires the DMR Number
as input parameter.  In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptOPR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptOPR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptOPR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActnAcceptSTK(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActnAcceptSTK
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Material to Stock) is created. This method requires the DMR Number as
the input parameter. In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptSTK
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptSTK_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptSTK_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActnAcceptCUST(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActnAcceptCUST
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Accepting Return to Customer) is created. This method requires the DMR Number as
the input parameter. In addition, this method sets the external fields to indicate
whether certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnAcceptCUST
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnAcceptCUST_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnAcceptCUST_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActnDebitMemo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActnDebitMemo
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Requesting Debit Memo) is created.  This method requires the DMR Number as input
parameter. In addition, this method sets the external fields to indicate whether
certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnDebitMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnDebitMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnDebitMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActnReject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActnReject
   Description: Call this method instead of GetNewDMRActn to assure that appropriate DMR Action
(Rejecting Material) is created.  This method requires the DMR Number as input
parameter. In addition, this method sets the external fields to indicate whether
certain fields are enabled or disabled for input.
   OperationID: GetNewDMRActnReject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActnReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActnReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPurPointInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPurPointInfo
   Description: This method updates Purchase Point default information when the PurPoint
field changes.
   OperationID: GetPurPointInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPurPointInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPurPointInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorInfo
   Description: This method updates the default Vendor information when the VendorNumVendorID
field changes.
   OperationID: GetVendorInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method does one thing.
1 . This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The requiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReasonCodeWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReasonCodeWhereClause
   Description: This method returns the reason code where clause for searching for Reason codes
for DMR Rejections or Request of Debit Memos.
   OperationID: ReasonCodeWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReasonCodeWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReasonCodeWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRHeadAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRHeadAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRHeadAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRHeadAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRHeadAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDMRActn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDMRActn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDMRActn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDMRActn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDMRActn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DMRProcessingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRActnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRActnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRHeadAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DMRHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DMRHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Erp_Tablesets_DMRActnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  DMR Action Date.  """  
      self.ActionType:str = obj["ActionType"]
      """  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  """  
      self.Quantity:int = obj["Quantity"]
      """  DMR Action quantity in base unit of measure.  Must be > ZERO.  """  
      self.DestinationType:str = obj["DestinationType"]
      """  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.DMRSeqNum:int = obj["DMRSeqNum"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.UnitCredit:int = obj["UnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DocUnitCredit:int = obj["DocUnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.CreditUM:str = obj["CreditUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DebitMemoNum:str = obj["DebitMemoNum"]
      """  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  """  
      self.DebitMemoLine:int = obj["DebitMemoLine"]
      """  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  """  
      self.ActionUserID:str = obj["ActionUserID"]
      """  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Required for all actions.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.FldWarehouseCode:str = obj["FldWarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.FldBinNum:str = obj["FldBinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1UnitCredit:int = obj["Rpt1UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCredit:int = obj["Rpt2UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCredit:int = obj["Rpt3UnitCredit"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Resolution:str = obj["Resolution"]
      """   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  """  
      self.ReturnToSupplier:bool = obj["ReturnToSupplier"]
      """  Flag indicating that the part will be returned to the supplier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  This is the supplier's packing slip number for the original receipt of the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.DisableRejection:bool = obj["DisableRejection"]
      """  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  """  
      self.DisableRejectionChar:str = obj["DisableRejectionChar"]
      """  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  """  
      self.RefInvoiceNum:str = obj["RefInvoiceNum"]
      """  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  IssuedComplete  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AcceptIUM:str = obj["AcceptIUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.ActionTypeDesc:str = obj["ActionTypeDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispQuantity:int = obj["DispQuantity"]
      """  External field for handling unit of measure conversions in the UI.  """  
      self.EnableBin:bool = obj["EnableBin"]
      """  Indicates if the Bin field should be enabled for input.  """  
      self.EnableReason:bool = obj["EnableReason"]
      """  Indicates if the Reason field should be enabled for input.  """  
      self.EnableReqMove:bool = obj["EnableReqMove"]
      """  Indicates if the RequestMove field should be enabled for input.  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      """  Indicates if the Warehouse field should be enabled for input.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OpenDMR:bool = obj["OpenDMR"]
      self.OperationComplete:bool = obj["OperationComplete"]
      """  Job Operation Complete  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.POCurrencyCode:str = obj["POCurrencyCode"]
      """  PO Currency Code.  """  
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.POUnitCost:int = obj["POUnitCost"]
      """  DMR item's unit cost in the POs currency.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RejectType:str = obj["RejectType"]
      self.RequestMove:bool = obj["RequestMove"]
      """  Request to Move  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      """  Reporting currency value of this field  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial processing for this transaction record  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  """  
      self.TotRemainQty:int = obj["TotRemainQty"]
      self.TranQty:int = obj["TranQty"]
      """  TranQty  """  
      self.TranUOM:str = obj["TranUOM"]
      """  TranUOM  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Displays the customer name for the Ship To contact related to the RMA.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Displays the customer Ship To name related to the RMA.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  Customer that is returning parts on related RMA.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number that the Return detail is related to.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line that the Return detail is related to.  """  
      self.ShipToID:str = obj["ShipToID"]
      """  Specifies the ID of the Ship To contact related to the RMA.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DMRNum:int = obj["DMRNum"]
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

class Erp_Tablesets_DMRHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.OpenDMR:bool = obj["OpenDMR"]
      """  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact Person Number  """  
      self.TotDiscrepantQty:int = obj["TotDiscrepantQty"]
      """  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  """  
      self.TotRejectedQty:int = obj["TotRejectedQty"]
      """  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  """  
      self.TotAcceptedQty:int = obj["TotAcceptedQty"]
      """  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  """  
      self.AvgMtlUnitCost:int = obj["AvgMtlUnitCost"]
      """  Average Material Unit Cost.  """  
      self.AvgLbrUnitCost:int = obj["AvgLbrUnitCost"]
      """  Average Labor Unit cost.  """  
      self.AvgBurUnitCost:int = obj["AvgBurUnitCost"]
      """  Average Burden unit cost.  """  
      self.AvgSubUnitCost:int = obj["AvgSubUnitCost"]
      """  Average Subcontract unit cost  """  
      self.AvgMtlBurUnitCost:int = obj["AvgMtlBurUnitCost"]
      """  Average Mtl Burden unit cost  """  
      self.PartNum:str = obj["PartNum"]
      """  Parrt Number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  """  
      self.IUM:str = obj["IUM"]
      """  Base Inventory Unit of Measure.  System maintained, not user modifiable.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total Mtl Sub unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Material  Bur unit component cost to date  """  
      self.ReqDMR:bool = obj["ReqDMR"]
      """  Indicates this requires a Vendor RMA number  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors RMA number.  Defaults to DMR Number.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.DispTotAcceptedQty:int = obj["DispTotAcceptedQty"]
      self.DispTotRejectedQty:int = obj["DispTotRejectedQty"]
      self.DispTotRemainQty:int = obj["DispTotRemainQty"]
      self.DispTotDiscrepantQty:int = obj["DispTotDiscrepantQty"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.OpenDMR:bool = obj["OpenDMR"]
      """  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact Person Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR line item. These will be printed on the DMR Status Report.  """  
      self.TotDiscrepantQty:int = obj["TotDiscrepantQty"]
      """  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  """  
      self.TotRejectedQty:int = obj["TotRejectedQty"]
      """  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  """  
      self.TotAcceptedQty:int = obj["TotAcceptedQty"]
      """  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  """  
      self.AvgMtlUnitCost:int = obj["AvgMtlUnitCost"]
      """  Average Material Unit Cost.  """  
      self.AvgLbrUnitCost:int = obj["AvgLbrUnitCost"]
      """  Average Labor Unit cost.  """  
      self.AvgBurUnitCost:int = obj["AvgBurUnitCost"]
      """  Average Burden unit cost.  """  
      self.AvgSubUnitCost:int = obj["AvgSubUnitCost"]
      """  Average Subcontract unit cost  """  
      self.AvgMtlBurUnitCost:int = obj["AvgMtlBurUnitCost"]
      """  Average Mtl Burden unit cost  """  
      self.PartNum:str = obj["PartNum"]
      """  Parrt Number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  """  
      self.IUM:str = obj["IUM"]
      """  Base Inventory Unit of Measure.  System maintained, not user modifiable.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional DMR check off # 1. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional DMR check off # 2. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional DMR check off # 3. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """   Optional DMR check off # 4. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """   Optional DMR check off # 5. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total Mtl Sub unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Material  Bur unit component cost to date  """  
      self.ReqDMR:bool = obj["ReqDMR"]
      """  Indicates this requires a Vendor RMA number  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors RMA number.  Defaults to DMR Number.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PONum:int = obj["PONum"]
      """  PONum  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.RMANum:int = obj["RMANum"]
      """  RMANum  """  
      self.RMALine:int = obj["RMALine"]
      """  RMALine  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNReturnDate:str = obj["CNReturnDate"]
      """  Return Date  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.AllowAcceptToMtl:bool = obj["AllowAcceptToMtl"]
      self.AllowAcceptToOpr:bool = obj["AllowAcceptToOpr"]
      self.AllowAcceptToStock:bool = obj["AllowAcceptToStock"]
      self.CheckOffLabel1:str = obj["CheckOffLabel1"]
      self.CheckOffLabel2:str = obj["CheckOffLabel2"]
      self.CheckOffLabel3:str = obj["CheckOffLabel3"]
      self.CheckOffLabel4:str = obj["CheckOffLabel4"]
      self.CheckOffLabel5:str = obj["CheckOffLabel5"]
      self.DiscrepantUM:str = obj["DiscrepantUM"]
      self.DispTotAcceptedQty:int = obj["DispTotAcceptedQty"]
      self.DispTotDiscrepantQty:int = obj["DispTotDiscrepantQty"]
      self.DispTotRejectedQty:int = obj["DispTotRejectedQty"]
      self.DispTotRemainQty:int = obj["DispTotRemainQty"]
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.NonConfID:int = obj["NonConfID"]
      self.PanelView:str = obj["PanelView"]
      """  Indicates the panel view for this record (S)tock, (M)aterial, (O)peration  """  
      self.PlantName:str = obj["PlantName"]
      """  PlantName of the Plant  """  
      self.QtyRemaining:int = obj["QtyRemaining"]
      """  Remaining Quantity is the Total Discrepant Qty except the sum of the totals of the  AcceptedQty and RejectedQty  """  
      self.RejectedUM:str = obj["RejectedUM"]
      self.RemainUM:str = obj["RemainUM"]
      self.AcceptedUM:str = obj["AcceptedUM"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      """  Flag in PlantConfCtrl that enables Package Control functionality  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumEmailAddress:str = obj["ConNumEmailAddress"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
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
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class ChangeCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeExchangeRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class ChangeExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobAsmSeq_input:
   """ Required : 
   ds
   iProposedAssemblySeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.iProposedAssemblySeq:int = obj["iProposedAssemblySeq"]
      """  The proposed AssmeblySeq value  """  
      pass

class ChangeJobAsmSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobMtlSeq_input:
   """ Required : 
   ds
   iProposedDMRSeqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.iProposedDMRSeqNum:int = obj["iProposedDMRSeqNum"]
      """  The proposed material sequence number  """  
      pass

class ChangeJobMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobNum_input:
   """ Required : 
   ds
   cProposedJobNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.cProposedJobNum:str = obj["cProposedJobNum"]
      """  The proposed Job Number  """  
      pass

class ChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackingSlipLine_input:
   """ Required : 
   ds
   iDMRNum
   cProposedPackLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.iDMRNum:int = obj["iDMRNum"]
      """  The DMR Number  """  
      self.cProposedPackLine:int = obj["cProposedPackLine"]
      """  The proposed PackLine  """  
      pass

class ChangePackingSlipLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePackingSlip_input:
   """ Required : 
   ds
   iDMRNum
   cProposedPackSlip
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.iDMRNum:int = obj["iDMRNum"]
      """  The DMR Number  """  
      self.cProposedPackSlip:str = obj["cProposedPackSlip"]
      """  The proposed PackSlip  """  
      pass

class ChangePackingSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRefInvoiceNum_input:
   """ Required : 
   ds
   cProposedRefInvoiceNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.cProposedRefInvoiceNum:str = obj["cProposedRefInvoiceNum"]
      """  The proposed Ref Invoice Number  """  
      pass

class ChangeRefInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeStkWhs_input:
   """ Required : 
   ds
   cProposedWarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.cProposedWarehouseCode:str = obj["cProposedWarehouseCode"]
      """  The proposed Accept to Stock warehouse  """  
      pass

class ChangeStkWhs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUnitCredit_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class ChangeUnitCredit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeWarehouse_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class ChangeWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCNCustomsDeclarationBillLine_input:
   """ Required : 
   bBeforeUpdate
   ds
   """  
   def __init__(self, obj):
      self.bBeforeUpdate:bool = obj["bBeforeUpdate"]
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class CheckCNCustomsDeclarationBillLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckIssueComplete_input:
   """ Required : 
   iDMRNum
   cJobNum
   iAssemblySeq
   iDMRSeqNum
   dQuantity
   cUOM
   lProposedIssueComplete
   """  
   def __init__(self, obj):
      self.iDMRNum:int = obj["iDMRNum"]
      """  The DMR Number  """  
      self.cJobNum:str = obj["cJobNum"]
      """  The Job Number  """  
      self.iAssemblySeq:int = obj["iAssemblySeq"]
      """  The Assembly Sequence Number  """  
      self.iDMRSeqNum:int = obj["iDMRSeqNum"]
      """  The DMR Action Sequence Number (Material Sequence)  """  
      self.dQuantity:int = obj["dQuantity"]
      """  The DMRActn Quantity  """  
      self.cUOM:str = obj["cUOM"]
      """  The DMRActn UOM  """  
      self.lProposedIssueComplete:bool = obj["lProposedIssueComplete"]
      """  The proposed value for the Issue Complete flag  """  
      pass

class CheckIssueComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckJobMtlSeq_input:
   """ Required : 
   cJobNum
   iAssemblySeq
   iDMRSeqNum
   """  
   def __init__(self, obj):
      self.cJobNum:str = obj["cJobNum"]
      """  The job number  """  
      self.iAssemblySeq:int = obj["iAssemblySeq"]
      """  The assembly sequence  """  
      self.iDMRSeqNum:int = obj["iDMRSeqNum"]
      """  The DMR sequequence number  """  
      pass

class CheckJobMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckOperationComplete_input:
   """ Required : 
   cJobNum
   iAssemblySeq
   iDMRSeqNum
   lProposedOperationComplete
   """  
   def __init__(self, obj):
      self.cJobNum:str = obj["cJobNum"]
      """  The Job Number  """  
      self.iAssemblySeq:int = obj["iAssemblySeq"]
      """  The Assembly Sequence Number  """  
      self.iDMRSeqNum:int = obj["iDMRSeqNum"]
      """  The DMR Action Sequence Number (Operation Sequence)  """  
      self.lProposedOperationComplete:bool = obj["lProposedOperationComplete"]
      """  The proposed value for the Operation Complete flag  """  
      pass

class CheckOperationComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPlanningContractBin_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class CheckPlanningContractBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.pcPCBinAction:str = obj["parameters"]
      self.pcPCBinMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRejectDisabled_input:
   """ Required : 
   iDMRNum
   iDMRAction
   """  
   def __init__(self, obj):
      self.iDMRNum:int = obj["iDMRNum"]
      """  Actual dmr num.  """  
      self.iDMRAction:int = obj["iDMRAction"]
      """  Actual dmr action.  """  
      pass

class CheckRejectDisabled_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DebitMemo:str = obj["parameters"]
      pass

      """  output parameters  """  

class CustomUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class CustomUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.opLegalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DefaultIssueComplete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class DefaultIssueComplete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   dmRNum
   """  
   def __init__(self, obj):
      self.dmRNum:int = obj["dmRNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DMRActnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number.  Auto assign/increment starting at 1 for each DMR record.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  DMR Action Date.  """  
      self.ActionType:str = obj["ActionType"]
      """  DMR Action Type. "R" is Reject Material, "A" is Accept Material, "D" is Debit Memo Request, "C" is Require Supplier Credit.  """  
      self.Quantity:int = obj["Quantity"]
      """  DMR Action quantity in base unit of measure.  Must be > ZERO.  """  
      self.DestinationType:str = obj["DestinationType"]
      """  DMR Destination Type.  "S" is Stock, "M" is Material, "O" is Operation, "C" is return to Customer.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  ID for the warehouse .... assigned by the user.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.BinNum:str = obj["BinNum"]
      """  The user defined bin number within the warehouse.   Only maintainable when Action Type is "A" or Accept type only.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that this DMR Action record is related to.  Only maintainable when Action Type is "A" or Accept type only.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence # that this DMR is associated with.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.DMRSeqNum:int = obj["DMRSeqNum"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level.  Only maintainable when the Action Type is "A" or Accept type only.  """  
      self.UnitCredit:int = obj["UnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DocUnitCredit:int = obj["DocUnitCredit"]
      """  DMR item's unit cost in the vendors unit of measure.  Default can be obtained from the PODetail.UnitCost(Base currency) if related.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.CreditUM:str = obj["CreditUM"]
      """  Unit of Measure code for the vendor's quantity. Defaulted in the following hierarchy: from the RcvDtl.PUM if packing slip is referenced, from PODetail.PUM if PO is referenced, from Part.PUM if valid part or finally from XaSyst.DefaultUM.  Optional.  Only maintainable if Action Type is "D" or Debit type only.  """  
      self.DebitMemoNum:str = obj["DebitMemoNum"]
      """  DMR Debit Memo Number to for the DMR record.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet. It will be assigned with the APInvHed.InvoiceNum once the APInvHed record is created.  """  
      self.DebitMemoLine:int = obj["DebitMemoLine"]
      """  The line number of a Debit memo in the DMR record. This number uniquely identifies the debit memo record within a Debit memo.  Only used when Action Type is "D" (Debit) or "C" (Credit).  Zero means that a debit memo has not been created yet.  It will be assign with the APInvDtl.InvoiceLine once the APInvHed record is created.  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors Return Merchandise Authorization number for a returned product.  Only used when the Action type is Reject or "R" type only.  """  
      self.ActionUserID:str = obj["ActionUserID"]
      """  A User ID that created the DMR. Assign by the system using the current UserID at the time the record was created.  Just like the Entry Person field.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  System maintained, set to today's date value(SysDate = Today).  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  System maintained, set to the current time that this record was created.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR action line item. These will be printed on the DMR Status Report.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  DMRs use Reason type "D".  Required for all actions.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  """  
      self.FldWarehouseCode:str = obj["FldWarehouseCode"]
      """  Contains the Warehouse code of where this bin exists. This must be valid in the WareHouse table.  """  
      self.FldBinNum:str = obj["FldBinNum"]
      """  The user defined bin number within the warehouse.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Rpt1UnitCredit:int = obj["Rpt1UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitCredit:int = obj["Rpt2UnitCredit"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitCredit:int = obj["Rpt3UnitCredit"]
      """  Reporting currency value of this field  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier  """  
      self.Resolution:str = obj["Resolution"]
      """   The resolution of this rejected material (Code/Description):
DEBIT/Request Debit Memo
CREDIT/Require Supplier Credit
NONE/No Further Action  """  
      self.ReturnToSupplier:bool = obj["ReturnToSupplier"]
      """  Flag indicating that the part will be returned to the supplier.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  This is the supplier's packing slip number for the original receipt of the part.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.DisableRejection:bool = obj["DisableRejection"]
      """  Is a boolean and tell us about to disable or not the entire Rejection Screen. DisableRejection checks DisableRejectionChar to enable or disable.  """  
      self.DisableRejectionChar:str = obj["DisableRejectionChar"]
      """  Is a character and has the Company~Debit~ActionNum, has the linkedDebitMemo and helps to check if is needed the DisableRejection.  """  
      self.RefInvoiceNum:str = obj["RefInvoiceNum"]
      """  Displays the link AP Invoice linked to the Resolution Request Debit memo, Request Correction Invoice, Request supplier credit, the Reference invoice is created.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  IssuedComplete  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AcceptIUM:str = obj["AcceptIUM"]
      """  This is the unit of measure of the part.  Display this as the UM of the quantity being accepted.  """  
      self.ActionTypeDesc:str = obj["ActionTypeDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CurrSymbol:str = obj["CurrSymbol"]
      self.DispQuantity:int = obj["DispQuantity"]
      """  External field for handling unit of measure conversions in the UI.  """  
      self.EnableBin:bool = obj["EnableBin"]
      """  Indicates if the Bin field should be enabled for input.  """  
      self.EnableReason:bool = obj["EnableReason"]
      """  Indicates if the Reason field should be enabled for input.  """  
      self.EnableReqMove:bool = obj["EnableReqMove"]
      """  Indicates if the RequestMove field should be enabled for input.  """  
      self.EnableWarehouse:bool = obj["EnableWarehouse"]
      """  Indicates if the Warehouse field should be enabled for input.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OpenDMR:bool = obj["OpenDMR"]
      self.OperationComplete:bool = obj["OperationComplete"]
      """  Job Operation Complete  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates whether this DMRActn requires serial numbers, based on Part.TrackSerialNum and other criteria  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.POCurrencyCode:str = obj["POCurrencyCode"]
      """  PO Currency Code.  """  
      self.POLine:int = obj["POLine"]
      self.PONum:int = obj["PONum"]
      self.POUnitCost:int = obj["POUnitCost"]
      """  DMR item's unit cost in the POs currency.  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      self.RejectType:str = obj["RejectType"]
      self.RequestMove:bool = obj["RequestMove"]
      """  Request to Move  """  
      self.Rpt1POUnitCost:int = obj["Rpt1POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt2POUnitCost:int = obj["Rpt2POUnitCost"]
      """  Reporting currency value of this field  """  
      self.Rpt3POUnitCost:int = obj["Rpt3POUnitCost"]
      """  Reporting currency value of this field  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial processing for this transaction record  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If the SerialControlPlantIsFromPlt this field contains the plant id for the "to" plant for serial processing  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  if the plant that is controlling the serial processing is the from plant this will be yes, if it is the to plant it will be no.  """  
      self.TotRemainQty:int = obj["TotRemainQty"]
      self.TranQty:int = obj["TranQty"]
      """  TranQty  """  
      self.TranUOM:str = obj["TranUOM"]
      """  TranUOM  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  Displays the customer name for the Ship To contact related to the RMA.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Displays the customer Ship To name related to the RMA.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  Customer that is returning parts on related RMA.  """  
      self.RMANum:int = obj["RMANum"]
      """  The RMA Number that the Return detail is related to.  """  
      self.RMALine:int = obj["RMALine"]
      """  The RMA line that the Return detail is related to.  """  
      self.ShipToID:str = obj["ShipToID"]
      """  Specifies the ID of the Ship To contact related to the RMA.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRHeadAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DMRNum:int = obj["DMRNum"]
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

class Erp_Tablesets_DMRHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.OpenDMR:bool = obj["OpenDMR"]
      """  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact Person Number  """  
      self.TotDiscrepantQty:int = obj["TotDiscrepantQty"]
      """  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  """  
      self.TotRejectedQty:int = obj["TotRejectedQty"]
      """  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  """  
      self.TotAcceptedQty:int = obj["TotAcceptedQty"]
      """  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  """  
      self.AvgMtlUnitCost:int = obj["AvgMtlUnitCost"]
      """  Average Material Unit Cost.  """  
      self.AvgLbrUnitCost:int = obj["AvgLbrUnitCost"]
      """  Average Labor Unit cost.  """  
      self.AvgBurUnitCost:int = obj["AvgBurUnitCost"]
      """  Average Burden unit cost.  """  
      self.AvgSubUnitCost:int = obj["AvgSubUnitCost"]
      """  Average Subcontract unit cost  """  
      self.AvgMtlBurUnitCost:int = obj["AvgMtlBurUnitCost"]
      """  Average Mtl Burden unit cost  """  
      self.PartNum:str = obj["PartNum"]
      """  Parrt Number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  """  
      self.IUM:str = obj["IUM"]
      """  Base Inventory Unit of Measure.  System maintained, not user modifiable.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total Mtl Sub unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Material  Bur unit component cost to date  """  
      self.ReqDMR:bool = obj["ReqDMR"]
      """  Indicates this requires a Vendor RMA number  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors RMA number.  Defaults to DMR Number.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.DispTotAcceptedQty:int = obj["DispTotAcceptedQty"]
      self.DispTotRejectedQty:int = obj["DispTotRejectedQty"]
      self.DispTotRemainQty:int = obj["DispTotRemainQty"]
      self.DispTotDiscrepantQty:int = obj["DispTotDiscrepantQty"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRHeadListTableset:
   def __init__(self, obj):
      self.DMRHeadList:list[Erp_Tablesets_DMRHeadListRow] = obj["DMRHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DMRHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.OpenDMR:bool = obj["OpenDMR"]
      """  DMR Open or Close flag.  Default value is TRUE.  User cannot close a DMR with quantity remaining on it.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  Maintainable only if NOT attached to a receipt.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor Purchase Point.  Maintainable only if NOT attached to a receipt.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact Person Number  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the detail DMR line item. These will be printed on the DMR Status Report.  """  
      self.TotDiscrepantQty:int = obj["TotDiscrepantQty"]
      """  The total amount of discrepant material moved into the DMR in base inventory unit of measure(IUM).  """  
      self.TotRejectedQty:int = obj["TotRejectedQty"]
      """  The total amount of rejected material from this DMR in base inventory unit of measure(IUM).  """  
      self.TotAcceptedQty:int = obj["TotAcceptedQty"]
      """  The total amount of accepted material that was accepted from this DMR in base inventory unit of measure(IUM).  """  
      self.AvgMtlUnitCost:int = obj["AvgMtlUnitCost"]
      """  Average Material Unit Cost.  """  
      self.AvgLbrUnitCost:int = obj["AvgLbrUnitCost"]
      """  Average Labor Unit cost.  """  
      self.AvgBurUnitCost:int = obj["AvgBurUnitCost"]
      """  Average Burden unit cost.  """  
      self.AvgSubUnitCost:int = obj["AvgSubUnitCost"]
      """  Average Subcontract unit cost  """  
      self.AvgMtlBurUnitCost:int = obj["AvgMtlBurUnitCost"]
      """  Average Mtl Burden unit cost  """  
      self.PartNum:str = obj["PartNum"]
      """  Parrt Number  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  Set from the receipt or must match a referenced receipt's dimension.  NOT user modifiable.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number for this DMR to be received into.  Set from the receipt or must match a referenced receipt's lot number.  NOT user modifiable.  """  
      self.IUM:str = obj["IUM"]
      """  Base Inventory Unit of Measure.  System maintained, not user modifiable.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional DMR check off # 1. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional DMR check off # 2. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional DMR check off # 3. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """   Optional DMR check off # 4. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """   Optional DMR check off # 5. The label for this field is found in XASyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for DMR processes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number.  Associates the assembly record back its parent JobHead record.  Not directly maintainable.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  This can be user assigned or assigned by the system.  The system assigns the next available number during add mode if its left blank.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Contains the Warehouse code of where this part exists. This must be valid in the WareHouse table.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an On hand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Total Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Total Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Total Mtl Sub unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Total Material  Bur unit component cost to date  """  
      self.ReqDMR:bool = obj["ReqDMR"]
      """  Indicates this requires a Vendor RMA number  """  
      self.VendRMANum:str = obj["VendRMANum"]
      """  Vendors RMA number.  Defaults to DMR Number.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.PONum:int = obj["PONum"]
      """  PONum  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.RMANum:int = obj["RMANum"]
      """  RMANum  """  
      self.RMALine:int = obj["RMALine"]
      """  RMALine  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNReturnDate:str = obj["CNReturnDate"]
      """  Return Date  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.CNDeclarationBillLine:int = obj["CNDeclarationBillLine"]
      """  CNDeclarationBillLine  """  
      self.AllowAcceptToMtl:bool = obj["AllowAcceptToMtl"]
      self.AllowAcceptToOpr:bool = obj["AllowAcceptToOpr"]
      self.AllowAcceptToStock:bool = obj["AllowAcceptToStock"]
      self.CheckOffLabel1:str = obj["CheckOffLabel1"]
      self.CheckOffLabel2:str = obj["CheckOffLabel2"]
      self.CheckOffLabel3:str = obj["CheckOffLabel3"]
      self.CheckOffLabel4:str = obj["CheckOffLabel4"]
      self.CheckOffLabel5:str = obj["CheckOffLabel5"]
      self.DiscrepantUM:str = obj["DiscrepantUM"]
      self.DispTotAcceptedQty:int = obj["DispTotAcceptedQty"]
      self.DispTotDiscrepantQty:int = obj["DispTotDiscrepantQty"]
      self.DispTotRejectedQty:int = obj["DispTotRejectedQty"]
      self.DispTotRemainQty:int = obj["DispTotRemainQty"]
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.NonConfID:int = obj["NonConfID"]
      self.PanelView:str = obj["PanelView"]
      """  Indicates the panel view for this record (S)tock, (M)aterial, (O)peration  """  
      self.PlantName:str = obj["PlantName"]
      """  PlantName of the Plant  """  
      self.QtyRemaining:int = obj["QtyRemaining"]
      """  Remaining Quantity is the Total Discrepant Qty except the sum of the totals of the  AcceptedQty and RejectedQty  """  
      self.RejectedUM:str = obj["RejectedUM"]
      self.RemainUM:str = obj["RemainUM"]
      self.AcceptedUM:str = obj["AcceptedUM"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      """  Flag in PlantConfCtrl that enables Package Control functionality  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.ConNumName:str = obj["ConNumName"]
      self.ConNumPhoneNum:str = obj["ConNumPhoneNum"]
      self.ConNumEmailAddress:str = obj["ConNumEmailAddress"]
      self.ConNumFaxNum:str = obj["ConNumFaxNum"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRHistoryRow:
   def __init__(self, obj):
      self.TranDate:str = obj["TranDate"]
      self.TranType:str = obj["TranType"]
      self.InvAdjReason:str = obj["InvAdjReason"]
      self.JobNum:str = obj["JobNum"]
      self.Quantity:int = obj["Quantity"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.JobSeq:int = obj["JobSeq"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.ExtCost:int = obj["ExtCost"]
      self.LotNum:str = obj["LotNum"]
      self.EntryPerson:str = obj["EntryPerson"]
      self.BurUnitCost:int = obj["BurUnitCost"]
      self.ActionNum:int = obj["ActionNum"]
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      self.SubUnitCost:int = obj["SubUnitCost"]
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      self.NonConfID:int = obj["NonConfID"]
      self.TranReference:str = obj["TranReference"]
      self.WhseDesc:str = obj["WhseDesc"]
      self.BinDesc:str = obj["BinDesc"]
      self.ReasonDesc:str = obj["ReasonDesc"]
      self.UOM:str = obj["UOM"]
      self.PrimKeyStr:str = obj["PrimKeyStr"]
      """  Primary key of PartTran.  """  
      self.PCID:str = obj["PCID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DMRHistoryTableset:
   def __init__(self, obj):
      self.DMRHistory:list[Erp_Tablesets_DMRHistoryRow] = obj["DMRHistory"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DMRProcessingTableset:
   def __init__(self, obj):
      self.DMRHead:list[Erp_Tablesets_DMRHeadRow] = obj["DMRHead"]
      self.DMRHeadAttch:list[Erp_Tablesets_DMRHeadAttchRow] = obj["DMRHeadAttch"]
      self.DMRActn:list[Erp_Tablesets_DMRActnRow] = obj["DMRActn"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDMRProcessingTableset:
   def __init__(self, obj):
      self.DMRHead:list[Erp_Tablesets_DMRHeadRow] = obj["DMRHead"]
      self.DMRHeadAttch:list[Erp_Tablesets_DMRHeadAttchRow] = obj["DMRHeadAttch"]
      self.DMRActn:list[Erp_Tablesets_DMRActnRow] = obj["DMRActn"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   dmRNum
   """  
   def __init__(self, obj):
      self.dmRNum:int = obj["dmRNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DMRProcessingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRProcessingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRProcessingTableset] = obj["returnObj"]
      pass

class GetContactInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class GetContactInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDMRHistory_input:
   """ Required : 
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  DMR Number  """  
      pass

class GetDMRHistory_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DMRHistoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DMRHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDMRActnAcceptCUST_input:
   """ Required : 
   ds
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  The DMR Number being processed.  """  
      pass

class GetNewDMRActnAcceptCUST_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRActnAcceptMTL_input:
   """ Required : 
   ds
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  The DMR Number being processed.  """  
      pass

class GetNewDMRActnAcceptMTL_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRActnAcceptOPR_input:
   """ Required : 
   ds
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  The DMR Number being processed.  """  
      pass

class GetNewDMRActnAcceptOPR_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRActnAcceptSTK_input:
   """ Required : 
   ds
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  The DMR Number being processed.  """  
      pass

class GetNewDMRActnAcceptSTK_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRActnDebitMemo_input:
   """ Required : 
   ds
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  The DMR Number being processed.  """  
      pass

class GetNewDMRActnDebitMemo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRActnReject_input:
   """ Required : 
   ds
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  The DMR Number being processed.  """  
      pass

class GetNewDMRActnReject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRActn_input:
   """ Required : 
   ds
   dmRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.dmRNum:int = obj["dmRNum"]
      pass

class GetNewDMRActn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRHeadAttch_input:
   """ Required : 
   ds
   dmRNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.dmRNum:int = obj["dmRNum"]
      pass

class GetNewDMRHeadAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDMRHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class GetNewDMRHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPurPointInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class GetPurPointInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDMRHead
   whereClauseDMRHeadAttch
   whereClauseDMRActn
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDMRHead:str = obj["whereClauseDMRHead"]
      self.whereClauseDMRHeadAttch:str = obj["whereClauseDMRHeadAttch"]
      self.whereClauseDMRActn:str = obj["whereClauseDMRActn"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DMRProcessingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipQuantity
   ipDestinationType
   ipActionType
   ipSerialControlPlant
   ipSerialControlPlantIsFromPlt
   ipDMRNum
   ipJobNum
   ipPartTrackSerialNum
   ipActionNum
   ipQtyIUM
   ipPCID
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  DMRActn Part Number  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      """  The part's attribute set  """  
      self.ipQuantity:int = obj["ipQuantity"]
      """  Serial Number quantity required  """  
      self.ipDestinationType:str = obj["ipDestinationType"]
      """  DMR Action destination  """  
      self.ipActionType:str = obj["ipActionType"]
      """  DMR Action action type  """  
      self.ipSerialControlPlant:str = obj["ipSerialControlPlant"]
      """  Plant that is controlling serial entry rules  """  
      self.ipSerialControlPlantIsFromPlt:bool = obj["ipSerialControlPlantIsFromPlt"]
      """  Indicates if the from plant is the controllin plant for serial entry  """  
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  DMR Number  """  
      self.ipJobNum:str = obj["ipJobNum"]
      """  DMR Action Job Number  """  
      self.ipPartTrackSerialNum:bool = obj["ipPartTrackSerialNum"]
      """  Indicates if Serial Numbers required on this DMR Action  """  
      self.ipActionNum:int = obj["ipActionNum"]
      """  DMR Action Number  """  
      self.ipQtyIUM:str = obj["ipQtyIUM"]
      """  UOM for the DMR quantity  """  
      self.ipPCID:str = obj["ipPCID"]
      """  PCID  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetVendorInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class GetVendorInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
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

class OnChangePCID_input:
   """ Required : 
   pcid
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.pCallProcess:str = obj["pCallProcess"]
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class OnChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResolution_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class OnChangeResolution_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      self.serialTrackPartMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReasonCodeWhereClause_input:
   """ Required : 
   cAction
   iDMRNum
   """  
   def __init__(self, obj):
      self.cAction:str = obj["cAction"]
      """  The reason the where clause is being built.  Values are "REJ" for reject
            or "DM" for debit memo  """  
      self.iDMRNum:int = obj["iDMRNum"]
      """  The DMR number.  This is needed when cAction is "REJ".  For
           cAction = "DM" the value can be 0 (zero)  """  
      pass

class ReasonCodeWhereClause_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cReasonWhereClause:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateDebitMemoNum_input:
   """ Required : 
   iDMRNum
   iDMRAction
   """  
   def __init__(self, obj):
      self.iDMRNum:int = obj["iDMRNum"]
      """  Actual dmr num.  """  
      self.iDMRAction:int = obj["iDMRAction"]
      """  Actual dmr action.  """  
      pass

class UpdateDebitMemoNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DebitMemo:str = obj["parameters"]
      self.DebitMemoLine:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDMRProcessingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDMRProcessingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DMRProcessingTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

