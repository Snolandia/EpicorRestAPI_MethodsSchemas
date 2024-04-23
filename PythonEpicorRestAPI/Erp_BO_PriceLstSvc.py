import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PriceLstSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLsts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts",headers=creds) as resp:
           return await resp.json()

async def post_PriceLsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode(Company, ListCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLst item
   Description: Calls GetByID to retrieve the PriceLst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLsts_Company_ListCode(Company, ListCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLst for the service
   Description: Calls UpdateExt to update PriceLst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLsts_Company_ListCode(Company, ListCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLst item
   Description: Call UpdateExt to delete PriceLst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode_PriceLstGroups(Company, ListCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PriceLstGroups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstGroups1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstGroups",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstGroup item
   Description: Calls GetByID to retrieve the PriceLstGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstGroup1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode_PriceLstParts(Company, ListCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PriceLstParts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstParts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstParts",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstPart item
   Description: Calls GetByID to retrieve the PriceLstPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstPart1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode_PriceLstAttches(Company, ListCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PriceLstAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PriceLstAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstAttches",headers=creds) as resp:
           return await resp.json()

async def get_PriceLsts_Company_ListCode_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstAttch item
   Description: Calls GetByID to retrieve the PriceLstAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLsts(" + Company + "," + ListCode + ")/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstGroupsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstGroup item
   Description: Calls GetByID to retrieve the PriceLstGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstGroup for the service
   Description: Calls UpdateExt to update PriceLstGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstGroupsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstGroups_Company_ListCode_ProdCode_UOMCode(Company, ListCode, ProdCode, UOMCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstGroup item
   Description: Call UpdateExt to delete PriceLstGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode_PLGrupBrks(Company, ListCode, ProdCode, UOMCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PLGrupBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLGrupBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstGroups_Company_ListCode_ProdCode_UOMCode_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLGrupBrk item
   Description: Calls GetByID to retrieve the PLGrupBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLGrupBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstGroups(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + ")/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def get_PLGrupBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PLGrupBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLGrupBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks",headers=creds) as resp:
           return await resp.json()

async def post_PLGrupBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLGrupBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLGrupBrk item
   Description: Calls GetByID to retrieve the PLGrupBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLGrupBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PLGrupBrk for the service
   Description: Calls UpdateExt to update PLGrupBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLGrupBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLGrupBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PLGrupBrks_Company_ListCode_ProdCode_UOMCode_Quantity(Company, ListCode, ProdCode, UOMCode, Quantity, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PLGrupBrk item
   Description: Call UpdateExt to delete PLGrupBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLGrupBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param ProdCode: Desc: ProdCode   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLGrupBrks(" + Company + "," + ListCode + "," + ProdCode + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstParts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstParts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstPartsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstParts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstPart item
   Description: Calls GetByID to retrieve the PriceLstPart item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstPart for the service
   Description: Calls UpdateExt to update PriceLstPart. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstPartsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstParts_Company_ListCode_PartNum_UOMCode(Company, ListCode, PartNum, UOMCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstPart item
   Description: Call UpdateExt to delete PriceLstPart item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstPart
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts_Company_ListCode_PartNum_UOMCode_PLPartBrks(Company, ListCode, PartNum, UOMCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PLPartBrks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PLPartBrks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstParts_Company_ListCode_PartNum_UOMCode_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLPartBrk item
   Description: Calls GetByID to retrieve the PLPartBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLPartBrk1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstParts(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + ")/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def get_PLPartBrks(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PLPartBrks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PLPartBrks
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks",headers=creds) as resp:
           return await resp.json()

async def post_PLPartBrks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PLPartBrks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PLPartBrk item
   Description: Calls GetByID to retrieve the PLPartBrk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PLPartBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PLPartBrk for the service
   Description: Calls UpdateExt to update PLPartBrk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PLPartBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PLPartBrkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PLPartBrks_Company_ListCode_PartNum_UOMCode_Quantity(Company, ListCode, PartNum, UOMCode, Quantity, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PLPartBrk item
   Description: Call UpdateExt to delete PLPartBrk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PLPartBrk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param UOMCode: Desc: UOMCode   Required: True   Allow empty value : True
      :param Quantity: Desc: Quantity   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PLPartBrks(" + Company + "," + ListCode + "," + PartNum + "," + UOMCode + "," + Quantity + ")",headers=creds) as resp:
           return await resp.json()

async def get_PriceLstAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PriceLstAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PriceLstAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches",headers=creds) as resp:
           return await resp.json()

async def post_PriceLstAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PriceLstAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PriceLstAttch item
   Description: Calls GetByID to retrieve the PriceLstAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PriceLstAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PriceLstAttch for the service
   Description: Calls UpdateExt to update PriceLstAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PriceLstAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PriceLstAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PriceLstAttches_Company_ListCode_DrawingSeq(Company, ListCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PriceLstAttch item
   Description: Call UpdateExt to delete PriceLstAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PriceLstAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ListCode: Desc: ListCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/PriceLstAttches(" + Company + "," + ListCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PriceLstListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePriceLst, whereClausePriceLstAttch, whereClausePriceLstGroups, whereClausePLGrupBrk, whereClausePriceLstParts, whereClausePLPartBrk, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePriceLst=" + whereClausePriceLst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePriceLstAttch=" + whereClausePriceLstAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePriceLstGroups=" + whereClausePriceLstGroups
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePLGrupBrk=" + whereClausePLGrupBrk
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePriceLstParts=" + whereClausePriceLstParts
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePLPartBrk=" + whereClausePLPartBrk
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(listCode, epicorHeaders = None):
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
   params += "listCode=" + listCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BuildUOMList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildUOMList
   Description: Build a list of all the valid UOM's defined for all the parts within
the product group.
   OperationID: BuildUOMList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildUOMList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildUOMList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Get the track multiple UOM setting when the part number changes.
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangingKeyParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangingKeyParts
   Description: Validate the entered part an UOM doesn't exist in the price list.
   OperationID: ChangingKeyParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingKeyParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingKeyParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUOM
   Description: Validate the sales UOM doesn't exist in the price list.
   OperationID: ValidateUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListFilterPriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListFilterPriceList
   Description: Filter parts by plant.  Call normal GetList method.
   OperationID: GetListFilterPriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListFilterPriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListFilterPriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceLstGroupDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceLstGroupDefaults
   Description: Gets the following fields for the product group: Description.
   OperationID: GetPriceLstGroupDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceLstGroupDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceLstGroupDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceLstPartsDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceLstPartsDefaults
   OperationID: GetPriceLstPartsDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceLstPartsDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceLstPartsDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidUOM
   OperationID: ValidUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingFSMSendTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingFSMSendTo
   OperationID: OnChangingFSMSendTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingFSMSendTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingFSMSendTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingEndDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingEndDate
   OperationID: OnChangingEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PriceLstGetValidRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PriceLstGetValidRows
   Description: Method calls the PriceLst GetRows, then it validates if a record has been retrieved (Kinetic UI Purposes)
   OperationID: PriceLstGetValidRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PriceLstGetValidRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PriceLstGetValidRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PLPartBrkGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PLPartBrkGetRows
   Description: Get the PLPartBrk Records by ListCode ID  and PartNum
   OperationID: PLPartBrkGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PLPartBrkGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PLPartBrkGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLstAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLstAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLstGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLstGroups
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstGroups_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstGroups_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPLGrupBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPLGrupBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLGrupBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLGrupBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLGrupBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPriceLstParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPriceLstParts
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPriceLstParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPriceLstParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPriceLstParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPLPartBrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPLPartBrk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPLPartBrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPLPartBrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPLPartBrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PriceLstSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PLGrupBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PLPartBrkRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstGroupsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstPartsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PriceLstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PriceLstRow] = obj["value"]
      pass

class Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique set of characters entered by the user to identify the Price List master within the company.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLGrupBrk:bool = obj["GlobalPLGrupBrk"]
      """  Marks this PLGrupBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button (P or D)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """   Unique set of characters entered by the user to identify
the Price List master within the company.  """  
      self.PartNum:str = obj["PartNum"]
      """  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLPartBrk:bool = obj["GlobalPLPartBrk"]
      """  Marks this PLPartBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button. (D or P)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Comments_c:str = obj["Comments_c"]
      pass

class Erp_Tablesets_PriceLstAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ListCode:str = obj["ListCode"]
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

class Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      """  List of WareHouse descriptions  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      """  Display Ware house list  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.LinkedPriceList_c:str = obj["LinkedPriceList_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildUOMList_input:
   """ Required : 
   ProdCode
   """  
   def __init__(self, obj):
      self.ProdCode:str = obj["ProdCode"]
      """  Order Number  """  
      pass

class BuildUOMList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.UomList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   ProposedPartNum
   pListCode
   """  
   def __init__(self, obj):
      self.ProposedPartNum:str = obj["ProposedPartNum"]
      """  Proposed Part Number  """  
      self.pListCode:str = obj["pListCode"]
      """  ListCode  """  
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.TrackMulti:bool = obj["TrackMulti"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangingKeyParts_input:
   """ Required : 
   pPartNum
   pListCode
   pUOMcode
   """  
   def __init__(self, obj):
      self.pPartNum:str = obj["pPartNum"]
      """  Part Number  """  
      self.pListCode:str = obj["pListCode"]
      """  List Code  """  
      self.pUOMcode:str = obj["pUOMcode"]
      """  UOM Code  """  
      pass

class ChangingKeyParts_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   listCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PLGrupBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique set of characters entered by the user to identify the Price List master within the company.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Descriptive code assigned by the user to uniquely identify a Product Group master.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break .  to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the group price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLGrupBrk:bool = obj["GlobalPLGrupBrk"]
      """  Marks this PLGrupBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button (P or D)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PLPartBrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """   Unique set of characters entered by the user to identify
the Price List master within the company.  """  
      self.PartNum:str = obj["PartNum"]
      """  Descriptive code assigned by the user to uniquely identify a Part master. Can't be blank.  """  
      self.Quantity:int = obj["Quantity"]
      """  The price break quantity  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  The Discount Percent that is to be given for this price break quantity. Do not allow both a discount percent and unit price for the same quantity break to be non-zero or both of them to be zero.  One must be entered but not both.  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  The "Flat Unit Price" that is to be given for this price break quantity. Order entry will use this value as an override to the unit price that is found in the part master.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list break.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPLPartBrk:bool = obj["GlobalPLPartBrk"]
      """  Marks this PLPartBrk as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RadioButtonValue:str = obj["RadioButtonValue"]
      """  Value of radio button. (D or P)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Comments_c:str = obj["Comments_c"]
      pass

class Erp_Tablesets_PriceLstAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ListCode:str = obj["ListCode"]
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

class Erp_Tablesets_PriceLstGroupsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdGrup.ProdCode value of the Product Group that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which a price break is to be given. The quantity represent the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Price List Group.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstGroups:bool = obj["GlobalPriceLstGroups"]
      """  Marks this PriceLstGroups as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProdGrpDescription:str = obj["ProdGrpDescription"]
      """  Product group description  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstListTableset:
   def __init__(self, obj):
      self.PriceLstList:list[Erp_Tablesets_PriceLstListRow] = obj["PriceLstList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PriceLstPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  PriceLst.ListCode value of the price list that this record is related to.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part.PartNum value of the Part that this record is related to.  """  
      self.BasePrice:int = obj["BasePrice"]
      """  Base Price for this product group against which the quantity breaks will be applied. Can be zero.  """  
      self.DiscountPercent1:int = obj["DiscountPercent1"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent2:int = obj["DiscountPercent2"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent3:int = obj["DiscountPercent3"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent4:int = obj["DiscountPercent4"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.DiscountPercent5:int = obj["DiscountPercent5"]
      """  Contains the Discount Percent that is to be given for a corresponding price break quantity.  """  
      self.QtyBreak1:int = obj["QtyBreak1"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak2:int = obj["QtyBreak2"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak3:int = obj["QtyBreak3"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak4:int = obj["QtyBreak4"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.QtyBreak5:int = obj["QtyBreak5"]
      """  Contains quantity at which price break is to be given. The quantity represents the minimum quantity at which the related discount would be applied.  """  
      self.UnitPrice1:int = obj["UnitPrice1"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice2:int = obj["UnitPrice2"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice3:int = obj["UnitPrice3"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice4:int = obj["UnitPrice4"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.UnitPrice5:int = obj["UnitPrice5"]
      """  Contains a flat unit price that is to be given for the corresponding price break quantity.  """  
      self.CommentText:str = obj["CommentText"]
      """  Additional comments that will be used as a default for customer price lists.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the part price list.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.GlobalPriceLstParts:bool = obj["GlobalPriceLstParts"]
      """  Marks this PriceLstParts as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  Part sales unit of measure  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """  Part selling factor  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Part price per code  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part description  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.BitFlag:int = obj["BitFlag"]
      self.ListCodeListDescription:str = obj["ListCodeListDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PriceLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ListCode:str = obj["ListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency assigned to the price list.  """  
      self.ListDescription:str = obj["ListDescription"]
      """  Description of the price list.  """  
      self.StartDate:str = obj["StartDate"]
      """  Date the price list become effective.  """  
      self.EndDate:str = obj["EndDate"]
      """  Date that the price list expires on.  """  
      self.WarehouseList:str = obj["WarehouseList"]
      """  The list of all warehouses associated with this price list.  The warehouse list is delimited by LIST-DELIM.  A blank warehouse list means all warehouses.  """  
      self.GlobalPriceLst:bool = obj["GlobalPriceLst"]
      """  Marks this PriceLst as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ListType:str = obj["ListType"]
      """  Indicates if Price List is to be used to calculate Discount (D), Unit Price (P) or Both (B)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseZeroPrice:bool = obj["UseZeroPrice"]
      """  UseZeroPrice  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.WareHouseListDescription:str = obj["WareHouseListDescription"]
      """  List of WareHouse descriptions  """  
      self.DspWareHouseList:str = obj["DspWareHouseList"]
      """  Display Ware house list  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.LinkedPriceList_c:str = obj["LinkedPriceList_c"]
      pass

class Erp_Tablesets_PriceLstTableset:
   def __init__(self, obj):
      self.PriceLst:list[Erp_Tablesets_PriceLstRow] = obj["PriceLst"]
      self.PriceLstAttch:list[Erp_Tablesets_PriceLstAttchRow] = obj["PriceLstAttch"]
      self.PriceLstGroups:list[Erp_Tablesets_PriceLstGroupsRow] = obj["PriceLstGroups"]
      self.PLGrupBrk:list[Erp_Tablesets_PLGrupBrkRow] = obj["PLGrupBrk"]
      self.PriceLstParts:list[Erp_Tablesets_PriceLstPartsRow] = obj["PriceLstParts"]
      self.PLPartBrk:list[Erp_Tablesets_PLPartBrkRow] = obj["PLPartBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPriceLstTableset:
   def __init__(self, obj):
      self.PriceLst:list[Erp_Tablesets_PriceLstRow] = obj["PriceLst"]
      self.PriceLstAttch:list[Erp_Tablesets_PriceLstAttchRow] = obj["PriceLstAttch"]
      self.PriceLstGroups:list[Erp_Tablesets_PriceLstGroupsRow] = obj["PriceLstGroups"]
      self.PLGrupBrk:list[Erp_Tablesets_PLGrupBrkRow] = obj["PLGrupBrk"]
      self.PriceLstParts:list[Erp_Tablesets_PriceLstPartsRow] = obj["PriceLstParts"]
      self.PLPartBrk:list[Erp_Tablesets_PLPartBrkRow] = obj["PLPartBrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   listCode
   """  
   def __init__(self, obj):
      self.listCode:str = obj["listCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetListFilterPriceList_input:
   """ Required : 
   OrderNum
   OrderLine
   PartNum
   ProdCode
   WhereClause
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Code.  """  
      self.WhereClause:str = obj["WhereClause"]
      """  Whereclause.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetListFilterPriceList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
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
      self.returnObj:list[Erp_Tablesets_PriceLstListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPLGrupBrk_input:
   """ Required : 
   ds
   listCode
   prodCode
   uoMCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.prodCode:str = obj["prodCode"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class GetNewPLGrupBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPLPartBrk_input:
   """ Required : 
   ds
   listCode
   partNum
   uoMCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.partNum:str = obj["partNum"]
      self.uoMCode:str = obj["uoMCode"]
      pass

class GetNewPLPartBrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLstAttch_input:
   """ Required : 
   ds
   listCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      pass

class GetNewPriceLstAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLstGroups_input:
   """ Required : 
   ds
   listCode
   prodCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.prodCode:str = obj["prodCode"]
      pass

class GetNewPriceLstGroups_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLstParts_input:
   """ Required : 
   ds
   listCode
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      self.listCode:str = obj["listCode"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPriceLstParts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPriceLst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

class GetNewPriceLst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPriceLstGroupDefaults_input:
   """ Required : 
   ProdCode
   """  
   def __init__(self, obj):
      self.ProdCode:str = obj["ProdCode"]
      """  Product group code to retrieve details for.  """  
      pass

class GetPriceLstGroupDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ProdGrpDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPriceLstPartsDefaults_input:
   """ Required : 
   PartNum
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      pass

class GetPriceLstPartsDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.PartNum:str = obj["parameters"]
      self.SalesUM:str = obj["parameters"]
      self.SellingFactor:int = obj["parameters"]
      self.PricePerCode:str = obj["parameters"]
      self.PartDescription:str = obj["parameters"]
      self.SellingFactorDirection:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePriceLst
   whereClausePriceLstAttch
   whereClausePriceLstGroups
   whereClausePLGrupBrk
   whereClausePriceLstParts
   whereClausePLPartBrk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePriceLst:str = obj["whereClausePriceLst"]
      self.whereClausePriceLstAttch:str = obj["whereClausePriceLstAttch"]
      self.whereClausePriceLstGroups:str = obj["whereClausePriceLstGroups"]
      self.whereClausePLGrupBrk:str = obj["whereClausePLGrupBrk"]
      self.whereClausePriceLstParts:str = obj["whereClausePriceLstParts"]
      self.whereClausePLPartBrk:str = obj["whereClausePLPartBrk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstTableset] = obj["returnObj"]
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

class OnChangingEndDate_input:
   """ Required : 
   endDate
   ds
   """  
   def __init__(self, obj):
      self.endDate:str = obj["endDate"]
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

class OnChangingEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingFSMSendTo_input:
   """ Required : 
   fsmSendTo
   ds
   """  
   def __init__(self, obj):
      self.fsmSendTo:bool = obj["fsmSendTo"]
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

class OnChangingFSMSendTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PLPartBrkGetRows_input:
   """ Required : 
   ListCode
   PartNum
   ds
   """  
   def __init__(self, obj):
      self.ListCode:str = obj["ListCode"]
      self.PartNum:str = obj["PartNum"]
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

class PLPartBrkGetRows_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PriceLstGetValidRows_input:
   """ Required : 
   whereClausePriceLst
   whereClausePriceLstAttch
   whereClausePriceLstGroups
   whereClausePLGrupBrk
   whereClausePriceLstParts
   whereClausePLPartBrk
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePriceLst:str = obj["whereClausePriceLst"]
      self.whereClausePriceLstAttch:str = obj["whereClausePriceLstAttch"]
      self.whereClausePriceLstGroups:str = obj["whereClausePriceLstGroups"]
      self.whereClausePLGrupBrk:str = obj["whereClausePLGrupBrk"]
      self.whereClausePriceLstParts:str = obj["whereClausePriceLstParts"]
      self.whereClausePLPartBrk:str = obj["whereClausePLPartBrk"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class PriceLstGetValidRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PriceLstTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceLstTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPriceLstTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PriceLstTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidUOM_input:
   """ Required : 
   prodGroup
   iPartNum
   iUOM
   """  
   def __init__(self, obj):
      self.prodGroup:str = obj["prodGroup"]
      self.iPartNum:str = obj["iPartNum"]
      self.iUOM:str = obj["iUOM"]
      pass

class ValidUOM_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateUOM_input:
   """ Required : 
   pPartNum
   pListCode
   pUOMcode
   """  
   def __init__(self, obj):
      self.pPartNum:str = obj["pPartNum"]
      """  Part Number  """  
      self.pListCode:str = obj["pListCode"]
      """  List Code  """  
      self.pUOMcode:str = obj["pUOMcode"]
      """  UOM Code  """  
      pass

class ValidateUOM_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

