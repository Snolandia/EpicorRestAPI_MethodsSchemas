import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BurdenSetSvc
# Description: The Burden Set BO used by Burden Set Maintenance.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BurdenSets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BurdenSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BurdenSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BdnSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets",headers=creds) as resp:
           return await resp.json()

async def post_BurdenSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BurdenSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BdnSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BdnSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BurdenSets_Company_BdnSetID(Company, BdnSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BurdenSet item
   Description: Calls GetByID to retrieve the BurdenSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BurdenSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BdnSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BurdenSets_Company_BdnSetID(Company, BdnSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BurdenSet for the service
   Description: Calls UpdateExt to update BurdenSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BurdenSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BdnSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BurdenSets_Company_BdnSetID(Company, BdnSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BurdenSet item
   Description: Call UpdateExt to delete BurdenSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BurdenSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BurdenSets_Company_BdnSetID_BSBdnCds(Company, BdnSetID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BSBdnCds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BSBdnCds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BSBdnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")/BSBdnCds",headers=creds) as resp:
           return await resp.json()

async def get_BurdenSets_Company_BdnSetID_BSBdnCds_Company_BdnSetID_BdnCd(Company, BdnSetID, BdnCd, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BSBdnCd item
   Description: Calls GetByID to retrieve the BSBdnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BSBdnCd1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BSBdnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_BurdenSets_Company_BdnSetID_BdnSetAttches(Company, BdnSetID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BdnSetAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BdnSetAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BdnSetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")/BdnSetAttches",headers=creds) as resp:
           return await resp.json()

async def get_BurdenSets_Company_BdnSetID_BdnSetAttches_Company_BdnSetID_DrawingSeq(Company, BdnSetID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BdnSetAttch item
   Description: Calls GetByID to retrieve the BdnSetAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BdnSetAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BdnSetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BurdenSets(" + Company + "," + BdnSetID + ")/BdnSetAttches(" + Company + "," + BdnSetID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BSBdnCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BSBdnCds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BSBdnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds",headers=creds) as resp:
           return await resp.json()

async def post_BSBdnCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BSBdnCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BSBdnCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BSBdnCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCds_Company_BdnSetID_BdnCd(Company, BdnSetID, BdnCd, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BSBdnCd item
   Description: Calls GetByID to retrieve the BSBdnCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BSBdnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BSBdnCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BSBdnCds_Company_BdnSetID_BdnCd(Company, BdnSetID, BdnCd, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BSBdnCd for the service
   Description: Calls UpdateExt to update BSBdnCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BSBdnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BSBdnCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BSBdnCds_Company_BdnSetID_BdnCd(Company, BdnSetID, BdnCd, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BSBdnCd item
   Description: Call UpdateExt to delete BSBdnCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BSBdnCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCds_Company_BdnSetID_BdnCd_BSBdnRts(Company, BdnSetID, BdnCd, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BSBdnRts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BSBdnRts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BSBdnRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")/BSBdnRts",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCds_Company_BdnSetID_BdnCd_BSBdnRts_Company_BdnSetID_BdnCd_EffDte(Company, BdnSetID, BdnCd, EffDte, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BSBdnRt item
   Description: Calls GetByID to retrieve the BSBdnRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BSBdnRt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param EffDte: Desc: EffDte   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BSBdnRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")/BSBdnRts(" + Company + "," + BdnSetID + "," + BdnCd + "," + EffDte + ")",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCds_Company_BdnSetID_BdnCd_BSBdnCdAttches(Company, BdnSetID, BdnCd, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BSBdnCdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BSBdnCdAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BSBdnCdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")/BSBdnCdAttches",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCds_Company_BdnSetID_BdnCd_BSBdnCdAttches_Company_BdnSetID_BdnCd_DrawingSeq(Company, BdnSetID, BdnCd, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BSBdnCdAttch item
   Description: Calls GetByID to retrieve the BSBdnCdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BSBdnCdAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BSBdnCdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCds(" + Company + "," + BdnSetID + "," + BdnCd + ")/BSBdnCdAttches(" + Company + "," + BdnSetID + "," + BdnCd + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnRts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BSBdnRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BSBdnRts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BSBdnRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnRts",headers=creds) as resp:
           return await resp.json()

async def post_BSBdnRts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BSBdnRts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BSBdnRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BSBdnRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnRts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BSBdnRts_Company_BdnSetID_BdnCd_EffDte(Company, BdnSetID, BdnCd, EffDte, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BSBdnRt item
   Description: Calls GetByID to retrieve the BSBdnRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BSBdnRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param EffDte: Desc: EffDte   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BSBdnRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnRts(" + Company + "," + BdnSetID + "," + BdnCd + "," + EffDte + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BSBdnRts_Company_BdnSetID_BdnCd_EffDte(Company, BdnSetID, BdnCd, EffDte, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BSBdnRt for the service
   Description: Calls UpdateExt to update BSBdnRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BSBdnRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param EffDte: Desc: EffDte   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BSBdnRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnRts(" + Company + "," + BdnSetID + "," + BdnCd + "," + EffDte + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BSBdnRts_Company_BdnSetID_BdnCd_EffDte(Company, BdnSetID, BdnCd, EffDte, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BSBdnRt item
   Description: Call UpdateExt to delete BSBdnRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BSBdnRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param EffDte: Desc: EffDte   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnRts(" + Company + "," + BdnSetID + "," + BdnCd + "," + EffDte + ")",headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCdAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BSBdnCdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BSBdnCdAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BSBdnCdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCdAttches",headers=creds) as resp:
           return await resp.json()

async def post_BSBdnCdAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BSBdnCdAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BSBdnCdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BSBdnCdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCdAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BSBdnCdAttches_Company_BdnSetID_BdnCd_DrawingSeq(Company, BdnSetID, BdnCd, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BSBdnCdAttch item
   Description: Calls GetByID to retrieve the BSBdnCdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BSBdnCdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BSBdnCdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCdAttches(" + Company + "," + BdnSetID + "," + BdnCd + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BSBdnCdAttches_Company_BdnSetID_BdnCd_DrawingSeq(Company, BdnSetID, BdnCd, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BSBdnCdAttch for the service
   Description: Calls UpdateExt to update BSBdnCdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BSBdnCdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BSBdnCdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCdAttches(" + Company + "," + BdnSetID + "," + BdnCd + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BSBdnCdAttches_Company_BdnSetID_BdnCd_DrawingSeq(Company, BdnSetID, BdnCd, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BSBdnCdAttch item
   Description: Call UpdateExt to delete BSBdnCdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BSBdnCdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param BdnCd: Desc: BdnCd   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BSBdnCdAttches(" + Company + "," + BdnSetID + "," + BdnCd + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BdnSetAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BdnSetAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BdnSetAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BdnSetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BdnSetAttches",headers=creds) as resp:
           return await resp.json()

async def post_BdnSetAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BdnSetAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BdnSetAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BdnSetAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BdnSetAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BdnSetAttches_Company_BdnSetID_DrawingSeq(Company, BdnSetID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BdnSetAttch item
   Description: Calls GetByID to retrieve the BdnSetAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BdnSetAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BdnSetAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BdnSetAttches(" + Company + "," + BdnSetID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BdnSetAttches_Company_BdnSetID_DrawingSeq(Company, BdnSetID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BdnSetAttch for the service
   Description: Calls UpdateExt to update BdnSetAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BdnSetAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BdnSetAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BdnSetAttches(" + Company + "," + BdnSetID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BdnSetAttches_Company_BdnSetID_DrawingSeq(Company, BdnSetID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BdnSetAttch item
   Description: Call UpdateExt to delete BdnSetAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BdnSetAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BdnSetID: Desc: BdnSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/BdnSetAttches(" + Company + "," + BdnSetID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BdnSetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBdnSet, whereClauseBdnSetAttch, whereClauseBSBdnCd, whereClauseBSBdnCdAttch, whereClauseBSBdnRt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseBdnSet=" + whereClauseBdnSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBdnSetAttch=" + whereClauseBdnSetAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBSBdnCd=" + whereClauseBSBdnCd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBSBdnCdAttch=" + whereClauseBSBdnCdAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBSBdnRt=" + whereClauseBSBdnRt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bdnSetID, epicorHeaders = None):
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
   params += "bdnSetID=" + bdnSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingInactive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingInactive
   Description: Performed when Inactive flag is changed.
   OperationID: OnChangingInactive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingInactive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingInactive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingBdnCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingBdnCd
   Description: Executed when Burden Code is changed.
   OperationID: OnChangingBdnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingBdnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingBdnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingEffDte(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingEffDte
   Description: Executed when Effective Date is changed.
   OperationID: OnChangingEffDte
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingEffDte_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEffDte_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBdnSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBdnSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBdnSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBdnSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBdnSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBdnSetAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBdnSetAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBdnSetAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBdnSetAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBdnSetAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBSBdnCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBSBdnCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBSBdnCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBSBdnCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBSBdnCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBSBdnCdAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBSBdnCdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBSBdnCdAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBSBdnCdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBSBdnCdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBSBdnRt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBSBdnRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBSBdnRt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBSBdnRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBSBdnRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BurdenSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BSBdnCdAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BSBdnCdAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BSBdnCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BSBdnCdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BSBdnRtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BSBdnRtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BdnSetAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BdnSetAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BdnSetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BdnSetListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BdnSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BdnSetRow] = obj["value"]
      pass

class Erp_Tablesets_BSBdnCdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BdnSetID:str = obj["BdnSetID"]
      self.BdnCd:str = obj["BdnCd"]
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

class Erp_Tablesets_BSBdnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.BdnCd:str = obj["BdnCd"]
      """  Burden Code.  """  
      self.ProcSeq:int = obj["ProcSeq"]
      """  The invoicing process will use this sequence to determine the sequence that the burden is calculated. When burdens are applied to other burden amounts then the sequence is important so that the correct values are very important for the correct calculations of burdens.  """  
      self.ApplyLbr:bool = obj["ApplyLbr"]
      """  If set to true this indicates the burden percentage is to be applied to the labor value.  """  
      self.ApplyMtl:bool = obj["ApplyMtl"]
      """  If set to true this indicates the burden percentage is to be applied to the material value.  """  
      self.ApplySubcon:bool = obj["ApplySubcon"]
      """  If set to true this indicates the burden percentage is to be applied to the subcontract value.  """  
      self.ApplyConLbr:bool = obj["ApplyConLbr"]
      """  If set to true this indicates the burden percentage is to be applied to the labor value booked by an employee that is flagged as a contract employee.  """  
      self.ApplyODC:bool = obj["ApplyODC"]
      """  If true the invoice process will calculate burden on costs that have been applied to the project from the AP Invoice Entry process.  """  
      self.ApplyFees:bool = obj["ApplyFees"]
      """  If true Fees can be applied to the burden amount calculated for this burden code.  """  
      self.BdnOnBdnList:str = obj["BdnOnBdnList"]
      """  A delimited list of the Burden Codes in this Burden Set whose calculated amount will be used in the calculation of the burden for the current burden code. If no other burden codes are selected then the burden for this burden code will be calculated as the Cost * the burden provisional percentage. If other burden codes are selected then the calculation will be the (Cost + the burden calculated for the selected burden codes) * prov pcnt.  """  
      self.ActBdnPcnt:int = obj["ActBdnPcnt"]
      """  This is the current actual burden percent.  """  
      self.ActEffDte:str = obj["ActEffDte"]
      """  This is the current effective date for the actual percentage.  """  
      self.GlobalBSBdnCd:bool = obj["GlobalBSBdnCd"]
      """  Marks this BSBdnCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BdnCdDescription:str = obj["BdnCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BSBdnRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.BdnCd:str = obj["BdnCd"]
      """  Burden Code.  """  
      self.EffDte:str = obj["EffDte"]
      """  The effective date of the burden code provisional percent.  """  
      self.ProvPcnt:int = obj["ProvPcnt"]
      """  The provisional percent for burden code for this burden set.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BdnSetAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BdnSetID:str = obj["BdnSetID"]
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

class Erp_Tablesets_BdnSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Burden Set.  """  
      self.InActive:bool = obj["InActive"]
      """  When set to true the burden set cannot be used.  """  
      self.GlobalBdnSet:bool = obj["GlobalBdnSet"]
      """  Marks this BdnSet as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BdnSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Burden Set.  """  
      self.InActive:bool = obj["InActive"]
      """  When set to true the burden set cannot be used.  """  
      self.GlobalBdnSet:bool = obj["GlobalBdnSet"]
      """  Marks this BdnSet as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   bdnSetID
   """  
   def __init__(self, obj):
      self.bdnSetID:str = obj["bdnSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BSBdnCdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BdnSetID:str = obj["BdnSetID"]
      self.BdnCd:str = obj["BdnCd"]
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

class Erp_Tablesets_BSBdnCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.BdnCd:str = obj["BdnCd"]
      """  Burden Code.  """  
      self.ProcSeq:int = obj["ProcSeq"]
      """  The invoicing process will use this sequence to determine the sequence that the burden is calculated. When burdens are applied to other burden amounts then the sequence is important so that the correct values are very important for the correct calculations of burdens.  """  
      self.ApplyLbr:bool = obj["ApplyLbr"]
      """  If set to true this indicates the burden percentage is to be applied to the labor value.  """  
      self.ApplyMtl:bool = obj["ApplyMtl"]
      """  If set to true this indicates the burden percentage is to be applied to the material value.  """  
      self.ApplySubcon:bool = obj["ApplySubcon"]
      """  If set to true this indicates the burden percentage is to be applied to the subcontract value.  """  
      self.ApplyConLbr:bool = obj["ApplyConLbr"]
      """  If set to true this indicates the burden percentage is to be applied to the labor value booked by an employee that is flagged as a contract employee.  """  
      self.ApplyODC:bool = obj["ApplyODC"]
      """  If true the invoice process will calculate burden on costs that have been applied to the project from the AP Invoice Entry process.  """  
      self.ApplyFees:bool = obj["ApplyFees"]
      """  If true Fees can be applied to the burden amount calculated for this burden code.  """  
      self.BdnOnBdnList:str = obj["BdnOnBdnList"]
      """  A delimited list of the Burden Codes in this Burden Set whose calculated amount will be used in the calculation of the burden for the current burden code. If no other burden codes are selected then the burden for this burden code will be calculated as the Cost * the burden provisional percentage. If other burden codes are selected then the calculation will be the (Cost + the burden calculated for the selected burden codes) * prov pcnt.  """  
      self.ActBdnPcnt:int = obj["ActBdnPcnt"]
      """  This is the current actual burden percent.  """  
      self.ActEffDte:str = obj["ActEffDte"]
      """  This is the current effective date for the actual percentage.  """  
      self.GlobalBSBdnCd:bool = obj["GlobalBSBdnCd"]
      """  Marks this BSBdnCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BdnCdDescription:str = obj["BdnCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BSBdnRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.BdnCd:str = obj["BdnCd"]
      """  Burden Code.  """  
      self.EffDte:str = obj["EffDte"]
      """  The effective date of the burden code provisional percent.  """  
      self.ProvPcnt:int = obj["ProvPcnt"]
      """  The provisional percent for burden code for this burden set.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BdnSetAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BdnSetID:str = obj["BdnSetID"]
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

class Erp_Tablesets_BdnSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Burden Set.  """  
      self.InActive:bool = obj["InActive"]
      """  When set to true the burden set cannot be used.  """  
      self.GlobalBdnSet:bool = obj["GlobalBdnSet"]
      """  Marks this BdnSet as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BdnSetListTableset:
   def __init__(self, obj):
      self.BdnSetList:list[Erp_Tablesets_BdnSetListRow] = obj["BdnSetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BdnSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BdnSetID:str = obj["BdnSetID"]
      """  Burden Set ID.  """  
      self.Description:str = obj["Description"]
      """  The description of the Burden Set.  """  
      self.InActive:bool = obj["InActive"]
      """  When set to true the burden set cannot be used.  """  
      self.GlobalBdnSet:bool = obj["GlobalBdnSet"]
      """  Marks this BdnSet as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DeleteAllowed:bool = obj["DeleteAllowed"]
      """  Flag that indicates if Delete is alllowed for this record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BurdenSetTableset:
   def __init__(self, obj):
      self.BdnSet:list[Erp_Tablesets_BdnSetRow] = obj["BdnSet"]
      self.BdnSetAttch:list[Erp_Tablesets_BdnSetAttchRow] = obj["BdnSetAttch"]
      self.BSBdnCd:list[Erp_Tablesets_BSBdnCdRow] = obj["BSBdnCd"]
      self.BSBdnCdAttch:list[Erp_Tablesets_BSBdnCdAttchRow] = obj["BSBdnCdAttch"]
      self.BSBdnRt:list[Erp_Tablesets_BSBdnRtRow] = obj["BSBdnRt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtBurdenSetTableset:
   def __init__(self, obj):
      self.BdnSet:list[Erp_Tablesets_BdnSetRow] = obj["BdnSet"]
      self.BdnSetAttch:list[Erp_Tablesets_BdnSetAttchRow] = obj["BdnSetAttch"]
      self.BSBdnCd:list[Erp_Tablesets_BSBdnCdRow] = obj["BSBdnCd"]
      self.BSBdnCdAttch:list[Erp_Tablesets_BSBdnCdAttchRow] = obj["BSBdnCdAttch"]
      self.BSBdnRt:list[Erp_Tablesets_BSBdnRtRow] = obj["BSBdnRt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   bdnSetID
   """  
   def __init__(self, obj):
      self.bdnSetID:str = obj["bdnSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BurdenSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BurdenSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BurdenSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BdnSetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBSBdnCdAttch_input:
   """ Required : 
   ds
   bdnSetID
   bdnCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      self.bdnSetID:str = obj["bdnSetID"]
      self.bdnCd:str = obj["bdnCd"]
      pass

class GetNewBSBdnCdAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBSBdnCd_input:
   """ Required : 
   ds
   bdnSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      self.bdnSetID:str = obj["bdnSetID"]
      pass

class GetNewBSBdnCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBSBdnRt_input:
   """ Required : 
   ds
   bdnSetID
   bdnCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      self.bdnSetID:str = obj["bdnSetID"]
      self.bdnCd:str = obj["bdnCd"]
      pass

class GetNewBSBdnRt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBdnSetAttch_input:
   """ Required : 
   ds
   bdnSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      self.bdnSetID:str = obj["bdnSetID"]
      pass

class GetNewBdnSetAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBdnSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

class GetNewBdnSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBdnSet
   whereClauseBdnSetAttch
   whereClauseBSBdnCd
   whereClauseBSBdnCdAttch
   whereClauseBSBdnRt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBdnSet:str = obj["whereClauseBdnSet"]
      self.whereClauseBdnSetAttch:str = obj["whereClauseBdnSetAttch"]
      self.whereClauseBSBdnCd:str = obj["whereClauseBSBdnCd"]
      self.whereClauseBSBdnCdAttch:str = obj["whereClauseBSBdnCdAttch"]
      self.whereClauseBSBdnRt:str = obj["whereClauseBSBdnRt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BurdenSetTableset] = obj["returnObj"]
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

class OnChangingBdnCd_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

class OnChangingBdnCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingEffDte_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

class OnChangingEffDte_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingInactive_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:bool = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

class OnChangingInactive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBurdenSetTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBurdenSetTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BurdenSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

