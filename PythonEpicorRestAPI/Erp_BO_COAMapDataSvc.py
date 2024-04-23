import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.COAMapDataSvc
# Description: Object to manage COA map data: COAMap, AccStrLink, SegmentLink
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_COAMapDatas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get COAMapDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_COAMapDatas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas",headers=creds) as resp:
           return await resp.json()

async def post_COAMapDatas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_COAMapDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.COAMapRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.COAMapRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_COAMapDatas_Company_COAMapUID(Company, COAMapUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the COAMapData item
   Description: Calls GetByID to retrieve the COAMapData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_COAMapData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.COAMapRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_COAMapDatas_Company_COAMapUID(Company, COAMapUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update COAMapData for the service
   Description: Calls UpdateExt to update COAMapData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_COAMapData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.COAMapRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_COAMapDatas_Company_COAMapUID(Company, COAMapUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete COAMapData item
   Description: Call UpdateExt to delete COAMapData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_COAMapData
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_COAMapDatas_Company_COAMapUID_GLAccLinks(Company, COAMapUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GLAccLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLAccLinks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/GLAccLinks",headers=creds) as resp:
           return await resp.json()

async def get_COAMapDatas_Company_COAMapUID_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company, COAMapUID, GLAccLinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAccLink item
   Description: Calls GetByID to retrieve the GLAccLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccLink1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param GLAccLinkUID: Desc: GLAccLinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_COAMapDatas_Company_COAMapUID_SegmentLinks(Company, COAMapUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SegmentLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SegmentLinks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegmentLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/SegmentLinks",headers=creds) as resp:
           return await resp.json()

async def get_COAMapDatas_Company_COAMapUID_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company, COAMapUID, SegmentLinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SegmentLink item
   Description: Calls GetByID to retrieve the SegmentLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegmentLink1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param SegmentLinkUID: Desc: SegmentLinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/COAMapDatas(" + Company + "," + COAMapUID + ")/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GLAccLinks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLAccLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLAccLinks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLAccLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks",headers=creds) as resp:
           return await resp.json()

async def post_GLAccLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLAccLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company, COAMapUID, GLAccLinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLAccLink item
   Description: Calls GetByID to retrieve the GLAccLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLAccLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param GLAccLinkUID: Desc: GLAccLinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company, COAMapUID, GLAccLinkUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLAccLink for the service
   Description: Calls UpdateExt to update GLAccLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLAccLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param GLAccLinkUID: Desc: GLAccLinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLAccLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLAccLinks_Company_COAMapUID_GLAccLinkUID(Company, COAMapUID, GLAccLinkUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLAccLink item
   Description: Call UpdateExt to delete GLAccLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLAccLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param GLAccLinkUID: Desc: GLAccLinkUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/GLAccLinks(" + Company + "," + COAMapUID + "," + GLAccLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SegmentLinks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SegmentLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SegmentLinks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SegmentLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks",headers=creds) as resp:
           return await resp.json()

async def post_SegmentLinks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SegmentLinks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company, COAMapUID, SegmentLinkUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SegmentLink item
   Description: Calls GetByID to retrieve the SegmentLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SegmentLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param SegmentLinkUID: Desc: SegmentLinkUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company, COAMapUID, SegmentLinkUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SegmentLink for the service
   Description: Calls UpdateExt to update SegmentLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SegmentLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param SegmentLinkUID: Desc: SegmentLinkUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SegmentLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SegmentLinks_Company_COAMapUID_SegmentLinkUID(Company, COAMapUID, SegmentLinkUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SegmentLink item
   Description: Call UpdateExt to delete SegmentLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SegmentLink
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param COAMapUID: Desc: COAMapUID   Required: True
      :param SegmentLinkUID: Desc: SegmentLinkUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/SegmentLinks(" + Company + "," + COAMapUID + "," + SegmentLinkUID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.COAMapListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCOAMap, whereClauseGLAccLink, whereClauseSegmentLink, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCOAMap=" + whereClauseCOAMap
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGLAccLink=" + whereClauseGLAccLink
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSegmentLink=" + whereClauseSegmentLink
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(coAMapUID, epicorHeaders = None):
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
   params += "coAMapUID=" + coAMapUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByDisplayName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByDisplayName
   Description: This method returns COAMapData dataset if display name is known
   OperationID: GetByDisplayName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByDisplayName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByDisplayName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCOA
   Description: This method called when value of Source/Target COA were changed.
   OperationID: OnChangeCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Populate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Populate
   Description: Populates dataset
   OperationID: Populate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Populate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Populate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTargetCOA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTargetCOA
   Description: Validate target coa against correct table
   OperationID: ValidateTargetCOA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTargetCOA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTargetCOA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTargetCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTargetCompany
   Description: Validate target coa against correct table
   OperationID: ValidateTargetCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTargetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTargetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSegmentLink_WithSegmentsFilled(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSegmentLink_WithSegmentsFilled
   Description: Get New Segment Link with Source/Target segment columns filled.
   OperationID: GetNewSegmentLink_WithSegmentsFilled
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSegmentLink_WithSegmentsFilled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegmentLink_WithSegmentsFilled_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMapTypeDescList(epicorHeaders = None):
   """  
   Summary: Invoke method GetMapTypeDescList
   OperationID: GetMapTypeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMapTypeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckCOAGlobalStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOAGlobalStatus
   Description: Returns true if COA is global and false otherwise.
   OperationID: CheckCOAGlobalStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOAGlobalStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOAGlobalStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCOAMap(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCOAMap
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCOAMap
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCOAMap_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCOAMap_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLAccLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLAccLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLAccLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLAccLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLAccLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSegmentLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSegmentLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSegmentLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSegmentLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSegmentLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.COAMapDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COAMapListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_COAMapRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_COAMapRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLAccLinkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLAccLinkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SegmentLinkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SegmentLinkRow] = obj["value"]
      pass

class Erp_Tablesets_COAMapListRow:
   def __init__(self, obj):
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed Description  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  type of COA for company  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  type of COA for company  """  
      self.MapType:int = obj["MapType"]
      """  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOASegmentTransform:bool = obj["GlobalCOASegmentTransform"]
      """  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  """  
      self.SourceCOADescription:str = obj["SourceCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TargetGLBCOADescription:str = obj["TargetGLBCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COAMapRow:
   def __init__(self, obj):
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed Description  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  type of COA for company  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  type of COA for company  """  
      self.MapType:int = obj["MapType"]
      """  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOASegmentTransform:bool = obj["GlobalCOASegmentTransform"]
      """  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company for Global Transform only.  """  
      self.TargetSegment:int = obj["TargetSegment"]
      """  Target Segment - combobox filter.  """  
      self.SourceSegment:int = obj["SourceSegment"]
      """  Target Segment - combobox filter.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourceCOADescription:str = obj["SourceCOADescription"]
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      self.TargetGLBCOADescription:str = obj["TargetGLBCOADescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccLinkRow:
   def __init__(self, obj):
      self.GLAccLinkUID:int = obj["GLAccLinkUID"]
      """  GLAccount Link unique ID.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.CreationDate:str = obj["CreationDate"]
      """  System date when the link was created.  """  
      self.CreationTime:int = obj["CreationTime"]
      """  System time when the link was created (seconds since midnight format).  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source Chart of Account ID  """  
      self.SourceGLAccount:str = obj["SourceGLAccount"]
      """  Source full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.SourceSegValue1:str = obj["SourceSegValue1"]
      """  Source SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SourceSegValue2:str = obj["SourceSegValue2"]
      """  Source SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SourceSegValue3:str = obj["SourceSegValue3"]
      """  Source SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SourceSegValue4:str = obj["SourceSegValue4"]
      """  Source SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SourceSegValue5:str = obj["SourceSegValue5"]
      """  Source SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SourceSegValue6:str = obj["SourceSegValue6"]
      """  Source SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SourceSegValue7:str = obj["SourceSegValue7"]
      """  Source SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SourceSegValue8:str = obj["SourceSegValue8"]
      """  Source SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SourceSegValue9:str = obj["SourceSegValue9"]
      """  Source SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SourceSegValue10:str = obj["SourceSegValue10"]
      """  Source SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SourceSegValue11:str = obj["SourceSegValue11"]
      """  Source SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SourceSegValue12:str = obj["SourceSegValue12"]
      """  Source SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SourceSegValue13:str = obj["SourceSegValue13"]
      """  Source SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SourceSegValue14:str = obj["SourceSegValue14"]
      """  Source SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SourceSegValue15:str = obj["SourceSegValue15"]
      """  Source SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SourceSegValue16:str = obj["SourceSegValue16"]
      """  Source SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SourceSegValue17:str = obj["SourceSegValue17"]
      """  Source SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SourceSegValue18:str = obj["SourceSegValue18"]
      """  Source SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SourceSegValue19:str = obj["SourceSegValue19"]
      """  Source SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SourceSegValue20:str = obj["SourceSegValue20"]
      """  Source SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Account ID  """  
      self.TargetGLAccount:str = obj["TargetGLAccount"]
      """  Target full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.TargetSegValue1:str = obj["TargetSegValue1"]
      """  Target SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.TargetSegValue2:str = obj["TargetSegValue2"]
      """  Target SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.TargetSegValue3:str = obj["TargetSegValue3"]
      """  Target SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.TargetSegValue4:str = obj["TargetSegValue4"]
      """  Target SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.TargetSegValue5:str = obj["TargetSegValue5"]
      """  Target SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.TargetSegValue6:str = obj["TargetSegValue6"]
      """  Target SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.TargetSegValue7:str = obj["TargetSegValue7"]
      """  Target SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.TargetSegValue8:str = obj["TargetSegValue8"]
      """  Target SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.TargetSegValue9:str = obj["TargetSegValue9"]
      """  Target SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.TargetSegValue10:str = obj["TargetSegValue10"]
      """  Target SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.TargetSegValue11:str = obj["TargetSegValue11"]
      """  Target SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.TargetSegValue12:str = obj["TargetSegValue12"]
      """  Target SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.TargetSegValue13:str = obj["TargetSegValue13"]
      """  Target SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.TargetSegValue14:str = obj["TargetSegValue14"]
      """  Target SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.TargetSegValue15:str = obj["TargetSegValue15"]
      """  Target SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.TargetSegValue16:str = obj["TargetSegValue16"]
      """  Target SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.TargetSegValue17:str = obj["TargetSegValue17"]
      """  Target SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.TargetSegValue18:str = obj["TargetSegValue18"]
      """  Target SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.TargetSegValue19:str = obj["TargetSegValue19"]
      """  Target SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.TargetSegValue20:str = obj["TargetSegValue20"]
      """  Target SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TargetCompany:str = obj["TargetCompany"]
      """  Target Company  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SrcGLAccountDisplayGLShortAcct:str = obj["SrcGLAccountDisplayGLShortAcct"]
      self.SrcGLAccountDisplayAccountDesc:str = obj["SrcGLAccountDisplayAccountDesc"]
      self.SrcGLAccountDisplayGLAcctDisp:str = obj["SrcGLAccountDisplayGLAcctDisp"]
      self.TgtGLAccountDisplayGLAcctDisp:str = obj["TgtGLAccountDisplayGLAcctDisp"]
      self.TgtGLAccountDisplayAccountDesc:str = obj["TgtGLAccountDisplayAccountDesc"]
      self.TgtGLAccountDisplayGLShortAcct:str = obj["TgtGLAccountDisplayGLShortAcct"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegmentLinkRow:
   def __init__(self, obj):
      self.SegmentLinkUID:int = obj["SegmentLinkUID"]
      """  Segment Link unique ID.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  type of COA for company  """  
      self.SourceSegment:int = obj["SourceSegment"]
      """  1-30  """  
      self.SourceSegValue:str = obj["SourceSegValue"]
      """  Source Segment Value  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  type of COA for company  """  
      self.TargetSegment:int = obj["TargetSegment"]
      """  1-30  """  
      self.TargetSegValue:str = obj["TargetSegValue"]
      """  Target Segment Value  """  
      self.CreationDate:str = obj["CreationDate"]
      """  System date when the link was created.  """  
      self.CreationTime:int = obj["CreationTime"]
      """  System time when the link was created (seconds since midnight format).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value used for Global Transform only.  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description used for Global Transform only.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckCOAGlobalStatus_input:
   """ Required : 
   ipCOACode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      pass

class CheckCOAGlobalStatus_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   coAMapUID
   """  
   def __init__(self, obj):
      self.coAMapUID:int = obj["coAMapUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_COAMapDataTableset:
   def __init__(self, obj):
      self.COAMap:list[Erp_Tablesets_COAMapRow] = obj["COAMap"]
      self.GLAccLink:list[Erp_Tablesets_GLAccLinkRow] = obj["GLAccLink"]
      self.SegmentLink:list[Erp_Tablesets_SegmentLinkRow] = obj["SegmentLink"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COAMapListRow:
   def __init__(self, obj):
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed Description  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  type of COA for company  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  type of COA for company  """  
      self.MapType:int = obj["MapType"]
      """  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOASegmentTransform:bool = obj["GlobalCOASegmentTransform"]
      """  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  """  
      self.SourceCOADescription:str = obj["SourceCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.TargetGLBCOADescription:str = obj["TargetGLBCOADescription"]
      """  The description or Name of this Chart of Accounts.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_COAMapListTableset:
   def __init__(self, obj):
      self.COAMapList:list[Erp_Tablesets_COAMapListRow] = obj["COAMapList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_COAMapRow:
   def __init__(self, obj):
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.DisplayName:str = obj["DisplayName"]
      """  Display name  """  
      self.DetailedDescription:str = obj["DetailedDescription"]
      """  Detailed Description  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  type of COA for company  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  type of COA for company  """  
      self.MapType:int = obj["MapType"]
      """  Map type: "Accounting Segment Map" = 0
                "Accounting String Map"      = 1  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TgtCompany:str = obj["TgtCompany"]
      """  Target Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlobalCOASegmentTransform:bool = obj["GlobalCOASegmentTransform"]
      """  Marks the record to be used as a Global COA Segment Transform record instead of a standard COAMap record  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  The ID of the interfaced company for Global Transform only.  """  
      self.TargetSegment:int = obj["TargetSegment"]
      """  Target Segment - combobox filter.  """  
      self.SourceSegment:int = obj["SourceSegment"]
      """  Target Segment - combobox filter.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SourceCOADescription:str = obj["SourceCOADescription"]
      self.TargetCOADescription:str = obj["TargetCOADescription"]
      self.TargetGLBCOADescription:str = obj["TargetGLBCOADescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccLinkRow:
   def __init__(self, obj):
      self.GLAccLinkUID:int = obj["GLAccLinkUID"]
      """  GLAccount Link unique ID.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.CreationDate:str = obj["CreationDate"]
      """  System date when the link was created.  """  
      self.CreationTime:int = obj["CreationTime"]
      """  System time when the link was created (seconds since midnight format).  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  Source Chart of Account ID  """  
      self.SourceGLAccount:str = obj["SourceGLAccount"]
      """  Source full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.SourceSegValue1:str = obj["SourceSegValue1"]
      """  Source SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SourceSegValue2:str = obj["SourceSegValue2"]
      """  Source SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SourceSegValue3:str = obj["SourceSegValue3"]
      """  Source SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SourceSegValue4:str = obj["SourceSegValue4"]
      """  Source SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SourceSegValue5:str = obj["SourceSegValue5"]
      """  Source SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SourceSegValue6:str = obj["SourceSegValue6"]
      """  Source SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SourceSegValue7:str = obj["SourceSegValue7"]
      """  Source SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SourceSegValue8:str = obj["SourceSegValue8"]
      """  Source SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SourceSegValue9:str = obj["SourceSegValue9"]
      """  Source SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SourceSegValue10:str = obj["SourceSegValue10"]
      """  Source SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SourceSegValue11:str = obj["SourceSegValue11"]
      """  Source SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SourceSegValue12:str = obj["SourceSegValue12"]
      """  Source SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SourceSegValue13:str = obj["SourceSegValue13"]
      """  Source SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SourceSegValue14:str = obj["SourceSegValue14"]
      """  Source SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SourceSegValue15:str = obj["SourceSegValue15"]
      """  Source SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SourceSegValue16:str = obj["SourceSegValue16"]
      """  Source SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SourceSegValue17:str = obj["SourceSegValue17"]
      """  Source SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SourceSegValue18:str = obj["SourceSegValue18"]
      """  Source SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SourceSegValue19:str = obj["SourceSegValue19"]
      """  Source SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SourceSegValue20:str = obj["SourceSegValue20"]
      """  Source SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  Target Chart of Account ID  """  
      self.TargetGLAccount:str = obj["TargetGLAccount"]
      """  Target full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.TargetSegValue1:str = obj["TargetSegValue1"]
      """  Target SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.TargetSegValue2:str = obj["TargetSegValue2"]
      """  Target SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.TargetSegValue3:str = obj["TargetSegValue3"]
      """  Target SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.TargetSegValue4:str = obj["TargetSegValue4"]
      """  Target SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.TargetSegValue5:str = obj["TargetSegValue5"]
      """  Target SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.TargetSegValue6:str = obj["TargetSegValue6"]
      """  Target SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.TargetSegValue7:str = obj["TargetSegValue7"]
      """  Target SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.TargetSegValue8:str = obj["TargetSegValue8"]
      """  Target SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.TargetSegValue9:str = obj["TargetSegValue9"]
      """  Target SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.TargetSegValue10:str = obj["TargetSegValue10"]
      """  Target SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.TargetSegValue11:str = obj["TargetSegValue11"]
      """  Target SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.TargetSegValue12:str = obj["TargetSegValue12"]
      """  Target SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.TargetSegValue13:str = obj["TargetSegValue13"]
      """  Target SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.TargetSegValue14:str = obj["TargetSegValue14"]
      """  Target SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.TargetSegValue15:str = obj["TargetSegValue15"]
      """  Target SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.TargetSegValue16:str = obj["TargetSegValue16"]
      """  Target SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.TargetSegValue17:str = obj["TargetSegValue17"]
      """  Target SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.TargetSegValue18:str = obj["TargetSegValue18"]
      """  Target SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.TargetSegValue19:str = obj["TargetSegValue19"]
      """  Target SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.TargetSegValue20:str = obj["TargetSegValue20"]
      """  Target SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TargetCompany:str = obj["TargetCompany"]
      """  Target Company  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SrcGLAccountDisplayGLShortAcct:str = obj["SrcGLAccountDisplayGLShortAcct"]
      self.SrcGLAccountDisplayAccountDesc:str = obj["SrcGLAccountDisplayAccountDesc"]
      self.SrcGLAccountDisplayGLAcctDisp:str = obj["SrcGLAccountDisplayGLAcctDisp"]
      self.TgtGLAccountDisplayGLAcctDisp:str = obj["TgtGLAccountDisplayGLAcctDisp"]
      self.TgtGLAccountDisplayAccountDesc:str = obj["TgtGLAccountDisplayAccountDesc"]
      self.TgtGLAccountDisplayGLShortAcct:str = obj["TgtGLAccountDisplayGLShortAcct"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SegmentLinkRow:
   def __init__(self, obj):
      self.SegmentLinkUID:int = obj["SegmentLinkUID"]
      """  Segment Link unique ID.  """  
      self.COAMapUID:int = obj["COAMapUID"]
      """  COA map unique ID.  """  
      self.SourceCOA:str = obj["SourceCOA"]
      """  type of COA for company  """  
      self.SourceSegment:int = obj["SourceSegment"]
      """  1-30  """  
      self.SourceSegValue:str = obj["SourceSegValue"]
      """  Source Segment Value  """  
      self.TargetCOA:str = obj["TargetCOA"]
      """  type of COA for company  """  
      self.TargetSegment:int = obj["TargetSegment"]
      """  1-30  """  
      self.TargetSegValue:str = obj["TargetSegValue"]
      """  Target Segment Value  """  
      self.CreationDate:str = obj["CreationDate"]
      """  System date when the link was created.  """  
      self.CreationTime:int = obj["CreationTime"]
      """  System time when the link was created (seconds since midnight format).  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SegmentAbbrev:str = obj["SegmentAbbrev"]
      """  Short name of the segment value used for Global Transform only.  """  
      self.SegmentDesc:str = obj["SegmentDesc"]
      """  Segment description used for Global Transform only.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCOAMapDataTableset:
   def __init__(self, obj):
      self.COAMap:list[Erp_Tablesets_COAMapRow] = obj["COAMap"]
      self.GLAccLink:list[Erp_Tablesets_GLAccLinkRow] = obj["GLAccLink"]
      self.SegmentLink:list[Erp_Tablesets_SegmentLinkRow] = obj["SegmentLink"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByDisplayName_input:
   """ Required : 
   displayName
   """  
   def __init__(self, obj):
      self.displayName:str = obj["displayName"]
      """  Display Name  """  
      pass

class GetByDisplayName_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAMapDataTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   coAMapUID
   """  
   def __init__(self, obj):
      self.coAMapUID:int = obj["coAMapUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAMapDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAMapDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAMapDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_COAMapListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMapTypeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewCOAMap_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

class GetNewCOAMap_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGLAccLink_input:
   """ Required : 
   ds
   coAMapUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      self.coAMapUID:int = obj["coAMapUID"]
      pass

class GetNewGLAccLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSegmentLink_WithSegmentsFilled_input:
   """ Required : 
   coAMapUID
   sourceSegment
   targetSegment
   ds
   """  
   def __init__(self, obj):
      self.coAMapUID:int = obj["coAMapUID"]
      self.sourceSegment:int = obj["sourceSegment"]
      self.targetSegment:int = obj["targetSegment"]
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

class GetNewSegmentLink_WithSegmentsFilled_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSegmentLink_input:
   """ Required : 
   ds
   coAMapUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      self.coAMapUID:int = obj["coAMapUID"]
      pass

class GetNewSegmentLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCOAMap
   whereClauseGLAccLink
   whereClauseSegmentLink
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCOAMap:str = obj["whereClauseCOAMap"]
      self.whereClauseGLAccLink:str = obj["whereClauseGLAccLink"]
      self.whereClauseSegmentLink:str = obj["whereClauseSegmentLink"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_COAMapDataTableset] = obj["returnObj"]
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

class OnChangeCOA_input:
   """ Required : 
   coa
   """  
   def __init__(self, obj):
      self.coa:str = obj["coa"]
      """  Source/Target COA  """  
      pass

class OnChangeCOA_output:
   def __init__(self, obj):
      pass

class Populate_input:
   """ Required : 
   iCoaMap
   cSource
   cTarget
   iSrcSeg
   iTrgSeg
   cFld
   ds
   """  
   def __init__(self, obj):
      self.iCoaMap:int = obj["iCoaMap"]
      """  srcSeg  """  
      self.cSource:str = obj["cSource"]
      """  field  """  
      self.cTarget:str = obj["cTarget"]
      """  field  """  
      self.iSrcSeg:int = obj["iSrcSeg"]
      """  srcSeg  """  
      self.iTrgSeg:int = obj["iTrgSeg"]
      """  trgSeg  """  
      self.cFld:str = obj["cFld"]
      """  field  """  
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

class Populate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOAMapDataTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCOAMapDataTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateTargetCOA_input:
   """ Required : 
   ipTargetCOA
   ds
   """  
   def __init__(self, obj):
      self.ipTargetCOA:str = obj["ipTargetCOA"]
      """  Proposed COA code  """  
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

class ValidateTargetCOA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateTargetCompany_input:
   """ Required : 
   ipTargetCompany
   ds
   """  
   def __init__(self, obj):
      self.ipTargetCompany:str = obj["ipTargetCompany"]
      """  Proposed target Company  """  
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

class ValidateTargetCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_COAMapDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

