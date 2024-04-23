import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PlantConfCtrlSvc
# Description: PlantConfCtrlSvc BO.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantConfCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfCtrls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls",headers=creds) as resp:
           return await resp.json()

async def post_PlantConfCtrls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfCtrls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant(Company, Plant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfCtrl item
   Description: Calls GetByID to retrieve the PlantConfCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantConfCtrls_Company_Plant(Company, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantConfCtrl for the service
   Description: Calls UpdateExt to update PlantConfCtrl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantConfCtrls_Company_Plant(Company, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantConfCtrl item
   Description: Call UpdateExt to delete PlantConfCtrl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfCtrl
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantConfCtrlEGLCs(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantConfCtrlEGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantConfCtrlEGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlEGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, Plant, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfCtrlEGLC item
   Description: Calls GetByID to retrieve the PlantConfCtrlEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlEGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantConfABCs(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantConfABCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantConfABCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfABCs",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantConfABCs_Company_Plant_ABCCode(Company, Plant, ABCCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfABC item
   Description: Calls GetByID to retrieve the PlantConfABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfABC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantMFBills(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantMFBills items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantMFBills1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantMFBills",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantMFBills_Company_Plant_PayBTFlag(Company, Plant, PayBTFlag, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantMFBill item
   Description: Calls GetByID to retrieve the PlantMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantMFBill1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantShareds(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantShareds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantShareds1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantSharedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantShareds",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantShareds_Company_WarehouseCode_Plant(Company, Plant, WarehouseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantShared item
   Description: Calls GetByID to retrieve the PlantShared item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantShared1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlntTranDefs(Company, Plant, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlntTranDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlntTranDefs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlntTranDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlntTranDefs",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlntTranDefs_Company_FromPlant_ToPlant(Company, Plant, FromPlant, ToPlant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlntTranDef item
   Description: Calls GetByID to retrieve the PlntTranDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlntTranDef1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param FromPlant: Desc: FromPlant   Required: True   Allow empty value : True
      :param ToPlant: Desc: ToPlant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PltUPSEmails(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PltUPSEmails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PltUPSEmails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PltUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PltUPSEmails",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PltUPSEmails_Company_Plant_UPSQVSeq(Company, Plant, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PltUPSEmail item
   Description: Calls GetByID to retrieve the PltUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PltUPSEmail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantConfCtrlAttches(Company, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantConfCtrlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantConfCtrlAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlAttches",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrls_Company_Plant_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfCtrlAttch item
   Description: Calls GetByID to retrieve the PlantConfCtrlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrlEGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantConfCtrlEGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfCtrlEGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs",headers=creds) as resp:
           return await resp.json()

async def post_PlantConfCtrlEGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfCtrlEGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfCtrlEGLC item
   Description: Calls GetByID to retrieve the PlantConfCtrlEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlEGLC
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantConfCtrlEGLC for the service
   Description: Calls UpdateExt to update PlantConfCtrlEGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfCtrlEGLC
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
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantConfCtrlEGLC item
   Description: Call UpdateExt to delete PlantConfCtrlEGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfCtrlEGLC
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfABCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantConfABCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfABCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs",headers=creds) as resp:
           return await resp.json()

async def post_PlantConfABCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfABCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantConfABCs_Company_Plant_ABCCode(Company, Plant, ABCCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfABC item
   Description: Calls GetByID to retrieve the PlantConfABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfABC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantConfABCs_Company_Plant_ABCCode(Company, Plant, ABCCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantConfABC for the service
   Description: Calls UpdateExt to update PlantConfABC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfABC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ABCCode: Desc: ABCCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantConfABCs_Company_Plant_ABCCode(Company, Plant, ABCCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantConfABC item
   Description: Call UpdateExt to delete PlantConfABC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfABC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantMFBills(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantMFBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantMFBills
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills",headers=creds) as resp:
           return await resp.json()

async def post_PlantMFBills(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantMFBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantMFBills_Company_Plant_PayBTFlag(Company, Plant, PayBTFlag, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantMFBill item
   Description: Calls GetByID to retrieve the PlantMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantMFBills_Company_Plant_PayBTFlag(Company, Plant, PayBTFlag, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantMFBill for the service
   Description: Calls UpdateExt to update PlantMFBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantMFBills_Company_Plant_PayBTFlag(Company, Plant, PayBTFlag, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantMFBill item
   Description: Call UpdateExt to delete PlantMFBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantShareds(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantShareds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantShareds
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantSharedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds",headers=creds) as resp:
           return await resp.json()

async def post_PlantShareds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantShareds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantShareds_Company_WarehouseCode_Plant(Company, WarehouseCode, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantShared item
   Description: Calls GetByID to retrieve the PlantShared item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantShared
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantShareds_Company_WarehouseCode_Plant(Company, WarehouseCode, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantShared for the service
   Description: Calls UpdateExt to update PlantShared. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantShared
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantShareds_Company_WarehouseCode_Plant(Company, WarehouseCode, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantShared item
   Description: Call UpdateExt to delete PlantShared item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantShared
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlntTranDefs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlntTranDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlntTranDefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlntTranDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs",headers=creds) as resp:
           return await resp.json()

async def post_PlntTranDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlntTranDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlntTranDefs_Company_FromPlant_ToPlant(Company, FromPlant, ToPlant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlntTranDef item
   Description: Calls GetByID to retrieve the PlntTranDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlntTranDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FromPlant: Desc: FromPlant   Required: True   Allow empty value : True
      :param ToPlant: Desc: ToPlant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlntTranDefs_Company_FromPlant_ToPlant(Company, FromPlant, ToPlant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlntTranDef for the service
   Description: Calls UpdateExt to update PlntTranDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlntTranDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FromPlant: Desc: FromPlant   Required: True   Allow empty value : True
      :param ToPlant: Desc: ToPlant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlntTranDefs_Company_FromPlant_ToPlant(Company, FromPlant, ToPlant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlntTranDef item
   Description: Call UpdateExt to delete PlntTranDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlntTranDef
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FromPlant: Desc: FromPlant   Required: True   Allow empty value : True
      :param ToPlant: Desc: ToPlant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlntTranDefs_Company_FromPlant_ToPlant_EntityGLCs(Company, FromPlant, ToPlant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FromPlant: Desc: FromPlant   Required: True   Allow empty value : True
      :param ToPlant: Desc: ToPlant   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PlntTranDefs_Company_FromPlant_ToPlant_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, FromPlant, ToPlant, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FromPlant: Desc: FromPlant   Required: True   Allow empty value : True
      :param ToPlant: Desc: ToPlant   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PltUPSEmails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PltUPSEmails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PltUPSEmails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PltUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails",headers=creds) as resp:
           return await resp.json()

async def post_PltUPSEmails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PltUPSEmails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PltUPSEmails_Company_Plant_UPSQVSeq(Company, Plant, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PltUPSEmail item
   Description: Calls GetByID to retrieve the PltUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PltUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PltUPSEmails_Company_Plant_UPSQVSeq(Company, Plant, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PltUPSEmail for the service
   Description: Calls UpdateExt to update PltUPSEmail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PltUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PltUPSEmails_Company_Plant_UPSQVSeq(Company, Plant, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PltUPSEmail item
   Description: Call UpdateExt to delete PltUPSEmail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PltUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrlAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantConfCtrlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfCtrlAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches",headers=creds) as resp:
           return await resp.json()

async def post_PlantConfCtrlAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfCtrlAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantConfCtrlAttch item
   Description: Calls GetByID to retrieve the PlantConfCtrlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantConfCtrlAttch for the service
   Description: Calls UpdateExt to update PlantConfCtrlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfCtrlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company, Plant, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantConfCtrlAttch item
   Description: Call UpdateExt to delete PlantConfCtrlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfCtrlAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePlantConfCtrl, whereClausePlantConfCtrlAttch, whereClausePlantConfABC, whereClausePlantMFBill, whereClausePlantShared, whereClausePlntTranDef, whereClauseEntityGLC, whereClausePltUPSEmail, whereClausePlantConfCtrlEGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePlantConfCtrl=" + whereClausePlantConfCtrl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantConfCtrlAttch=" + whereClausePlantConfCtrlAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantConfABC=" + whereClausePlantConfABC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantMFBill=" + whereClausePlantMFBill
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantShared=" + whereClausePlantShared
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlntTranDef=" + whereClausePlntTranDef
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
   params += "whereClausePltUPSEmail=" + whereClausePltUPSEmail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantConfCtrlEGLC=" + whereClausePlantConfCtrlEGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, epicorHeaders = None):
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
   params += "plant=" + plant

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CustomGetNewPlantShared(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomGetNewPlantShared
   Description: Logic for new PlantShared
   OperationID: CustomGetNewPlantShared
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetNewPlantShared_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetNewPlantShared_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckApprovalDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckApprovalDefaults
   Description: Checks if a workflow group already exists for any of the selected options.
If yes, returns a message asking if the defaults should be rebuilt
   OperationID: CheckApprovalDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckApprovalDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckApprovalDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateApprovalDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateApprovalDefaults
   Description: Creates default records needed for time and expense approvals.
   OperationID: CreateApprovalDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateApprovalDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateApprovalDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCompleteList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCompleteList
   Description: This method is the same as GetList(), except that it causes a bypass of the call to
removeUnauthorizedRows.  It is to be used only in the situations where the
user is allowed to see Plants for which they are not authorized, such as in
this example from Vantage Help for Multi-Plant Management:
The selection list for Plants will include all Plants for the To option
when creating Plant to Plant transfers. However, when receiving a Plant
to Plant transfer the user must be authorized to the receiving Plant.
   OperationID: GetCompleteList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCompleteList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompleteList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDfltApprTasksParam(epicorHeaders = None):
   """  
   Summary: Invoke method GetDfltApprTasksParam
   Description: Creates a record in the DfltApprTasksParams DataSet so the user can choose
what default tasks are created
   OperationID: GetDfltApprTasksParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDfltApprTasksParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDisabledFields(epicorHeaders = None):
   """  
   Summary: Invoke method GetDisabledFields
   Description: This method will send a list of fields to be disabled on the UI
side if either the Multi-Plant or Advanced Planning and Scheduling
license is not available or MRP, data collection and field service.
   OperationID: GetDisabledFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisabledFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_IsAuthorizedForPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsAuthorizedForPlant
   Description: IsAuthorizedForPlant
   OperationID: IsAuthorizedForPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAuthorizedForPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAuthorizedForPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfAbcCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfAbcCode
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">PlantConf data set </param><param name="ipABCCode">Plant ABC code</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfCCProdCal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfCCProdCal
   Description: This method validates CCProdCal
   OperationID: OnChangeOfCCProdCal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfCCProdCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCCProdCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfExpenseApprovalReqd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfExpenseApprovalReqd
   Description: This method resets default values when ExpenseApprovalReqd changes
   OperationID: OnChangeOfExpenseApprovalReqd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfExpenseApprovalReqd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfExpenseApprovalReqd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfExpenseRestrictEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfExpenseRestrictEntry
   Description: This method resets default values when ExpenseRestrictEntry changes
   OperationID: OnChangeOfExpenseRestrictEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfExpenseRestrictEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfExpenseRestrictEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLowLvlSerialTrk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLowLvlSerialTrk
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipLLSerTrk">PlantConfCtrl.LowLvlSerialTrk</param><param name="ds">The Plant data set </param>
   OperationID: OnChangeOfLowLvlSerialTrk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLowLvlSerialTrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLowLvlSerialTrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfMaintTmpJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfMaintTmpJobNum
   Description: This method should be called when Equip.TemplateJobNum changes.
   OperationID: OnChangeOfMaintTmpJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfMaintTmpJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfMaintTmpJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEnablePartAllocQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEnablePartAllocQueue
   Description: Invoked when any of the EnablePartAllocQueue flags are changed.
   OperationID: OnChangeEnablePartAllocQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEnablePartAllocQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEnablePartAllocQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfSerialTracking(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfSerialTracking
   Description: This method validates SerialTracking
   OperationID: OnChangeOfSerialTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfSerialTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfStockValPcnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfStockValPcnt
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipStockValPcnt">Stock Value Percent</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfTimeApprovalReqd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfTimeApprovalReqd
   Description: This method resets default values when TimeApprovalReqd changes
   OperationID: OnChangeOfTimeApprovalReqd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfTimeApprovalReqd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTimeApprovalReqd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfTimeRestrictEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfTimeRestrictEntry
   Description: This method resets default values when TimeRestrictEntry changes
   OperationID: OnChangeOfTimeRestrictEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfTimeRestrictEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTimeRestrictEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfValueTolerance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfValueTolerance
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipValTolerance">Value of tolerance</param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResourceTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResourceTransfer
   Description: Plant Resource Transfers allow you to create new plants from the resources available in current plants.
Once resources are moved to a new plant, they are no longer available in their previous plant.
   OperationID: ResourceTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResourceTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResourceTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVEnable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVEnable
   Description: SetUPSQVEnable
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePayBTFlag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePayBTFlag
   Description: ValidatePayBTFlag
   OperationID: ValidatePayBTFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePayBTFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePayBTFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBinContractTypeWarehousesList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBinContractTypeWarehousesList
   Description: Return a generic dataset: datatable(string WarehouseCode, string WarehouseDescription)
List of warehouses with at least a bin of BinType = 'Cont'
   OperationID: GetBinContractTypeWarehousesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBinContractTypeWarehousesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBinContractTypeWarehousesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCWarehouseCode
   Description: Validates PlantConfCtrl.DefPlanContractWhse column changing:
The WarehouseCode field should only allow warehouses with at least one bin location flagged as contract bin.
   OperationID: OnChangePCWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestMachineMESODataConnection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestMachineMESODataConnection
   Description: Tests the connection to Mattec OData
   OperationID: TestMachineMESODataConnection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestMachineMESODataConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestMachineMESODataConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantConfCtrl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantConfCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfCtrl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantConfCtrlAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantConfCtrlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfCtrlAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfCtrlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfCtrlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantConfABC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantConfABC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfABC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfABC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfABC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantMFBill(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantMFBill
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantMFBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantMFBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantMFBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantShared(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantShared
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantShared
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantShared_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantShared_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlntTranDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlntTranDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlntTranDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlntTranDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlntTranDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPltUPSEmail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPltUPSEmail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPltUPSEmail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPltUPSEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPltUPSEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantConfCtrlEGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantConfCtrlEGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfCtrlEGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfCtrlEGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfCtrlEGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfABCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantConfABCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantConfCtrlAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlEGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantConfCtrlEGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantConfCtrlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantConfCtrlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantMFBillRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantMFBillRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantSharedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantSharedRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlntTranDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlntTranDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PltUPSEmailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PltUPSEmailRow] = obj["value"]
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

class Erp_Tablesets_PlantConfABCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.OvrrideCountFreq:bool = obj["OvrrideCountFreq"]
      """  This flag indicates whether the CountFreq defined in this record should over ride the count frequency in the AbcCode table.  """  
      self.CountFreq:int = obj["CountFreq"]
      """  This setting can be overrides AbcCode.CountFreq and can be overridden in WarehseABC.  """  
      self.ExcludeFromCC:bool = obj["ExcludeFromCC"]
      """  This flag is set to true prevent items that should only be counted during physical inventory from being selected for cycle counting. This setting can be overridden in WarehseABC.  """  
      self.StockValPcnt:int = obj["StockValPcnt"]
      """  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting can be overridden in WarehseABC.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of tolerance  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  """  
      self.OvrrideStockValPcnt:bool = obj["OvrrideStockValPcnt"]
      """  This flag indicates whether the StockValPcnt defined in this record should over ride the count frequency in the AbcCode table.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, or WarehseABC.  An entry of zero will indicate that any value variance will be considered out  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
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

class Erp_Tablesets_PlantConfCtrlEGLCRow:
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
      self.Plant:str = obj["Plant"]
      """  Plant for PlantConfCtrl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name.  """  
      self.DefaultWhse:str = obj["DefaultWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default warehouse for this Site.  """  
      self.MRPLastRunDate:str = obj["MRPLastRunDate"]
      """  System date on which the last MRP processing was run.  """  
      self.MRPLastRunTime:int = obj["MRPLastRunTime"]
      """  System Time (hr-min-sec) when the last MRP process was run.  """  
      self.DefInspWhse:str = obj["DefInspWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default inspection warehouse for this Site.  """  
      self.CalcIdleTime:bool = obj["CalcIdleTime"]
      """  Indicates if Labor Collection should calculate Idle time.  Idle time is the time that the employee is getting paid for but is not doing any direct or Indirect labor activity.  The Labor Collection will automatically generate an Indirect detail record to capture these hours if this flag is set to "Yes".  If this is "yes" then the IdleIndirectCode and IdleWCCode must be entered and valid.  """  
      self.IdleResourceGrpID:str = obj["IdleResourceGrpID"]
      """  The ResourceGrpID used by labor collection to create the LaborDtl entry for idle time when CalcIdleTime = Yes. For production labor (LaborType = "S" or "P") the default is from the JobOpDtl.ResourceGrpId from the primary JobOpDtl.  For indirect labor (LaborType = I) there is no default.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  The indirect labor code (Indirect.IndirectCode) that Labor Collection will use when it creates the Idle Time detail record in LaborDtl.  This must be valid if the CalcIdleTime = Yes.  """  
      self.TimeZoneOffset:int = obj["TimeZoneOffset"]
      """  The number of hours (+-) difference from the server time zone to the Site time zone.  Data collection transactions will be offset by this amount.  """  
      self.TimeOffsetSec:int = obj["TimeOffsetSec"]
      """  Related to TimeZoneOffset. Calculated from users entry in TimeZoneOffset, the number of seconds (+-) difference from the server time zone to the Site time zone.   Used for clock in clock out in data collection.  """  
      self.UnfirmJobPrefix:str = obj["UnfirmJobPrefix"]
      """  This is the job number prefix that MRP uses when generating an unfirm job. Two Sites of the same company cannot have the same prefix.  """  
      self.FirmJobPrefix:str = obj["FirmJobPrefix"]
      """  This is the job number prefix that for firm jobs.  """  
      self.DefRcvWhse:str = obj["DefRcvWhse"]
      """  Default receiving warehouse. Used as default in receipt entry.  """  
      self.DefRcvBin:str = obj["DefRcvBin"]
      """  Default receiving bin Used as default in receipt entry.  """  
      self.DefShipWhse:str = obj["DefShipWhse"]
      """  Default shipping warehouse. Used as default in shipment entry.  """  
      self.DefShipBin:str = obj["DefShipBin"]
      """  Default shipping bin. Used as default in shipping entry.  """  
      self.KanBanPrefix:str = obj["KanBanPrefix"]
      """  KanBan Prefix  """  
      self.MRPTOPrefix:str = obj["MRPTOPrefix"]
      """  This is the job number prefix that MRP uses when generating an unfirm transfer order. Two Sites of the same company cannot have the same prefix.  """  
      self.ManualTOPrefix:str = obj["ManualTOPrefix"]
      """  This is the job number prefix that Epicor ERP uses when generating a firm transfer order. Two Sites of the same company cannot have the same prefix.  """  
      self.MRPLastScheduledDate:str = obj["MRPLastScheduledDate"]
      """  Scheduled Date used in last MRP run  """  
      self.MRPLastCutOffDate:str = obj["MRPLastCutOffDate"]
      """  Cut Off Date used in last MRP run  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ProductionYieldDefault:bool = obj["ProductionYieldDefault"]
      """  Default for JobHead.ProductionYield for this Site.  """  
      self.PrdYldAdjust:bool = obj["PrdYldAdjust"]
      """  Indicates whether the calculated production yield adjustment should be automatically applied.  """  
      self.PrdYldAlert:bool = obj["PrdYldAlert"]
      """  Indicates whether an alert should be sent if the production yield calculation determines that an adjustment should be made. The alert will indicate if the adjustment has been made automatically or not (based on the setting of Site.PrdYieldAdjust). If the  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificates of Origin required flag. Used in manifesting.  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice required flag. Used in manifesting.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration required flag. Used in manifesting.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction required. Used in manifesting.  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID.  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder first address line.  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  Freight Forwarder second address line.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Freight Forwarder third address line.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder city portion of address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder state portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder postal code or zip code portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder country portion of address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Non Standard Package flag. Used in manifesting.  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag. Used in manifesting.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder country number portion of address.  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder phone Number.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.DefInspBin:str = obj["DefInspBin"]
      """  Default inspection bin. Used as default in inspection processing.  """  
      self.DefDMRWhse:str = obj["DefDMRWhse"]
      """  Default DMR warehouse. Used as default in DMR processing.  """  
      self.DefDMRBin:str = obj["DefDMRBin"]
      """  Default DMR bin. Used as default in DMR processing.  """  
      self.BinToBinReqSN:bool = obj["BinToBinReqSN"]
      """   Indicates whether serial number entry will be required when inventory movement is bin-to-bin within the same warehouse. All other inventory movement will still require serial number entry. This flag is only used if Serial Tracking Option is set to Full Serial Trace.
Defaults to True.  """  
      self.LowLvlSerialTrk:int = obj["LowLvlSerialTrk"]
      """   Indicates the level of serial tracking for component items for the Site.
Defaults to 1.
Requires code/desc entry in object designer:
1 = No Lower Level Serial Tracking
2 = Full Lower Level Serial Tracking
3 = Outbound Serial Tracking Only.  """  
      self.SerialTracking:int = obj["SerialTracking"]
      """   Indicates the level of serial tracking for the Site.
Default value for new SiteConfigCtrl = 1.
Requires code/desc entry in object designer:
1 = No Serial Tracking
2 = Full Serial Tracking
3 = Outbound Serial Tracking Only.  """  
      self.SerialMatchWarn:int = obj["SerialMatchWarn"]
      """   Controls the level of warnings that the user is given during job receipt processes for matching component serial numbers to the top level serial numbers.
Defaults to 1
Requires code/desc entry in object designer:
1 = No Warnings
2 = Warn but Allow Processing
3 = Warn and Do Not Allow Processing  """  
      self.HHAutoSelectTranMax:int = obj["HHAutoSelectTranMax"]
      """  The maximum number of transactions to be auto-selected by the Handheld Auto-Select Transactions function.  """  
      self.CCSelectMethod:int = obj["CCSelectMethod"]
      """   Defines what method will be used to automatically select parts for cycle counting. This can be overridden in the Warehse table.
Default = 1.
Code/Desc:
1 = Repetitive, 2 = Random.  """  
      self.SearchSortOrder:str = obj["SearchSortOrder"]
      """  Default Search Sort for Sales Order Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.SearchSortJob:str = obj["SearchSortJob"]
      """  Default Search Sort for Job Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.SearchSortTransfer:str = obj["SearchSortTransfer"]
      """  Default Search Sort for Transfer Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.PriorityPick:int = obj["PriorityPick"]
      """  Default Priority for a Pick Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.PriorityPutaway:int = obj["PriorityPutaway"]
      """  Default Priority for a Putaway Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.PriorityBinToBinReplenish:int = obj["PriorityBinToBinReplenish"]
      """  Default Priority for a Bin To Bin Replenishment Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.ReplenishBy:str = obj["ReplenishBy"]
      """  Replenish By Quantity or Volume.  Valid values:  Q and V  """  
      self.LockOrdersOnPick:bool = obj["LockOrdersOnPick"]
      """  Lock Orders on Pick?  """  
      self.SortQueueByPriority:bool = obj["SortQueueByPriority"]
      """  Sort Queue by Priority?  """  
      self.DefJobPickWhse:str = obj["DefJobPickWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Job Allocation Picks in this Site.  """  
      self.DefJobPickBin:str = obj["DefJobPickBin"]
      """  Default Job Pick bin. Used as default in Job Allocation Picks.  """  
      self.DefTFOrdPickWhse:str = obj["DefTFOrdPickWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Transfer Order Allocation Picks in this Site.  """  
      self.DefTFOrdPickBin:str = obj["DefTFOrdPickBin"]
      """  Default Transfer Order Pick bin. Used as default in Transfer Order Allocation Picks.  """  
      self.CCProdCal:str = obj["CCProdCal"]
      """  The Production Calendar to be used in the calculation of the schedules for Cycle Counting. If this field is left blank then the current Production Calendar defined on the Site.  """  
      self.DefNetWeightUOM:str = obj["DefNetWeightUOM"]
      """   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  """  
      self.DefNetVolumeUOM:str = obj["DefNetVolumeUOM"]
      """   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  """  
      self.JobReleaseAutoReserve:bool = obj["JobReleaseAutoReserve"]
      """  The Job should automatically attempt to reserve inventory upon Release.  """  
      self.RecycleLastDate:str = obj["RecycleLastDate"]
      """  System date on which the last Recycle Job processing was run.  """  
      self.RecycleLastTime:int = obj["RecycleLastTime"]
      """  System Time (hr-min-sec) when the last Recycle Job process was run.  """  
      self.AllowJobMtlLoans:bool = obj["AllowJobMtlLoans"]
      """  By default this field will be false. Setting this to true will allow the loan logic to be enabled in Job Material Transfer Etnry.  """  
      self.JobMtlRepayMethod:str = obj["JobMtlRepayMethod"]
      """   This field will be disabled if the above field is false.
The combo box will have two options:
1.  Repay Material when All Materials Received (AllRecvd)
2.  Repay Material when sufficient has been Received (SuffRecvd)  """  
      self.DefDSWhse:str = obj["DefDSWhse"]
      """  Default Drop Shipping warehouse. Used as default in Drop Shipment processing.  """  
      self.TimeApprovalReqd:bool = obj["TimeApprovalReqd"]
      """  Determines if time needs to be approved.  """  
      self.TimeApproverCanAdd:bool = obj["TimeApproverCanAdd"]
      """  Defines if time approver can add a time transaction.  """  
      self.TimeApproverCanDel:bool = obj["TimeApproverCanDel"]
      """  Defines if time approver can delete a time transaction.  """  
      self.TimeApproverCanUpd:bool = obj["TimeApproverCanUpd"]
      """  Defines if time approver can update a time transaction.  """  
      self.TimeIndirectLogic:str = obj["TimeIndirectLogic"]
      """  Defines if the method for approving indirect time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.TimeProductionLogic:str = obj["TimeProductionLogic"]
      """  Defines if the method for approving production time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  The default workflow group for Time transactions entered in this Site.  """  
      self.TimeTaskSetID:str = obj["TimeTaskSetID"]
      """  The default task set for Time transactions entered in this Site.  """  
      self.ExpenseApprovalReqd:bool = obj["ExpenseApprovalReqd"]
      """  Determines if expenses need to be approved.  """  
      self.ExpenseApproverCanAdd:bool = obj["ExpenseApproverCanAdd"]
      """  Defines if expense approver can add an expense transaction.  """  
      self.ExpenseApproverCanDel:bool = obj["ExpenseApproverCanDel"]
      """  Defines if expense approver can delete an expense transaction.  """  
      self.ExpenseApproverCanUpd:bool = obj["ExpenseApproverCanUpd"]
      """  Defines if expense approver can update an expense transaction.  """  
      self.ExpenseIndirectLogic:str = obj["ExpenseIndirectLogic"]
      """  Defines if the method for approving indirect expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.ExpenseProductionLogic:str = obj["ExpenseProductionLogic"]
      """  Defines if the method for approving production expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  The default workflow group for Expense transactions entered in this Site.  """  
      self.ExpenseTaskSetID:str = obj["ExpenseTaskSetID"]
      """  The default task set for Expense transactions entered in this Site.  """  
      self.TimeMESApprovalReqd:bool = obj["TimeMESApprovalReqd"]
      """  Determines if labor time needs to be approved.  """  
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      """  Indicates if the current user is restricted to entering time against employees where their username is set in the Employee record.  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      """  Indicates if the current user is restricted to entering expenses against employees where their username is set in the Employee record.  """  
      self.OnlyPostedLabor:bool = obj["OnlyPostedLabor"]
      """  Used in Project Analysis to check if it should only include posted labor during the processing.  """  
      self.MaintTmpJobNum:str = obj["MaintTmpJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.MaintJobPrefix:str = obj["MaintJobPrefix"]
      """  Prefix that will be used when generating  Maintenance Job numbers for this Site.  Note: If blank, then system will use value defined at company level (see MMSyst.JobPrefix).  """  
      self.TimeSuperCanMaintain:bool = obj["TimeSuperCanMaintain"]
      """  Indicates if the supervisor of an employee can maintain time transactions on behalf of the employee.  """  
      self.ExpenseSuperCanMaintain:bool = obj["ExpenseSuperCanMaintain"]
      """  Indicates if the supervisor of an employee can maintain expense transactions on behalf of the employee.  """  
      self.EnforceAllocations:str = obj["EnforceAllocations"]
      """  This field determines how inventory allocations are enforced at the Site level.  """  
      self.ExpenseAdvReqLogic:str = obj["ExpenseAdvReqLogic"]
      """  Defines if the method for approving advance request expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.ExpenseAutoSubmit:bool = obj["ExpenseAutoSubmit"]
      """  Indicates if the new Expense Detail will be automatically submitted when saved.  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """  Indicates if the new Time Detail will be automatically submitted when saved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.ExternalMESType:str = obj["ExternalMESType"]
      """  The Machine MES Integration type  """  
      self.ExternalMESRoute:str = obj["ExternalMESRoute"]
      """  The Machine MES output file location  """  
      self.AllowReleaseOfCreditHoldOrder:bool = obj["AllowReleaseOfCreditHoldOrder"]
      """  Allow Credit Hold Orders to be released for Picking  """  
      self.AllowReleaseOfPartialSalesOrder:bool = obj["AllowReleaseOfPartialSalesOrder"]
      """  This flag determies if partially reserved or allocated sales order releases can be Released for Picking.   If checked, then the "Ship Order Complete" and "Ship Line Complete" flags on the sales order are ignored when determining if a sales order releases can be Released for Picking.  """  
      self.ExternalMESInput:str = obj["ExternalMESInput"]
      """  The Machine MES input file location  """  
      self.DisablePackOut:bool = obj["DisablePackOut"]
      """  Select this check box to disable the Pack Out sheet of Customer Shipment Entry  """  
      self.SuppressSOMakeDirWrn:bool = obj["SuppressSOMakeDirWrn"]
      """  Suppress Sales Order make direct Job warning  """  
      self.AssumePickedOrders:bool = obj["AssumePickedOrders"]
      """  Unpack to Picked Status  """  
      self.DefOrdShipWhseBin:bool = obj["DefOrdShipWhseBin"]
      """  Use Order or Shipping Warehouse/Bin  """  
      self.ApplyBurdenCost:bool = obj["ApplyBurdenCost"]
      """  Apply Burden to all operation Resources  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      """  If the Purchase Contracts module is being used, specify how the related demand requirements should be handled for this site.  """  
      self.IncludeCompleteQtys:bool = obj["IncludeCompleteQtys"]
      """  Include Completed Qtys/Hours in Send Ahead Calculations  """  
      self.AssignMtlDates:str = obj["AssignMtlDates"]
      """  Assign Material Dates (engineered, unengineered, scheduling)  """  
      self.AutoCompleteSetup:bool = obj["AutoCompleteSetup"]
      """  If you select this check box, the Setup is marked as Complete and load for Setup Hours is relieved when production for an operation is marked as Complete.  """  
      self.MtlIssuedAction:str = obj["MtlIssuedAction"]
      """  Controls the action to be taken when part number of a Job Mtl is being changed and there is already an issued qty to the original part number.  """  
      self.DefPlanContractWhse:str = obj["DefPlanContractWhse"]
      """  Default Planning Contract Wharehouse. It is only allowed warehouses with at least one bin location flagged as contract bin.  """  
      self.PartLeadTime:bool = obj["PartLeadTime"]
      """  PartLeadTime's flag allows the user to trigger the CTP calculations to include the parts lead time and net out existing supply and demand for the part.  """  
      self.ReadyToFulfillRequired:bool = obj["ReadyToFulfillRequired"]
      """  This flag controls which sales order releases can be processed by the Fulfillment Workbench.  If checked, then only those order releases where the associated OrderHed.ReadyToFulfill = true can be loaded into the workbench.  If not checked, then OrderHed.ReadyToFulfill is not considered when loading the workbench.  """  
      self.EnforceJobRcptToInv:bool = obj["EnforceJobRcptToInv"]
      """  Indicates if there is to be package control enforcement during Job Receipt to Inventory.  """  
      self.TimeExpenseDefaultEmpID:str = obj["TimeExpenseDefaultEmpID"]
      """  The default package control employee for Time and Expense.  """  
      self.SupervisorOverridePassword:str = obj["SupervisorOverridePassword"]
      """  The package control supervisor override password.  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Indicates if Package Control is enabled for this site.  """  
      self.DefaultRepackReasonCode:str = obj["DefaultRepackReasonCode"]
      """  Identifies the default Reason Code for a repack.  """  
      self.DefGenBin:str = obj["DefGenBin"]
      """  Default General bin. Used as default in receipt entry.  """  
      self.CTPJobCreateMTO:str = obj["CTPJobCreateMTO"]
      """  This flag affects the job creation in CTP for a Make to Order release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Order  will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  """  
      self.CTPJobCreateMTS:str = obj["CTPJobCreateMTS"]
      """  This flag affects the job creation in CTP for a Make To Stock release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Stock will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  """  
      self.MaxPCIDAllowedToCreate:int = obj["MaxPCIDAllowedToCreate"]
      """  Maximum Number of PCIDs allowed to be created during the Generate PCID function in various UI’s  """  
      self.ConsumeReturnables:str = obj["ConsumeReturnables"]
      """  ConsumeReturnables  """  
      self.ConsumeExpendables:str = obj["ConsumeExpendables"]
      """  ConsumeExpendables  """  
      self.IsDockingStationDistinct:bool = obj["IsDockingStationDistinct"]
      """  True if the Docking Station on the ShipDtl is a distinct value.  """  
      self.Use3rdPartySched:bool = obj["Use3rdPartySched"]
      """  Use3rdPartySched  """  
      self.MtlQueueMaxRowsToReturn:int = obj["MtlQueueMaxRowsToReturn"]
      """  MtlQueueMaxRowsToReturn  """  
      self.MtlQueueEndDaysOffset:int = obj["MtlQueueEndDaysOffset"]
      """  MtlQueueEndDaysOffset  """  
      self.GenNewPCIDDelaySeconds:int = obj["GenNewPCIDDelaySeconds"]
      """  GenNewPCIDDelaySeconds  """  
      self.GenNewPCIDLimitDays:int = obj["GenNewPCIDLimitDays"]
      """  GenNewPCIDLimitDays  """  
      self.CanEmployeeOverrideHCM:bool = obj["CanEmployeeOverrideHCM"]
      """  Logical field to indicate if the site configuration will allow to the Employee override HCM Payroll default  """  
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  List field the default payroll configuration for HCM Integration  """  
      self.ManifestRateShopping:bool = obj["ManifestRateShopping"]
      """  Indicates whether Rate Shopping functionality is enabled for the site.  """  
      self.ManifestRateShoppingURL:str = obj["ManifestRateShoppingURL"]
      """  The URL of the Rate Shopping website for this site.  """  
      self.MinJOGenerateInterval:int = obj["MinJOGenerateInterval"]
      """  Minimum Job Output Generate Interval. This value is in seconds. A value of 0 means no limit.  """  
      self.MaxJOReprintWindow:int = obj["MaxJOReprintWindow"]
      """  Maximum Job Output Reprint Window. This value is in minutes. A value of 0 means no limit.  """  
      self.MaxAHJOJobWindow:int = obj["MaxAHJOJobWindow"]
      """  Maximum Ad Hoc Job Output Job Window. This value is in days. A value of 0 means no limit.  """  
      self.MaxPartialJobWindow:int = obj["MaxPartialJobWindow"]
      """  Maximum Partial PCID Job Window. This value is in days. A value of 0 means no limit.  """  
      self.SiteIDCode:str = obj["SiteIDCode"]
      """  Code used when generating Identificatin Numbers.  """  
      self.VoidPCIDWhenEmpty:bool = obj["VoidPCIDWhenEmpty"]
      """  The flag in Site Configuration that allows to automatically void a PCID when it becomes empty  """  
      self.AllowAllocationOfPCIDInventory:bool = obj["AllowAllocationOfPCIDInventory"]
      """  When true, the allocation of inventory within a PCID will be allowed.  """  
      self.DefTOShipWhseBin:bool = obj["DefTOShipWhseBin"]
      """  False = Transfer Order shipping whs/bin will default to the From Site primary warehouse and bin for the part if defined, else use the From Site Default General Whse. True = shipping whs/bin will default to: PartAlloc whs/bin if an entry exists for TFOrdDtl, else use the TFOrdDtl Staging warehouse and bin.  """  
      self.ExternalMESODataURL:str = obj["ExternalMESODataURL"]
      """  The Machine MES OData URL  """  
      self.ExternalMESODataUsername:str = obj["ExternalMESODataUsername"]
      """  The Machine MES OData username  """  
      self.ExternalMESODataPassword:str = obj["ExternalMESODataPassword"]
      """  The Machine MES OData password  """  
      self.EnablePartAllocQueueOrder:bool = obj["EnablePartAllocQueueOrder"]
      """  Indicates if the fulfillment queue is available for sales orders.  """  
      self.AllocTemplateIDOrder:str = obj["AllocTemplateIDOrder"]
      """  Indicates the PartAllocTemplate to use when allocating sales orders using automated fulfillment.  """  
      self.LogWIPChanges:bool = obj["LogWIPChanges"]
      """  If Log WIP Changes is set to true, changes to PartWip will be logged in PartWipTran.  Default is false.  Must have AMM to set this to true.  Once WIP Changes have been logged, they will remain indefinitely.  Use the Database Purge and Summarice to purge history that is no longer desired.  """  
      self.SendToPartAllocQueueOrder:str = obj["SendToPartAllocQueueOrder"]
      """  Indicates if/when sales order releases should automatically be sent to the fulfillment queue.  """  
      self.AllocTemplateIDJob:str = obj["AllocTemplateIDJob"]
      """  Indicates the PartAllocTemplate to use when allocating jobs using automated fulfillment.  """  
      self.AllocTemplateIDTransfer:str = obj["AllocTemplateIDTransfer"]
      """  Indicates the PartAllocTemplate to use when allocating transfer orders using automated fulfillment.  """  
      self.EnablePartAllocQueueJob:bool = obj["EnablePartAllocQueueJob"]
      """  Indicates if the fulfillment queue is available for jobs.  """  
      self.EnablePartAllocQueueTransfer:bool = obj["EnablePartAllocQueueTransfer"]
      """  Indicates if the fulfillment queue is available for transfer orders.  """  
      self.OpCompleteConsumeWIP:bool = obj["OpCompleteConsumeWIP"]
      """  OpCompleteConsumeWIP  """  
      self.SendToPartAllocQueueJob:str = obj["SendToPartAllocQueueJob"]
      """  Indicates if/when job materials should automatically be sent to the fulfillment queue.  """  
      self.SendToPartAllocQueueTransfer:str = obj["SendToPartAllocQueueTransfer"]
      """  Indicates if/when transfer order lines should automatically be sent to the fulfillment queue.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  If this field is true, it marks the selected site as Connected Process Control (CPC) as enabled. If disabled, connection and/or sync will not be done.  """  
      self.WIPShippingAction:str = obj["WIPShippingAction"]
      """  Controls the action that is to be taken when job ship quantity is not in shipping location  """  
      self.ShippingProdCal:str = obj["ShippingProdCal"]
      """  ShippingProdCal  """  
      self.InvalidRequestDateAction:str = obj["InvalidRequestDateAction"]
      """  InvalidRequestDateAction  """  
      self.InvalidNeedByDateAction:str = obj["InvalidNeedByDateAction"]
      """  InvalidNeedByDateAction  """  
      self.AfterUpdateMessage:str = obj["AfterUpdateMessage"]
      """  Place to populate a warning message to be displayed after update.  """  
      self.EnableSerTrkOpts:bool = obj["EnableSerTrkOpts"]
      self.ExpenseApproverCanAddDel:bool = obj["ExpenseApproverCanAddDel"]
      """  Defines if expense approver can add and delete an expense transaction.  """  
      self.IsHCMCompanyEnabled:bool = obj["IsHCMCompanyEnabled"]
      """  External field used on the Site Configuration Entry in order to enable or disable HCM fields  """  
      self.LowLvlSrlTrkDesc:str = obj["LowLvlSrlTrkDesc"]
      self.SerialMatchWrnDesc:str = obj["SerialMatchWrnDesc"]
      self.SerialTrkDesc:str = obj["SerialTrkDesc"]
      self.TimeApproverCanAddDel:bool = obj["TimeApproverCanAddDel"]
      """  Defines if time approver can add and delete a time transaction.  """  
      self.AssignMtlDatesDesc:str = obj["AssignMtlDatesDesc"]
      self.ExternalMESODataPasswordMasked:str = obj["ExternalMESODataPasswordMasked"]
      """  External MES OData Password masked.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefaultRepackReasonCodeDescription:str = obj["DefaultRepackReasonCodeDescription"]
      self.DefaultWhseDescription:str = obj["DefaultWhseDescription"]
      self.DefDMRBinDescription:str = obj["DefDMRBinDescription"]
      self.DefDMRWhseDescription:str = obj["DefDMRWhseDescription"]
      self.DefInspBinDescription:str = obj["DefInspBinDescription"]
      self.DefInspWhseDescription:str = obj["DefInspWhseDescription"]
      self.DefJobPickBinDescription:str = obj["DefJobPickBinDescription"]
      self.DefJobPickWhseDescription:str = obj["DefJobPickWhseDescription"]
      self.DefPCWhseDescription:str = obj["DefPCWhseDescription"]
      self.DefRcvBinDescription:str = obj["DefRcvBinDescription"]
      self.DefRcvWhseDescription:str = obj["DefRcvWhseDescription"]
      self.DefShipBinDescription:str = obj["DefShipBinDescription"]
      self.DefShipWhseDescription:str = obj["DefShipWhseDescription"]
      self.DefTFOrdPickBinDescription:str = obj["DefTFOrdPickBinDescription"]
      self.DefTFOrdPickWhseDescription:str = obj["DefTFOrdPickWhseDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.IdleResourceIDDescription:str = obj["IdleResourceIDDescription"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.PlantSendToFSA:bool = obj["PlantSendToFSA"]
      self.PlantName:str = obj["PlantName"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ShippingProdCalDescription:str = obj["ShippingProdCalDescription"]
      self.TimeExpenseDefaultEmpIDName:str = obj["TimeExpenseDefaultEmpIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantMFBillRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.PayBTFlag:str = obj["PayBTFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayTypeDesc:str = obj["PayTypeDesc"]
      """   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Billing Address  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping biling address line 2  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping biling address line 3.  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping billing city  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Shipping Billing state or province  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Pay billing postal code  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Shipping biling country  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Internal field used to store the country number.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping billing phone number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantSharedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for the Site that shares the warehouse.  This field cannot be blank.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  A warehouse that is owned by the RemoteSite and shared with the Site. This field cannot be blank.  """  
      self.RemotePlant:str = obj["RemotePlant"]
      """  Remote Site Identifier for the Site that owns the warehouse.  This field cannot be blank.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RemotePlantName:str = obj["RemotePlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlntTranDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.TranDays:int = obj["TranDays"]
      """  Estimated number of days to transfer material between Sites.  """  
      self.ConsolidationDivision:str = obj["ConsolidationDivision"]
      """  ID of the division that is used to create eliminating entries.  """  
      self.InterDivSalesCatID:str = obj["InterDivSalesCatID"]
      """  Unique identifier for this category assigned by the user.  """  
      self.DefaultShipViaCode:str = obj["DefaultShipViaCode"]
      """  Default ShipVia Code used for Unfirm Transfer Orders in MRP.  Cannot be blank  """  
      self.InterDivisional:bool = obj["InterDivisional"]
      """   Previous version used the following structure:
if (FromSite.GLDivision <> ToSite.GLDivision) then ?
now wil be more flexible
if (   PlntTranDef.InterDivisional   =  Yes   ) then  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PlantARAcct:str = obj["PlantARAcct"]
      """  Plant A/R GL Account  """  
      self.PlantARAcctDesc:str = obj["PlantARAcctDesc"]
      """  Plant A/R GL Account Desc  """  
      self.PlantAPAcct:str = obj["PlantAPAcct"]
      """  Plant AP GL Account Number  """  
      self.PlantAPAcctDesc:str = obj["PlantAPAcctDesc"]
      """  Plant AP GL Account Description  """  
      self.ContraARAcct:str = obj["ContraARAcct"]
      """  Contra AR GL Account Number  """  
      self.ContraARAcctDesc:str = obj["ContraARAcctDesc"]
      """  Contra AR GL Account Description  """  
      self.ContraAPAcct:str = obj["ContraAPAcct"]
      """  Contra AP GL Account  """  
      self.ContraAPAcctDesc:str = obj["ContraAPAcctDesc"]
      """  Contra AP GL Account Description  """  
      self.ContraCOGSAcct:str = obj["ContraCOGSAcct"]
      """  Contra COGS GL Account  """  
      self.ContraCOGSAcctDesc:str = obj["ContraCOGSAcctDesc"]
      """  Contra COGS GL Account Description  """  
      self.ContraRevenueAcct:str = obj["ContraRevenueAcct"]
      """  Contra Revenue GL Account  """  
      self.ContraRevenueAcctDesc:str = obj["ContraRevenueAcctDesc"]
      """  Contra Revenue GL Account Description  """  
      self.ContraAssetAcct:str = obj["ContraAssetAcct"]
      """  Contra Asset GL Account  """  
      self.ContraAssetAcctDesc:str = obj["ContraAssetAcctDesc"]
      """  Contra Asset GL Account Description  """  
      self.JournalCodeDesc:str = obj["JournalCodeDesc"]
      """  Journal Code Description  """  
      self.ConsolidationDivisionDesc:str = obj["ConsolidationDivisionDesc"]
      """  Consolidation Division Description  """  
      self.TransitAcct:str = obj["TransitAcct"]
      """  Transit GL Account  """  
      self.TransitAcctDesc:str = obj["TransitAcctDesc"]
      """  Transit GL Account Description  """  
      self.InterDivSalesCatDesc:str = obj["InterDivSalesCatDesc"]
      """  Inter Division Sales Category Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefautShipViaDescription:str = obj["DefautShipViaDescription"]
      self.DefautShipViaWebDesc:str = obj["DefautShipViaWebDesc"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.InverDivSalesCatDescription:str = obj["InverDivSalesCatDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.ToPlantName:str = obj["ToPlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PltUPSEmailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email address to notify for a UPS shipment  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating to the UI if the QV Detail and list is to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckApprovalDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DfltApprTasksParamsTableset] = obj["ds"]
      pass

class CheckApprovalDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DfltApprTasksParamsTableset] = obj["ds"]
      self.cQuestionText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CreateApprovalDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DfltApprTasksParamsTableset] = obj["ds"]
      pass

class CreateApprovalDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DfltApprTasksParamsTableset] = obj["ds"]
      self.cReturnText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CustomGetNewPlantShared_input:
   """ Required : 
   ds
   plant
   remotePlant
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      """  Plant  """  
      self.remotePlant:str = obj["remotePlant"]
      """  Remote Plant  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  Warehouse Code  """  
      pass

class CustomGetNewPlantShared_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DfltApprTasksParamsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CreateForMultiLvlApp:bool = obj["CreateForMultiLvlApp"]
      """  Create defaults for multi-level approval  """  
      self.CreateForSuperApp:bool = obj["CreateForSuperApp"]
      """  Create defaults for supervisor approval  """  
      self.CreateForPMApp:bool = obj["CreateForPMApp"]
      """  Create defaults for project manager approval  """  
      self.CreateForPMAndSupApp:bool = obj["CreateForPMAndSupApp"]
      """  Create defaults for project manager/supervisor approval  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DfltApprTasksParamsTableset:
   def __init__(self, obj):
      self.DfltApprTasksParams:list[Erp_Tablesets_DfltApprTasksParamsRow] = obj["DfltApprTasksParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_PlantConfABCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.ABCCode:str = obj["ABCCode"]
      """  ABC Code.  Valid values are "A" through "Z".  """  
      self.OvrrideCountFreq:bool = obj["OvrrideCountFreq"]
      """  This flag indicates whether the CountFreq defined in this record should over ride the count frequency in the AbcCode table.  """  
      self.CountFreq:int = obj["CountFreq"]
      """  This setting can be overrides AbcCode.CountFreq and can be overridden in WarehseABC.  """  
      self.ExcludeFromCC:bool = obj["ExcludeFromCC"]
      """  This flag is set to true prevent items that should only be counted during physical inventory from being selected for cycle counting. This setting can be overridden in WarehseABC.  """  
      self.StockValPcnt:int = obj["StockValPcnt"]
      """  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting can be overridden in WarehseABC.  """  
      self.PcntTolerance:int = obj["PcntTolerance"]
      """  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of tolerance  """  
      self.CalcPcnt:bool = obj["CalcPcnt"]
      """  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcQty:bool = obj["CalcQty"]
      """  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  """  
      self.CalcValue:bool = obj["CalcValue"]
      """  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  """  
      self.OvrrideStockValPcnt:bool = obj["OvrrideStockValPcnt"]
      """  This flag indicates whether the StockValPcnt defined in this record should over ride the count frequency in the AbcCode table.  """  
      self.QtyTolerance:int = obj["QtyTolerance"]
      """  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of  """  
      self.ValueTolerance:int = obj["ValueTolerance"]
      """  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, or WarehseABC.  An entry of zero will indicate that any value variance will be considered out  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
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

class Erp_Tablesets_PlantConfCtrlEGLCRow:
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
      self.Plant:str = obj["Plant"]
      """  Plant for PlantConfCtrl  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlListTableset:
   def __init__(self, obj):
      self.PlantConfCtrlList:list[Erp_Tablesets_PlantConfCtrlListRow] = obj["PlantConfCtrlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlantConfCtrlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  The Site name.  """  
      self.DefaultWhse:str = obj["DefaultWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default warehouse for this Site.  """  
      self.MRPLastRunDate:str = obj["MRPLastRunDate"]
      """  System date on which the last MRP processing was run.  """  
      self.MRPLastRunTime:int = obj["MRPLastRunTime"]
      """  System Time (hr-min-sec) when the last MRP process was run.  """  
      self.DefInspWhse:str = obj["DefInspWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default inspection warehouse for this Site.  """  
      self.CalcIdleTime:bool = obj["CalcIdleTime"]
      """  Indicates if Labor Collection should calculate Idle time.  Idle time is the time that the employee is getting paid for but is not doing any direct or Indirect labor activity.  The Labor Collection will automatically generate an Indirect detail record to capture these hours if this flag is set to "Yes".  If this is "yes" then the IdleIndirectCode and IdleWCCode must be entered and valid.  """  
      self.IdleResourceGrpID:str = obj["IdleResourceGrpID"]
      """  The ResourceGrpID used by labor collection to create the LaborDtl entry for idle time when CalcIdleTime = Yes. For production labor (LaborType = "S" or "P") the default is from the JobOpDtl.ResourceGrpId from the primary JobOpDtl.  For indirect labor (LaborType = I) there is no default.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  The indirect labor code (Indirect.IndirectCode) that Labor Collection will use when it creates the Idle Time detail record in LaborDtl.  This must be valid if the CalcIdleTime = Yes.  """  
      self.TimeZoneOffset:int = obj["TimeZoneOffset"]
      """  The number of hours (+-) difference from the server time zone to the Site time zone.  Data collection transactions will be offset by this amount.  """  
      self.TimeOffsetSec:int = obj["TimeOffsetSec"]
      """  Related to TimeZoneOffset. Calculated from users entry in TimeZoneOffset, the number of seconds (+-) difference from the server time zone to the Site time zone.   Used for clock in clock out in data collection.  """  
      self.UnfirmJobPrefix:str = obj["UnfirmJobPrefix"]
      """  This is the job number prefix that MRP uses when generating an unfirm job. Two Sites of the same company cannot have the same prefix.  """  
      self.FirmJobPrefix:str = obj["FirmJobPrefix"]
      """  This is the job number prefix that for firm jobs.  """  
      self.DefRcvWhse:str = obj["DefRcvWhse"]
      """  Default receiving warehouse. Used as default in receipt entry.  """  
      self.DefRcvBin:str = obj["DefRcvBin"]
      """  Default receiving bin Used as default in receipt entry.  """  
      self.DefShipWhse:str = obj["DefShipWhse"]
      """  Default shipping warehouse. Used as default in shipment entry.  """  
      self.DefShipBin:str = obj["DefShipBin"]
      """  Default shipping bin. Used as default in shipping entry.  """  
      self.KanBanPrefix:str = obj["KanBanPrefix"]
      """  KanBan Prefix  """  
      self.MRPTOPrefix:str = obj["MRPTOPrefix"]
      """  This is the job number prefix that MRP uses when generating an unfirm transfer order. Two Sites of the same company cannot have the same prefix.  """  
      self.ManualTOPrefix:str = obj["ManualTOPrefix"]
      """  This is the job number prefix that Epicor ERP uses when generating a firm transfer order. Two Sites of the same company cannot have the same prefix.  """  
      self.MRPLastScheduledDate:str = obj["MRPLastScheduledDate"]
      """  Scheduled Date used in last MRP run  """  
      self.MRPLastCutOffDate:str = obj["MRPLastCutOffDate"]
      """  Cut Off Date used in last MRP run  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ProductionYieldDefault:bool = obj["ProductionYieldDefault"]
      """  Default for JobHead.ProductionYield for this Site.  """  
      self.PrdYldAdjust:bool = obj["PrdYldAdjust"]
      """  Indicates whether the calculated production yield adjustment should be automatically applied.  """  
      self.PrdYldAlert:bool = obj["PrdYldAlert"]
      """  Indicates whether an alert should be sent if the production yield calculation determines that an adjustment should be made. The alert will indicate if the adjustment has been made automatically or not (based on the setting of Site.PrdYieldAdjust). If the  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificates of Origin required flag. Used in manifesting.  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice required flag. Used in manifesting.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration required flag. Used in manifesting.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction required. Used in manifesting.  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID.  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder first address line.  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  Freight Forwarder second address line.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Freight Forwarder third address line.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder city portion of address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder state portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder postal code or zip code portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder country portion of address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Non Standard Package flag. Used in manifesting.  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Additional Handling flag. Used in manifesting.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder country number portion of address.  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder phone Number.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View From Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.DefInspBin:str = obj["DefInspBin"]
      """  Default inspection bin. Used as default in inspection processing.  """  
      self.DefDMRWhse:str = obj["DefDMRWhse"]
      """  Default DMR warehouse. Used as default in DMR processing.  """  
      self.DefDMRBin:str = obj["DefDMRBin"]
      """  Default DMR bin. Used as default in DMR processing.  """  
      self.BinToBinReqSN:bool = obj["BinToBinReqSN"]
      """   Indicates whether serial number entry will be required when inventory movement is bin-to-bin within the same warehouse. All other inventory movement will still require serial number entry. This flag is only used if Serial Tracking Option is set to Full Serial Trace.
Defaults to True.  """  
      self.LowLvlSerialTrk:int = obj["LowLvlSerialTrk"]
      """   Indicates the level of serial tracking for component items for the Site.
Defaults to 1.
Requires code/desc entry in object designer:
1 = No Lower Level Serial Tracking
2 = Full Lower Level Serial Tracking
3 = Outbound Serial Tracking Only.  """  
      self.SerialTracking:int = obj["SerialTracking"]
      """   Indicates the level of serial tracking for the Site.
Default value for new SiteConfigCtrl = 1.
Requires code/desc entry in object designer:
1 = No Serial Tracking
2 = Full Serial Tracking
3 = Outbound Serial Tracking Only.  """  
      self.SerialMatchWarn:int = obj["SerialMatchWarn"]
      """   Controls the level of warnings that the user is given during job receipt processes for matching component serial numbers to the top level serial numbers.
Defaults to 1
Requires code/desc entry in object designer:
1 = No Warnings
2 = Warn but Allow Processing
3 = Warn and Do Not Allow Processing  """  
      self.HHAutoSelectTranMax:int = obj["HHAutoSelectTranMax"]
      """  The maximum number of transactions to be auto-selected by the Handheld Auto-Select Transactions function.  """  
      self.CCSelectMethod:int = obj["CCSelectMethod"]
      """   Defines what method will be used to automatically select parts for cycle counting. This can be overridden in the Warehse table.
Default = 1.
Code/Desc:
1 = Repetitive, 2 = Random.  """  
      self.SearchSortOrder:str = obj["SearchSortOrder"]
      """  Default Search Sort for Sales Order Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.SearchSortJob:str = obj["SearchSortJob"]
      """  Default Search Sort for Job Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.SearchSortTransfer:str = obj["SearchSortTransfer"]
      """  Default Search Sort for Transfer Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  """  
      self.PriorityPick:int = obj["PriorityPick"]
      """  Default Priority for a Pick Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.PriorityPutaway:int = obj["PriorityPutaway"]
      """  Default Priority for a Putaway Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.PriorityBinToBinReplenish:int = obj["PriorityBinToBinReplenish"]
      """  Default Priority for a Bin To Bin Replenishment Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  """  
      self.ReplenishBy:str = obj["ReplenishBy"]
      """  Replenish By Quantity or Volume.  Valid values:  Q and V  """  
      self.LockOrdersOnPick:bool = obj["LockOrdersOnPick"]
      """  Lock Orders on Pick?  """  
      self.SortQueueByPriority:bool = obj["SortQueueByPriority"]
      """  Sort Queue by Priority?  """  
      self.DefJobPickWhse:str = obj["DefJobPickWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Job Allocation Picks in this Site.  """  
      self.DefJobPickBin:str = obj["DefJobPickBin"]
      """  Default Job Pick bin. Used as default in Job Allocation Picks.  """  
      self.DefTFOrdPickWhse:str = obj["DefTFOrdPickWhse"]
      """  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Transfer Order Allocation Picks in this Site.  """  
      self.DefTFOrdPickBin:str = obj["DefTFOrdPickBin"]
      """  Default Transfer Order Pick bin. Used as default in Transfer Order Allocation Picks.  """  
      self.CCProdCal:str = obj["CCProdCal"]
      """  The Production Calendar to be used in the calculation of the schedules for Cycle Counting. If this field is left blank then the current Production Calendar defined on the Site.  """  
      self.DefNetWeightUOM:str = obj["DefNetWeightUOM"]
      """   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  """  
      self.DefNetVolumeUOM:str = obj["DefNetVolumeUOM"]
      """   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  """  
      self.JobReleaseAutoReserve:bool = obj["JobReleaseAutoReserve"]
      """  The Job should automatically attempt to reserve inventory upon Release.  """  
      self.RecycleLastDate:str = obj["RecycleLastDate"]
      """  System date on which the last Recycle Job processing was run.  """  
      self.RecycleLastTime:int = obj["RecycleLastTime"]
      """  System Time (hr-min-sec) when the last Recycle Job process was run.  """  
      self.AllowJobMtlLoans:bool = obj["AllowJobMtlLoans"]
      """  By default this field will be false. Setting this to true will allow the loan logic to be enabled in Job Material Transfer Etnry.  """  
      self.JobMtlRepayMethod:str = obj["JobMtlRepayMethod"]
      """   This field will be disabled if the above field is false.
The combo box will have two options:
1.  Repay Material when All Materials Received (AllRecvd)
2.  Repay Material when sufficient has been Received (SuffRecvd)  """  
      self.DefDSWhse:str = obj["DefDSWhse"]
      """  Default Drop Shipping warehouse. Used as default in Drop Shipment processing.  """  
      self.TimeApprovalReqd:bool = obj["TimeApprovalReqd"]
      """  Determines if time needs to be approved.  """  
      self.TimeApproverCanAdd:bool = obj["TimeApproverCanAdd"]
      """  Defines if time approver can add a time transaction.  """  
      self.TimeApproverCanDel:bool = obj["TimeApproverCanDel"]
      """  Defines if time approver can delete a time transaction.  """  
      self.TimeApproverCanUpd:bool = obj["TimeApproverCanUpd"]
      """  Defines if time approver can update a time transaction.  """  
      self.TimeIndirectLogic:str = obj["TimeIndirectLogic"]
      """  Defines if the method for approving indirect time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.TimeProductionLogic:str = obj["TimeProductionLogic"]
      """  Defines if the method for approving production time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  The default workflow group for Time transactions entered in this Site.  """  
      self.TimeTaskSetID:str = obj["TimeTaskSetID"]
      """  The default task set for Time transactions entered in this Site.  """  
      self.ExpenseApprovalReqd:bool = obj["ExpenseApprovalReqd"]
      """  Determines if expenses need to be approved.  """  
      self.ExpenseApproverCanAdd:bool = obj["ExpenseApproverCanAdd"]
      """  Defines if expense approver can add an expense transaction.  """  
      self.ExpenseApproverCanDel:bool = obj["ExpenseApproverCanDel"]
      """  Defines if expense approver can delete an expense transaction.  """  
      self.ExpenseApproverCanUpd:bool = obj["ExpenseApproverCanUpd"]
      """  Defines if expense approver can update an expense transaction.  """  
      self.ExpenseIndirectLogic:str = obj["ExpenseIndirectLogic"]
      """  Defines if the method for approving indirect expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.ExpenseProductionLogic:str = obj["ExpenseProductionLogic"]
      """  Defines if the method for approving production expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  The default workflow group for Expense transactions entered in this Site.  """  
      self.ExpenseTaskSetID:str = obj["ExpenseTaskSetID"]
      """  The default task set for Expense transactions entered in this Site.  """  
      self.TimeMESApprovalReqd:bool = obj["TimeMESApprovalReqd"]
      """  Determines if labor time needs to be approved.  """  
      self.TimeRestrictEntry:bool = obj["TimeRestrictEntry"]
      """  Indicates if the current user is restricted to entering time against employees where their username is set in the Employee record.  """  
      self.ExpenseRestrictEntry:bool = obj["ExpenseRestrictEntry"]
      """  Indicates if the current user is restricted to entering expenses against employees where their username is set in the Employee record.  """  
      self.OnlyPostedLabor:bool = obj["OnlyPostedLabor"]
      """  Used in Project Analysis to check if it should only include posted labor during the processing.  """  
      self.MaintTmpJobNum:str = obj["MaintTmpJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.MaintJobPrefix:str = obj["MaintJobPrefix"]
      """  Prefix that will be used when generating  Maintenance Job numbers for this Site.  Note: If blank, then system will use value defined at company level (see MMSyst.JobPrefix).  """  
      self.TimeSuperCanMaintain:bool = obj["TimeSuperCanMaintain"]
      """  Indicates if the supervisor of an employee can maintain time transactions on behalf of the employee.  """  
      self.ExpenseSuperCanMaintain:bool = obj["ExpenseSuperCanMaintain"]
      """  Indicates if the supervisor of an employee can maintain expense transactions on behalf of the employee.  """  
      self.EnforceAllocations:str = obj["EnforceAllocations"]
      """  This field determines how inventory allocations are enforced at the Site level.  """  
      self.ExpenseAdvReqLogic:str = obj["ExpenseAdvReqLogic"]
      """  Defines if the method for approving advance request expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  """  
      self.ExpenseAutoSubmit:bool = obj["ExpenseAutoSubmit"]
      """  Indicates if the new Expense Detail will be automatically submitted when saved.  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """  Indicates if the new Time Detail will be automatically submitted when saved.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.ExternalMESType:str = obj["ExternalMESType"]
      """  The Machine MES Integration type  """  
      self.ExternalMESRoute:str = obj["ExternalMESRoute"]
      """  The Machine MES output file location  """  
      self.AllowReleaseOfCreditHoldOrder:bool = obj["AllowReleaseOfCreditHoldOrder"]
      """  Allow Credit Hold Orders to be released for Picking  """  
      self.AllowReleaseOfPartialSalesOrder:bool = obj["AllowReleaseOfPartialSalesOrder"]
      """  This flag determies if partially reserved or allocated sales order releases can be Released for Picking.   If checked, then the "Ship Order Complete" and "Ship Line Complete" flags on the sales order are ignored when determining if a sales order releases can be Released for Picking.  """  
      self.ExternalMESInput:str = obj["ExternalMESInput"]
      """  The Machine MES input file location  """  
      self.DisablePackOut:bool = obj["DisablePackOut"]
      """  Select this check box to disable the Pack Out sheet of Customer Shipment Entry  """  
      self.SuppressSOMakeDirWrn:bool = obj["SuppressSOMakeDirWrn"]
      """  Suppress Sales Order make direct Job warning  """  
      self.AssumePickedOrders:bool = obj["AssumePickedOrders"]
      """  Unpack to Picked Status  """  
      self.DefOrdShipWhseBin:bool = obj["DefOrdShipWhseBin"]
      """  Use Order or Shipping Warehouse/Bin  """  
      self.ApplyBurdenCost:bool = obj["ApplyBurdenCost"]
      """  Apply Burden to all operation Resources  """  
      self.PurchaseScheduleMode:str = obj["PurchaseScheduleMode"]
      """  If the Purchase Contracts module is being used, specify how the related demand requirements should be handled for this site.  """  
      self.IncludeCompleteQtys:bool = obj["IncludeCompleteQtys"]
      """  Include Completed Qtys/Hours in Send Ahead Calculations  """  
      self.AssignMtlDates:str = obj["AssignMtlDates"]
      """  Assign Material Dates (engineered, unengineered, scheduling)  """  
      self.AutoCompleteSetup:bool = obj["AutoCompleteSetup"]
      """  If you select this check box, the Setup is marked as Complete and load for Setup Hours is relieved when production for an operation is marked as Complete.  """  
      self.MtlIssuedAction:str = obj["MtlIssuedAction"]
      """  Controls the action to be taken when part number of a Job Mtl is being changed and there is already an issued qty to the original part number.  """  
      self.DefPlanContractWhse:str = obj["DefPlanContractWhse"]
      """  Default Planning Contract Wharehouse. It is only allowed warehouses with at least one bin location flagged as contract bin.  """  
      self.PartLeadTime:bool = obj["PartLeadTime"]
      """  PartLeadTime's flag allows the user to trigger the CTP calculations to include the parts lead time and net out existing supply and demand for the part.  """  
      self.ReadyToFulfillRequired:bool = obj["ReadyToFulfillRequired"]
      """  This flag controls which sales order releases can be processed by the Fulfillment Workbench.  If checked, then only those order releases where the associated OrderHed.ReadyToFulfill = true can be loaded into the workbench.  If not checked, then OrderHed.ReadyToFulfill is not considered when loading the workbench.  """  
      self.EnforceJobRcptToInv:bool = obj["EnforceJobRcptToInv"]
      """  Indicates if there is to be package control enforcement during Job Receipt to Inventory.  """  
      self.TimeExpenseDefaultEmpID:str = obj["TimeExpenseDefaultEmpID"]
      """  The default package control employee for Time and Expense.  """  
      self.SupervisorOverridePassword:str = obj["SupervisorOverridePassword"]
      """  The package control supervisor override password.  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Indicates if Package Control is enabled for this site.  """  
      self.DefaultRepackReasonCode:str = obj["DefaultRepackReasonCode"]
      """  Identifies the default Reason Code for a repack.  """  
      self.DefGenBin:str = obj["DefGenBin"]
      """  Default General bin. Used as default in receipt entry.  """  
      self.CTPJobCreateMTO:str = obj["CTPJobCreateMTO"]
      """  This flag affects the job creation in CTP for a Make to Order release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Order  will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  """  
      self.CTPJobCreateMTS:str = obj["CTPJobCreateMTS"]
      """  This flag affects the job creation in CTP for a Make To Stock release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Stock will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  """  
      self.MaxPCIDAllowedToCreate:int = obj["MaxPCIDAllowedToCreate"]
      """  Maximum Number of PCIDs allowed to be created during the Generate PCID function in various UI’s  """  
      self.ConsumeReturnables:str = obj["ConsumeReturnables"]
      """  ConsumeReturnables  """  
      self.ConsumeExpendables:str = obj["ConsumeExpendables"]
      """  ConsumeExpendables  """  
      self.IsDockingStationDistinct:bool = obj["IsDockingStationDistinct"]
      """  True if the Docking Station on the ShipDtl is a distinct value.  """  
      self.Use3rdPartySched:bool = obj["Use3rdPartySched"]
      """  Use3rdPartySched  """  
      self.MtlQueueMaxRowsToReturn:int = obj["MtlQueueMaxRowsToReturn"]
      """  MtlQueueMaxRowsToReturn  """  
      self.MtlQueueEndDaysOffset:int = obj["MtlQueueEndDaysOffset"]
      """  MtlQueueEndDaysOffset  """  
      self.GenNewPCIDDelaySeconds:int = obj["GenNewPCIDDelaySeconds"]
      """  GenNewPCIDDelaySeconds  """  
      self.GenNewPCIDLimitDays:int = obj["GenNewPCIDLimitDays"]
      """  GenNewPCIDLimitDays  """  
      self.CanEmployeeOverrideHCM:bool = obj["CanEmployeeOverrideHCM"]
      """  Logical field to indicate if the site configuration will allow to the Employee override HCM Payroll default  """  
      self.PayrollValuesForHCM:str = obj["PayrollValuesForHCM"]
      """  List field the default payroll configuration for HCM Integration  """  
      self.ManifestRateShopping:bool = obj["ManifestRateShopping"]
      """  Indicates whether Rate Shopping functionality is enabled for the site.  """  
      self.ManifestRateShoppingURL:str = obj["ManifestRateShoppingURL"]
      """  The URL of the Rate Shopping website for this site.  """  
      self.MinJOGenerateInterval:int = obj["MinJOGenerateInterval"]
      """  Minimum Job Output Generate Interval. This value is in seconds. A value of 0 means no limit.  """  
      self.MaxJOReprintWindow:int = obj["MaxJOReprintWindow"]
      """  Maximum Job Output Reprint Window. This value is in minutes. A value of 0 means no limit.  """  
      self.MaxAHJOJobWindow:int = obj["MaxAHJOJobWindow"]
      """  Maximum Ad Hoc Job Output Job Window. This value is in days. A value of 0 means no limit.  """  
      self.MaxPartialJobWindow:int = obj["MaxPartialJobWindow"]
      """  Maximum Partial PCID Job Window. This value is in days. A value of 0 means no limit.  """  
      self.SiteIDCode:str = obj["SiteIDCode"]
      """  Code used when generating Identificatin Numbers.  """  
      self.VoidPCIDWhenEmpty:bool = obj["VoidPCIDWhenEmpty"]
      """  The flag in Site Configuration that allows to automatically void a PCID when it becomes empty  """  
      self.AllowAllocationOfPCIDInventory:bool = obj["AllowAllocationOfPCIDInventory"]
      """  When true, the allocation of inventory within a PCID will be allowed.  """  
      self.DefTOShipWhseBin:bool = obj["DefTOShipWhseBin"]
      """  False = Transfer Order shipping whs/bin will default to the From Site primary warehouse and bin for the part if defined, else use the From Site Default General Whse. True = shipping whs/bin will default to: PartAlloc whs/bin if an entry exists for TFOrdDtl, else use the TFOrdDtl Staging warehouse and bin.  """  
      self.ExternalMESODataURL:str = obj["ExternalMESODataURL"]
      """  The Machine MES OData URL  """  
      self.ExternalMESODataUsername:str = obj["ExternalMESODataUsername"]
      """  The Machine MES OData username  """  
      self.ExternalMESODataPassword:str = obj["ExternalMESODataPassword"]
      """  The Machine MES OData password  """  
      self.EnablePartAllocQueueOrder:bool = obj["EnablePartAllocQueueOrder"]
      """  Indicates if the fulfillment queue is available for sales orders.  """  
      self.AllocTemplateIDOrder:str = obj["AllocTemplateIDOrder"]
      """  Indicates the PartAllocTemplate to use when allocating sales orders using automated fulfillment.  """  
      self.LogWIPChanges:bool = obj["LogWIPChanges"]
      """  If Log WIP Changes is set to true, changes to PartWip will be logged in PartWipTran.  Default is false.  Must have AMM to set this to true.  Once WIP Changes have been logged, they will remain indefinitely.  Use the Database Purge and Summarice to purge history that is no longer desired.  """  
      self.SendToPartAllocQueueOrder:str = obj["SendToPartAllocQueueOrder"]
      """  Indicates if/when sales order releases should automatically be sent to the fulfillment queue.  """  
      self.AllocTemplateIDJob:str = obj["AllocTemplateIDJob"]
      """  Indicates the PartAllocTemplate to use when allocating jobs using automated fulfillment.  """  
      self.AllocTemplateIDTransfer:str = obj["AllocTemplateIDTransfer"]
      """  Indicates the PartAllocTemplate to use when allocating transfer orders using automated fulfillment.  """  
      self.EnablePartAllocQueueJob:bool = obj["EnablePartAllocQueueJob"]
      """  Indicates if the fulfillment queue is available for jobs.  """  
      self.EnablePartAllocQueueTransfer:bool = obj["EnablePartAllocQueueTransfer"]
      """  Indicates if the fulfillment queue is available for transfer orders.  """  
      self.OpCompleteConsumeWIP:bool = obj["OpCompleteConsumeWIP"]
      """  OpCompleteConsumeWIP  """  
      self.SendToPartAllocQueueJob:str = obj["SendToPartAllocQueueJob"]
      """  Indicates if/when job materials should automatically be sent to the fulfillment queue.  """  
      self.SendToPartAllocQueueTransfer:str = obj["SendToPartAllocQueueTransfer"]
      """  Indicates if/when transfer order lines should automatically be sent to the fulfillment queue.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  If this field is true, it marks the selected site as Connected Process Control (CPC) as enabled. If disabled, connection and/or sync will not be done.  """  
      self.WIPShippingAction:str = obj["WIPShippingAction"]
      """  Controls the action that is to be taken when job ship quantity is not in shipping location  """  
      self.ShippingProdCal:str = obj["ShippingProdCal"]
      """  ShippingProdCal  """  
      self.InvalidRequestDateAction:str = obj["InvalidRequestDateAction"]
      """  InvalidRequestDateAction  """  
      self.InvalidNeedByDateAction:str = obj["InvalidNeedByDateAction"]
      """  InvalidNeedByDateAction  """  
      self.AfterUpdateMessage:str = obj["AfterUpdateMessage"]
      """  Place to populate a warning message to be displayed after update.  """  
      self.EnableSerTrkOpts:bool = obj["EnableSerTrkOpts"]
      self.ExpenseApproverCanAddDel:bool = obj["ExpenseApproverCanAddDel"]
      """  Defines if expense approver can add and delete an expense transaction.  """  
      self.IsHCMCompanyEnabled:bool = obj["IsHCMCompanyEnabled"]
      """  External field used on the Site Configuration Entry in order to enable or disable HCM fields  """  
      self.LowLvlSrlTrkDesc:str = obj["LowLvlSrlTrkDesc"]
      self.SerialMatchWrnDesc:str = obj["SerialMatchWrnDesc"]
      self.SerialTrkDesc:str = obj["SerialTrkDesc"]
      self.TimeApproverCanAddDel:bool = obj["TimeApproverCanAddDel"]
      """  Defines if time approver can add and delete a time transaction.  """  
      self.AssignMtlDatesDesc:str = obj["AssignMtlDatesDesc"]
      self.ExternalMESODataPasswordMasked:str = obj["ExternalMESODataPasswordMasked"]
      """  External MES OData Password masked.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefaultRepackReasonCodeDescription:str = obj["DefaultRepackReasonCodeDescription"]
      self.DefaultWhseDescription:str = obj["DefaultWhseDescription"]
      self.DefDMRBinDescription:str = obj["DefDMRBinDescription"]
      self.DefDMRWhseDescription:str = obj["DefDMRWhseDescription"]
      self.DefInspBinDescription:str = obj["DefInspBinDescription"]
      self.DefInspWhseDescription:str = obj["DefInspWhseDescription"]
      self.DefJobPickBinDescription:str = obj["DefJobPickBinDescription"]
      self.DefJobPickWhseDescription:str = obj["DefJobPickWhseDescription"]
      self.DefPCWhseDescription:str = obj["DefPCWhseDescription"]
      self.DefRcvBinDescription:str = obj["DefRcvBinDescription"]
      self.DefRcvWhseDescription:str = obj["DefRcvWhseDescription"]
      self.DefShipBinDescription:str = obj["DefShipBinDescription"]
      self.DefShipWhseDescription:str = obj["DefShipWhseDescription"]
      self.DefTFOrdPickBinDescription:str = obj["DefTFOrdPickBinDescription"]
      self.DefTFOrdPickWhseDescription:str = obj["DefTFOrdPickWhseDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.IdleResourceIDDescription:str = obj["IdleResourceIDDescription"]
      self.IndirectCodeDescription:str = obj["IndirectCodeDescription"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.PlantSendToFSA:bool = obj["PlantSendToFSA"]
      self.PlantName:str = obj["PlantName"]
      self.ProdCalDescription:str = obj["ProdCalDescription"]
      self.ShippingProdCalDescription:str = obj["ShippingProdCalDescription"]
      self.TimeExpenseDefaultEmpIDName:str = obj["TimeExpenseDefaultEmpIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantConfCtrlTableset:
   def __init__(self, obj):
      self.PlantConfCtrl:list[Erp_Tablesets_PlantConfCtrlRow] = obj["PlantConfCtrl"]
      self.PlantConfCtrlAttch:list[Erp_Tablesets_PlantConfCtrlAttchRow] = obj["PlantConfCtrlAttch"]
      self.PlantConfABC:list[Erp_Tablesets_PlantConfABCRow] = obj["PlantConfABC"]
      self.PlantMFBill:list[Erp_Tablesets_PlantMFBillRow] = obj["PlantMFBill"]
      self.PlantShared:list[Erp_Tablesets_PlantSharedRow] = obj["PlantShared"]
      self.PlntTranDef:list[Erp_Tablesets_PlntTranDefRow] = obj["PlntTranDef"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.PltUPSEmail:list[Erp_Tablesets_PltUPSEmailRow] = obj["PltUPSEmail"]
      self.PlantConfCtrlEGLC:list[Erp_Tablesets_PlantConfCtrlEGLCRow] = obj["PlantConfCtrlEGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlantMFBillRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.PayBTFlag:str = obj["PayBTFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayTypeDesc:str = obj["PayTypeDesc"]
      """   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Billing Address  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping biling address line 2  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping biling address line 3.  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping billing city  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Shipping Billing state or province  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Pay billing postal code  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Shipping biling country  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Internal field used to store the country number.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping billing phone number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlantSharedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier for the Site that shares the warehouse.  This field cannot be blank.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  A warehouse that is owned by the RemoteSite and shared with the Site. This field cannot be blank.  """  
      self.RemotePlant:str = obj["RemotePlant"]
      """  Remote Site Identifier for the Site that owns the warehouse.  This field cannot be blank.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PlantName:str = obj["PlantName"]
      self.RemotePlantName:str = obj["RemotePlantName"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlntTranDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.TranDays:int = obj["TranDays"]
      """  Estimated number of days to transfer material between Sites.  """  
      self.ConsolidationDivision:str = obj["ConsolidationDivision"]
      """  ID of the division that is used to create eliminating entries.  """  
      self.InterDivSalesCatID:str = obj["InterDivSalesCatID"]
      """  Unique identifier for this category assigned by the user.  """  
      self.DefaultShipViaCode:str = obj["DefaultShipViaCode"]
      """  Default ShipVia Code used for Unfirm Transfer Orders in MRP.  Cannot be blank  """  
      self.InterDivisional:bool = obj["InterDivisional"]
      """   Previous version used the following structure:
if (FromSite.GLDivision <> ToSite.GLDivision) then ?
now wil be more flexible
if (   PlntTranDef.InterDivisional   =  Yes   ) then  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PlantARAcct:str = obj["PlantARAcct"]
      """  Plant A/R GL Account  """  
      self.PlantARAcctDesc:str = obj["PlantARAcctDesc"]
      """  Plant A/R GL Account Desc  """  
      self.PlantAPAcct:str = obj["PlantAPAcct"]
      """  Plant AP GL Account Number  """  
      self.PlantAPAcctDesc:str = obj["PlantAPAcctDesc"]
      """  Plant AP GL Account Description  """  
      self.ContraARAcct:str = obj["ContraARAcct"]
      """  Contra AR GL Account Number  """  
      self.ContraARAcctDesc:str = obj["ContraARAcctDesc"]
      """  Contra AR GL Account Description  """  
      self.ContraAPAcct:str = obj["ContraAPAcct"]
      """  Contra AP GL Account  """  
      self.ContraAPAcctDesc:str = obj["ContraAPAcctDesc"]
      """  Contra AP GL Account Description  """  
      self.ContraCOGSAcct:str = obj["ContraCOGSAcct"]
      """  Contra COGS GL Account  """  
      self.ContraCOGSAcctDesc:str = obj["ContraCOGSAcctDesc"]
      """  Contra COGS GL Account Description  """  
      self.ContraRevenueAcct:str = obj["ContraRevenueAcct"]
      """  Contra Revenue GL Account  """  
      self.ContraRevenueAcctDesc:str = obj["ContraRevenueAcctDesc"]
      """  Contra Revenue GL Account Description  """  
      self.ContraAssetAcct:str = obj["ContraAssetAcct"]
      """  Contra Asset GL Account  """  
      self.ContraAssetAcctDesc:str = obj["ContraAssetAcctDesc"]
      """  Contra Asset GL Account Description  """  
      self.JournalCodeDesc:str = obj["JournalCodeDesc"]
      """  Journal Code Description  """  
      self.ConsolidationDivisionDesc:str = obj["ConsolidationDivisionDesc"]
      """  Consolidation Division Description  """  
      self.TransitAcct:str = obj["TransitAcct"]
      """  Transit GL Account  """  
      self.TransitAcctDesc:str = obj["TransitAcctDesc"]
      """  Transit GL Account Description  """  
      self.InterDivSalesCatDesc:str = obj["InterDivSalesCatDesc"]
      """  Inter Division Sales Category Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DefautShipViaDescription:str = obj["DefautShipViaDescription"]
      self.DefautShipViaWebDesc:str = obj["DefautShipViaWebDesc"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.InverDivSalesCatDescription:str = obj["InverDivSalesCatDescription"]
      self.JournalCodeJrnlDescription:str = obj["JournalCodeJrnlDescription"]
      self.ToPlantName:str = obj["ToPlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PltUPSEmailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email address to notify for a UPS shipment  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating to the UI if the QV Detail and list is to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPlantConfCtrlTableset:
   def __init__(self, obj):
      self.PlantConfCtrl:list[Erp_Tablesets_PlantConfCtrlRow] = obj["PlantConfCtrl"]
      self.PlantConfCtrlAttch:list[Erp_Tablesets_PlantConfCtrlAttchRow] = obj["PlantConfCtrlAttch"]
      self.PlantConfABC:list[Erp_Tablesets_PlantConfABCRow] = obj["PlantConfABC"]
      self.PlantMFBill:list[Erp_Tablesets_PlantMFBillRow] = obj["PlantMFBill"]
      self.PlantShared:list[Erp_Tablesets_PlantSharedRow] = obj["PlantShared"]
      self.PlntTranDef:list[Erp_Tablesets_PlntTranDefRow] = obj["PlntTranDef"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.PltUPSEmail:list[Erp_Tablesets_PltUPSEmailRow] = obj["PltUPSEmail"]
      self.PlantConfCtrlEGLC:list[Erp_Tablesets_PlantConfCtrlEGLCRow] = obj["PlantConfCtrlEGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetBinContractTypeWarehousesList_input:
   """ Required : 
   sPlantID
   """  
   def __init__(self, obj):
      self.sPlantID:str = obj["sPlantID"]
      pass

class GetBinContractTypeWarehousesList_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetByID_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   systemCode
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCompleteList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  (optional)Additional Where conditions.  """  
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetCompleteList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantConfCtrlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetDfltApprTasksParam_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DfltApprTasksParamsTableset] = obj["returnObj"]
      pass

class GetDisabledFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DisabledList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_PlantConfCtrlListTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantConfABC_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewPlantConfABC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantConfCtrlAttch_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewPlantConfCtrlAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantConfCtrlEGLC_input:
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
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewPlantConfCtrlEGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantConfCtrl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class GetNewPlantConfCtrl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantMFBill_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewPlantMFBill_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlantShared_input:
   """ Required : 
   ds
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewPlantShared_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlntTranDef_input:
   """ Required : 
   ds
   fromPlant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.fromPlant:str = obj["fromPlant"]
      pass

class GetNewPlntTranDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPltUPSEmail_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewPltUPSEmail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePlantConfCtrl
   whereClausePlantConfCtrlAttch
   whereClausePlantConfABC
   whereClausePlantMFBill
   whereClausePlantShared
   whereClausePlntTranDef
   whereClauseEntityGLC
   whereClausePltUPSEmail
   whereClausePlantConfCtrlEGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePlantConfCtrl:str = obj["whereClausePlantConfCtrl"]
      self.whereClausePlantConfCtrlAttch:str = obj["whereClausePlantConfCtrlAttch"]
      self.whereClausePlantConfABC:str = obj["whereClausePlantConfABC"]
      self.whereClausePlantMFBill:str = obj["whereClausePlantMFBill"]
      self.whereClausePlantShared:str = obj["whereClausePlantShared"]
      self.whereClausePlntTranDef:str = obj["whereClausePlntTranDef"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClausePltUPSEmail:str = obj["whereClausePltUPSEmail"]
      self.whereClausePlantConfCtrlEGLC:str = obj["whereClausePlantConfCtrlEGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["returnObj"]
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

class IsAuthorizedForPlant_input:
   """ Required : 
   plantID
   """  
   def __init__(self, obj):
      self.plantID:str = obj["plantID"]
      """  Plant ID  """  
      pass

class IsAuthorizedForPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isValid:bool = obj["isValid"]
      pass

      """  output parameters  """  

class OnChangeEnablePartAllocQueue_input:
   """ Required : 
   enable
   demandType
   ds
   """  
   def __init__(self, obj):
      self.enable:bool = obj["enable"]
      """  The new value of the enable flag.  """  
      self.demandType:str = obj["demandType"]
      """  The demandType related to the enable flag that is being changed (Job, Order, Transfer).  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeEnablePartAllocQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeOfAbcCode_input:
   """ Required : 
   ds
   ipABCCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.ipABCCode:str = obj["ipABCCode"]
      pass

class OnChangeOfAbcCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfCCProdCal_input:
   """ Required : 
   calendarID
   ds
   """  
   def __init__(self, obj):
      self.calendarID:str = obj["calendarID"]
      """  Proposed Cycle Count Calendar ID field  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfCCProdCal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfExpenseApprovalReqd_input:
   """ Required : 
   ipApprovalRequired
   ds
   """  
   def __init__(self, obj):
      self.ipApprovalRequired:bool = obj["ipApprovalRequired"]
      """  Proposed ExpenseApprovalReqd field  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfExpenseApprovalReqd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfExpenseRestrictEntry_input:
   """ Required : 
   ipRestrictEntry
   ds
   """  
   def __init__(self, obj):
      self.ipRestrictEntry:bool = obj["ipRestrictEntry"]
      """  Proposed ExpenseRestrictEntry field  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfExpenseRestrictEntry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLowLvlSerialTrk_input:
   """ Required : 
   ipLLSerTrk
   ds
   """  
   def __init__(self, obj):
      self.ipLLSerTrk:int = obj["ipLLSerTrk"]
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfLowLvlSerialTrk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfMaintTmpJobNum_input:
   """ Required : 
   ipJobNum
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Num  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfMaintTmpJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfPcntTolerance_input:
   """ Required : 
   ipPcntTolerance
   """  
   def __init__(self, obj):
      self.ipPcntTolerance:int = obj["ipPcntTolerance"]
      """  Percentage Tolerance  """  
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
      """  Quantity Tolerance Value  """  
      pass

class OnChangeOfQtyTolerance_output:
   def __init__(self, obj):
      pass

class OnChangeOfSerialTracking_input:
   """ Required : 
   ipSerialTracking
   ds
   """  
   def __init__(self, obj):
      self.ipSerialTracking:int = obj["ipSerialTracking"]
      """  Proposed Serial Tracking field  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfSerialTracking_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfStockValPcnt_input:
   """ Required : 
   ipStockValPcnt
   """  
   def __init__(self, obj):
      self.ipStockValPcnt:int = obj["ipStockValPcnt"]
      pass

class OnChangeOfStockValPcnt_output:
   def __init__(self, obj):
      pass

class OnChangeOfTimeApprovalReqd_input:
   """ Required : 
   ipApprovalRequired
   ds
   """  
   def __init__(self, obj):
      self.ipApprovalRequired:bool = obj["ipApprovalRequired"]
      """  Proposed TimeApprovalReqd field  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfTimeApprovalReqd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfTimeRestrictEntry_input:
   """ Required : 
   ipRestrictEntry
   ds
   """  
   def __init__(self, obj):
      self.ipRestrictEntry:bool = obj["ipRestrictEntry"]
      """  Proposed TimeRestrictEntry field  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class OnChangeOfTimeRestrictEntry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class OnChangePCWarehouseCode_input:
   """ Required : 
   ds
   WarehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      pass

class OnChangePCWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResourceTransfer_input:
   """ Required : 
   pcPlant
   pcRemotePlant
   pcWrkCenterList
   pcWareHseList
   plExecuteTransfer
   """  
   def __init__(self, obj):
      self.pcPlant:str = obj["pcPlant"]
      """  The plant from where you want to move the resources  """  
      self.pcRemotePlant:str = obj["pcRemotePlant"]
      """  The plant where you want to move the resources  """  
      self.pcWrkCenterList:str = obj["pcWrkCenterList"]
      """  The delimited list of Work centers that you want to transfer to the remote plant  """  
      self.pcWareHseList:str = obj["pcWareHseList"]
      """  The delimited list of warehouses that you want to transfer to the remote plant  """  
      self.plExecuteTransfer:bool = obj["plExecuteTransfer"]
      """  Yes will update the records.  No will run a simulation  """  
      pass

class ResourceTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMessage:str = obj["parameters"]
      self.cTransferLog:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetUPSQVEnable_input:
   """ Required : 
   ipQVEnable
   ds
   """  
   def __init__(self, obj):
      self.ipQVEnable:bool = obj["ipQVEnable"]
      """  logical indicating if the quantum view is to enabled/disabled  """  
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class SetUPSQVEnable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TestMachineMESODataConnection_input:
   """ Required : 
   plant
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      pass

class TestMachineMESODataConnection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.msgConnection:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlantConfCtrlTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlantConfCtrlTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlantConfCtrlTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePayBTFlag_input:
   """ Required : 
   ipPayBTFlag
   """  
   def __init__(self, obj):
      self.ipPayBTFlag:str = obj["ipPayBTFlag"]
      """  requested pay bt flag to edit  """  
      pass

class ValidatePayBTFlag_output:
   def __init__(self, obj):
      pass

