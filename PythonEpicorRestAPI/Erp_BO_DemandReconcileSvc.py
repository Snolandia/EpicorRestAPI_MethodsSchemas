import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandReconcileSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DemandReconciles(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandReconciles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandReconciles
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandReconcileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles",headers=creds) as resp:
           return await resp.json()

async def post_DemandReconciles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandReconciles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandReconciles_Company_ReconcileNum(Company, ReconcileNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandReconcile item
   Description: Calls GetByID to retrieve the DemandReconcile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandReconcile
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandReconciles_Company_ReconcileNum(Company, ReconcileNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandReconcile for the service
   Description: Calls UpdateExt to update DemandReconcile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandReconcile
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandReconcileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandReconciles_Company_ReconcileNum(Company, ReconcileNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandReconcile item
   Description: Call UpdateExt to delete DemandReconcile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandReconcile
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandReconciles_Company_ReconcileNum_DemReconAdjusts(Company, ReconcileNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemReconAdjusts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemReconAdjusts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconAdjustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconAdjusts",headers=creds) as resp:
           return await resp.json()

async def get_DemandReconciles_Company_ReconcileNum_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company, ReconcileNum, SysDate, SysTime, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemReconAdjust item
   Description: Calls GetByID to retrieve the DemReconAdjust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconAdjust1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandReconciles_Company_ReconcileNum_DemReconcileShipments(Company, ReconcileNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemReconcileShipments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemReconcileShipments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconcileShipmentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconcileShipments",headers=creds) as resp:
           return await resp.json()

async def get_DemandReconciles_Company_ReconcileNum_DemReconcileShipments_Company_ReconcileNum_PackNum(Company, ReconcileNum, PackNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemReconcileShipment item
   Description: Calls GetByID to retrieve the DemReconcileShipment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconcileShipment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemandReconciles(" + Company + "," + ReconcileNum + ")/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemReconAdjusts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemReconAdjusts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemReconAdjusts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconAdjustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts",headers=creds) as resp:
           return await resp.json()

async def post_DemReconAdjusts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemReconAdjusts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company, ReconcileNum, SysDate, SysTime, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemReconAdjust item
   Description: Calls GetByID to retrieve the DemReconAdjust item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconAdjust
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company, ReconcileNum, SysDate, SysTime, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemReconAdjust for the service
   Description: Calls UpdateExt to update DemReconAdjust. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemReconAdjust
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemReconAdjustRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemReconAdjusts_Company_ReconcileNum_SysDate_SysTime_TranNum(Company, ReconcileNum, SysDate, SysTime, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemReconAdjust item
   Description: Call UpdateExt to delete DemReconAdjust item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemReconAdjust
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param TranNum: Desc: TranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconAdjusts(" + Company + "," + ReconcileNum + "," + SysDate + "," + SysTime + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemReconcileShipments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemReconcileShipments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemReconcileShipments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemReconcileShipmentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments",headers=creds) as resp:
           return await resp.json()

async def post_DemReconcileShipments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemReconcileShipments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemReconcileShipments_Company_ReconcileNum_PackNum(Company, ReconcileNum, PackNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemReconcileShipment item
   Description: Calls GetByID to retrieve the DemReconcileShipment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemReconcileShipment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemReconcileShipments_Company_ReconcileNum_PackNum(Company, ReconcileNum, PackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemReconcileShipment for the service
   Description: Calls UpdateExt to update DemReconcileShipment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemReconcileShipment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param PackNum: Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemReconcileShipmentsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemReconcileShipments_Company_ReconcileNum_PackNum(Company, ReconcileNum, PackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemReconcileShipment item
   Description: Call UpdateExt to delete DemReconcileShipment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemReconcileShipment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReconcileNum: Desc: ReconcileNum   Required: True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/DemReconcileShipments(" + Company + "," + ReconcileNum + "," + PackNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandReconcileListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDemandReconcile, whereClauseDemReconAdjust, whereClauseDemReconcileShipments, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDemandReconcile=" + whereClauseDemandReconcile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemReconAdjust=" + whereClauseDemReconAdjust
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemReconcileShipments=" + whereClauseDemReconcileShipments
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reconcileNum, epicorHeaders = None):
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
   params += "reconcileNum=" + reconcileNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRAdjustmentQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRAdjustmentQty
   Description: Recalc Variance when the Adjustment Quantity changes.
   OperationID: ChangeDRAdjustmentQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRAdjustmentQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRAdjustmentQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRCustID
   Description: Used when the CustID field is being changed to a new value.
   OperationID: ChangeDRCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRDemandContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRDemandContract
   Description: Used when the DemandContract field is being changed to a new value.
   OperationID: ChangeDRDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRPartNum
   Description: Used when the PartNum field is being changed to a new value.
   OperationID: ChangeDRPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRReconcileCUMMQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRReconcileCUMMQty
   Description: Recalc Adjust Quantity when the Reconcile Quantity changes.
   OperationID: ChangeDRReconcileCUMMQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRReconcileCUMMQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRReconcileCUMMQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRReconcileStartCumQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRReconcileStartCumQty
   Description: Recalc Adjust Quantity and set Company Cumulative Quantity when the Start Cumulative Quantity changes.
   OperationID: ChangeDRReconcileStartCumQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRReconcileStartCumQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRReconcileStartCumQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRShippedCUMMQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRShippedCUMMQty
   Description: Changed event of Company Cumulative Quantity field.
   OperationID: ChangeDRShippedCUMMQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRShippedCUMMQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRShippedCUMMQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRSReconcileQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRSReconcileQty
   Description: Updates the Reconcile Qty for the selected PackNum.
   OperationID: ChangeDRSReconcileQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRSReconcileQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRSReconcileQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDRTPCUMMQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDRTPCUMMQty
   Description: Changed event of Trading Partner Quantity field.
   OperationID: ChangeDRTPCUMMQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDRTPCUMMQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDRTPCUMMQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateAdjustmentCredit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateAdjustmentCredit
   OperationID: CreateAdjustmentCredit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateAdjustmentCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateAdjustmentCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RestartCumInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RestartCumInfo
   Description: Restart the cumulative info stored for the company. B
   OperationID: RestartCumInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RestartCumInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestartCumInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsSearch
   Description: Returns Demand Reconcile records for search
   OperationID: GetRowsSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandReconcile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandReconcile
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandReconcile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandReconcile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandReconcile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandReconcileSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconAdjustRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemReconAdjustRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemReconcileShipmentsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemReconcileShipmentsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandReconcileListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandReconcileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandReconcileRow] = obj["value"]
      pass

class Erp_Tablesets_DemReconAdjustRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReconcileNum:int = obj["ReconcileNum"]
      self.TranNum:int = obj["TranNum"]
      self.SysDate:str = obj["SysDate"]
      self.SysTime:int = obj["SysTime"]
      self.TranQty:int = obj["TranQty"]
      self.TranDate:str = obj["TranDate"]
      self.DispSysTime:str = obj["DispSysTime"]
      self.IUM:str = obj["IUM"]
      self.AvailPackNum:bool = obj["AvailPackNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemReconcileShipmentsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReconcileNum:int = obj["ReconcileNum"]
      self.PackNum:int = obj["PackNum"]
      self.Invoiced:bool = obj["Invoiced"]
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      self.SalesUM:str = obj["SalesUM"]
      self.ShipDate:str = obj["ShipDate"]
      self.ReconcileQty:int = obj["ReconcileQty"]
      """  The reconciled qty should be populated as the last shipped qty received in the inbound file for that specific packing slip.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReconcileListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  The customers Purchase Order Number the reconcilliation is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the reconcilliation is for.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo the reconcilliation is for.  """  
      self.ShippedCUMMQty:int = obj["ShippedCUMMQty"]
      """  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  """  
      self.TPCUMMQty:int = obj["TPCUMMQty"]
      """  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  """  
      self.ReconcileCUMMQty:int = obj["ReconcileCUMMQty"]
      """  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  """  
      self.ShippedCUMMDate:str = obj["ShippedCUMMDate"]
      """  The date the ShippedCUMMQty field was last updated.  """  
      self.TPCUMMDate:str = obj["TPCUMMDate"]
      """  The date the TPCUMMQty field was last updated.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.TPLastShipmentID:int = obj["TPLastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.TPLastShipmentQty:int = obj["TPLastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.TPLastShipmentDate:str = obj["TPLastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.TPScheduleNumber:str = obj["TPScheduleNumber"]
      """  The current schedule number of the file where the cumulative info was received  """  
      self.CILastShipmentID:int = obj["CILastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.CILastShipmentQty:int = obj["CILastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.CILastShipmentDate:str = obj["CILastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.RestartDate:str = obj["RestartDate"]
      """  Date when the Restart process is executed on this Reconcile record.  """  
      self.RestartSchedNum:str = obj["RestartSchedNum"]
      """  Last Schedule Number before restart Cumulative Information.  """  
      self.RestartPONum:str = obj["RestartPONum"]
      """  PO Number that executed the Restart Cumulative Information process.  """  
      self.TPLastMasterPack:int = obj["TPLastMasterPack"]
      """  Trading partner Last Master Pack.  """  
      self.CILastMasterPack:int = obj["CILastMasterPack"]
      """  Company Information Last Master Pack.  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  Starting Cumulative Quantity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DemandUOM:str = obj["DemandUOM"]
      """  The UOM code that represents the unit of measure in which the quantity is expressed.  """  
      self.AdjustmentQty:int = obj["AdjustmentQty"]
      self.Variance:int = obj["Variance"]
      """  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustID:str = obj["CustID"]
      """  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.AllowDelete:bool = obj["AllowDelete"]
      """  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReconcileRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  The customers Purchase Order Number the reconcilliation is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the reconcilliation is for.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo the reconcilliation is for.  """  
      self.ShippedCUMMQty:int = obj["ShippedCUMMQty"]
      """  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  """  
      self.TPCUMMQty:int = obj["TPCUMMQty"]
      """  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  """  
      self.ReconcileCUMMQty:int = obj["ReconcileCUMMQty"]
      """  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  """  
      self.ShippedCUMMDate:str = obj["ShippedCUMMDate"]
      """  The date the ShippedCUMMQty field was last updated.  """  
      self.TPCUMMDate:str = obj["TPCUMMDate"]
      """  The date the TPCUMMQty field was last updated.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.TPLastShipmentID:int = obj["TPLastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.TPLastShipmentQty:int = obj["TPLastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.TPLastShipmentDate:str = obj["TPLastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.TPScheduleNumber:str = obj["TPScheduleNumber"]
      """  The current schedule number of the file where the cumulative info was received  """  
      self.CILastShipmentID:int = obj["CILastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.CILastShipmentQty:int = obj["CILastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.CILastShipmentDate:str = obj["CILastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.RestartDate:str = obj["RestartDate"]
      """  Date when the Restart process is executed on this Reconcile record.  """  
      self.RestartSchedNum:str = obj["RestartSchedNum"]
      """  Last Schedule Number before restart Cumulative Information.  """  
      self.RestartPONum:str = obj["RestartPONum"]
      """  PO Number that executed the Restart Cumulative Information process.  """  
      self.TPLastMasterPack:int = obj["TPLastMasterPack"]
      """  Trading partner Last Master Pack.  """  
      self.CILastMasterPack:int = obj["CILastMasterPack"]
      """  Company Information Last Master Pack.  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  Starting Cumulative Quantity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DemandUOM:str = obj["DemandUOM"]
      """  The UOM code that represents the unit of measure in which the quantity is expressed.  """  
      self.AdjustmentQty:int = obj["AdjustmentQty"]
      self.Variance:int = obj["Variance"]
      """  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustID:str = obj["CustID"]
      """  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.AllowDelete:bool = obj["AllowDelete"]
      """  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeDRAdjustmentQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      """  The proposed Adjustment Quantity  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRAdjustmentQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRCustID_input:
   """ Required : 
   proposedCustID
   ds
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      """  The proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRDemandContract_input:
   """ Required : 
   proposedDemandContract
   ds
   """  
   def __init__(self, obj):
      self.proposedDemandContract:str = obj["proposedDemandContract"]
      """  The proposed Demand Contract  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRDemandContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRPartNum_input:
   """ Required : 
   proposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.proposedPartNum:str = obj["proposedPartNum"]
      """  The proposed Part Number  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRReconcileCUMMQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      """  The proposed Reconcile Quantity  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRReconcileCUMMQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRReconcileStartCumQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      """  The proposed Start Cumulative Quantity  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRReconcileStartCumQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRSReconcileQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      """  The proposed Reconcile Quantity  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRSReconcileQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRShippedCUMMQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      """  The proposed Shipped Cumulative Quantity  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRShippedCUMMQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDRTPCUMMQty_input:
   """ Required : 
   proposedQty
   ds
   """  
   def __init__(self, obj):
      self.proposedQty:int = obj["proposedQty"]
      """  The proposed Trading Partner Cumulative Quantity  """  
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class ChangeDRTPCUMMQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateAdjustmentCredit_input:
   """ Required : 
   iReconcileNum
   iPackNum
   iTranNum
   iSysDate
   iSysTime
   """  
   def __init__(self, obj):
      self.iReconcileNum:int = obj["iReconcileNum"]
      self.iPackNum:int = obj["iPackNum"]
      self.iTranNum:int = obj["iTranNum"]
      self.iSysDate:str = obj["iSysDate"]
      self.iSysTime:int = obj["iSysTime"]
      pass

class CreateAdjustmentCredit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iInvoiceNum:int = obj["parameters"]
      self.iInvoiceLine:int = obj["parameters"]
      self.opErrMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   reconcileNum
   """  
   def __init__(self, obj):
      self.reconcileNum:int = obj["reconcileNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DemReconAdjustRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReconcileNum:int = obj["ReconcileNum"]
      self.TranNum:int = obj["TranNum"]
      self.SysDate:str = obj["SysDate"]
      self.SysTime:int = obj["SysTime"]
      self.TranQty:int = obj["TranQty"]
      self.TranDate:str = obj["TranDate"]
      self.DispSysTime:str = obj["DispSysTime"]
      self.IUM:str = obj["IUM"]
      self.AvailPackNum:bool = obj["AvailPackNum"]
      self.InvoiceLine:int = obj["InvoiceLine"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemReconcileShipmentsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ReconcileNum:int = obj["ReconcileNum"]
      self.PackNum:int = obj["PackNum"]
      self.Invoiced:bool = obj["Invoiced"]
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      self.SellingInventoryShipQty:int = obj["SellingInventoryShipQty"]
      self.SalesUM:str = obj["SalesUM"]
      self.ShipDate:str = obj["ShipDate"]
      self.ReconcileQty:int = obj["ReconcileQty"]
      """  The reconciled qty should be populated as the last shipped qty received in the inbound file for that specific packing slip.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReconcileListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  The customers Purchase Order Number the reconcilliation is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the reconcilliation is for.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo the reconcilliation is for.  """  
      self.ShippedCUMMQty:int = obj["ShippedCUMMQty"]
      """  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  """  
      self.TPCUMMQty:int = obj["TPCUMMQty"]
      """  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  """  
      self.ReconcileCUMMQty:int = obj["ReconcileCUMMQty"]
      """  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  """  
      self.ShippedCUMMDate:str = obj["ShippedCUMMDate"]
      """  The date the ShippedCUMMQty field was last updated.  """  
      self.TPCUMMDate:str = obj["TPCUMMDate"]
      """  The date the TPCUMMQty field was last updated.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.TPLastShipmentID:int = obj["TPLastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.TPLastShipmentQty:int = obj["TPLastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.TPLastShipmentDate:str = obj["TPLastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.TPScheduleNumber:str = obj["TPScheduleNumber"]
      """  The current schedule number of the file where the cumulative info was received  """  
      self.CILastShipmentID:int = obj["CILastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.CILastShipmentQty:int = obj["CILastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.CILastShipmentDate:str = obj["CILastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.RestartDate:str = obj["RestartDate"]
      """  Date when the Restart process is executed on this Reconcile record.  """  
      self.RestartSchedNum:str = obj["RestartSchedNum"]
      """  Last Schedule Number before restart Cumulative Information.  """  
      self.RestartPONum:str = obj["RestartPONum"]
      """  PO Number that executed the Restart Cumulative Information process.  """  
      self.TPLastMasterPack:int = obj["TPLastMasterPack"]
      """  Trading partner Last Master Pack.  """  
      self.CILastMasterPack:int = obj["CILastMasterPack"]
      """  Company Information Last Master Pack.  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  Starting Cumulative Quantity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DemandUOM:str = obj["DemandUOM"]
      """  The UOM code that represents the unit of measure in which the quantity is expressed.  """  
      self.AdjustmentQty:int = obj["AdjustmentQty"]
      self.Variance:int = obj["Variance"]
      """  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustID:str = obj["CustID"]
      """  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.AllowDelete:bool = obj["AllowDelete"]
      """  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      """  The unique identifier of the demand contract.  This must be unique for a customer.  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReconcileListTableset:
   def __init__(self, obj):
      self.DemandReconcileList:list[Erp_Tablesets_DemandReconcileListRow] = obj["DemandReconcileList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandReconcileRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  A number which is used to allow create a unique key for the file.  The value for this field comes from database Sequence DemandReconcileSeq.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.PONum:str = obj["PONum"]
      """  The customers Purchase Order Number the reconcilliation is for.  """  
      self.PartNum:str = obj["PartNum"]
      """  The part number the reconcilliation is for.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo the reconcilliation is for.  """  
      self.ShippedCUMMQty:int = obj["ShippedCUMMQty"]
      """  The total shipped quantity for the reconcilliation.  This field is populated when a demand order is shipped.  """  
      self.TPCUMMQty:int = obj["TPCUMMQty"]
      """  The trading partner's cumulative quantity for the reconcilliation.  This is the quantity the trading partner states they have received.  """  
      self.ReconcileCUMMQty:int = obj["ReconcileCUMMQty"]
      """  This is the reconciled shipped quantity.  This will typically have the same quantity as TPCUMMQty, but it can be different.  """  
      self.ShippedCUMMDate:str = obj["ShippedCUMMDate"]
      """  The date the ShippedCUMMQty field was last updated.  """  
      self.TPCUMMDate:str = obj["TPCUMMDate"]
      """  The date the TPCUMMQty field was last updated.  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  For Epicor Development Use Only  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  For Epicor Development Use Only  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  For Epicor Development Use Only  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  For Epicor Development Use Only  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  For Epicor Development Use Only  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  For Epicor Development Use Only  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  For Epicor Development Use Only  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  For Epicor Development Use Only  """  
      self.TPLastShipmentID:int = obj["TPLastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.TPLastShipmentQty:int = obj["TPLastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.TPLastShipmentDate:str = obj["TPLastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.TPScheduleNumber:str = obj["TPScheduleNumber"]
      """  The current schedule number of the file where the cumulative info was received  """  
      self.CILastShipmentID:int = obj["CILastShipmentID"]
      """  The pack id of the last trading partner information received by the trading partner.  """  
      self.CILastShipmentQty:int = obj["CILastShipmentQty"]
      """  The quantity received in the last shipment according to the trading partner information  """  
      self.CILastShipmentDate:str = obj["CILastShipmentDate"]
      """  The date when of the last shipment according to the trading partner information  """  
      self.RestartDate:str = obj["RestartDate"]
      """  Date when the Restart process is executed on this Reconcile record.  """  
      self.RestartSchedNum:str = obj["RestartSchedNum"]
      """  Last Schedule Number before restart Cumulative Information.  """  
      self.RestartPONum:str = obj["RestartPONum"]
      """  PO Number that executed the Restart Cumulative Information process.  """  
      self.TPLastMasterPack:int = obj["TPLastMasterPack"]
      """  Trading partner Last Master Pack.  """  
      self.CILastMasterPack:int = obj["CILastMasterPack"]
      """  Company Information Last Master Pack.  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  Starting Cumulative Quantity.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DemandUOM:str = obj["DemandUOM"]
      """  The UOM code that represents the unit of measure in which the quantity is expressed.  """  
      self.AdjustmentQty:int = obj["AdjustmentQty"]
      self.Variance:int = obj["Variance"]
      """  Variance = Company Cumulative Qty - (TP Cumulative Qty + Adjustment)  """  
      self.CUMMSetting:str = obj["CUMMSetting"]
      """  The setting for reconciling cumulative shipping quantities.  """  
      self.DemandContract:str = obj["DemandContract"]
      """  The demand contract this reconcilliation is for.  """  
      self.CustID:str = obj["CustID"]
      """  Contains the Customer ID that the reconcilliation is for.  This must be valid in the Customer table.  """  
      self.AllowDelete:bool = obj["AllowDelete"]
      """  We should allow to delete demand reconciliation records if there are not shipments related to the demand reconciliation  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.DemandContractDemandContract:str = obj["DemandContractDemandContract"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandReconcileTableset:
   def __init__(self, obj):
      self.DemandReconcile:list[Erp_Tablesets_DemandReconcileRow] = obj["DemandReconcile"]
      self.DemReconAdjust:list[Erp_Tablesets_DemReconAdjustRow] = obj["DemReconAdjust"]
      self.DemReconcileShipments:list[Erp_Tablesets_DemReconcileShipmentsRow] = obj["DemReconcileShipments"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDemandReconcileTableset:
   def __init__(self, obj):
      self.DemandReconcile:list[Erp_Tablesets_DemandReconcileRow] = obj["DemandReconcile"]
      self.DemReconAdjust:list[Erp_Tablesets_DemReconAdjustRow] = obj["DemReconAdjust"]
      self.DemReconcileShipments:list[Erp_Tablesets_DemReconcileShipmentsRow] = obj["DemReconcileShipments"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   reconcileNum
   """  
   def __init__(self, obj):
      self.reconcileNum:int = obj["reconcileNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandReconcileTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandReconcileTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandReconcileTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandReconcileListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDemandReconcile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class GetNewDemandReconcile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsSearch_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      pass

class GetRowsSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandReconcileTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDemandReconcile
   whereClauseDemReconAdjust
   whereClauseDemReconcileShipments
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDemandReconcile:str = obj["whereClauseDemandReconcile"]
      self.whereClauseDemReconAdjust:str = obj["whereClauseDemReconAdjust"]
      self.whereClauseDemReconcileShipments:str = obj["whereClauseDemReconcileShipments"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandReconcileTableset] = obj["returnObj"]
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

class RestartCumInfo_input:
   """ Required : 
   iReconcileNum
   """  
   def __init__(self, obj):
      self.iReconcileNum:int = obj["iReconcileNum"]
      """  Reconcile Number  """  
      pass

class RestartCumInfo_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandReconcileTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandReconcileTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandReconcileTableset] = obj["ds"]
      pass

      """  output parameters  """  

