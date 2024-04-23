import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TransOrderReceiptSvc
# Description: Dataset to receive items shipped to another plant using Transfer Order Shipment Process
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderReceipts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TransOrderReceipts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TransOrderReceipts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts",headers=creds) as resp:
           return await resp.json()

async def post_TransOrderReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TransOrderReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TransOrderReceipts_Company_PackNum(Company, PackNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TransOrderReceipt item
   Description: Calls GetByID to retrieve the TransOrderReceipt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TransOrderReceipt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TransOrderReceipts_Company_PackNum(Company, PackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TransOrderReceipt for the service
   Description: Calls UpdateExt to update TransOrderReceipt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TransOrderReceipt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TransOrderReceipts_Company_PackNum(Company, PackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TransOrderReceipt item
   Description: Call UpdateExt to delete TransOrderReceipt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TransOrderReceipt
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderReceipts_Company_PackNum_TFShipDtls(Company, PackNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TFShipDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TFShipDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")/TFShipDtls",headers=creds) as resp:
           return await resp.json()

async def get_TransOrderReceipts_Company_PackNum_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TransOrderReceipts(" + Company + "," + PackNum + ")/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TFShipDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TFShipDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls",headers=creds) as resp:
           return await resp.json()

async def post_TFShipDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TFShipDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TFShipDtl item
   Description: Calls GetByID to retrieve the TFShipDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TFShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TFShipDtl for the service
   Description: Calls UpdateExt to update TFShipDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TFShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TFShipDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TFShipDtls_Company_PackNum_PackLine(Company, PackNum, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TFShipDtl item
   Description: Call UpdateExt to delete TFShipDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TFShipDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls_Company_PackNum_PackLine_PlantTrans(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlantTrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantTrans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/PlantTrans",headers=creds) as resp:
           return await resp.json()

async def get_TFShipDtls_Company_PackNum_PackLine_PlantTrans_Company_TranNum(Company, PackNum, PackLine, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantTran item
   Description: Calls GetByID to retrieve the PlantTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantTran1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/TFShipDtls(" + Company + "," + PackNum + "," + PackLine + ")/PlantTrans(" + Company + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlantTrans(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlantTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantTrans
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans",headers=creds) as resp:
           return await resp.json()

async def post_PlantTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlantTrans_Company_TranNum(Company, TranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlantTran item
   Description: Calls GetByID to retrieve the PlantTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans(" + Company + "," + TranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlantTrans_Company_TranNum(Company, TranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlantTran for the service
   Description: Calls UpdateExt to update PlantTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans(" + Company + "," + TranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlantTrans_Company_TranNum(Company, TranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlantTran item
   Description: Call UpdateExt to delete PlantTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantTran
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/PlantTrans(" + Company + "," + TranNum + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TFShipHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTFShipHead, whereClauseTFShipDtl, whereClausePlantTran, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTFShipHead=" + whereClauseTFShipHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTFShipDtl=" + whereClauseTFShipDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlantTran=" + whereClausePlantTran
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(packNum, epicorHeaders = None):
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
   params += "packNum=" + packNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantTranAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantTranAssemblySeq
   Description: This methods updates fields associated with PlantTran.AssemblySeq field.
This method should run when the PlantTran.AssemblySeq field changes.
   OperationID: ChangePlantTranAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantTranJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantTranJobMtl
   Description: This methods assigns fields associated with PlantTran.JobMtl changing.
This method should run before the PlantTran.JobMtl field changes.
   OperationID: ChangePlantTranJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantTranJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantTranJobNum
   Description: This methods assigns fields associated with PlantTran.JobNum changing.
This method should run before the PlantTran.JobNum field changes.
   OperationID: ChangePlantTranJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantTranReceivedTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantTranReceivedTo
   Description: This methods updates fields associated with PlantTran.ReceiveTo field.
This method should run when the PlantTran.ReceiveTo field changes.
   OperationID: ChangePlantTranReceivedTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranReceivedTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranReceivedTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantTranReceivedToBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantTranReceivedToBinNum
   Description: This methods changes the BinNumDescription when changing the PlantTran.BinNum
This method should run before the PlantTran.BinNum field changes.
   OperationID: ChangePlantTranReceivedToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranReceivedToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranReceivedToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlantTranReceivedToWhseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlantTranReceivedToWhseCode
   Description: This methods changes the ReceiveToBinNum when changing the PlantTran.ReceiveToWhseCode
This method should run before the PlantTran.ReceiveToWhseCode field changes.
   OperationID: ChangePlantTranReceivedToWhseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlantTranReceivedToWhseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlantTranReceivedToWhseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlantTranJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlantTranJobMtl
   Description: This methods validates the JobMtl when changing the PlantTran.JobMtl
This method should run before the PlantTran.JobMtl field changes.
   OperationID: CheckPlantTranJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlantTranJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlantTranJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlantTranJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlantTranJobNum
   Description: This methods validates the JobNum when changing the PlantTran.JobNum
This method should run before the PlantTran.JobNum field changes.
   OperationID: CheckPlantTranJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlantTranJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlantTranJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPlantTranReceivedToBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPlantTranReceivedToBinNum
   Description: This methods validates the BinNum when changing the PlantTran.BinNum
This method should run before the PlantTran.BinNum field changes.
   OperationID: CheckPlantTranReceivedToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPlantTranReceivedToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPlantTranReceivedToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomUpdate
   Description: This is a custom version of the standard Update method.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListBasicSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListBasicSearch
   Description: Returns the Transfer Orders as the GetList does but filtering them out by received or unreceived ones.
   OperationID: GetListBasicSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBasicSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBasicSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListBasicSearchWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListBasicSearchWhereClause
   Description: Returns the Transfer Orders as the GetListBasicSearch does after getting the receipt status from a where clause.
   OperationID: GetListBasicSearchWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListBasicSearchWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListBasicSearchWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsLandingPage(epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsLandingPage
   Description: Returns all Transfer Orders filtered by ToPlant and set their TransStatusDescription.
   OperationID: GetRowsLandingPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SetReceiptDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetReceiptDates
   Description: Set or clear Receipt Date
   OperationID: SetReceiptDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetReceiptDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetReceiptDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartPlantPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartPlantPKs
   Description: Returns a string with the PartTranPKs list to send to the report screen.
   OperationID: GetPartPlantPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartPlantPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartPlantPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetAllLinesSameWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetAllLinesSameWhseBin
   Description: Set the same warehouse bin for all the lines.
   OperationID: SetAllLinesSameWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetAllLinesSameWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetAllLinesSameWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="attributeSetID"></param><param name="ipQuantity">ipQuantity</param><param name="ipUOM">ipUOM</param><param name="ipOrderNum">ipOrderNum</param><param name="ipOrderLine">ipOrderLine</param><param name="ipPackSlip">ipPackSlip</param><param name="ipPackSlipLine">ipPackSlipLine</param><param name="ipReceivedTo">ipReceivedTo</param><returns></returns>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransferOrders(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransferOrders
   Description: Returns the Transfer Orders as the GetRows does but filtering them out by received or unreceived ones.
   OperationID: GetTransferOrders
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreReceiptPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreReceiptPCID
   Description: This method will return true if ParentFromPCID has more that one child
   OperationID: PreReceiptPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreReceiptPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreReceiptPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTFShipDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTFShipDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTFShipDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTFShipDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTFShipDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlantTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlantTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlantTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TransOrderReceiptSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantTranRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlantTranRow] = obj["value"]
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

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TFShipHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TFShipHeadRow] = obj["value"]
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

class Erp_Tablesets_PlantTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) the record was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID  """  
      self.TranStatus:str = obj["TranStatus"]
      """   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transfer is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the "From" Bin location that this transfer affected.  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  The Job that the material is being transferred from.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  The Job Assembly (zero for final assembly) that the material is being transferred from.  """  
      self.WarehseCodeTo:str = obj["WarehseCodeTo"]
      """  The Warehouse the part is being transferred To.  """  
      self.JobNum:str = obj["JobNum"]
      """  "To" Job Number that this transfer is associated with, if any.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence associated with the JobNum.  """  
      self.JobMtl:int = obj["JobMtl"]
      """  Sequence number of the specific Job Material record.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transfer Quantity.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  From Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.PlntTranReference:str = obj["PlntTranReference"]
      """  Used to hold a short comment on the Site transfer.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.RecSysDate:str = obj["RecSysDate"]
      """  System date at time that record was received.  """  
      self.RecSysTime:int = obj["RecSysTime"]
      """  System Time (hr-min-sec) when transaction was received.  """  
      self.RecTranDate:str = obj["RecTranDate"]
      """  date of receipt transaction.  """  
      self.RecEntryPerson:str = obj["RecEntryPerson"]
      """  This field is set equal to the Login ID variable.  It cannot be overridden.  """  
      self.RecIssuedComplete:bool = obj["RecIssuedComplete"]
      """  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  PCID to receive from  """  
      self.ToPCID:str = obj["ToPCID"]
      """  PCID to receive to  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.calcDimTranQty:int = obj["calcDimTranQty"]
      self.calcRequiredQty:int = obj["calcRequiredQty"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The generated legal number  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      """  Part tran record's primary key - for the later use in the report  """  
      self.ReceiveIssueComplete:bool = obj["ReceiveIssueComplete"]
      self.ReceiveTo:str = obj["ReceiveTo"]
      """  Where to receive item to? (Values:  Stock or Job)  """  
      self.ReceiveToBinNum:str = obj["ReceiveToBinNum"]
      """  The bin num to receive to.  """  
      self.ReceiveToDescription:str = obj["ReceiveToDescription"]
      """  ReceiveToDescription  """  
      self.ReceiveToWhseCode:str = obj["ReceiveToWhseCode"]
      """  The warehouse code to receive to.  """  
      self.ReceiveToWhseDescription:str = obj["ReceiveToWhseDescription"]
      """  ReceiveToWhseDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.SerialNumTranType:str = obj["SerialNumTranType"]
      self.SerialProcessing:bool = obj["SerialProcessing"]
      self.TFRequestedQty:int = obj["TFRequestedQty"]
      self.TFRequestedQtyUOM:str = obj["TFRequestedQtyUOM"]
      self.ThisInvtyUOM:str = obj["ThisInvtyUOM"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.ParentFromPCID:str = obj["ParentFromPCID"]
      """  Parent PCID to the FromPCID field.  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
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

class Erp_Tablesets_TFShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is defaulted as Job Number.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.requestdate:str = obj["requestdate"]
      """  requestdate  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Calculated price for the item being transferred.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AllocatedShippedQty:int = obj["AllocatedShippedQty"]
      """  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      """  Are there available serial numbers?  """  
      self.direct_transfer:bool = obj["direct_transfer"]
      """  direct-transfer  """  
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockShippedQty * DimConvFactor  """  
      self.LineShipped:bool = obj["LineShipped"]
      """  Indicates if the Shipment line has been shipped  """  
      self.OrderShipmentQty:int = obj["OrderShipmentQty"]
      """  Current Shipment in OrderUOM  """  
      self.OrderUOM:str = obj["OrderUOM"]
      """  UOM from Transfer Order  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by the freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by the freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by the freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by the freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by the freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by the freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by the freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by the freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by the freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by the freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by the freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by the freight web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by the freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by the freight web service  """  
      self.Received:bool = obj["Received"]
      """  Indicates if the Shipment line has been received  """  
      self.RemainingQty:int = obj["RemainingQty"]
      """  The remaining quantity  """  
      self.RequestQty:int = obj["RequestQty"]
      """  The request quantity  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  The shipped quantity  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      """  Enable Attribute Set Search  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
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
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
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
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.PackClssDescription:str = obj["PackClssDescription"]
      """  Full description of the Packaging Classification.  """  
      self.PackingDescription:str = obj["PackingDescription"]
      """  Full description of Packing Code.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
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
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
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
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.AGShippingWay:str = obj["AGShippingWay"]
      """  AGShippingWay  """  
      self.AGCOTMark:bool = obj["AGCOTMark"]
      """  AGCOTMark  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Creation date and time  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Certificate Serial Number  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Certificate  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  Fiscal Folio (UUID)  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  SAT Certificate Serial Number  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Digital Seal  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  SAT Seal  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  Original String  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  TFD Original String  """  
      self.MXSerie:str = obj["MXSerie"]
      """  Serie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Arrival  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.DriverID:str = obj["DriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.VNAccordingToDemand:str = obj["VNAccordingToDemand"]
      self.VNCarrier:str = obj["VNCarrier"]
      self.VNContractNumber:str = obj["VNContractNumber"]
      self.VNDate:str = obj["VNDate"]
      self.VNFor:str = obj["VNFor"]
      self.VNFrom:str = obj["VNFrom"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Logical indicating if the package control functionality should be enabled.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer order number  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.AGLegalNumCnfgDescription:str = obj["AGLegalNumCnfgDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.PackClssDescription:str = obj["PackClssDescription"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangePlantTranAssemblySeq_input:
   """ Required : 
   TranNum
   ipProposedAssemblySeq
   ds
   """  
   def __init__(self, obj):
      self.TranNum:int = obj["TranNum"]
      """  Transaction line to check  """  
      self.ipProposedAssemblySeq:int = obj["ipProposedAssemblySeq"]
      """  The new proposed PlantTran.AssemblySeq value  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class ChangePlantTranAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantTranJobMtl_input:
   """ Required : 
   tranNum
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class ChangePlantTranJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantTranJobNum_input:
   """ Required : 
   tranNum
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class ChangePlantTranJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantTranReceivedToBinNum_input:
   """ Required : 
   tranNum
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class ChangePlantTranReceivedToBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantTranReceivedToWhseCode_input:
   """ Required : 
   tranNum
   ipProposedWhseCode
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ipProposedWhseCode:str = obj["ipProposedWhseCode"]
      """  The new proposed PlantTran.WhseCode value  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class ChangePlantTranReceivedToWhseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePlantTranReceivedTo_input:
   """ Required : 
   tranNum
   ipProposedReceiveTo
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ipProposedReceiveTo:str = obj["ipProposedReceiveTo"]
      """  The new proposed PlantTran.ReceiveTo value
            (values: STOCK or JOB)  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class ChangePlantTranReceivedTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPlanningContractBin_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class CheckPlanningContractBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      self.pcPCBinAction:str = obj["parameters"]
      self.pcPCBinMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckPlantTranJobMtl_input:
   """ Required : 
   tranNum
   ipProposedJobMtl
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ipProposedJobMtl:int = obj["ipProposedJobMtl"]
      """  The new proposed PlantTran.JobMtl value  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class CheckPlantTranJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPlantTranJobNum_input:
   """ Required : 
   tranNum
   ipProposedJobNum
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ipProposedJobNum:str = obj["ipProposedJobNum"]
      """  The new proposed PlantTran.JobNum value  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class CheckPlantTranJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPlantTranReceivedToBinNum_input:
   """ Required : 
   tranNum
   ipProposedBinNum
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction line to check  """  
      self.ipProposedBinNum:str = obj["ipProposedBinNum"]
      """  The new proposed PlantTran.BinNum value  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class CheckPlantTranReceivedToBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CustomUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class CustomUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      self.opLegalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
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

class Erp_Tablesets_PlantTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) the record was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique ID  """  
      self.TranStatus:str = obj["TranStatus"]
      """   Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transfer is for.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. The user does not directly enter this. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part,JobOPer,JobMtl, ShipDtl, SubShipD ....  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Site that the transfer is from.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site that the transfer is to.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the "From" Bin location that this transfer affected.  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  The Job that the material is being transferred from.  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  The Job Assembly (zero for final assembly) that the material is being transferred from.  """  
      self.WarehseCodeTo:str = obj["WarehseCodeTo"]
      """  The Warehouse the part is being transferred To.  """  
      self.JobNum:str = obj["JobNum"]
      """  "To" Job Number that this transfer is associated with, if any.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence associated with the JobNum.  """  
      self.JobMtl:int = obj["JobMtl"]
      """  Sequence number of the specific Job Material record.  """  
      self.TranQty:int = obj["TranQty"]
      """  Transfer Quantity.  """  
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  """  
      self.LotNum:str = obj["LotNum"]
      """  From Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.PlntTranReference:str = obj["PlntTranReference"]
      """  Used to hold a short comment on the Site transfer.  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It cannot be overridden.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
J = Job
I = Inventory
TO = Transfer Order  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """   Internal Selling Price.  The total price associated with the activity of moving an item from one Site to another. Calculated when the material is sent.
Calculated as Quantity * (InternalUnitPrice/PricePer).
This price will be duplicated to the related P  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack ID  """  
      self.RecSysDate:str = obj["RecSysDate"]
      """  System date at time that record was received.  """  
      self.RecSysTime:int = obj["RecSysTime"]
      """  System Time (hr-min-sec) when transaction was received.  """  
      self.RecTranDate:str = obj["RecTranDate"]
      """  date of receipt transaction.  """  
      self.RecEntryPerson:str = obj["RecEntryPerson"]
      """  This field is set equal to the Login ID variable.  It cannot be overridden.  """  
      self.RecIssuedComplete:bool = obj["RecIssuedComplete"]
      """  For Inter-Site receipts to a job material/assembly only.  Indicates if this material requirement has been issued complete.  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.MtlMtlBurUnitCost:int = obj["MtlMtlBurUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a TF Packing slip. This is assigned by the system. Read last TFShipDtl record for PackNum and add 1.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  PCID to receive from  """  
      self.ToPCID:str = obj["ToPCID"]
      """  PCID to receive to  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.calcDimTranQty:int = obj["calcDimTranQty"]
      self.calcRequiredQty:int = obj["calcRequiredQty"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  The generated legal number  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      """  Part tran record's primary key - for the later use in the report  """  
      self.ReceiveIssueComplete:bool = obj["ReceiveIssueComplete"]
      self.ReceiveTo:str = obj["ReceiveTo"]
      """  Where to receive item to? (Values:  Stock or Job)  """  
      self.ReceiveToBinNum:str = obj["ReceiveToBinNum"]
      """  The bin num to receive to.  """  
      self.ReceiveToDescription:str = obj["ReceiveToDescription"]
      """  ReceiveToDescription  """  
      self.ReceiveToWhseCode:str = obj["ReceiveToWhseCode"]
      """  The warehouse code to receive to.  """  
      self.ReceiveToWhseDescription:str = obj["ReceiveToWhseDescription"]
      """  ReceiveToWhseDescription  """  
      self.RequiredQty:int = obj["RequiredQty"]
      """  The required quantity  """  
      self.SerialNumTranType:str = obj["SerialNumTranType"]
      self.SerialProcessing:bool = obj["SerialProcessing"]
      self.TFRequestedQty:int = obj["TFRequestedQty"]
      self.TFRequestedQtyUOM:str = obj["TFRequestedQtyUOM"]
      self.ThisInvtyUOM:str = obj["ThisInvtyUOM"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.ParentFromPCID:str = obj["ParentFromPCID"]
      """  Parent PCID to the FromPCID field.  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  System Transaction Type: StockWIP/StockStock is used in the filter of TranDocType combo-box.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
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

class Erp_Tablesets_TFShipDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped. Duplicated from OrderDtl.PartNum at time of creation. This is not user maintainable. If this is a shipment from inventory use this part number to reduce the Part.Onhand qty.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Description  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure...duplicated from the OrderDtl.IUM...Not user maintainable.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.ShipCmpl:bool = obj["ShipCmpl"]
      """  Indicates if this shipment should mark the order release as being shipped complete. Only one ShipDtl for a release can be marked as being complete. As the user toggles this field it also sets the OrderRel.ShipCmpl field and adjusts the PartBin.OnHand, PartWhse.AllocQty if necessary.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """   Indicates the warehouse from which the quantity was shipped. This is only valid if the ShipDtl.Inventory quantity is > 0 and this is a valid part number.

The default should be retrieved from the OrderDtl.WareHseCode. .  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.UpdatedInventory:bool = obj["UpdatedInventory"]
      """  Indicates if this transaction affected inventory at time of creation.  """  
      self.NetWeightUOM:str = obj["NetWeightUOM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...).  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is defaulted as Job Number.  """  
      self.TotalNetWeight:int = obj["TotalNetWeight"]
      """  The Part's Net Weight * (SellingJobShipQty + SellingInventoryShipQty)  """  
      self.WIPWarehouseCode:str = obj["WIPWarehouseCode"]
      """   Identifies the warehouse for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area warehouse (Site.DefShipWhse) otherwise it's blank.  """  
      self.WIPBinNum:str = obj["WIPBinNum"]
      """   Identifies the warehouse bin for WIP shipments. Valid only when ShipDtl.OurJobShippedQty is > 0 and the Adv Mtl Mgt module is installed.
When AM is installed this is defaulted as the Shipping Area bin (Site.DefShipBin) otherwise it's blank.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  This field along with Company and TFOrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  Quantity ,using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  Actual quantity ,using Our U/M, shipped from Stock.  Updated via the shipping process.  """  
      self.requestdate:str = obj["requestdate"]
      """  requestdate  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  """  
      self.TFLineNum:str = obj["TFLineNum"]
      """  This is the unique key for this table.  It will have a prefix like Job to indicate firm or unfirm orders.  The record can be linked to an Order Header by using the TFOrdNum TFOrdSeq keys.  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  Unit price discount percent.  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """   Indicates the pricing per quantity.  It can be "E" = per each,
"C" = per hundred,  "M" = per thousand.  Used to calculate the extended unit price for the line item.  The logic is to divide the InvcDtl.ShipQty by the appropriate "per" value and then multiply by unit price.  Use the OrderDtl.PricePerCode as default if referenced to an order else use Part.PricePerCode as a default.  If Part record does not exist then default as "E".  """  
      self.Discount:int = obj["Discount"]
      """  A flat discount amount for the line item.  It can be zero.  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  A flat discount amount for the line item.  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Reporting currency value of this field  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Reporting currency value of this field  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.DocExtPrice:int = obj["DocExtPrice"]
      """  Extended Price for the invoice line item.  """  
      self.Rpt1ExtPrice:int = obj["Rpt1ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2ExtPrice:int = obj["Rpt2ExtPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3ExtPrice:int = obj["Rpt3ExtPrice"]
      """  Reporting currency value of this field  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  Calculated price for the item being transferred.  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  Unit Price.  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Reporting currency value of this field  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Reporting currency value of this field  """  
      self.PickedAutoAllocatedQty:int = obj["PickedAutoAllocatedQty"]
      """  Quantity picked from inventory that was not manually allocated. This quantity is automatically added to PartAlloc such when inventory is picked, it is considered allocated to this Transfer Order.  This quantity is in the IUM unit of measure.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AllocatedShippedQty:int = obj["AllocatedShippedQty"]
      """  If AMM is licensed this column will hold how much of this shipment was allocated prior to the shipment in case this shipment is ever "unshipped"  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.MXEstValue:int = obj["MXEstValue"]
      """  Estimated Value  """  
      self.MXEstValueCurrencyCode:str = obj["MXEstValueCurrencyCode"]
      """  Estimated Value Currency  """  
      self.MXHazardousShipment:bool = obj["MXHazardousShipment"]
      """  Hazardous Shipment  """  
      self.MXHazardousType:str = obj["MXHazardousType"]
      """  Hazardous Type  """  
      self.MXPackageType:str = obj["MXPackageType"]
      """  Package Type  """  
      self.AvailSerialNumbers:bool = obj["AvailSerialNumbers"]
      """  Are there available serial numbers?  """  
      self.direct_transfer:bool = obj["direct_transfer"]
      """  direct-transfer  """  
      self.DisplayShipQty:int = obj["DisplayShipQty"]
      """  OurStockShippedQty * DimConvFactor  """  
      self.LineShipped:bool = obj["LineShipped"]
      """  Indicates if the Shipment line has been shipped  """  
      self.OrderShipmentQty:int = obj["OrderShipmentQty"]
      """  Current Shipment in OrderUOM  """  
      self.OrderUOM:str = obj["OrderUOM"]
      """  UOM from Transfer Order  """  
      self.PartAESExp:str = obj["PartAESExp"]
      """  Used by the freight web service  """  
      self.PartECNNumber:str = obj["PartECNNumber"]
      """  Used by the freight web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freight web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  used by freight web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by the freight web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by the freight web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by the freight web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by the freight web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      """  Used by the freight web service  """  
      self.PartHazTechName:str = obj["PartHazTechName"]
      """  Used by the freight web service  """  
      self.PartHTS:str = obj["PartHTS"]
      """  Used by the freight web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by the freight web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by the freight web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by the freight web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by the freight web service  """  
      self.PartSchedBcode:str = obj["PartSchedBcode"]
      """  Used by the freight web service  """  
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      """  Used by the freight web service  """  
      self.Received:bool = obj["Received"]
      """  Indicates if the Shipment line has been received  """  
      self.RemainingQty:int = obj["RemainingQty"]
      """  The remaining quantity  """  
      self.RequestQty:int = obj["RequestQty"]
      """  The request quantity  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  The shipped quantity  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Ship Status of the Transfer Order Shipment line, copied from the Transfer Order Shipment header.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      """  Enable Attribute Set Search  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
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
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
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
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.PackClssDescription:str = obj["PackClssDescription"]
      """  Full description of the Packaging Classification.  """  
      self.PackingDescription:str = obj["PackingDescription"]
      """  Full description of Packing Code.  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TFShipHeadListTableset:
   def __init__(self, obj):
      self.TFShipHeadList:list[Erp_Tablesets_TFShipHeadListRow] = obj["TFShipHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TFShipHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
      self.ShipPerson:str = obj["ShipPerson"]
      """  Short name or initials of person who actually did the shipping.  An optional field which can be used for internal reference.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Initials (user ID) of the person who did the data entry. This can be used as a selection criteria when "batch" printing packing slips so that users can print packing slips that only they entered. This defaults as current user ID, but can be changed.  """  
      self.ShipLog:str = obj["ShipLog"]
      """  An optional field which can be used to enter a shipping log reference #.  """  
      self.LabelComment:str = obj["LabelComment"]
      """  An optional field that will be printed on the shipping labels for this packing slip.  """  
      self.ShipComment:str = obj["ShipComment"]
      """  Packing slip comments.  This will print on the Packing Slip.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.ExternalDeliveryNote:bool = obj["ExternalDeliveryNote"]
      """  This flag indicates if an external delivery note is required.  This field is available only when send shipments for financial integration is turned on.  When checked, the shipment will be sent to an external financial system where a legal number will be generated.  The shipment will then be sent back with the legal number and processing will continue as normal.  When checked, the shipment is not available to be marked as shipped until a legal number has been assigned.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  External  ID  """  
      self.directtransfer:bool = obj["directtransfer"]
      """  directtransfer  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Site Identifier.  This field cannot be blank.  """  
      self.Shipped:bool = obj["Shipped"]
      """  Shipped flag  """  
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
      self.MFTransNum:str = obj["MFTransNum"]
      """  Transaction Number returned by the Manifest Engine  """  
      self.MFCallTag:str = obj["MFCallTag"]
      """  Manifest Call Tag Number  """  
      self.MFPickupNum:str = obj["MFPickupNum"]
      """  Manifest Pickup Number  """  
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      """  Manifest Discount Freight Amount  """  
      self.MFTemplate:str = obj["MFTemplate"]
      """  Manifest Template Code  """  
      self.MFUse3B:bool = obj["MFUse3B"]
      """  Manifest flag to use 3 party billing  """  
      self.MF3BAccount:str = obj["MF3BAccount"]
      """  Manifest's 3rd Party Billing Account  """  
      self.MFDimWeight:int = obj["MFDimWeight"]
      """  Manifest Dimension Weight  """  
      self.MFZone:str = obj["MFZone"]
      """  Manifest Delivery Zone  """  
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      """  Manifest Published Freight Amount  """  
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      """  Manifest Other Amount  """  
      self.MFOversized:bool = obj["MFOversized"]
      """  Manifest Oversized flag  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  Status of the shipment.  Some of the valid values are Open, Closed, Freighted, Void, Staged, Shipped  """  
      self.ShipGroup:str = obj["ShipGroup"]
      """  Group the shipment belongs to for "Staging"  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Package Code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
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
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that the part was shipped from. Must be valid in the WhseBin table or can be blank.  """  
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.HazardousShipment:bool = obj["HazardousShipment"]
      """  International Shipping - HazardousShipment  """  
      self.PayFlag:str = obj["PayFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping, The city portion of the Payer main address.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  The state or province portion of the shipment payer main address.  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  The zip or postal code portion of the shipping payers main address.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  The country of the main shipping payers address.  """  
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  International Shipping. The first line of the Frieght Forwarder main address.  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  International Shipping. The second line of the Frieght Forwarder main address.  """  
      self.FFCity:str = obj["FFCity"]
      """  Shipping, The city portion of the Frieght Forwarder main address.  """  
      self.FFState:str = obj["FFState"]
      """  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  """  
      self.FFZip:str = obj["FFZip"]
      """  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  """  
      self.FFCountry:str = obj["FFCountry"]
      """  International shipping. The country of the Frieght Forwarder .  """  
      self.FFContact:str = obj["FFContact"]
      """  International Shipping. Frieght Forwarder Contact  """  
      self.FFCompName:str = obj["FFCompName"]
      """  International Shipping. Frieght Forwarder company name  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  International Shipping. Frieght Forwarder Phone number  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Freight Forwarder Third address line  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country portion of the address  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Payer Bill To Third Address line  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Payer Bill To Country Number  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Payer Bill To Phone Number  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Yes indicates this pack consists of phantom packs and the user does not care about what is shipped.  The shipment is shipped as a "masterpack" without being a master pack.  If no, the shipment follows normal shipping logic.  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      """   Unit of measure used to qualify the PkgLenth, PkgHeight, PkgWidth.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.ManifestSizeUOM:str = obj["ManifestSizeUOM"]
      """  Unit of Measure the Manifest system expects the pack sizet to be measured in.  """  
      self.ManifestWtUOM:str = obj["ManifestWtUOM"]
      """  Unit of Measure of the Manifest system expects the pack to be weighed in.  """  
      self.ManifestWeight:int = obj["ManifestWeight"]
      """  Package Weight in the Manifest System's unit of measure.  """  
      self.ManifestLength:int = obj["ManifestLength"]
      """  The pack length in the Manifest Unit of Measure.  """  
      self.ManifestWidth:int = obj["ManifestWidth"]
      """  The pack width in the manifest unit of measure.  """  
      self.ManifestHeight:int = obj["ManifestHeight"]
      """  The pack height in the manifest unit of measure.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Indicates the inventory warehouse in the ShipTo Site.  """  
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGAuthorizationCode:str = obj["AGAuthorizationCode"]
      """  AGAuthorizationCode  """  
      self.AGAuthorizationDate:str = obj["AGAuthorizationDate"]
      """  AGAuthorizationDate  """  
      self.AGCarrierCUIT:str = obj["AGCarrierCUIT"]
      """  AGCarrierCUIT  """  
      self.AGDocumentLetter:str = obj["AGDocumentLetter"]
      """  AGDocumentLetter  """  
      self.AGInvoicingPoint:str = obj["AGInvoicingPoint"]
      """  AGInvoicingPoint  """  
      self.AGLegalNumber:str = obj["AGLegalNumber"]
      """  AGLegalNumber  """  
      self.AGPrintingControlType:str = obj["AGPrintingControlType"]
      """  AGPrintingControlType  """  
      self.AGTrackLicense:str = obj["AGTrackLicense"]
      """  AGTrackLicense  """  
      self.AGShippingWay:str = obj["AGShippingWay"]
      """  AGShippingWay  """  
      self.AGCOTMark:bool = obj["AGCOTMark"]
      """  AGCOTMark  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.DigitalSignature:str = obj["DigitalSignature"]
      """  DigitalSignature  """  
      self.SignedOn:str = obj["SignedOn"]
      """  SignedOn  """  
      self.SignedBy:str = obj["SignedBy"]
      """  SignedBy  """  
      self.FirstPrintDate:str = obj["FirstPrintDate"]
      """  FirstPrintDate  """  
      self.DocCopyNum:int = obj["DocCopyNum"]
      """  DocCopyNum  """  
      self.MXCertifiedTimestamp:str = obj["MXCertifiedTimestamp"]
      """  Creation date and time  """  
      self.MXCertificateSN:str = obj["MXCertificateSN"]
      """  Certificate Serial Number  """  
      self.MXCertificate:str = obj["MXCertificate"]
      """  Certificate  """  
      self.MXFiscalFolio:str = obj["MXFiscalFolio"]
      """  Fiscal Folio (UUID)  """  
      self.MXSATCertificateSN:str = obj["MXSATCertificateSN"]
      """  SAT Certificate Serial Number  """  
      self.MXDigitalSeal:str = obj["MXDigitalSeal"]
      """  Digital Seal  """  
      self.MXSATSeal:str = obj["MXSATSeal"]
      """  SAT Seal  """  
      self.MXOriginalString:str = obj["MXOriginalString"]
      """  Original String  """  
      self.MXOriginalStringTFD:str = obj["MXOriginalStringTFD"]
      """  TFD Original String  """  
      self.MXSerie:str = obj["MXSerie"]
      """  Serie  """  
      self.MXFolio:str = obj["MXFolio"]
      """  Folio  """  
      self.MXETD:str = obj["MXETD"]
      """  Estimated Date and Time of Departure  """  
      self.MXETA:str = obj["MXETA"]
      """  Estimated Date and Time of Arrival  """  
      self.MXDistance:int = obj["MXDistance"]
      """  Distance in Km  """  
      self.MXPermitType:str = obj["MXPermitType"]
      """  Permit Type  """  
      self.MXPermitNum:str = obj["MXPermitNum"]
      """  Permit Number  """  
      self.MXCartaPorteStatus:str = obj["MXCartaPorteStatus"]
      """  Carta Porte Status  """  
      self.VehicleLicensePlate:str = obj["VehicleLicensePlate"]
      """  Vehicle License Plate  """  
      self.VehicleType:str = obj["VehicleType"]
      """  Vehicle Type  """  
      self.VehicleYear:int = obj["VehicleYear"]
      """  Vehicle Year  """  
      self.DriverID:str = obj["DriverID"]
      """  Driver  """  
      self.MXCancelFiscalFolio:str = obj["MXCancelFiscalFolio"]
      """  MXCancelFiscalFolio  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the value of the items in the carton.  List prices - dscount + sales tax for each item.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number.  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton Width  """  
      self.DspFromAddr:str = obj["DspFromAddr"]
      """  Display for the Ship From Address  """  
      self.DspShipAddr:str = obj["DspShipAddr"]
      """  Display for the Ship To Address  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableShipped:bool = obj["EnableShipped"]
      """  Flag to control if the Shipped flag is enabled/disabled  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if the transaction document type is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for subcontract shipments  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  Set to Y if the carton is the last one being shiped to the customer.  Set to N when the sum of the quantity packed does not equl the quantity ordered for each line.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  Zero indicates the height prompt is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  1 = disable / 0 = enable  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width is enabled.  """  
      self.SlipStatus:str = obj["SlipStatus"]
      """  Translated field of ShipStatus  """  
      self.TranStatus:str = obj["TranStatus"]
      """  Indicates if the material has been received at the destination.
Valid values are "Open" and "Closed".  """  
      self.TranStatusDescription:str = obj["TranStatusDescription"]
      """  Extended description for the TranStatus that comes from PlantTran table. Where 'Open' = 'Not Received', 'Closed' = 'Received' and '' = 'Not Shipped'  """  
      self.VNAccordingToDemand:str = obj["VNAccordingToDemand"]
      self.VNCarrier:str = obj["VNCarrier"]
      self.VNContractNumber:str = obj["VNContractNumber"]
      self.VNDate:str = obj["VNDate"]
      self.VNFor:str = obj["VNFor"]
      self.VNFrom:str = obj["VNFrom"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.CalcPSPrices:bool = obj["CalcPSPrices"]
      """  Intended for internal use.  Indicates if prices are to be calculated  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Logical indicating if the package control functionality should be enabled.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer order number  """  
      self.MXETADate:str = obj["MXETADate"]
      """  Estimated Date of Arrival  """  
      self.MXETATime:int = obj["MXETATime"]
      """  Estimated Time of Arrival  """  
      self.MXETDDate:str = obj["MXETDDate"]
      """  Estimated Date of Departure  """  
      self.MXETDTime:int = obj["MXETDTime"]
      """  Estimated Time of Departure  """  
      self.EnablePhantom:bool = obj["EnablePhantom"]
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.AGLegalNumCnfgDescription:str = obj["AGLegalNumCnfgDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.PackClssDescription:str = obj["PackClssDescription"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TransOrderReceiptTableset:
   def __init__(self, obj):
      self.TFShipHead:list[Erp_Tablesets_TFShipHeadRow] = obj["TFShipHead"]
      self.TFShipDtl:list[Erp_Tablesets_TFShipDtlRow] = obj["TFShipDtl"]
      self.PlantTran:list[Erp_Tablesets_PlantTranRow] = obj["PlantTran"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTransOrderReceiptTableset:
   def __init__(self, obj):
      self.TFShipHead:list[Erp_Tablesets_TFShipHeadRow] = obj["TFShipHead"]
      self.TFShipDtl:list[Erp_Tablesets_TFShipDtlRow] = obj["TFShipDtl"]
      self.PlantTran:list[Erp_Tablesets_PlantTranRow] = obj["PlantTran"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
      pass

class GetListBasicSearchWhereClause_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  WhereClause containing the receipt status  """  
      self.pageSize:int = obj["pageSize"]
      """  Number of records to retrieve.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page Number.  """  
      pass

class GetListBasicSearchWhereClause_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TFShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListBasicSearch_input:
   """ Required : 
   Received
   pageSize
   absolutePage
   startsWith
   """  
   def __init__(self, obj):
      self.Received:bool = obj["Received"]
      """  Flag to specify if we want to return Received Transfer Orders, false to return the Unreceived ones.  """  
      self.pageSize:int = obj["pageSize"]
      """  Number of records to retrieve.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page Number.  """  
      self.startsWith:int = obj["startsWith"]
      """  Filter out PackNums lesser than this number.  """  
      pass

class GetListBasicSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TFShipHeadListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TFShipHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPlantTran_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class GetNewPlantTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipDtl_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewTFShipDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTFShipHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class GetNewTFShipHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartPlantPKs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class GetPartPlantPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsLandingPage_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseTFShipHead
   whereClauseTFShipDtl
   whereClausePlantTran
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTFShipHead:str = obj["whereClauseTFShipHead"]
      self.whereClauseTFShipDtl:str = obj["whereClauseTFShipDtl"]
      self.whereClausePlantTran:str = obj["whereClausePlantTran"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   attributeSetID
   ipQuantity
   ipUOM
   ipOrderNum
   ipOrderLine
   ipPackSlip
   ipPackSlipLine
   ipReceivedTo
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.ipQuantity:int = obj["ipQuantity"]
      self.ipUOM:str = obj["ipUOM"]
      self.ipOrderNum:str = obj["ipOrderNum"]
      self.ipOrderLine:int = obj["ipOrderLine"]
      self.ipPackSlip:int = obj["ipPackSlip"]
      self.ipPackSlipLine:int = obj["ipPackSlipLine"]
      self.ipReceivedTo:str = obj["ipReceivedTo"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetTransferOrders_input:
   """ Required : 
   Received
   WhereClauseTFShipHead
   WhereClauseTFShipDtl
   WhereClausePlantTran
   WhereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.Received:bool = obj["Received"]
      """  Flag to specify if we want to return Received Transfer Orders, false to return the Unreceived ones.  """  
      self.WhereClauseTFShipHead:str = obj["WhereClauseTFShipHead"]
      """  Where clause to filter the TFShipHead table.  """  
      self.WhereClauseTFShipDtl:str = obj["WhereClauseTFShipDtl"]
      """  Where clause to filter the TFShipDtl table.  """  
      self.WhereClausePlantTran:str = obj["WhereClausePlantTran"]
      """  Where clause to filter the PlantTran table.  """  
      self.WhereClauseLegalNumGenOpts:str = obj["WhereClauseLegalNumGenOpts"]
      """  Where clause to filter the LegalNumGenOpts table.  """  
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      """  Where clause to filter the SelectedSerialNumbers table.  """  
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      """  Where clause to filter the SNFormat table.  """  
      self.PageSize:int = obj["PageSize"]
      """  Number of records to retrieve.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Page Number.  """  
      pass

class GetTransferOrders_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
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

class PreReceiptPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class PreReceiptPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      self.RequiresAllChildPCIDUpdateInput:bool = obj["RequiresAllChildPCIDUpdateInput"]
      self.errorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class SetAllLinesSameWhseBin_input:
   """ Required : 
   tranNum
   ds
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      """  Transaction number  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class SetAllLinesSameWhseBin_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetReceiptDates_input:
   """ Required : 
   packNum
   setDate
   ds
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Current Pack  """  
      self.setDate:bool = obj["setDate"]
      """  Bool to set or clear the receipt date  """  
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class SetReceiptDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransOrderReceiptTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTransOrderReceiptTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TransOrderReceiptTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ipPartNum
   ipSerialNumber
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part number to validate.  """  
      self.ipSerialNumber:str = obj["ipSerialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

