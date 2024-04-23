import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WarehseSvc
# Description: Warehouse BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Warehses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Warehses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Warehses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WarehseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses",headers=creds) as resp:
           return await resp.json()

async def post_Warehses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Warehses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WarehseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WarehseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode(Company, WarehouseCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Warehse item
   Description: Calls GetByID to retrieve the Warehse item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Warehse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WarehseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Warehses_Company_WarehouseCode(Company, WarehouseCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Warehse for the service
   Description: Calls UpdateExt to update Warehse. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Warehse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WarehseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Warehses_Company_WarehouseCode(Company, WarehouseCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Warehse item
   Description: Call UpdateExt to delete Warehse item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Warehse
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_EntityGLCs(Company, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, WarehouseCode, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_WhsePrinters(Company, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhsePrinters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhsePrinters1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhsePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/WhsePrinters",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_WhsePrinters_Company_WarehouseCode_PrinterID(Company, WarehouseCode, PrinterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhsePrinter item
   Description: Calls GetByID to retrieve the WhsePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhsePrinter1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhsePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/WhsePrinters(" + Company + "," + WarehouseCode + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_WarehseABCs(Company, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WarehseABCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WarehseABCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WarehseABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/WarehseABCs",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_WarehseABCs_Company_WarehouseCode_ABCCode(Company, WarehouseCode, ABCCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WarehseABC item
   Description: Calls GetByID to retrieve the WarehseABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WarehseABC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WarehseABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/WarehseABCs(" + Company + "," + WarehouseCode + "," + ABCCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_WarehseAttches(Company, WarehouseCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WarehseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WarehseAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WarehseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/WarehseAttches",headers=creds) as resp:
           return await resp.json()

async def get_Warehses_Company_WarehouseCode_WarehseAttches_Company_WarehouseCode_DrawingSeq(Company, WarehouseCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WarehseAttch item
   Description: Calls GetByID to retrieve the WarehseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WarehseAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WarehseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/Warehses(" + Company + "," + WarehouseCode + ")/WarehseAttches(" + Company + "," + WarehouseCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhsePrinters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhsePrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhsePrinters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WhsePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WhsePrinters",headers=creds) as resp:
           return await resp.json()

async def post_WhsePrinters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhsePrinters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WhsePrinterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WhsePrinterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WhsePrinters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhsePrinters_Company_WarehouseCode_PrinterID(Company, WarehouseCode, PrinterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhsePrinter item
   Description: Calls GetByID to retrieve the WhsePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhsePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WhsePrinterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WhsePrinters(" + Company + "," + WarehouseCode + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhsePrinters_Company_WarehouseCode_PrinterID(Company, WarehouseCode, PrinterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhsePrinter for the service
   Description: Calls UpdateExt to update WhsePrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhsePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WhsePrinterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WhsePrinters(" + Company + "," + WarehouseCode + "," + PrinterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhsePrinters_Company_WarehouseCode_PrinterID(Company, WarehouseCode, PrinterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhsePrinter item
   Description: Call UpdateExt to delete WhsePrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhsePrinter
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param PrinterID: Desc: PrinterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WhsePrinters(" + Company + "," + WarehouseCode + "," + PrinterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WarehseABCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WarehseABCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WarehseABCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WarehseABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseABCs",headers=creds) as resp:
           return await resp.json()

async def post_WarehseABCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WarehseABCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WarehseABCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WarehseABCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseABCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WarehseABCs_Company_WarehouseCode_ABCCode(Company, WarehouseCode, ABCCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WarehseABC item
   Description: Calls GetByID to retrieve the WarehseABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WarehseABC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WarehseABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseABCs(" + Company + "," + WarehouseCode + "," + ABCCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WarehseABCs_Company_WarehouseCode_ABCCode(Company, WarehouseCode, ABCCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WarehseABC for the service
   Description: Calls UpdateExt to update WarehseABC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WarehseABC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WarehseABCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseABCs(" + Company + "," + WarehouseCode + "," + ABCCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WarehseABCs_Company_WarehouseCode_ABCCode(Company, WarehouseCode, ABCCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WarehseABC item
   Description: Call UpdateExt to delete WarehseABC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WarehseABC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseABCs(" + Company + "," + WarehouseCode + "," + ABCCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_WarehseAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WarehseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WarehseAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WarehseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseAttches",headers=creds) as resp:
           return await resp.json()

async def post_WarehseAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WarehseAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WarehseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WarehseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WarehseAttches_Company_WarehouseCode_DrawingSeq(Company, WarehouseCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WarehseAttch item
   Description: Calls GetByID to retrieve the WarehseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WarehseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WarehseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseAttches(" + Company + "," + WarehouseCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WarehseAttches_Company_WarehouseCode_DrawingSeq(Company, WarehouseCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WarehseAttch for the service
   Description: Calls UpdateExt to update WarehseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WarehseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WarehseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseAttches(" + Company + "," + WarehouseCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WarehseAttches_Company_WarehouseCode_DrawingSeq(Company, WarehouseCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WarehseAttch item
   Description: Call UpdateExt to delete WarehseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WarehseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/WarehseAttches(" + Company + "," + WarehouseCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WarehseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWarehse, whereClauseWarehseAttch, whereClauseEntityGLC, whereClauseWhsePrinter, whereClauseWarehseABC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseWarehse=" + whereClauseWarehse
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWarehseAttch=" + whereClauseWarehseAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhsePrinter=" + whereClauseWhsePrinter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWarehseABC=" + whereClauseWarehseABC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(warehouseCode, epicorHeaders = None):
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
   params += "warehouseCode=" + warehouseCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlant
   Description: This method is used to verify Plant on current Warehouse.
   OperationID: CheckPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckWhseBin
   Description: This method is used to verify that a bin exists for the current warehouse.  It should be
called before exiting Warehouse Maintenance or before selecting a different
warehouse.  If a bin doesn't exist for the current warehouse then a message will be returned
in the output parameter opMessage.  If opMessage isn't null then the message should be displayed
to the user and they shouldn't be allowed to exit Warehouse maintenance or select a different
warehouse until a bin is added.
   OperationID: CheckWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckWhseBinFullMessage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckWhseBinFullMessage
   Description: Do the same validation as CheckWhseBin but return the full message instead of completing it in client code.
   OperationID: CheckWhseBinFullMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckWhseBinFullMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckWhseBinFullMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ETCAfterAddrVal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ETCAfterAddrVal
   Description: After the tax integration has been called, update the WareHse address if it
was changed.
   OperationID: ETCAfterAddrVal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCAfterAddrVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCAfterAddrVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ETCValidateAddress(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ETCValidateAddress
   Description: Call tax integration and loads temp tables from the results.
   OperationID: ETCValidateAddress
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ETCValidateAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCValidateAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListNoActiveCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListNoActiveCount
   Description: Filter warehouses that do not have an active cycle count or physical inventory.  Call normal GetList method.
   OperationID: GetListNoActiveCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListNoActiveCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListNoActiveCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfAbcCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfAbcCode
   OperationID: OnChangeOfAbcCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfAbcCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfAbcCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfCountFreq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfCountFreq
   OperationID: OnChangeOfCountFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfCountFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCountFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfPcntTolerance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfPcntTolerance
   OperationID: OnChangeOfPcntTolerance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfPcntTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfPcntTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfQtyTolerance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfQtyTolerance
   OperationID: OnChangeOfQtyTolerance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfQtyTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfQtyTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfStockValPcnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfStockValPcnt
   Description: execute this code if Stock Valuation column changes
   OperationID: OnChangeOfStockValPcnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfStockValPcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfStockValPcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfValueTolerance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfValueTolerance
   OperationID: OnChangeOfValueTolerance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfValueTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfValueTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePrinterID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePrinterID
   Description: Handles behavior when the Printer ID in Warehse changes.
   OperationID: OnChangePrinterID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePrinterID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePrinterID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckOtherWarehouseTypeDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckOtherWarehouseTypeDefaults
   Description: Check If Other Defaults Warehouse Of This Type Exist For Plant
   OperationID: CheckOtherWarehouseTypeDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckOtherWarehouseTypeDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckOtherWarehouseTypeDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshHasBins(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshHasBins
   Description: This method will refresh the bin status for each warehouse. The Warehouse can be passed
in as a parameter or if left blank, the bin status will be returned for all warehouses
of a company
   OperationID: RefreshHasBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshHasBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshHasBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWarehse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWarehse
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWarehse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWarehse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWarehse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWarehseAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWarehseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWarehseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWarehseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWarehseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhsePrinter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhsePrinter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhsePrinter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhsePrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhsePrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWarehseABC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWarehseABC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWarehseABC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWarehseABC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWarehseABC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WarehseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WarehseABCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WarehseABCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WarehseAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WarehseAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WarehseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WarehseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WarehseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WarehseRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WhsePrinterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WhsePrinterRow] = obj["value"]
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WarehseABCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.OvrrideCountFreq:bool = obj["OvrrideCountFreq"]
      """  This flag indicates whether the CountFreq defined in this record should over ride the count frequency in the AbcCode or SiteConfABC tables.  """  
      self.CountFreq:int = obj["CountFreq"]
      """  This setting overrides values in AbcCode and/or SiteConfABC  """  
      self.ExcludeFromCC:bool = obj["ExcludeFromCC"]
      """  This flag is set to true prevent parts that should only be counted during physical inventory from being selected for cycle counting This setting overrides values in AbcCode and/or SiteConfABC  """  
      self.StockValPcnt:int = obj["StockValPcnt"]
      """  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting overrides values in AbcCode and/or SiteConfABC  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, or PartSite. Zero indicates that any quantity variance is considered out of tolerance. A number g  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  """  
      self.OvrrideStockValPcnt:bool = obj["OvrrideStockValPcnt"]
      """  This flag indicates whether the StockValPcnt defined in this record should over ride the value in the AbcCode or SiteConfABC tables.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.PartsAssigned:int = obj["PartsAssigned"]
      """  The number of parts in this warehouse that are assigned to this ABC code. Set by Calculate ABC and used by the random selection method to determine the default for the number of parts to select for this ABC code for the month.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, or PartSite. Zero indicates that any quantity variance is considered out of tolerance. A  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, or PartSite.  An entry of zero will indicate that any value variance will be considered out of toleranc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WarehseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
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

class Erp_Tablesets_WarehseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WarehseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.Name:str = obj["Name"]
      """  Shipping name for the Warehouse. Used by PO entry. Each warehouse has its own name, address, city, state, zip and country fields which override the info found in the company master.  Think of them like customer's ship to's or vendor purchase points except they are for the users company.  Purchase Order entry uses these to  provide a different Ship to address than the one found in the Company master.  These are not mandatory, can be left blank. PO entry only uses these if the Name field is not blank otherwise it will use the info from the Company master.  """  
      self.Address1:str = obj["Address1"]
      """  Shipping Address for the warehouse. Used by PO entry.  """  
      self.Address2:str = obj["Address2"]
      """  Shipping Address for the warehouse. Used by PO entry.  """  
      self.Address3:str = obj["Address3"]
      """  Shipping Address for the warehouse. Used by PO entry.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Provinence  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.GLDivision:str = obj["GLDivision"]
      """  The G/L Division to be used for activity in this warehouse.  This can be left blank or must be valid in the GLDiv master.  When filled in, the system will attempt to use it in constructing a G/L account number for transactions that affect inventory.  If this combination yields a valid GL account (if combination exists in GLAcct and GLAcct.Active = yes) then it is used.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the Warehse.Country value.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCSelectMethod:int = obj["CCSelectMethod"]
      """   Defines what method will be used to automatically select parts for cycle counting. This will override any value in SiteConfCtrl.CCSelectMethod.
Default = 0
Code/Desc:
0 = Use Site Config
1 = Repetitive, 2 = Random.  """  
      self.ExcludeInactive:bool = obj["ExcludeInactive"]
      """  Indicates whether to exclude inactive parts in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.ExcludeOnHold:bool = obj["ExcludeOnHold"]
      """  Indicates whether to exclude part that are on hold in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.ExcludeZeroQOH:bool = obj["ExcludeZeroQOH"]
      """  Indicates whether to exclude parts with zero QOH in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.ExcludeNegQOH:bool = obj["ExcludeNegQOH"]
      """  Indicates whether to exclude parts with negative QOH in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.LastSheetNum:int = obj["LastSheetNum"]
      """  The last number used as a sheet number when generating cycle count tags for this warehouse.  """  
      self.LastTagNum:int = obj["LastTagNum"]
      """  Last tag number generated for this warehouse. To keep tag numbers unique for a warehouse so count tag historical data can be retained.  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Name of the person who makes stock issue  """  
      self.DefRcvWhse:str = obj["DefRcvWhse"]
      """  Default receiving warehouse. Used as default in receipt entry, can be the same id as warehouse.  If left blank the default from SiteConfCtrl will be used  """  
      self.DefRcvBin:str = obj["DefRcvBin"]
      """  Default receiving bin Used as default in receipt entry.  If left blank the default from SiteConfCtrl will be used  """  
      self.DefShipWhse:str = obj["DefShipWhse"]
      """  Default shipping warehouse. Used as default in shipment entry.  Not currently used  If left blank the default from SiteConfCtrl will be used  """  
      self.DefShipBin:str = obj["DefShipBin"]
      """  Default shipping bin. Used as default in shipping entry. Not currently used  If left blank the default from SiteConfCtrl will be used  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the warehouse.  Not currently used  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the warehouse.  Not currently used  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode contact Not currently used  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnforcePkgControlRules:bool = obj["EnforcePkgControlRules"]
      """  Indicates if Package Control Rules are enforced within the warehouse.  """  
      self.AllowBuildParent:bool = obj["AllowBuildParent"]
      """  Indicates if the building of parent PCIDs will be allowed within the warehouse.  """  
      self.IsHoldWarehouse:bool = obj["IsHoldWarehouse"]
      """  Indicates if the warehouse is designated as a Hold Warehouse.  """  
      self.WarehouseType:str = obj["WarehouseType"]
      """  Indicates the Warehouse Type. Valid values: Quality, WIP, Stock.  """  
      self.WarehouseTypeDefault:bool = obj["WarehouseTypeDefault"]
      """  Indicates if this warehouse is the default warehouse for the warehouse type.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warehouse has to be synchronized with Epicor FSA application.  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.HasBins:bool = obj["HasBins"]
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PlantSendToFSA:bool = obj["PlantSendToFSA"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WhsePrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode  """  
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID  """  
      self.IsDefaultPrinter:bool = obj["IsDefaultPrinter"]
      """  IsDefaultPrinter  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  DisplaySeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SysPrinterDescription:str = obj["SysPrinterDescription"]
      self.SysPrinterNetworkPath:str = obj["SysPrinterNetworkPath"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckOtherWarehouseTypeDefaults_input:
   """ Required : 
   WarehouseCode
   PlantID
   WarehouseType
   """  
   def __init__(self, obj):
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode  """  
      self.PlantID:str = obj["PlantID"]
      """  PlantID  """  
      self.WarehouseType:str = obj["WarehouseType"]
      """  WarehouseType  """  
      pass

class CheckOtherWarehouseTypeDefaults_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class CheckPlant_input:
   """ Required : 
   ipWarehouseCode
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Current Warehouse Code  """  
      pass

class CheckPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckWhseBinFullMessage_input:
   """ Required : 
   ipWarehouseCode
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Current Warehouse Code  """  
      pass

class CheckWhseBinFullMessage_output:
   def __init__(self, obj):
      pass

class CheckWhseBin_input:
   """ Required : 
   ipWarehouseCode
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Current Warehouse Code  """  
      pass

class CheckWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   warehouseCode
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class ETCAfterAddrVal_input:
   """ Required : 
   ds
   ds1
   wareHouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["ds1"]
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  WareHse.WareHouseCode  """  
      pass

class ETCAfterAddrVal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ETCValidateAddress_input:
   """ Required : 
   wareHouseCode
   """  
   def __init__(self, obj):
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  WareHse.WareHouseCode  """  
      pass

class ETCValidateAddress_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ETCAddrValidationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.statusFlag:bool = obj["statusFlag"]
      self.errorFlag:bool = obj["errorFlag"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_ETCAddrValidationTableset:
   def __init__(self, obj):
      self.ETCAddress:list[Erp_Tablesets_ETCAddressRow] = obj["ETCAddress"]
      self.ETCMessage:list[Erp_Tablesets_ETCMessageRow] = obj["ETCMessage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ETCAddressRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.City:str = obj["City"]
      """  City name  """  
      self.Country:str = obj["Country"]
      """  Country name  """  
      self.Line1:str = obj["Line1"]
      """  Address line 1  """  
      self.Line2:str = obj["Line2"]
      """  Address line 2  """  
      self.Line3:str = obj["Line3"]
      """  Address line 3  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal or ZIP code  """  
      self.Region:str = obj["Region"]
      """  State or province name  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.UpdateAddr:bool = obj["UpdateAddr"]
      """  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  """  
      self.UpdateAllowed:bool = obj["UpdateAllowed"]
      """  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  """  
      self.RequestID:str = obj["RequestID"]
      """  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  """  
      self.AddressCode:str = obj["AddressCode"]
      """  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  """  
      self.AddressType:str = obj["AddressType"]
      """  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  """  
      self.CarrierRoute:str = obj["CarrierRoute"]
      """  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  """  
      self.ValidCity:str = obj["ValidCity"]
      """  City name  """  
      self.ValidCountry:str = obj["ValidCountry"]
      """  Country name  """  
      self.County:str = obj["County"]
      """  County name  """  
      self.FipsCode:str = obj["FipsCode"]
      """  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  """  
      self.ValidLine1:str = obj["ValidLine1"]
      """  Line one of the valid address returned by the tax integration.  """  
      self.ValidLine2:str = obj["ValidLine2"]
      """  Line two of the valid address returned by the tax integration.  """  
      self.ValidLine3:str = obj["ValidLine3"]
      """  Line three of the valid address returned by the tax integration.  """  
      self.ValidLine4:str = obj["ValidLine4"]
      """  Line four of the valid address returned by the tax integration.  """  
      self.ValidPostalCode:str = obj["ValidPostalCode"]
      """  Postal code returned by the tax integration.  """  
      self.PostNet:str = obj["PostNet"]
      """  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  """  
      self.ValidRegion:str = obj["ValidRegion"]
      """  State or province name or abbreviation returned by the tax integration.  """  
      self.ResultCode:str = obj["ResultCode"]
      """  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.ResultSeq:int = obj["ResultSeq"]
      """  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  """  
      self.CarrierRouteDesc:str = obj["CarrierRouteDesc"]
      """  Carrier Route description  """  
      self.AddressTypeDesc:str = obj["AddressTypeDesc"]
      """  Address type description  """  
      self.OTSCountry:str = obj["OTSCountry"]
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Foreign key to the InvcHead.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  """  
      self.ACWPercentage:int = obj["ACWPercentage"]
      """   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ETCMessageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Details:str = obj["Details"]
      self.Helplink:str = obj["Helplink"]
      """  URL to help page for this message  """  
      self.Name:str = obj["Name"]
      """  Gets the name of the message  """  
      self.RefersTo:str = obj["RefersTo"]
      """  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  """  
      self.Severity:str = obj["Severity"]
      """  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  """  
      self.Source:str = obj["Source"]
      """  source of the message  """  
      self.Summary:str = obj["Summary"]
      """  concise summary of the message  """  
      self.TransactionID:str = obj["TransactionID"]
      """  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  """  
      self.AddrSource:str = obj["AddrSource"]
      """  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  """  
      self.AddrSourceID:str = obj["AddrSourceID"]
      """  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  """  
      self.RequestID:str = obj["RequestID"]
      """  Programitically assigned.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtWarehseTableset:
   def __init__(self, obj):
      self.Warehse:list[Erp_Tablesets_WarehseRow] = obj["Warehse"]
      self.WarehseAttch:list[Erp_Tablesets_WarehseAttchRow] = obj["WarehseAttch"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.WhsePrinter:list[Erp_Tablesets_WhsePrinterRow] = obj["WhsePrinter"]
      self.WarehseABC:list[Erp_Tablesets_WarehseABCRow] = obj["WarehseABC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WarehseABCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.OvrrideCountFreq:bool = obj["OvrrideCountFreq"]
      """  This flag indicates whether the CountFreq defined in this record should over ride the count frequency in the AbcCode or SiteConfABC tables.  """  
      self.CountFreq:int = obj["CountFreq"]
      """  This setting overrides values in AbcCode and/or SiteConfABC  """  
      self.ExcludeFromCC:bool = obj["ExcludeFromCC"]
      """  This flag is set to true prevent parts that should only be counted during physical inventory from being selected for cycle counting This setting overrides values in AbcCode and/or SiteConfABC  """  
      self.StockValPcnt:int = obj["StockValPcnt"]
      """  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting overrides values in AbcCode and/or SiteConfABC  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, or PartSite. Zero indicates that any quantity variance is considered out of tolerance. A number g  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  """  
      self.OvrrideStockValPcnt:bool = obj["OvrrideStockValPcnt"]
      """  This flag indicates whether the StockValPcnt defined in this record should over ride the value in the AbcCode or SiteConfABC tables.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.PartsAssigned:int = obj["PartsAssigned"]
      """  The number of parts in this warehouse that are assigned to this ABC code. Set by Calculate ABC and used by the random selection method to determine the default for the number of parts to select for this ABC code for the month.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, or PartSite. Zero indicates that any quantity variance is considered out of tolerance. A  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, or PartSite.  An entry of zero will indicate that any value variance will be considered out of toleranc  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WarehseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
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

class Erp_Tablesets_WarehseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WarehseListTableset:
   def __init__(self, obj):
      self.WarehseList:list[Erp_Tablesets_WarehseListRow] = obj["WarehseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WarehseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.Name:str = obj["Name"]
      """  Shipping name for the Warehouse. Used by PO entry. Each warehouse has its own name, address, city, state, zip and country fields which override the info found in the company master.  Think of them like customer's ship to's or vendor purchase points except they are for the users company.  Purchase Order entry uses these to  provide a different Ship to address than the one found in the Company master.  These are not mandatory, can be left blank. PO entry only uses these if the Name field is not blank otherwise it will use the info from the Company master.  """  
      self.Address1:str = obj["Address1"]
      """  Shipping Address for the warehouse. Used by PO entry.  """  
      self.Address2:str = obj["Address2"]
      """  Shipping Address for the warehouse. Used by PO entry.  """  
      self.Address3:str = obj["Address3"]
      """  Shipping Address for the warehouse. Used by PO entry.  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Provinence  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country  """  
      self.GLDivision:str = obj["GLDivision"]
      """  The G/L Division to be used for activity in this warehouse.  This can be left blank or must be valid in the GLDiv master.  When filled in, the system will attempt to use it in constructing a G/L account number for transactions that affect inventory.  If this combination yields a valid GL account (if combination exists in GLAcct and GLAcct.Active = yes) then it is used.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the Warehse.Country value.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCSelectMethod:int = obj["CCSelectMethod"]
      """   Defines what method will be used to automatically select parts for cycle counting. This will override any value in SiteConfCtrl.CCSelectMethod.
Default = 0
Code/Desc:
0 = Use Site Config
1 = Repetitive, 2 = Random.  """  
      self.ExcludeInactive:bool = obj["ExcludeInactive"]
      """  Indicates whether to exclude inactive parts in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.ExcludeOnHold:bool = obj["ExcludeOnHold"]
      """  Indicates whether to exclude part that are on hold in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.ExcludeZeroQOH:bool = obj["ExcludeZeroQOH"]
      """  Indicates whether to exclude parts with zero QOH in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.ExcludeNegQOH:bool = obj["ExcludeNegQOH"]
      """  Indicates whether to exclude parts with negative QOH in cycle count selection. This can be overridden at the time of monthly selection.  """  
      self.LastSheetNum:int = obj["LastSheetNum"]
      """  The last number used as a sheet number when generating cycle count tags for this warehouse.  """  
      self.LastTagNum:int = obj["LastTagNum"]
      """  Last tag number generated for this warehouse. To keep tag numbers unique for a warehouse so count tag historical data can be retained.  """  
      self.ManagerName:str = obj["ManagerName"]
      """  Name of the person who makes stock issue  """  
      self.DefRcvWhse:str = obj["DefRcvWhse"]
      """  Default receiving warehouse. Used as default in receipt entry, can be the same id as warehouse.  If left blank the default from SiteConfCtrl will be used  """  
      self.DefRcvBin:str = obj["DefRcvBin"]
      """  Default receiving bin Used as default in receipt entry.  If left blank the default from SiteConfCtrl will be used  """  
      self.DefShipWhse:str = obj["DefShipWhse"]
      """  Default shipping warehouse. Used as default in shipment entry.  Not currently used  If left blank the default from SiteConfCtrl will be used  """  
      self.DefShipBin:str = obj["DefShipBin"]
      """  Default shipping bin. Used as default in shipping entry. Not currently used  If left blank the default from SiteConfCtrl will be used  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The business phone number for the warehouse.  Not currently used  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The fax number for the warehouse.  Not currently used  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep.SalesRepCode contact Not currently used  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnforcePkgControlRules:bool = obj["EnforcePkgControlRules"]
      """  Indicates if Package Control Rules are enforced within the warehouse.  """  
      self.AllowBuildParent:bool = obj["AllowBuildParent"]
      """  Indicates if the building of parent PCIDs will be allowed within the warehouse.  """  
      self.IsHoldWarehouse:bool = obj["IsHoldWarehouse"]
      """  Indicates if the warehouse is designated as a Hold Warehouse.  """  
      self.WarehouseType:str = obj["WarehouseType"]
      """  Indicates the Warehouse Type. Valid values: Quality, WIP, Stock.  """  
      self.WarehouseTypeDefault:bool = obj["WarehouseTypeDefault"]
      """  Indicates if this warehouse is the default warehouse for the warehouse type.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the warehouse has to be synchronized with Epicor FSA application.  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  CNBonded  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.HasBins:bool = obj["HasBins"]
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PlantSendToFSA:bool = obj["PlantSendToFSA"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WarehseTableset:
   def __init__(self, obj):
      self.Warehse:list[Erp_Tablesets_WarehseRow] = obj["Warehse"]
      self.WarehseAttch:list[Erp_Tablesets_WarehseAttchRow] = obj["WarehseAttch"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.WhsePrinter:list[Erp_Tablesets_WhsePrinterRow] = obj["WhsePrinter"]
      self.WarehseABC:list[Erp_Tablesets_WarehseABCRow] = obj["WarehseABC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WhsePrinterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode  """  
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID  """  
      self.IsDefaultPrinter:bool = obj["IsDefaultPrinter"]
      """  IsDefaultPrinter  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  DisplaySeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SysPrinterDescription:str = obj["SysPrinterDescription"]
      self.SysPrinterNetworkPath:str = obj["SysPrinterNetworkPath"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetByID_input:
   """ Required : 
   warehouseCode
   """  
   def __init__(self, obj):
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WarehseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WarehseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WarehseTableset] = obj["returnObj"]
      pass

class GetListNoActiveCount_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Whereclause.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetListNoActiveCount_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WarehseListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WarehseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWarehseABC_input:
   """ Required : 
   ds
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewWarehseABC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWarehseAttch_input:
   """ Required : 
   ds
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewWarehseAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWarehse_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

class GetNewWarehse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhsePrinter_input:
   """ Required : 
   ds
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewWhsePrinter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWarehse
   whereClauseWarehseAttch
   whereClauseEntityGLC
   whereClauseWhsePrinter
   whereClauseWarehseABC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWarehse:str = obj["whereClauseWarehse"]
      self.whereClauseWarehseAttch:str = obj["whereClauseWarehseAttch"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseWhsePrinter:str = obj["whereClauseWhsePrinter"]
      self.whereClauseWarehseABC:str = obj["whereClauseWarehseABC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WarehseTableset] = obj["returnObj"]
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

class OnChangeOfAbcCode_input:
   """ Required : 
   ds
   ipABCCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      self.ipABCCode:str = obj["ipABCCode"]
      """  Warehouse ABC code  """  
      pass

class OnChangeOfAbcCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfCountFreq_input:
   """ Required : 
   ipCountFreq
   ipOvrrideCountFreq
   """  
   def __init__(self, obj):
      self.ipCountFreq:int = obj["ipCountFreq"]
      """  Cycle Count Frequency  """  
      self.ipOvrrideCountFreq:bool = obj["ipOvrrideCountFreq"]
      """  Override count frequency  """  
      pass

class OnChangeOfCountFreq_output:
   def __init__(self, obj):
      pass

class OnChangeOfPcntTolerance_input:
   """ Required : 
   ipPcntTolerance
   """  
   def __init__(self, obj):
      self.ipPcntTolerance:int = obj["ipPcntTolerance"]
      pass

class OnChangeOfPcntTolerance_output:
   def __init__(self, obj):
      pass

class OnChangeOfQtyTolerance_input:
   """ Required : 
   ipQtyTolerance
   """  
   def __init__(self, obj):
      self.ipQtyTolerance:int = obj["ipQtyTolerance"]
      pass

class OnChangeOfQtyTolerance_output:
   def __init__(self, obj):
      pass

class OnChangeOfStockValPcnt_input:
   """ Required : 
   ipStockValPcnt
   """  
   def __init__(self, obj):
      self.ipStockValPcnt:int = obj["ipStockValPcnt"]
      """  Stock Value Percent  """  
      pass

class OnChangeOfStockValPcnt_output:
   def __init__(self, obj):
      pass

class OnChangeOfValueTolerance_input:
   """ Required : 
   ipValTolerance
   """  
   def __init__(self, obj):
      self.ipValTolerance:int = obj["ipValTolerance"]
      pass

class OnChangeOfValueTolerance_output:
   def __init__(self, obj):
      pass

class OnChangePrinterID_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:str = obj["proposedValue"]
      """  New proposed value.  """  
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

class OnChangePrinterID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshHasBins_input:
   """ Required : 
   iplant
   iWarehousecode
   """  
   def __init__(self, obj):
      self.iplant:str = obj["iplant"]
      """  Plant that is to have its bin status refreshed or blank for all plants  """  
      self.iWarehousecode:str = obj["iWarehousecode"]
      """  Warehouse code that is to have its bin status refreshed or blank for all warehouses  """  
      pass

class RefreshHasBins_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WarehseTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWarehseTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWarehseTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WarehseTableset] = obj["ds"]
      pass

      """  output parameters  """  

