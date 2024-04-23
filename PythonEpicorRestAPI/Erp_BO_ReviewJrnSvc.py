import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReviewJrnSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ReviewJrns(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReviewJrns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReviewJrns
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns",headers=creds) as resp:
           return await resp.json()

async def post_ReviewJrns(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReviewJrns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RvJrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReviewJrns_Company_RvJrnUID(Company, RvJrnUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReviewJrn item
   Description: Calls GetByID to retrieve the ReviewJrn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReviewJrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReviewJrns_Company_RvJrnUID(Company, RvJrnUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReviewJrn for the service
   Description: Calls UpdateExt to update ReviewJrn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReviewJrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReviewJrns_Company_RvJrnUID(Company, RvJrnUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReviewJrn item
   Description: Call UpdateExt to delete ReviewJrn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReviewJrn
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ReviewJrns_Company_RvJrnUID_RvJrnTrs(Company, RvJrnUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RvJrnTrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")/RvJrnTrs",headers=creds) as resp:
           return await resp.json()

async def get_ReviewJrns_Company_RvJrnUID_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company, RvJrnUID, RvJrnTrUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTr item
   Description: Calls GetByID to retrieve the RvJrnTr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs",headers=creds) as resp:
           return await resp.json()

async def post_RvJrnTrs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company, RvJrnUID, RvJrnTrUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTr item
   Description: Calls GetByID to retrieve the RvJrnTr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company, RvJrnUID, RvJrnTrUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RvJrnTr for the service
   Description: Calls UpdateExt to update RvJrnTr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company, RvJrnUID, RvJrnTrUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RvJrnTr item
   Description: Call UpdateExt to delete RvJrnTr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtls(Company, RvJrnUID, RvJrnTrUID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RvJrnTrDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrDtls",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company, RvJrnUID, RvJrnTrUID, RvJrnTrDtlUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTrDtl item
   Description: Calls GetByID to retrieve the RvJrnTrDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param RvJrnTrDtlUID: Desc: RvJrnTrDtlUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrTreeLeaves(Company, RvJrnUID, RvJrnTrUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RvJrnTrTreeLeaves items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrTreeLeaves1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrTreeLeafRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrTreeLeaves",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrTreeLeaves_SysRowID(Company, RvJrnUID, RvJrnTrUID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTrTreeLeaf item
   Description: Calls GetByID to retrieve the RvJrnTrTreeLeaf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrTreeLeaf1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrTreeLeaves(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_WErrors(Company, RvJrnUID, RvJrnTrUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WErrors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WErrors1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/WErrors",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company, RvJrnUID, RvJrnTrUID, ErrorUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WError item
   Description: Calls GetByID to retrieve the WError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WError1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param ErrorUID: Desc: ErrorUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls",headers=creds) as resp:
           return await resp.json()

async def post_RvJrnTrDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company, RvJrnUID, RvJrnTrUID, RvJrnTrDtlUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTrDtl item
   Description: Calls GetByID to retrieve the RvJrnTrDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param RvJrnTrDtlUID: Desc: RvJrnTrDtlUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company, RvJrnUID, RvJrnTrUID, RvJrnTrDtlUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RvJrnTrDtl for the service
   Description: Calls UpdateExt to update RvJrnTrDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTrDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param RvJrnTrDtlUID: Desc: RvJrnTrDtlUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company, RvJrnUID, RvJrnTrUID, RvJrnTrDtlUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RvJrnTrDtl item
   Description: Call UpdateExt to delete RvJrnTrDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTrDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param RvJrnTrDtlUID: Desc: RvJrnTrDtlUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID_RvJrnTrDtlRefs(Company, RvJrnUID, RvJrnTrUID, RvJrnTrDtlUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RvJrnTrDtlRefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrDtlRefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param RvJrnTrDtlUID: Desc: RvJrnTrDtlUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")/RvJrnTrDtlRefs",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID_RvJrnTrDtlRefs_SysRowID(Company, RvJrnUID, RvJrnTrUID, RvJrnTrDtlUID, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTrDtlRef item
   Description: Calls GetByID to retrieve the RvJrnTrDtlRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtlRef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param RvJrnTrDtlUID: Desc: RvJrnTrDtlUID   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")/RvJrnTrDtlRefs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrDtlRefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrDtlRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrDtlRefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs",headers=creds) as resp:
           return await resp.json()

async def post_RvJrnTrDtlRefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrDtlRefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrDtlRefs_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTrDtlRef item
   Description: Calls GetByID to retrieve the RvJrnTrDtlRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtlRef
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RvJrnTrDtlRefs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RvJrnTrDtlRef for the service
   Description: Calls UpdateExt to update RvJrnTrDtlRef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTrDtlRef
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RvJrnTrDtlRefs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RvJrnTrDtlRef item
   Description: Call UpdateExt to delete RvJrnTrDtlRef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTrDtlRef
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrTreeLeaves(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrTreeLeaves items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrTreeLeaves
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrTreeLeafRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves",headers=creds) as resp:
           return await resp.json()

async def post_RvJrnTrTreeLeaves(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrTreeLeaves
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RvJrnTrTreeLeaves_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RvJrnTrTreeLeaf item
   Description: Calls GetByID to retrieve the RvJrnTrTreeLeaf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrTreeLeaf
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RvJrnTrTreeLeaves_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RvJrnTrTreeLeaf for the service
   Description: Calls UpdateExt to update RvJrnTrTreeLeaf. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTrTreeLeaf
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RvJrnTrTreeLeaves_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RvJrnTrTreeLeaf item
   Description: Call UpdateExt to delete RvJrnTrTreeLeaf item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTrTreeLeaf
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WErrors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WErrors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WErrors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors",headers=creds) as resp:
           return await resp.json()

async def post_WErrors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WErrors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WErrorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WErrorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company, RvJrnUID, RvJrnTrUID, ErrorUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WError item
   Description: Calls GetByID to retrieve the WError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WError
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param ErrorUID: Desc: ErrorUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WErrorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company, RvJrnUID, RvJrnTrUID, ErrorUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WError for the service
   Description: Calls UpdateExt to update WError. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WError
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param ErrorUID: Desc: ErrorUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WErrorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company, RvJrnUID, RvJrnTrUID, ErrorUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WError item
   Description: Call UpdateExt to delete WError item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WError
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RvJrnUID: Desc: RvJrnUID   Required: True
      :param RvJrnTrUID: Desc: RvJrnTrUID   Required: True
      :param ErrorUID: Desc: ErrorUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRvJrn, whereClauseRvJrnTr, whereClauseRvJrnTrDtl, whereClauseRvJrnTrDtlRef, whereClauseRvJrnTrTreeLeaf, whereClauseWError, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRvJrn=" + whereClauseRvJrn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRvJrnTr=" + whereClauseRvJrnTr
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRvJrnTrDtl=" + whereClauseRvJrnTrDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRvJrnTrDtlRef=" + whereClauseRvJrnTrDtlRef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRvJrnTrTreeLeaf=" + whereClauseRvJrnTrTreeLeaf
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWError=" + whereClauseWError
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rvJrnUID, epicorHeaders = None):
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
   params += "rvJrnUID=" + rvJrnUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetJournalHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournalHeader
   OperationID: GetJournalHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournalHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJournalTreeLeaf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournalTreeLeaf
   Description: This method populates RvJrnTrDtl datatable in reference ReviewJrnTableset dataset.
It depends on ipRvJrnTrUID, ipTreeLeafUID (Leef Node number) and Leef records limit (1000 by the default).
   OperationID: GetJournalTreeLeaf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournalTreeLeaf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalTreeLeaf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RestoreTmpJournalLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RestoreTmpJournalLine
   OperationID: RestoreTmpJournalLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RestoreTmpJournalLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreTmpJournalLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExcludeFromList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExcludeFromList
   Description: Exclude journals from the list with do not conform search criteria.
   OperationID: ExcludeFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExcludeFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExcludeFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRefTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetRefTypeList
   Description: Get list of reference types.
   OperationID: GetRefTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRefTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ProcessJournal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessJournal
   Description: Confirm or cancel journal entry.
   OperationID: ProcessJournal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLockRecords(epicorHeaders = None):
   """  
   Summary: Invoke method GetLockRecords
   Description: Populates Lock records list. Based on RvLock table (ABTUID = '').
   OperationID: GetLockRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLockRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeleteRvLockRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRvLockRecords
   Description: This method removed selected RvLock records with child related lockings from the database
   OperationID: DeleteRvLockRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRvLockRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRvLockRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TransValidate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TransValidate
   Description: Validate Transactions for current journal.
   OperationID: TransValidate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TransValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWithGroupCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWithGroupCheck
   Description: The extended method for retireving rows with additional filter by Group
   OperationID: GetRowsWithGroupCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWithGroupCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithGroupCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRvJrn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRvJrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRvJrn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRvJrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRvJrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRvJrnTr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRvJrnTr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRvJrnTr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRvJrnTr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRvJrnTr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRvJrnTrDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRvJrnTrDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRvJrnTrDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRvJrnTrDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRvJrnTrDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWError(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWError
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWError
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWError_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWError_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RvJrnListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RvJrnRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RvJrnTrDtlRefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RvJrnTrDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RvJrnTrRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrTreeLeafRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RvJrnTrTreeLeafRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WErrorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WErrorRow] = obj["value"]
      pass

class Erp_Tablesets_RvJrnListRow:
   def __init__(self, obj):
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.JeDate:str = obj["JeDate"]
      """  Journal Entry Date  """  
      self.IsValid:bool = obj["IsValid"]
      """  True if transaction is valid.  """  
      self.PostingMode:str = obj["PostingMode"]
      """  Posting Mode.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.UserUID:str = obj["UserUID"]
      """  User unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.RvDate:str = obj["RvDate"]
      """  Review date  """  
      self.Simulation:bool = obj["Simulation"]
      """  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasErr:bool = obj["HasErr"]
      """  Error flag.  """  
      self.IsLcked:int = obj["IsLcked"]
      """   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Text value of IsLcked field  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnRow:
   def __init__(self, obj):
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.JeDate:str = obj["JeDate"]
      """  Journal Entry Date  """  
      self.IsValid:bool = obj["IsValid"]
      """  True if transaction is valid.  """  
      self.PostingMode:str = obj["PostingMode"]
      """  Posting Mode.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.UserUID:str = obj["UserUID"]
      """  User unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.RvDate:str = obj["RvDate"]
      """  Review date  """  
      self.Simulation:bool = obj["Simulation"]
      """  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasErr:bool = obj["HasErr"]
      """  Error flag.  """  
      self.IsLcked:int = obj["IsLcked"]
      """   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Text value of IsLcked field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrDtlRefRow:
   def __init__(self, obj):
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Reference to RvJrn.  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Reference to RvJrnTr.  """  
      self.RvJrnTrDtlUID:int = obj["RvJrnTrDtlUID"]
      """  Reference to RvJrnTrDtl.  """  
      self.RefCode:str = obj["RefCode"]
      """  Reference code.  """  
      self.RefUID:int = obj["RefUID"]
      """  Reference UID.  """  
      self.RefValue:str = obj["RefValue"]
      """  Reference value.  """  
      self.IsSummarize:bool = obj["IsSummarize"]
      """  Line can be summarized.  """  
      self.Company:str = obj["Company"]
      self.ParentLine:int = obj["ParentLine"]
      """  ParentLine  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrDtlRow:
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
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  Ext Segment Value 2  """  
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
      self.SkipBalances:bool = obj["SkipBalances"]
      """  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  """  
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
      """  Internal system calcualted sequence number not inteneded for external use.  """  
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
      """   P = derived from Period Balance records via Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations  """  
      self.RvJrnTrDtlUID:int = obj["RvJrnTrDtlUID"]
      """  Review Journal Transaction Detail unique ID.  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Review Journal Transaction Table unique ID.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.BRuleUID:int = obj["BRuleUID"]
      """  Technical identifier.  """  
      self.IsSummarize:bool = obj["IsSummarize"]
      """  True if transaction is summarized.  """  
      self.RefUID:int = obj["RefUID"]
      """  Reference unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.TranSeq:int = obj["TranSeq"]
      """  Tran Seq  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  Book Credit Amount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.ParentLine:int = obj["ParentLine"]
      """  ParentLine  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp to affect this GLJrnDtl.  """  
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
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  External GL Account, from Main COA of External Company (GLBGLAccount)  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA, should be MAin COA from External Company (GLBCOA)  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  """  
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
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.DebitCreditLine:str = obj["DebitCreditLine"]
      self.IsDebitAmount:bool = obj["IsDebitAmount"]
      """  Debit Amount flag.  """  
      self.LineAmount:int = obj["LineAmount"]
      """  Line Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Show Yes if it is Red Storno transaction  """  
      self.StatAmount:int = obj["StatAmount"]
      """  Statistical Amount. UI display value.  """  
      self.TreeLeafUID:int = obj["TreeLeafUID"]
      """  TreeLeafUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.GLGLAcctDisp:str = obj["GLGLAcctDisp"]
      self.GLGLShortAcct:str = obj["GLGLShortAcct"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.LinkToBookingRuleDisplayName:str = obj["LinkToBookingRuleDisplayName"]
      self.RvTranGLCGLAcctContext:str = obj["RvTranGLCGLAcctContext"]
      self.RvTranGLCKey6:str = obj["RvTranGLCKey6"]
      self.RvTranGLCKey5:str = obj["RvTranGLCKey5"]
      self.RvTranGLCKey3:str = obj["RvTranGLCKey3"]
      self.RvTranGLCRelatedToFile:str = obj["RvTranGLCRelatedToFile"]
      self.RvTranGLCKey2:str = obj["RvTranGLCKey2"]
      self.RvTranGLCKey1:str = obj["RvTranGLCKey1"]
      self.RvTranGLCKey4:str = obj["RvTranGLCKey4"]
      self.RvTranGLCSysGLControlType:str = obj["RvTranGLCSysGLControlType"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrRow:
   def __init__(self, obj):
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Review Journal Transaction Table unique ID.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.IsValid:bool = obj["IsValid"]
      """  True if transaction is valid.  """  
      self.IsReverse:bool = obj["IsReverse"]
      """  True if transaction is reverse.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction number.  """  
      self.LegalNum:int = obj["LegalNum"]
      """  Legal number.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.UserUID:str = obj["UserUID"]
      """  User unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.COACode:str = obj["COACode"]
      """  Code of Chart of Account  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  Book Credit Amount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Account transaction revision UID. Technical identifier.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Account transaction type UID. Technical identifier. Reference to an account transaction type.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID,guid  """  
      self.Simulation:bool = obj["Simulation"]
      """  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows the Total Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows the Total Credit statistical amount.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasErr:bool = obj["HasErr"]
      """  Error flag.  """  
      self.MarkBook:bool = obj["MarkBook"]
      """  Flag to show book using special font.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Balance Amount.  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.ActRevisionRevisionCode:str = obj["ActRevisionRevisionCode"]
      self.ActTypeDisplayName:str = obj["ActTypeDisplayName"]
      self.BookCurrencyCode_:str = obj["BookCurrencyCode_"]
      self.BookDescription:str = obj["BookDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrTreeLeafRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  RvJrnTrUID  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  RvJrnUID  """  
      self.TreeLeafUID:int = obj["TreeLeafUID"]
      """  TreeLeafUID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WErrorRow:
   def __init__(self, obj):
      self.ErrorUID:int = obj["ErrorUID"]
      """  Error unique ID.  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Review Journal Transaction Table unique ID.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.IsError:bool = obj["IsError"]
      """  True if record represents error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Persistent:bool = obj["Persistent"]
      """  1 - Warning/Error was added during creation of transaction line. Cannot be revalidated in Review Journal. 0 - Warning/Error can be revalidated in Review Journal.  """  
      self.ErrKind:str = obj["ErrKind"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   rvJrnUID
   """  
   def __init__(self, obj):
      self.rvJrnUID:int = obj["rvJrnUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteRvLockRecords_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RvLockTableset] = obj["ds"]
      pass

class DeleteRvLockRecords_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RvLockTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ReviewJrnTableset:
   def __init__(self, obj):
      self.RvJrn:list[Erp_Tablesets_RvJrnRow] = obj["RvJrn"]
      self.RvJrnTr:list[Erp_Tablesets_RvJrnTrRow] = obj["RvJrnTr"]
      self.RvJrnTrDtl:list[Erp_Tablesets_RvJrnTrDtlRow] = obj["RvJrnTrDtl"]
      self.RvJrnTrDtlRef:list[Erp_Tablesets_RvJrnTrDtlRefRow] = obj["RvJrnTrDtlRef"]
      self.RvJrnTrTreeLeaf:list[Erp_Tablesets_RvJrnTrTreeLeafRow] = obj["RvJrnTrTreeLeaf"]
      self.WError:list[Erp_Tablesets_WErrorRow] = obj["WError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RvJrnListRow:
   def __init__(self, obj):
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.JeDate:str = obj["JeDate"]
      """  Journal Entry Date  """  
      self.IsValid:bool = obj["IsValid"]
      """  True if transaction is valid.  """  
      self.PostingMode:str = obj["PostingMode"]
      """  Posting Mode.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.UserUID:str = obj["UserUID"]
      """  User unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.RvDate:str = obj["RvDate"]
      """  Review date  """  
      self.Simulation:bool = obj["Simulation"]
      """  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasErr:bool = obj["HasErr"]
      """  Error flag.  """  
      self.IsLcked:int = obj["IsLcked"]
      """   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Text value of IsLcked field  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnListTableset:
   def __init__(self, obj):
      self.RvJrnList:list[Erp_Tablesets_RvJrnListRow] = obj["RvJrnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RvJrnRow:
   def __init__(self, obj):
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.JeDate:str = obj["JeDate"]
      """  Journal Entry Date  """  
      self.IsValid:bool = obj["IsValid"]
      """  True if transaction is valid.  """  
      self.PostingMode:str = obj["PostingMode"]
      """  Posting Mode.  """  
      self.SourceModule:str = obj["SourceModule"]
      """   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  """  
      self.UserUID:str = obj["UserUID"]
      """  User unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.RvDate:str = obj["RvDate"]
      """  Review date  """  
      self.Simulation:bool = obj["Simulation"]
      """  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasErr:bool = obj["HasErr"]
      """  Error flag.  """  
      self.IsLcked:int = obj["IsLcked"]
      """   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Text value of IsLcked field  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrDtlRefRow:
   def __init__(self, obj):
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Reference to RvJrn.  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Reference to RvJrnTr.  """  
      self.RvJrnTrDtlUID:int = obj["RvJrnTrDtlUID"]
      """  Reference to RvJrnTrDtl.  """  
      self.RefCode:str = obj["RefCode"]
      """  Reference code.  """  
      self.RefUID:int = obj["RefUID"]
      """  Reference UID.  """  
      self.RefValue:str = obj["RefValue"]
      """  Reference value.  """  
      self.IsSummarize:bool = obj["IsSummarize"]
      """  Line can be summarized.  """  
      self.Company:str = obj["Company"]
      self.ParentLine:int = obj["ParentLine"]
      """  ParentLine  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrDtlRow:
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
      self.ExtSegValue1:str = obj["ExtSegValue1"]
      """  External Segment Value 1  """  
      self.ExtSegValue2:str = obj["ExtSegValue2"]
      """  Ext Segment Value 2  """  
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
      self.SkipBalances:bool = obj["SkipBalances"]
      """  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  """  
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
      """  Internal system calcualted sequence number not inteneded for external use.  """  
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
      """   P = derived from Period Balance records via Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations  """  
      self.RvJrnTrDtlUID:int = obj["RvJrnTrDtlUID"]
      """  Review Journal Transaction Detail unique ID.  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Review Journal Transaction Table unique ID.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.BRuleUID:int = obj["BRuleUID"]
      """  Technical identifier.  """  
      self.IsSummarize:bool = obj["IsSummarize"]
      """  True if transaction is summarized.  """  
      self.RefUID:int = obj["RefUID"]
      """  Reference unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.CloseFiscalPeriod:int = obj["CloseFiscalPeriod"]
      """  CloseFiscalPeriod  """  
      self.TranSeq:int = obj["TranSeq"]
      """  Tran Seq  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  Book Credit Amount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.ParentLine:int = obj["ParentLine"]
      """  ParentLine  """  
      self.ParentRUID:str = obj["ParentRUID"]
      """  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  """  
      self.HasReverseLine:bool = obj["HasReverseLine"]
      """  if has reverse line  """  
      self.AllocationStamp:str = obj["AllocationStamp"]
      """  This is the last allocation stamp to affect this GLJrnDtl.  """  
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
      self.ExtGLAccount:str = obj["ExtGLAccount"]
      """  External GL Account, from Main COA of External Company (GLBGLAccount)  """  
      self.ExtCOACode:str = obj["ExtCOACode"]
      """  External COA, should be MAin COA from External Company (GLBCOA)  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  """  
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
      self.CustNum:int = obj["CustNum"]
      """  The Internal CustNum that ties back to the Customer master file.  """  
      self.SourcePlant:str = obj["SourcePlant"]
      """  SourcePlant  """  
      self.ExtSysType:str = obj["ExtSysType"]
      """  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  """  
      self.ExtSysURL:str = obj["ExtSysURL"]
      """  URL for drill back to an integrated external system  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.DebitCreditLine:str = obj["DebitCreditLine"]
      self.IsDebitAmount:bool = obj["IsDebitAmount"]
      """  Debit Amount flag.  """  
      self.LineAmount:int = obj["LineAmount"]
      """  Line Amount.  """  
      self.RedStorno:bool = obj["RedStorno"]
      """  Show Yes if it is Red Storno transaction  """  
      self.StatAmount:int = obj["StatAmount"]
      """  Statistical Amount. UI display value.  """  
      self.TreeLeafUID:int = obj["TreeLeafUID"]
      """  TreeLeafUID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.GLAccountDesc:str = obj["GLAccountDesc"]
      self.GLGLAcctDisp:str = obj["GLGLAcctDisp"]
      self.GLGLShortAcct:str = obj["GLGLShortAcct"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.LinkToBookingRuleDisplayName:str = obj["LinkToBookingRuleDisplayName"]
      self.RvTranGLCGLAcctContext:str = obj["RvTranGLCGLAcctContext"]
      self.RvTranGLCKey6:str = obj["RvTranGLCKey6"]
      self.RvTranGLCKey5:str = obj["RvTranGLCKey5"]
      self.RvTranGLCKey3:str = obj["RvTranGLCKey3"]
      self.RvTranGLCRelatedToFile:str = obj["RvTranGLCRelatedToFile"]
      self.RvTranGLCKey2:str = obj["RvTranGLCKey2"]
      self.RvTranGLCKey1:str = obj["RvTranGLCKey1"]
      self.RvTranGLCKey4:str = obj["RvTranGLCKey4"]
      self.RvTranGLCSysGLControlType:str = obj["RvTranGLCSysGLControlType"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrRow:
   def __init__(self, obj):
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Review Journal Transaction Table unique ID.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.BookID:str = obj["BookID"]
      """  BookID  """  
      self.IsValid:bool = obj["IsValid"]
      """  True if transaction is valid.  """  
      self.IsReverse:bool = obj["IsReverse"]
      """  True if transaction is reverse.  """  
      self.TranNum:int = obj["TranNum"]
      """  Transaction number.  """  
      self.LegalNum:int = obj["LegalNum"]
      """  Legal number.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  """  
      self.UserUID:str = obj["UserUID"]
      """  User unique ID.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  Change date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year that entry applies to.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period that this journal entry applies to.  """  
      self.COACode:str = obj["COACode"]
      """  Code of Chart of Account  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  Book Credit Amount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.JEDate:str = obj["JEDate"]
      """  Date for this journal transaction entry.  """  
      self.PostedDate:str = obj["PostedDate"]
      """  Date that this transaction was posted to the G/L files.  """  
      self.ACTRevisionUID:int = obj["ACTRevisionUID"]
      """  Account transaction revision UID. Technical identifier.  """  
      self.ACTTypeUID:int = obj["ACTTypeUID"]
      """  Account transaction type UID. Technical identifier. Reference to an account transaction type.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  ABTUID,guid  """  
      self.Simulation:bool = obj["Simulation"]
      """  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows the Total Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows the Total Credit statistical amount.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasErr:bool = obj["HasErr"]
      """  Error flag.  """  
      self.MarkBook:bool = obj["MarkBook"]
      """  Flag to show book using special font.  """  
      self.BalanceAmount:int = obj["BalanceAmount"]
      """  Balance Amount.  """  
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.ActRevisionRevisionCode:str = obj["ActRevisionRevisionCode"]
      self.ActTypeDisplayName:str = obj["ActTypeDisplayName"]
      self.BookCurrencyCode_:str = obj["BookCurrencyCode_"]
      self.BookDescription:str = obj["BookDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.StatUOMStatUOMDesc:str = obj["StatUOMStatUOMDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvJrnTrTreeLeafRow:
   def __init__(self, obj):
      self.BookID:str = obj["BookID"]
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  RvJrnTrUID  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  RvJrnUID  """  
      self.TreeLeafUID:int = obj["TreeLeafUID"]
      """  TreeLeafUID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvLockRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  Identifies the master file to which the record is related to.  """  
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
      self.LockDate:str = obj["LockDate"]
      """  Date when document has been locked  """  
      self.LockTime:int = obj["LockTime"]
      """  Time when document has been locked  """  
      self.LockedBy:str = obj["LockedBy"]
      """  User ID that locked this document.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Reference to Review Journal UID.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Show Status of locked document. Can be "Posting" - if the document has been sent to Posting, "Reviewing" - if the document has not been posted and transaction left in review Journal.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to ABT, that is used in posting  """  
      self.GlbABTUID:str = obj["GlbABTUID"]
      """  GlbABTUID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.ReleaseRvLockFlag:bool = obj["ReleaseRvLockFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RvLockTableset:
   def __init__(self, obj):
      self.RvLock:list[Erp_Tablesets_RvLockRow] = obj["RvLock"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtReviewJrnTableset:
   def __init__(self, obj):
      self.RvJrn:list[Erp_Tablesets_RvJrnRow] = obj["RvJrn"]
      self.RvJrnTr:list[Erp_Tablesets_RvJrnTrRow] = obj["RvJrnTr"]
      self.RvJrnTrDtl:list[Erp_Tablesets_RvJrnTrDtlRow] = obj["RvJrnTrDtl"]
      self.RvJrnTrDtlRef:list[Erp_Tablesets_RvJrnTrDtlRefRow] = obj["RvJrnTrDtlRef"]
      self.RvJrnTrTreeLeaf:list[Erp_Tablesets_RvJrnTrTreeLeafRow] = obj["RvJrnTrTreeLeaf"]
      self.WError:list[Erp_Tablesets_WErrorRow] = obj["WError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WErrorRow:
   def __init__(self, obj):
      self.ErrorUID:int = obj["ErrorUID"]
      """  Error unique ID.  """  
      self.RvJrnTrUID:int = obj["RvJrnTrUID"]
      """  Review Journal Transaction Table unique ID.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.IsError:bool = obj["IsError"]
      """  True if record represents error.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal unique ID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Persistent:bool = obj["Persistent"]
      """  1 - Warning/Error was added during creation of transaction line. Cannot be revalidated in Review Journal. 0 - Warning/Error can be revalidated in Review Journal.  """  
      self.ErrKind:str = obj["ErrKind"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class ExcludeFromList_input:
   """ Required : 
   intRvJrnUID
   intACTTypeUID
   strGroupID
   """  
   def __init__(self, obj):
      self.intRvJrnUID:int = obj["intRvJrnUID"]
      """  Journal number  """  
      self.intACTTypeUID:int = obj["intACTTypeUID"]
      """  Search criteria for RvJrnTr table  """  
      self.strGroupID:str = obj["strGroupID"]
      """  Search criteria for RvJrnTrDtl table  """  
      pass

class ExcludeFromList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lExclude:bool = obj["lExclude"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   rvJrnUID
   """  
   def __init__(self, obj):
      self.rvJrnUID:int = obj["rvJrnUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReviewJrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReviewJrnTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ReviewJrnTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   systemCode
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  systemCode  """  
      self.tableName:str = obj["tableName"]
      """  tableName  """  
      self.fieldName:str = obj["fieldName"]
      """  fieldName  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetJournalHeader_input:
   """ Required : 
   ipRvJrnUID
   ipRecLimitPerTr
   ds
   """  
   def __init__(self, obj):
      self.ipRvJrnUID:int = obj["ipRvJrnUID"]
      """  RvJrnUID  """  
      self.ipRecLimitPerTr:int = obj["ipRecLimitPerTr"]
      """  RecLimitPerTr  """  
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

class GetJournalHeader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetJournalTreeLeaf_input:
   """ Required : 
   ipRvJrnUID
   ipRvJrnTrUID
   ipBookID
   ipTreeLeafUID
   ipRecLimitPerTr
   ds
   """  
   def __init__(self, obj):
      self.ipRvJrnUID:int = obj["ipRvJrnUID"]
      """  RvJrnUID  """  
      self.ipRvJrnTrUID:int = obj["ipRvJrnTrUID"]
      """  RvJrnTrUID  """  
      self.ipBookID:str = obj["ipBookID"]
      """  BookID  """  
      self.ipTreeLeafUID:int = obj["ipTreeLeafUID"]
      """  TreeLeafUID  """  
      self.ipRecLimitPerTr:int = obj["ipRecLimitPerTr"]
      """  RecLimitPerTr  """  
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

class GetJournalTreeLeaf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_RvJrnListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetLockRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RvLockTableset] = obj["returnObj"]
      pass

class GetNewRvJrnTrDtl_input:
   """ Required : 
   ds
   rvJrnUID
   rvJrnTrUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      self.rvJrnUID:int = obj["rvJrnUID"]
      self.rvJrnTrUID:int = obj["rvJrnTrUID"]
      pass

class GetNewRvJrnTrDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRvJrnTr_input:
   """ Required : 
   ds
   rvJrnUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      self.rvJrnUID:int = obj["rvJrnUID"]
      pass

class GetNewRvJrnTr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRvJrn_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

class GetNewRvJrn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWError_input:
   """ Required : 
   ds
   rvJrnUID
   rvJrnTrUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      self.rvJrnUID:int = obj["rvJrnUID"]
      self.rvJrnTrUID:int = obj["rvJrnTrUID"]
      pass

class GetNewWError_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRefTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.strList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsWithGroupCheck_input:
   """ Required : 
   whereClauseRvJrn
   whereClauseRvJrnTr
   whereClauseRvJrnTrDtl
   whereClauseRvJrnTrDtlRef
   whereClauseRvJrnTrTreeLeaf
   whereClauseWError
   groupID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRvJrn:str = obj["whereClauseRvJrn"]
      self.whereClauseRvJrnTr:str = obj["whereClauseRvJrnTr"]
      self.whereClauseRvJrnTrDtl:str = obj["whereClauseRvJrnTrDtl"]
      self.whereClauseRvJrnTrDtlRef:str = obj["whereClauseRvJrnTrDtlRef"]
      self.whereClauseRvJrnTrTreeLeaf:str = obj["whereClauseRvJrnTrTreeLeaf"]
      self.whereClauseWError:str = obj["whereClauseWError"]
      self.groupID:str = obj["groupID"]
      """  The group ID  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWithGroupCheck_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReviewJrnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRvJrn
   whereClauseRvJrnTr
   whereClauseRvJrnTrDtl
   whereClauseRvJrnTrDtlRef
   whereClauseRvJrnTrTreeLeaf
   whereClauseWError
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRvJrn:str = obj["whereClauseRvJrn"]
      self.whereClauseRvJrnTr:str = obj["whereClauseRvJrnTr"]
      self.whereClauseRvJrnTrDtl:str = obj["whereClauseRvJrnTrDtl"]
      self.whereClauseRvJrnTrDtlRef:str = obj["whereClauseRvJrnTrDtlRef"]
      self.whereClauseRvJrnTrTreeLeaf:str = obj["whereClauseRvJrnTrTreeLeaf"]
      self.whereClauseWError:str = obj["whereClauseWError"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReviewJrnTableset] = obj["returnObj"]
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

class ProcessJournal_input:
   """ Required : 
   bConfirm
   inrvJrnUID
   """  
   def __init__(self, obj):
      self.bConfirm:bool = obj["bConfirm"]
      """  True if confirm  """  
      self.inrvJrnUID:int = obj["inrvJrnUID"]
      """  journal number  """  
      pass

class ProcessJournal_output:
   def __init__(self, obj):
      pass

class RestoreTmpJournalLine_input:
   """ Required : 
   ipRvJrnUID
   ipRvJrnTrUID
   ipBookID
   ipTreeLeafUID
   ds
   """  
   def __init__(self, obj):
      self.ipRvJrnUID:int = obj["ipRvJrnUID"]
      """  RvJrnUID  """  
      self.ipRvJrnTrUID:int = obj["ipRvJrnTrUID"]
      """  RvJrnTrUID  """  
      self.ipBookID:str = obj["ipBookID"]
      """  BookID  """  
      self.ipTreeLeafUID:int = obj["ipTreeLeafUID"]
      """  TreeLeafUID  """  
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

class RestoreTmpJournalLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TransValidate_input:
   """ Required : 
   rvJrnUID
   """  
   def __init__(self, obj):
      self.rvJrnUID:int = obj["rvJrnUID"]
      """  journal number  """  
      pass

class TransValidate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isValid:bool = obj["isValid"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReviewJrnTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtReviewJrnTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReviewJrnTableset] = obj["ds"]
      pass

      """  output parameters  """  

