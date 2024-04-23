import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PackingSvc
# Description: Packing Data Set
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Packings(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Packings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Packings
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings",headers=creds) as resp:
           return await resp.json()

async def post_Packings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Packings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PackingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PackingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Packings_Company_PkgCode(Company, PkgCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Packing item
   Description: Calls GetByID to retrieve the Packing item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Packing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PackingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Packings_Company_PkgCode(Company, PkgCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Packing for the service
   Description: Calls UpdateExt to update Packing. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Packing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PackingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Packings_Company_PkgCode(Company, PkgCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Packing item
   Description: Call UpdateExt to delete Packing item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Packing
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Packings_Company_PkgCode_PackingPlants(Company, PkgCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PackingPlants items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PackingPlants1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingPlants",headers=creds) as resp:
           return await resp.json()

async def get_Packings_Company_PkgCode_PackingPlants_Company_PkgCode_Plant(Company, PkgCode, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PackingPlant item
   Description: Calls GetByID to retrieve the PackingPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingPlant1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_Packings_Company_PkgCode_PackingShipToes(Company, PkgCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PackingShipToes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PackingShipToes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingShipToes",headers=creds) as resp:
           return await resp.json()

async def get_Packings_Company_PkgCode_PackingShipToes_Company_PkgCode_ShipToSeq(Company, PkgCode, ShipToSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PackingShipTo item
   Description: Calls GetByID to retrieve the PackingShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingShipTo1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param ShipToSeq: Desc: ShipToSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/Packings(" + Company + "," + PkgCode + ")/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PackingPlants(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PackingPlants items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PackingPlants
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants",headers=creds) as resp:
           return await resp.json()

async def post_PackingPlants(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PackingPlants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PackingPlants_Company_PkgCode_Plant(Company, PkgCode, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PackingPlant item
   Description: Calls GetByID to retrieve the PackingPlant item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingPlant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PackingPlants_Company_PkgCode_Plant(Company, PkgCode, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PackingPlant for the service
   Description: Calls UpdateExt to update PackingPlant. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PackingPlant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PackingPlantRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PackingPlants_Company_PkgCode_Plant(Company, PkgCode, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PackingPlant item
   Description: Call UpdateExt to delete PackingPlant item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PackingPlant
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingPlants(" + Company + "," + PkgCode + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PackingShipToes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PackingShipToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PackingShipToes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes",headers=creds) as resp:
           return await resp.json()

async def post_PackingShipToes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PackingShipToes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PackingShipToes_Company_PkgCode_ShipToSeq(Company, PkgCode, ShipToSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PackingShipTo item
   Description: Calls GetByID to retrieve the PackingShipTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PackingShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param ShipToSeq: Desc: ShipToSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PackingShipToes_Company_PkgCode_ShipToSeq(Company, PkgCode, ShipToSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PackingShipTo for the service
   Description: Calls UpdateExt to update PackingShipTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PackingShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param ShipToSeq: Desc: ShipToSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PackingShipToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PackingShipToes_Company_PkgCode_ShipToSeq(Company, PkgCode, ShipToSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PackingShipTo item
   Description: Call UpdateExt to delete PackingShipTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PackingShipTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param ShipToSeq: Desc: ShipToSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/PackingShipToes(" + Company + "," + PkgCode + "," + ShipToSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PackingListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePacking, whereClausePackingPlant, whereClausePackingShipTo, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePacking=" + whereClausePacking
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePackingPlant=" + whereClausePackingPlant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePackingShipTo=" + whereClausePackingShipTo
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(pkgCode, epicorHeaders = None):
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
   params += "pkgCode=" + pkgCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPackingList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackingList
   Description: Retrieve a packing list for combo by part number. If part is not specified then it return all packing codes.
   OperationID: GetPackingList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackingList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackingList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackingByPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackingByPart
   Description: Purpose:     Used by combo to retrieve package codes by part and plant
Parameters:  whereclause
Notes:
///<param name="packingPlantWhereClause">Where Clause</param>
   OperationID: GetPackingByPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackingByPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackingByPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Purpose:
Parameters:  none
Notes:
///<param name="ipPartNum">Part Number</param>
/// <param name="ds">Packing dataset</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCustomerCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCustomerCustID
   Description: Update Customer information when the Customer is changed.
   OperationID: OnChangeCustomerCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCustomerCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCustomerCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeShipToID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeShipToID
   Description: Update PackingShipTo information with values from the Ship To when the Ship To is changed.
   OperationID: OnChangeShipToID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeShipToID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeShipToID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackingRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackingRecords
   Description: Used to retrieve Packing, PackingPlant and PackingShipTo records for the current plant.
<returns>Packing Tableset</returns><param name="pkgWClause" type="string">WhereClause for Packing table</param><param name="pkgPlantWClause" type="string">WhereClause for PackingPlant table</param><param name="pkgShipToWClause" type="string">WhereClause for PackingShipTo table</param><param name="table" type="string">Search form will display records from this table</param><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
   OperationID: GetPackingRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackingRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackingRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPacking(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPacking
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPacking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPacking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPacking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPackingPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPackingPlant
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPackingPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPackingPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPackingPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPackingShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPackingShipTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPackingShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPackingShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPackingShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackingSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PackingListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingPlantRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PackingPlantRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PackingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PackingShipToRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PackingShipToRow] = obj["value"]
      pass

class Erp_Tablesets_PackingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  """  
      self.Description:str = obj["Description"]
      """  Full description of Packing Code.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for this package code  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for this package code  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for this package code  """  
      self.PromptSetLength:int = obj["PromptSetLength"]
      """  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  """  
      self.PromptSetWidth:int = obj["PromptSetWidth"]
      """  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.PromptSetHeight:int = obj["PromptSetHeight"]
      """  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.Serialized:bool = obj["Serialized"]
      """  Serialized  """  
      self.Returnable:bool = obj["Returnable"]
      """  Returnable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.Weight:int = obj["Weight"]
      """  Tare Weight.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  """  
      self.PromptSetWeight:int = obj["PromptSetWeight"]
      """  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  """  
      self.GlobalPacking:bool = obj["GlobalPacking"]
      """  Marks this Packing as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  If yes then the system will track the returnable container.  If yes the Internal Part Number must be defined.  """  
      self.TrackingReasonCodeIn:str = obj["TrackingReasonCodeIn"]
      """  Reason Code used by the Container Return Receipt transaction when the package is returned.  """  
      self.TrackingReasonCodeOut:str = obj["TrackingReasonCodeOut"]
      """  Reason Code used when a Quantity Adjustment is triggered when the package is shipped.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  If yes then the system will track the expendable container.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PlantInvalidForUser:bool = obj["PlantInvalidForUser"]
      """  A flag used to indicate if the user is not authorized for the PackingPlant.Plant - to prevent updates in the UI.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InternalPartSellingFactor:int = obj["InternalPartSellingFactor"]
      self.InternalPartPartDescription:str = obj["InternalPartPartDescription"]
      self.InternalPartPricePerCode:str = obj["InternalPartPricePerCode"]
      self.InternalPartTrackDimension:bool = obj["InternalPartTrackDimension"]
      self.InternalPartTrackLots:bool = obj["InternalPartTrackLots"]
      self.InternalPartIUM:str = obj["InternalPartIUM"]
      self.InternalPartSalesUM:str = obj["InternalPartSalesUM"]
      self.InternalPartTrackSerialNum:bool = obj["InternalPartTrackSerialNum"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ReasonInDescription:str = obj["ReasonInDescription"]
      self.ReasonOutDescription:str = obj["ReasonOutDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  """  
      self.Description:str = obj["Description"]
      """  Full description of Packing Code.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for this package code  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for this package code  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for this package code  """  
      self.PromptSetLength:int = obj["PromptSetLength"]
      """  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  """  
      self.PromptSetWidth:int = obj["PromptSetWidth"]
      """  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.PromptSetHeight:int = obj["PromptSetHeight"]
      """  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.Serialized:bool = obj["Serialized"]
      """  Serialized  """  
      self.Returnable:bool = obj["Returnable"]
      """  Returnable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.Weight:int = obj["Weight"]
      """  Tare Weight.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  """  
      self.PromptSetWeight:int = obj["PromptSetWeight"]
      """  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  """  
      self.GlobalPacking:bool = obj["GlobalPacking"]
      """  Marks this Packing as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PkgTypeCode:str = obj["PkgTypeCode"]
      """  Package Type Code assigned by the user  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum Stack  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Gross Weight not to exceed for both the package and its contents.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  Volume unit of measure.  """  
      self.InternalVolume:int = obj["InternalVolume"]
      """  Internal Volume.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the package code has been inactivated.  """  
      self.Expendable:bool = obj["Expendable"]
      """  Expendable  """  
      self.PkgInternalLength:int = obj["PkgInternalLength"]
      """  Internal length dimension for this package code.  """  
      self.PkgInternalWidth:int = obj["PkgInternalWidth"]
      """  Internal width dimension for this package code.  """  
      self.PkgInternalHeight:int = obj["PkgInternalHeight"]
      """  Internal height dimension for this package code.  """  
      self.InternalPromptSetLength:int = obj["InternalPromptSetLength"]
      """  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  """  
      self.InternalPromptSetWidth:int = obj["InternalPromptSetWidth"]
      """  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.InternalPromptSetHeight:int = obj["InternalPromptSetHeight"]
      """  Determines whether or not the packaging height is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.PkgMtlTypeCode:str = obj["PkgMtlTypeCode"]
      """  Unique package material type code assigned by the user.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.EnableInactive:bool = obj["EnableInactive"]
      """  Flag to be used internally for row rules for whether to allow the Packing Code to be set to inactive.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PackingMtlTypePkgMtlTypeCodeDesc:str = obj["PackingMtlTypePkgMtlTypeCodeDesc"]
      self.PackingTypePkgTypeDesc:str = obj["PackingTypePkgTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ShipToSeq:int = obj["ShipToSeq"]
      """  ShipToSeq  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      """  The ship to specified container part ID.  """  
      self.ShipToContainerPartDesc:str = obj["ShipToContainerPartDesc"]
      """  The ship to specified container part description.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      """  Holds "~" delimited name and address data from the ShipTo record.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      self.CustID:str = obj["CustID"]
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  The name and address data from the ShipTo record formatted.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.ShipToName:str = obj["ShipToName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   pkgCode
   """  
   def __init__(self, obj):
      self.pkgCode:str = obj["pkgCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PackingListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  """  
      self.Description:str = obj["Description"]
      """  Full description of Packing Code.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for this package code  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for this package code  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for this package code  """  
      self.PromptSetLength:int = obj["PromptSetLength"]
      """  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  """  
      self.PromptSetWidth:int = obj["PromptSetWidth"]
      """  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.PromptSetHeight:int = obj["PromptSetHeight"]
      """  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.Serialized:bool = obj["Serialized"]
      """  Serialized  """  
      self.Returnable:bool = obj["Returnable"]
      """  Returnable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.Weight:int = obj["Weight"]
      """  Tare Weight.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  """  
      self.PromptSetWeight:int = obj["PromptSetWeight"]
      """  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  """  
      self.GlobalPacking:bool = obj["GlobalPacking"]
      """  Marks this Packing as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingListTableset:
   def __init__(self, obj):
      self.PackingList:list[Erp_Tablesets_PackingListRow] = obj["PackingList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PackingPlantRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  If yes then the system will track the returnable container.  If yes the Internal Part Number must be defined.  """  
      self.TrackingReasonCodeIn:str = obj["TrackingReasonCodeIn"]
      """  Reason Code used by the Container Return Receipt transaction when the package is returned.  """  
      self.TrackingReasonCodeOut:str = obj["TrackingReasonCodeOut"]
      """  Reason Code used when a Quantity Adjustment is triggered when the package is shipped.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  If yes then the system will track the expendable container.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PlantInvalidForUser:bool = obj["PlantInvalidForUser"]
      """  A flag used to indicate if the user is not authorized for the PackingPlant.Plant - to prevent updates in the UI.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InternalPartSellingFactor:int = obj["InternalPartSellingFactor"]
      self.InternalPartPartDescription:str = obj["InternalPartPartDescription"]
      self.InternalPartPricePerCode:str = obj["InternalPartPricePerCode"]
      self.InternalPartTrackDimension:bool = obj["InternalPartTrackDimension"]
      self.InternalPartTrackLots:bool = obj["InternalPartTrackLots"]
      self.InternalPartIUM:str = obj["InternalPartIUM"]
      self.InternalPartSalesUM:str = obj["InternalPartSalesUM"]
      self.InternalPartTrackSerialNum:bool = obj["InternalPartTrackSerialNum"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ReasonInDescription:str = obj["ReasonInDescription"]
      self.ReasonOutDescription:str = obj["ReasonOutDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user. For example - box, skid, drum...etc.  """  
      self.Description:str = obj["Description"]
      """  Full description of Packing Code.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for this package code  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for this package code  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for this package code  """  
      self.PromptSetLength:int = obj["PromptSetLength"]
      """  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  """  
      self.PromptSetWidth:int = obj["PromptSetWidth"]
      """  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.PromptSetHeight:int = obj["PromptSetHeight"]
      """  Determines whether or not the packaging height is predefined or if users are able to enter a different height than what is specified on this record.  A zero indicates the height is prompted.  A one indicates the height specified on this record is the value used.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLength, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.Serialized:bool = obj["Serialized"]
      """  Serialized  """  
      self.Returnable:bool = obj["Returnable"]
      """  Returnable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  If defined will override the extension digit at the company level. The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.Weight:int = obj["Weight"]
      """  Tare Weight.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new records.  """  
      self.PromptSetWeight:int = obj["PromptSetWeight"]
      """  Determines whether or not the packaging weight is predefined or if users are able to enter a different weight than what is specified on this record.  A zero indicates the weight is prompted.  A one indicates the weight specified on this record is the value used.  """  
      self.GlobalPacking:bool = obj["GlobalPacking"]
      """  Marks this Packing as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PkgTypeCode:str = obj["PkgTypeCode"]
      """  Package Type Code assigned by the user  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum Stack  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Gross Weight not to exceed for both the package and its contents.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  Volume unit of measure.  """  
      self.InternalVolume:int = obj["InternalVolume"]
      """  Internal Volume.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the package code has been inactivated.  """  
      self.Expendable:bool = obj["Expendable"]
      """  Expendable  """  
      self.PkgInternalLength:int = obj["PkgInternalLength"]
      """  Internal length dimension for this package code.  """  
      self.PkgInternalWidth:int = obj["PkgInternalWidth"]
      """  Internal width dimension for this package code.  """  
      self.PkgInternalHeight:int = obj["PkgInternalHeight"]
      """  Internal height dimension for this package code.  """  
      self.InternalPromptSetLength:int = obj["InternalPromptSetLength"]
      """  Determines whether or not the packaging length is predefined or if users are able to enter a different length than what is specified on this record.  A zero indicates the length is prompted.  A one indicates the length specified on this record is the value used.  """  
      self.InternalPromptSetWidth:int = obj["InternalPromptSetWidth"]
      """  Determines whether or not the packaging width is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.InternalPromptSetHeight:int = obj["InternalPromptSetHeight"]
      """  Determines whether or not the packaging height is predefined or if users are able to enter a different width than what is specified on this record.  A zero indicates the width is prompted.  A one indicates the width specified on this record is the value used.  """  
      self.PkgMtlTypeCode:str = obj["PkgMtlTypeCode"]
      """  Unique package material type code assigned by the user.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the record is active or not. Default is true.  """  
      self.EnableInactive:bool = obj["EnableInactive"]
      """  Flag to be used internally for row rules for whether to allow the Packing Code to be set to inactive.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PackingMtlTypePkgMtlTypeCodeDesc:str = obj["PackingMtlTypePkgMtlTypeCodeDesc"]
      self.PackingTypePkgTypeDesc:str = obj["PackingTypePkgTypeDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingShipToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ShipToSeq:int = obj["ShipToSeq"]
      """  ShipToSeq  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      """  The ship to specified container part ID.  """  
      self.ShipToContainerPartDesc:str = obj["ShipToContainerPartDesc"]
      """  The ship to specified container part description.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      """  Holds "~" delimited name and address data from the ShipTo record.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      self.CustID:str = obj["CustID"]
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      """  The name and address data from the ShipTo record formatted.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.ShipToName:str = obj["ShipToName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackingTableset:
   def __init__(self, obj):
      self.Packing:list[Erp_Tablesets_PackingRow] = obj["Packing"]
      self.PackingPlant:list[Erp_Tablesets_PackingPlantRow] = obj["PackingPlant"]
      self.PackingShipTo:list[Erp_Tablesets_PackingShipToRow] = obj["PackingShipTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPackingTableset:
   def __init__(self, obj):
      self.Packing:list[Erp_Tablesets_PackingRow] = obj["Packing"]
      self.PackingPlant:list[Erp_Tablesets_PackingPlantRow] = obj["PackingPlant"]
      self.PackingShipTo:list[Erp_Tablesets_PackingShipToRow] = obj["PackingShipTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   pkgCode
   """  
   def __init__(self, obj):
      self.pkgCode:str = obj["pkgCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PackingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PackingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PackingListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPackingPlant_input:
   """ Required : 
   ds
   pkgCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      self.pkgCode:str = obj["pkgCode"]
      pass

class GetNewPackingPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPackingShipTo_input:
   """ Required : 
   ds
   pkgCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      self.pkgCode:str = obj["pkgCode"]
      pass

class GetNewPackingShipTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPacking_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

class GetNewPacking_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackingByPart_input:
   """ Required : 
   packingPlantWhereClause
   """  
   def __init__(self, obj):
      self.packingPlantWhereClause:str = obj["packingPlantWhereClause"]
      pass

class GetPackingByPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackingListTableset] = obj["returnObj"]
      pass

class GetPackingList_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      pass

class GetPackingList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackingListTableset] = obj["returnObj"]
      pass

class GetPackingRecords_input:
   """ Required : 
   pkgWClause
   pkgPlantWClause
   pkgShipToWClause
   table
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.pkgWClause:str = obj["pkgWClause"]
      self.pkgPlantWClause:str = obj["pkgPlantWClause"]
      self.pkgShipToWClause:str = obj["pkgShipToWClause"]
      self.table:str = obj["table"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPackingRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackingTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePacking
   whereClausePackingPlant
   whereClausePackingShipTo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePacking:str = obj["whereClausePacking"]
      self.whereClausePackingPlant:str = obj["whereClausePackingPlant"]
      self.whereClausePackingShipTo:str = obj["whereClausePackingShipTo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackingTableset] = obj["returnObj"]
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

class OnChangeCustomerCustID_input:
   """ Required : 
   ipCustId
   ds
   """  
   def __init__(self, obj):
      self.ipCustId:str = obj["ipCustId"]
      """  The Customer ID  """  
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

class OnChangeCustomerCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeShipToID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

class OnChangeShipToID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPackingTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPackingTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PackingTableset] = obj["ds"]
      pass

      """  output parameters  """  

