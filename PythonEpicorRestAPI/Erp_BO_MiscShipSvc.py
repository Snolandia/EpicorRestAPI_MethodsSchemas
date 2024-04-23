import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MiscShipSvc
# Description: Miscellaneous Shipment Maintenance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MiscShips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MiscShips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips",headers=creds) as resp:
           return await resp.json()

async def post_MiscShips(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MiscShips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpHdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MscShpHdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum(Company, PackNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MiscShip item
   Description: Calls GetByID to retrieve the MiscShip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MiscShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpHdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MiscShips_Company_PackNum(Company, PackNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MiscShip for the service
   Description: Calls UpdateExt to update MiscShip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MiscShip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpHdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MiscShips_Company_PackNum(Company, PackNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MiscShip item
   Description: Call UpdateExt to delete MiscShip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MiscShip
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_CartonTrkDtls(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CartonTrkDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CartonTrkDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/CartonTrkDtls",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, PackNum, ShipmentType, CaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param CaseNum: Desc: CaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_MscShpDts(Company, PackNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MscShpDts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpDts1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpDts",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_MscShpDts_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpDt item
   Description: Calls GetByID to retrieve the MscShpDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_MscShpUPS(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MscShpUPS items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpUPS1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpUPS",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_MscShpUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpUP item
   Description: Calls GetByID to retrieve the MscShpUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpUP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_MscShpHdAttches(Company, PackNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MscShpHdAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpHdAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpHdAttches",headers=creds) as resp:
           return await resp.json()

async def get_MiscShips_Company_PackNum_MscShpHdAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpHdAttch item
   Description: Calls GetByID to retrieve the MscShpHdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpHdAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MiscShips(" + Company + "," + PackNum + ")/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CartonTrkDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CartonTrkDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CartonTrkDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls",headers=creds) as resp:
           return await resp.json()

async def post_CartonTrkDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CartonTrkDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CartonTrkDtl item
   Description: Calls GetByID to retrieve the CartonTrkDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CartonTrkDtl for the service
   Description: Calls UpdateExt to update CartonTrkDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CartonTrkDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CartonTrkDtls_Company_ShipmentType_PackNum_CaseNum(Company, ShipmentType, PackNum, CaseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CartonTrkDtl item
   Description: Call UpdateExt to delete CartonTrkDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CartonTrkDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ShipmentType: Desc: ShipmentType   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param CaseNum: Desc: CaseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/CartonTrkDtls(" + Company + "," + ShipmentType + "," + PackNum + "," + CaseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_MscShpDts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MscShpDts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpDts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts",headers=creds) as resp:
           return await resp.json()

async def post_MscShpDts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpDts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MscShpDts_Company_PackNum_PackLine(Company, PackNum, PackLine, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpDt item
   Description: Calls GetByID to retrieve the MscShpDt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MscShpDts_Company_PackNum_PackLine(Company, PackNum, PackLine, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MscShpDt for the service
   Description: Calls UpdateExt to update MscShpDt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpDt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpDtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MscShpDts_Company_PackNum_PackLine(Company, PackNum, PackLine, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MscShpDt item
   Description: Call UpdateExt to delete MscShpDt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpDt
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")",headers=creds) as resp:
           return await resp.json()

async def get_MscShpDts_Company_PackNum_PackLine_ShipCOOs(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ShipCOOs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ShipCOOs1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs",headers=creds) as resp:
           return await resp.json()

async def get_MscShpDts_Company_PackNum_PackLine_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, PackNum, PackLine, RelatedToFile, OrigCountry, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def get_MscShpDts_Company_PackNum_PackLine_MscShpDtAttches(Company, PackNum, PackLine, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get MscShpDtAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MscShpDtAttches1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/MscShpDtAttches",headers=creds) as resp:
           return await resp.json()

async def get_MscShpDts_Company_PackNum_PackLine_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpDtAttch item
   Description: Calls GetByID to retrieve the MscShpDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDtAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDts(" + Company + "," + PackNum + "," + PackLine + ")/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ShipCOOs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ShipCOOs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ShipCOOs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs",headers=creds) as resp:
           return await resp.json()

async def post_ShipCOOs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ShipCOOs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ShipCOO item
   Description: Calls GetByID to retrieve the ShipCOO item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ShipCOO for the service
   Description: Calls UpdateExt to update ShipCOO. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ShipCOORow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ShipCOOs_Company_RelatedToFile_PackNum_PackLine_OrigCountry(Company, RelatedToFile, PackNum, PackLine, OrigCountry, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ShipCOO item
   Description: Call UpdateExt to delete ShipCOO item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ShipCOO
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param OrigCountry: Desc: OrigCountry   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/ShipCOOs(" + Company + "," + RelatedToFile + "," + PackNum + "," + PackLine + "," + OrigCountry + ")",headers=creds) as resp:
           return await resp.json()

async def get_MscShpDtAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MscShpDtAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpDtAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches",headers=creds) as resp:
           return await resp.json()

async def post_MscShpDtAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpDtAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpDtAttch item
   Description: Calls GetByID to retrieve the MscShpDtAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpDtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MscShpDtAttch for the service
   Description: Calls UpdateExt to update MscShpDtAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpDtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpDtAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MscShpDtAttches_Company_PackNum_PackLine_DrawingSeq(Company, PackNum, PackLine, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MscShpDtAttch item
   Description: Call UpdateExt to delete MscShpDtAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpDtAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param PackLine: Desc: PackLine   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpDtAttches(" + Company + "," + PackNum + "," + PackLine + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MscShpUPS(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MscShpUPS items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpUPS
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS",headers=creds) as resp:
           return await resp.json()

async def post_MscShpUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MscShpUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpUP item
   Description: Calls GetByID to retrieve the MscShpUP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MscShpUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MscShpUP for the service
   Description: Calls UpdateExt to update MscShpUP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpUPSRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MscShpUPS_Company_PackNum_UPSQVSeq(Company, PackNum, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MscShpUP item
   Description: Call UpdateExt to delete MscShpUP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpUP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpUPS(" + Company + "," + PackNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_MscShpHdAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MscShpHdAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MscShpHdAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches",headers=creds) as resp:
           return await resp.json()

async def post_MscShpHdAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MscShpHdAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MscShpHdAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MscShpHdAttch item
   Description: Calls GetByID to retrieve the MscShpHdAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MscShpHdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MscShpHdAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MscShpHdAttch for the service
   Description: Calls UpdateExt to update MscShpHdAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MscShpHdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MscShpHdAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MscShpHdAttches_Company_PackNum_DrawingSeq(Company, PackNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MscShpHdAttch item
   Description: Call UpdateExt to delete MscShpHdAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MscShpHdAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PackNum: Desc: PackNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/MscShpHdAttches(" + Company + "," + PackNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MscShpHdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMscShpHd, whereClauseMscShpHdAttch, whereClauseMscShpDt, whereClauseMscShpDtAttch, whereClauseShipCOO, whereClauseMscShpUPS, whereClauseCartonTrkDtl, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMscShpHd=" + whereClauseMscShpHd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMscShpHdAttch=" + whereClauseMscShpHdAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMscShpDt=" + whereClauseMscShpDt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMscShpDtAttch=" + whereClauseMscShpDtAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseShipCOO=" + whereClauseShipCOO
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseMscShpUPS=" + whereClauseMscShpUPS
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCartonTrkDtl=" + whereClauseCartonTrkDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number to the miscellaneous shipment.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CalculateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateWeight
   Description: calculate the weight of a carton based upon Part.Weight.
   OperationID: CalculateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CancelVoidCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CancelVoidCarton
   Description: Checks to see if the carton void can be cancelled and re-opens it if it is allowed.
   OperationID: CancelVoidCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CancelVoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CancelVoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCOOPercents(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCOOPercents
   Description: Checks to see if the Qty percent and value percent fields total 100 percent.
   OperationID: CheckCOOPercents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCOOPercents_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCOOPercents_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearConvertedManifest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearConvertedManifest
   Description: Clear MscShpHd Manifest fields when Unfreighting.
   OperationID: ClearConvertedManifest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearConvertedManifest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearConvertedManifest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CloseCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CloseCarton
   Description: Checks to see if the carton can be closed and closes it if it is allowed.
   OperationID: CloseCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CloseCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CloseCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertToManifestUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertToManifestUOM
   Description: Populate MscShpHd Manifest fields.
   OperationID: ConvertToManifestUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertToManifestUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertToManifestUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateMiscShipRecsFromDMR(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateMiscShipRecsFromDMR
   Description: Creates Miscellaneous Shipment Records from DRM Entries. Header and details.
   OperationID: CreateMiscShipRecsFromDMR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateMiscShipRecsFromDMR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateMiscShipRecsFromDMR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CallsCreateCustomerCartons(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CallsCreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipPackNum">Current packNum</param><param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:  Called from Kinetic so first need to dirty rows
   OperationID: CallsCreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CallsCreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CallsCreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateCustomerCartons(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateCustomerCartons
   Description: Purpose:  Create Phantom Customer Cartons
Parameters:
<param name="ipNbrCartonsToCreate">Number of cartons or cases to create</param><param name="ipPkgCode">Package Code to use when creating cartons</param><param name="ipPkgLength">length to use when creating cartons</param><param name="ipPkgWidth">Width to use when creating cartons</param><param name="ipPkgHeight">Height to use when creating cartons</param><param name="ipRecalcAmts">Logical indicating if the amounts are to be recalculated</param><param name="ipZeroWeight">Logical indicating if the weights are recalculated</param><param name="ds"></param>
Notes:
   OperationID: CreateCustomerCartons
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateCustomerCartons_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateCustomerCartons_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CartonValidateWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CartonValidateWeight
   Description: Purpose:
<param name="ipWeight"> weight to validate</param>
Notes:
   OperationID: CartonValidateWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CartonValidateWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CartonValidateWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckValidCartonWeight(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckValidCartonWeight
   Description: Purpose: Ensure the carton weight is valid.
<param name="ipPackNum">Pack Num to validate weights</param>
Notes:
   OperationID: CheckValidCartonWeight
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckValidCartonWeight_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckValidCartonWeight_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCartonPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCartonPackaging
   Description: Purpose: Obtain the carton package specs
<param name="ipPkgCode">package code</param><param name="opPkgHeight">package height</param><param name="opPkgWidth">package width</param><param name="opPkgLength">package length</param>
Notes:
   OperationID: GetCartonPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCartonPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCartonPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackWeightWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackWeightWithCarton
   Description: Purpose:Update the Pack Weight with the carton weight
<param name="ipPackNum">Pack Number to process</param><param name="ipOldWeight">Previous weight</param><param name="ipWeight">Current Case weight</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackWeightWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackWeightWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackWeightWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackCODWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackCODWithCarton
   Description: Purpose: Update pack COD amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero</param><param name="ipOldCOD">Previous COD</param><param name="ipCOD">Current Case COD</param><param name="ipFlag">Current COD flag value</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackCODWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackCODWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackCODWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePackDeclaredWithCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePackDeclaredWithCarton
   Description: Purpose:  Update Pack Delcared Value Amounts
<param name="ipPackNum">Pack Number to process</param><param name="ipCaseNum">Case Number to set value to zero </param><param name="ipOldDeclared">Previous COD</param><param name="ipDeclared">Current Case COD</param><param name="ipDeclaredFlag">current setting of declared insurance</param><param name="ds">Customer Shipment data set</param>
Notes:
   OperationID: UpdatePackDeclaredWithCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePackDeclaredWithCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePackDeclaredWithCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeletePhantomPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeletePhantomPacks
   Description: Purpose:
<param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeletePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeletePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeletePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRangePhantomPacks(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRangePhantomPacks
   Description: Purpose:
<param name="ipFromCase">First case number to start deletes</param><param name="ipToCase">Last case number to delete</param><param name="ds">Customer Shipment data set </param>
Notes:
   OperationID: DeleteRangePhantomPacks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRangePhantomPacks_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRangePhantomPacks_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAddrInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAddrInfo
   Description: This method updates the address information from either the Vendor or Customer
table when the Shipto or PurPoint field has been changed.  If custID and VendorID fields are
both blank this procedure assumes that the user is entering the information in free form and
there is nothing to default (or no need to call this method).
   OperationID: GetAddrInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAddrInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAddrInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCallInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCallInfo
   Description: This method defaults the Call Number and shipto fields when the Job, PO or Order
number fields change
   OperationID: GetCallInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCallInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCallInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultUOM
   Description: Gets the default UOM from Part or XaSyst
   OperationID: GetDefaultUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDMRSupplierInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDMRSupplierInfo
   Description: Gets DRM Supplier's info
   OperationID: GetDMRSupplierInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDMRSupplierInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDMRSupplierInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumGenOpts
   Description: Returns the legal number generation options.
   OperationID: GetLegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumGenOpts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumGenOpts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlInfo
   Description: This method defaults the Quantity, Part and Line description fields
when the MtlSeq field has been updated
   OperationID: GetMtlInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackageClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackageClass
   OperationID: GetPackageClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackageClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the value of PartNum changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQuantity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQuantity
   Description: Call this method when the value of Quantity changes.
   OperationID: OnChangeQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIUM
   Description: Call this method when the value of IUM changes.
   OperationID: OnChangeIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackaging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackaging
   OperationID: GetPackaging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackaging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackaging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPOSupplierInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPOSupplierInfo
   Description: Gets PO Supplier's info
   OperationID: GetPOSupplierInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPOSupplierInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOSupplierInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetScale(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetScale
   Description: none
   OperationID: GetScale
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetScale_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetScale_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranDocTypeID
   Description: Sets default values when the TranDocTypeID changes
   OperationID: GetTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRMACustomerInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRMACustomerInfo
   Description: Gets RMA Ship to's info
   OperationID: GetRMACustomerInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRMACustomerInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMACustomerInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OpenCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OpenCarton
   Description: Checks to see if the carton can be opened and opens it if it is allowed.
   OperationID: OpenCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OpenCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OpenCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintSlip
   Description: This method prints the Miscellaneous Packing Slip
   OperationID: PrintSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVEnable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVEnable
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVShipStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVShipStatus
   OperationID: SetUPSQVShipStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVShipStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVShipStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrigCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrigCountry
   Description: Method to change related fields to the country. Run when the country changes.
   OperationID: ChangeOrigCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrigCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrigCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StageCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StageCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: StageCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StageCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StageCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateManifestChargeAmts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateManifestChargeAmts
   Description: Calculate the CODAmount and DeclaredAmt
   OperationID: UpdateManifestChargeAmts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateManifestChargeAmts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateManifestChargeAmts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidCarton(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidCarton
   Description: Checks to see if the carton can be voided and voids it if it is allowed.
   OperationID: VoidCarton
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidCarton_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidCarton_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumber
   Description: Voids the legal number.
   OperationID: VoidLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateDigitalSignature(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateDigitalSignature
   Description: Generate Digital Signature
   OperationID: GenerateDigitalSignature
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDigitalSignature_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDigitalSignature_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: none
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: none
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetAllowsDecimals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllowsDecimals
   Description: Checks if the current UOM class allows decimals
   OperationID: GetAllowsDecimals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllowsDecimals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllowsDecimals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateShipmentFromWIP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateShipmentFromWIP
   Description: Creates a shipment from a Job with a make to stock demand link marked as Misc Shipment from WIP
   OperationID: CreateShipmentFromWIP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateShipmentFromWIP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateShipmentFromWIP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMscShpHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMscShpHd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMscShpHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMscShpHdAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMscShpHdAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpHdAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMscShpHdAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpHdAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMscShpDt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMscShpDt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpDt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMscShpDt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpDt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMscShpDtAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMscShpDtAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpDtAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMscShpDtAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpDtAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewShipCOO(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewShipCOO
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewShipCOO
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewShipCOO_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewShipCOO_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMscShpUPS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMscShpUPS
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMscShpUPS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMscShpUPS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMscShpUPS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCartonTrkDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCartonTrkDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCartonTrkDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCartonTrkDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCartonTrkDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MiscShipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CartonTrkDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MscShpDtAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpDtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MscShpDtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MscShpHdAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MscShpHdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpHdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MscShpHdRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MscShpUPSRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MscShpUPSRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ShipCOORow] = obj["value"]
      pass

class Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  """  
      self.PackNum:int = obj["PackNum"]
      """  The pack number associated with the tracking number.  """  
      self.CaseNum:int = obj["CaseNum"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.PkgWeight:int = obj["PkgWeight"]
      """  Package Weight  """  
      self.CODFlag:bool = obj["CODFlag"]
      """  Prefer COD delivery.  Reserved for future development.  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order.  Reserved for future development.  """  
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      """  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  """  
      self.DeclaredValue:int = obj["DeclaredValue"]
      """  Declared Insurance Amount.  Reserved for future development.  """  
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
      self.CODValue:int = obj["CODValue"]
      """  Collect On Delivery Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CaseID:str = obj["CaseID"]
      """  Concatenated field consisting of PackNum and CaseNum separated by a dash.  """  
      self.PackStatus:str = obj["PackStatus"]
      """  Status of the shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  logical used by UI for row rules  """  
      self.CapturePt:str = obj["CapturePt"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.BitFlag:int = obj["BitFlag"]
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

class Erp_Tablesets_MscShpDtAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
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

class Erp_Tablesets_MscShpDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line description.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is defaulted as Job Number.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.Quantity:int = obj["Quantity"]
      """  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is related to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is related to.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The JobMtl seq that this record relates to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this shipment is associated with.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  This is the job that the service call line is linke to.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Related RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Related RMA Disposition  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the Shipment has to be synchronized with Epicor FSA application.  """  
      self.FSAInstallationPrice:int = obj["FSAInstallationPrice"]
      """  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  """  
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      """  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  """  
      self.FSAInstallationTypeDescription:str = obj["FSAInstallationTypeDescription"]
      self.FSARequiresServiceOrder:bool = obj["FSARequiresServiceOrder"]
      """  Indicates if the shipment requires to create an Equipment Delivery Performed line on the resulting FSA Service Order in Epicor FSA.  """  
      self.PartAESExp:str = obj["PartAESExp"]
      self.PartEcnNumber:str = obj["PartEcnNumber"]
      """  Used by freighting web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freighting web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freighting web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freighting web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freighting web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freighting web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freighting web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      self.PartHazTechName:str = obj["PartHazTechName"]
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freighting web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freighting web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freighting web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freighting web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freighting web service  """  
      self.PartSchedBCode:str = obj["PartSchedBCode"]
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      self.ServiceJob:bool = obj["ServiceJob"]
      """  Indicates if the Job is a Service Call  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  ship status of the MscShpHd  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MtlSeqSalvageDescription:str = obj["MtlSeqSalvageDescription"]
      self.MtlSeqDescription:str = obj["MtlSeqDescription"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MscShpHdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
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

class Erp_Tablesets_MscShpHdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
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
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the main address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the main address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the shipping  address.  """  
      self.State:str = obj["State"]
      """  State ID for the ShipTo.  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the shipping  address.  """  
      self.Country:str = obj["Country"]
      """  The country is used as part of the mailing address. It can be left blank.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer to identify vendors.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is related to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is related to.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
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
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
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
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
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
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
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
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
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
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
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
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OnCreditHold:bool = obj["OnCreditHold"]
      """  Indicates if Customer is on credit Hold  """  
      self.JobType:str = obj["JobType"]
      """  Job Type Description  """  
      self.AddrList:str = obj["AddrList"]
      """  List delimited Address fields using the Address Format rules  """  
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the vlaue of items in the carton.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  logical indicating if the weight prompt is enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      """  defaults from the company file.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MscShpHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
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
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the main address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the main address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the shipping  address.  """  
      self.State:str = obj["State"]
      """  State ID for the ShipTo.  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the shipping  address.  """  
      self.Country:str = obj["Country"]
      """  The country is used as part of the mailing address. It can be left blank.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer to identify vendors.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is related to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is related to.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
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
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
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
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
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
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
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
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
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
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
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
      self.IsDMRPack:bool = obj["IsDMRPack"]
      """  Indicates if the Miscellaneous Shipment is a DMR Pack  """  
      self.DispatchReason:str = obj["DispatchReason"]
      """  Dispatch Reason Code used for Customer Shipment  """  
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
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number linked to the Miscellaneous Shipment.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line linked to the Miscellaneous Shipment.  """  
      self.FSAReady:bool = obj["FSAReady"]
      """  True if ready to send to FSA  """  
      self.FromDepotRepair:bool = obj["FromDepotRepair"]
      """  True if created as return shipment from RMA or DMR or Job  """  
      self.FromJobClosing:bool = obj["FromJobClosing"]
      """  True if MscShpHd was created from Job Closing for Misc Shipment to WIP functionality.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the vlaue of items in the carton.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  logical indicating if the weight prompt is enabled.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.JobType:str = obj["JobType"]
      """  Job Type Description  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.OnCreditHold:bool = obj["OnCreditHold"]
      """  Indicates if Customer is on credit Hold  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.AddrList:str = obj["AddrList"]
      """  List delimited Address fields using the Address Format rules  """  
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the PhantomPack checkbox is to be enabled.  """  
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      """  Logical indicating if CartonTrkDtl records exist for this pack. Used by the UI for row rules.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MscShpUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantity View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email adress to be used for notifications.  """  
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
      """  Logical indicating if the UPS quantum view is to be enabled.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.OrigCountry:int = obj["OrigCountry"]
      """  CountryNum for Country of Origin  """  
      self.QtyPerc:int = obj["QtyPerc"]
      """  Qty percent of this part which is from this country of origin.  """  
      self.ValuePerc:int = obj["ValuePerc"]
      """  Value percent of this part from this country of origin.  """  
      self.Primary:bool = obj["Primary"]
      """  Is this the primary country of origin for this part  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.opLegalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CalculateWeight_input:
   """ Required : 
   cartonNumber
   """  
   def __init__(self, obj):
      self.cartonNumber:int = obj["cartonNumber"]
      """  Carton Number  """  
      pass

class CalculateWeight_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.calculatedWeight:int = obj["parameters"]
      pass

      """  output parameters  """  

class CallsCreateCustomerCartons_input:
   """ Required : 
   ipPackNum
   ipNbrCartonsToCreate
   ipPkgCode
   ipPkgLength
   ipPkgWidth
   ipPkgHeight
   ipRecalcAmts
   ipZeroWeight
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipNbrCartonsToCreate:int = obj["ipNbrCartonsToCreate"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgLength:int = obj["ipPkgLength"]
      self.ipPkgWidth:int = obj["ipPkgWidth"]
      self.ipPkgHeight:int = obj["ipPkgHeight"]
      self.ipRecalcAmts:bool = obj["ipRecalcAmts"]
      self.ipZeroWeight:bool = obj["ipZeroWeight"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class CallsCreateCustomerCartons_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CancelVoidCarton_input:
   """ Required : 
   iPackNum
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to open  """  
      pass

class CancelVoidCarton_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

class CartonValidateWeight_input:
   """ Required : 
   ipWeight
   """  
   def __init__(self, obj):
      self.ipWeight:int = obj["ipWeight"]
      pass

class CartonValidateWeight_output:
   def __init__(self, obj):
      pass

class ChangeOrigCountry_input:
   """ Required : 
   i_CountryNum
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      pass

class ChangeOrigCountry_output:
   def __init__(self, obj):
      pass

class CheckCOOPercents_input:
   """ Required : 
   iPackNum
   iPackLine
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The current PackNum  """  
      self.iPackLine:int = obj["iPackLine"]
      """  The current PackLine  """  
      pass

class CheckCOOPercents_output:
   def __init__(self, obj):
      pass

class CheckValidCartonWeight_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      pass

class CheckValidCartonWeight_output:
   def __init__(self, obj):
      pass

class ClearConvertedManifest_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Pack Num to clear Manifest fields  """  
      pass

class ClearConvertedManifest_output:
   def __init__(self, obj):
      pass

class CloseCarton_input:
   """ Required : 
   iPackNum
   ds
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to close  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class CloseCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConvertToManifestUOM_input:
   """ Required : 
   ipPackNum
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Pack Num to populate Manifest fields  """  
      pass

class ConvertToManifestUOM_output:
   def __init__(self, obj):
      pass

class CreateCustomerCartons_input:
   """ Required : 
   ipNbrCartonsToCreate
   ipPkgCode
   ipPkgLength
   ipPkgWidth
   ipPkgHeight
   ipRecalcAmts
   ipZeroWeight
   ds
   """  
   def __init__(self, obj):
      self.ipNbrCartonsToCreate:int = obj["ipNbrCartonsToCreate"]
      self.ipPkgCode:str = obj["ipPkgCode"]
      self.ipPkgLength:int = obj["ipPkgLength"]
      self.ipPkgWidth:int = obj["ipPkgWidth"]
      self.ipPkgHeight:int = obj["ipPkgHeight"]
      self.ipRecalcAmts:bool = obj["ipRecalcAmts"]
      self.ipZeroWeight:bool = obj["ipZeroWeight"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class CreateCustomerCartons_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateMiscShipRecsFromDMR_input:
   """ Required : 
   ipDMRNum
   """  
   def __init__(self, obj):
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  DMR number supplied  """  
      pass

class CreateMiscShipRecsFromDMR_output:
   def __init__(self, obj):
      pass

class CreateShipmentFromWIP_input:
   """ Required : 
   jobNum
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      pass

class CreateShipmentFromWIP_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

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

class DeletePhantomPacks_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class DeletePhantomPacks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteRangePhantomPacks_input:
   """ Required : 
   ipFromCase
   ipToCase
   ds
   """  
   def __init__(self, obj):
      self.ipFromCase:int = obj["ipFromCase"]
      self.ipToCase:int = obj["ipToCase"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class DeleteRangePhantomPacks_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CartonTrkDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company ID  """  
      self.ShipmentType:str = obj["ShipmentType"]
      """  Defines the type of shipment the tracking number is for.  Shipment type is either Misc for miscellaneous, Sales for Customer shipments, Sub for subcontractor shipments Transfer for Transfer order shipment or Master for Masterpack Shipments.  """  
      self.PackNum:int = obj["PackNum"]
      """  The pack number associated with the tracking number.  """  
      self.CaseNum:int = obj["CaseNum"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last CartonTrkDtl record for PackNum and add 1. This number is not displayed to the user.  The case number the user sees is the concatenation of the Packnum and this number separated by a dash.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length dimension for the packaging used to ship this shipment.  """  
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height dimension for the packaging used to ship this shipment.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width dimension for the packaging used to ship this shipment.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.PkgWeight:int = obj["PkgWeight"]
      """  Package Weight  """  
      self.CODFlag:bool = obj["CODFlag"]
      """  Prefer COD delivery.  Reserved for future development.  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery
Reserved for future development.  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order.  Reserved for future development.  """  
      self.DeclaredValueFlag:bool = obj["DeclaredValueFlag"]
      """  Flag to indicate that an insurance value was declared on delivery.  Reserved for future development.  """  
      self.DeclaredValue:int = obj["DeclaredValue"]
      """  Declared Insurance Amount.  Reserved for future development.  """  
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
      self.CODValue:int = obj["CODValue"]
      """  Collect On Delivery Value  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CaseID:str = obj["CaseID"]
      """  Concatenated field consisting of PackNum and CaseNum separated by a dash.  """  
      self.PackStatus:str = obj["PackStatus"]
      """  Status of the shipment.  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  logical used by UI for row rules  """  
      self.CapturePt:str = obj["CapturePt"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the phantom cartonTrkDtl fields are to be enabled.  This is based upon whether or not the workstation is setup for manifesting.  """  
      self.KitPartAttrClassID:str = obj["KitPartAttrClassID"]
      self.BitFlag:int = obj["BitFlag"]
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

class Erp_Tablesets_MiscShipTableset:
   def __init__(self, obj):
      self.MscShpHd:list[Erp_Tablesets_MscShpHdRow] = obj["MscShpHd"]
      self.MscShpHdAttch:list[Erp_Tablesets_MscShpHdAttchRow] = obj["MscShpHdAttch"]
      self.MscShpDt:list[Erp_Tablesets_MscShpDtRow] = obj["MscShpDt"]
      self.MscShpDtAttch:list[Erp_Tablesets_MscShpDtAttchRow] = obj["MscShpDtAttch"]
      self.ShipCOO:list[Erp_Tablesets_ShipCOORow] = obj["ShipCOO"]
      self.MscShpUPS:list[Erp_Tablesets_MscShpUPSRow] = obj["MscShpUPS"]
      self.CartonTrkDtl:list[Erp_Tablesets_CartonTrkDtlRow] = obj["CartonTrkDtl"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MscShpDtAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.PackLine:int = obj["PackLine"]
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

class Erp_Tablesets_MscShpDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system. Read last ShipDtl record for PackNum and add 1.  """  
      self.LineType:str = obj["LineType"]
      """  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  """  
      self.Packages:int = obj["Packages"]
      """  Number of Packages.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number of item actually shipped.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line description.  """  
      self.IUM:str = obj["IUM"]
      """  Unit of measure  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part revision number. Not user maintainable. Duplicated from the OrderDtl.RevisionNum at time of creation.  """  
      self.ShipComment:str = obj["ShipComment"]
      """   Holds any comments about the order line being shipped.  Viewed as an Editor widget.

This gets duplicated from the OrderDtl.ShipComment.  """  
      self.XPartNum:str = obj["XPartNum"]
      """   An optional field that is used if the customer has a different  Part number  than the users internal part number.
This field is defaulted from the OrderDtl.XPartNum.  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  Optional field that contains the customers revision. Default from the OrderDtl.XRevisionNum field.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact in the CUSTCNT table. This is duplicated from the OrderRel.ShpConNum.  """  
      self.WUM:str = obj["WUM"]
      """  Weight Unit of measure...qualifies the weight field value. (Lb, Oz, Gr...). Defaulted from XASyst.DefaultWUM  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number is defaulted as Job Number.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the shipment is for.  Duplicated from ShipHead.CustNum.  Used to allow efficient browsing of the ShipDtl records for a specific customer.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The shipto number. Used for warranty validation.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  For Warranty shipments.  Defaults as Shiphead.shipdate. But can be maintained from the Service Call center.  """  
      self.Plant:str = obj["Plant"]
      """  Site that the shipment is from.  Duplicated from ShipHead.Site.  Used to allow efficient browsing of the ShipDtl records.  """  
      self.Quantity:int = obj["Quantity"]
      """  Holds the Quantity onhand for this Part in the warehouse in the specific bin location.  Whenever this quantity becomes zero the record should be deleted. This quantity needs to added to or subtracted from Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse Transfers, Shipping and Adjustments.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is related to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is related to.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  The JobMtl seq that this record relates to.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number that this shipment is associated with.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  This is the job that the service call line is linke to.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Related RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Related RMA Disposition  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Determines if the Shipment has to be synchronized with Epicor FSA application.  """  
      self.FSAInstallationPrice:int = obj["FSAInstallationPrice"]
      """  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  """  
      self.FSAInstallationRequired:bool = obj["FSAInstallationRequired"]
      """  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  """  
      self.FSAInstallationType:str = obj["FSAInstallationType"]
      """  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  """  
      self.FSAInstallationTypeDescription:str = obj["FSAInstallationTypeDescription"]
      self.FSARequiresServiceOrder:bool = obj["FSARequiresServiceOrder"]
      """  Indicates if the shipment requires to create an Equipment Delivery Performed line on the resulting FSA Service Order in Epicor FSA.  """  
      self.PartAESExp:str = obj["PartAESExp"]
      self.PartEcnNumber:str = obj["PartEcnNumber"]
      """  Used by freighting web service  """  
      self.PartExpLicNumber:str = obj["PartExpLicNumber"]
      """  Used by freighting web service  """  
      self.PartExpLicType:str = obj["PartExpLicType"]
      """  Used by freighting web service  """  
      self.PartHazClass:str = obj["PartHazClass"]
      """  Used by freighting web service  """  
      self.PartHazGvrnmtID:str = obj["PartHazGvrnmtID"]
      """  Used by freighting web service  """  
      self.PartHazItem:bool = obj["PartHazItem"]
      """  Used by freighting web service  """  
      self.PartHazPackInstr:str = obj["PartHazPackInstr"]
      """  Used by freighting web service  """  
      self.PartHazSub:str = obj["PartHazSub"]
      self.PartHazTechName:str = obj["PartHazTechName"]
      self.PartHTS:str = obj["PartHTS"]
      """  Used by freighting web service  """  
      self.PartNAFTAOrigCountry:str = obj["PartNAFTAOrigCountry"]
      """  Used by freighting web service  """  
      self.PartNAFTAPref:str = obj["PartNAFTAPref"]
      """  Used by freighting web service  """  
      self.PartNAFTAProd:str = obj["PartNAFTAProd"]
      """  Used by freighting web service  """  
      self.PartOrigCountry:str = obj["PartOrigCountry"]
      """  Used by freighting web service  """  
      self.PartSchedBCode:str = obj["PartSchedBCode"]
      self.PartUseHTSDesc:bool = obj["PartUseHTSDesc"]
      self.ServiceJob:bool = obj["ServiceJob"]
      """  Indicates if the Job is a Service Call  """  
      self.ShipStatus:str = obj["ShipStatus"]
      """  ship status of the MscShpHd  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MtlSeqSalvageDescription:str = obj["MtlSeqSalvageDescription"]
      self.MtlSeqDescription:str = obj["MtlSeqDescription"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MscShpHdAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
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

class Erp_Tablesets_MscShpHdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
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
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the main address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the main address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the shipping  address.  """  
      self.State:str = obj["State"]
      """  State ID for the ShipTo.  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the shipping  address.  """  
      self.Country:str = obj["Country"]
      """  The country is used as part of the mailing address. It can be left blank.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer to identify vendors.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is related to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is related to.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
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
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
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
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
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
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
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
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
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
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
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
      self.AutoPrintReady:bool = obj["AutoPrintReady"]
      """  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OnCreditHold:bool = obj["OnCreditHold"]
      """  Indicates if Customer is on credit Hold  """  
      self.JobType:str = obj["JobType"]
      """  Job Type Description  """  
      self.AddrList:str = obj["AddrList"]
      """  List delimited Address fields using the Address Format rules  """  
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the vlaue of items in the carton.  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  """  
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  logical indicating if the weight prompt is enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input  """  
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      """  Country name  """  
      self.CustomerBTName:str = obj["CustomerBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.CustomerName:str = obj["CustomerName"]
      """  The full name of the customer.  """  
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      """  Description of delivery type  """  
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      """  The member's name on the credit card.  """  
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      """  Second address line  """  
      self.PurPointCountry:str = obj["PurPointCountry"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.PurPointState:str = obj["PurPointState"]
      """  State portion of the address  """  
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      """  Third address line  """  
      self.PurPointName:str = obj["PurPointName"]
      """  Purchase Point Name...can't be blank.  """  
      self.PurPointZip:str = obj["PurPointZip"]
      """  Postal Code or Zip code portion of the address  """  
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      """  First address line  """  
      self.PurPointCity:str = obj["PurPointCity"]
      """  City portion of the address  """  
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      """  "External" Ship Via description for Customer Connect (StoreFront) selection.  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  Full description for the shipping company (carrier).  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      """  defaults from the company file.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MscShpHdListTableset:
   def __init__(self, obj):
      self.MscShpHdList:list[Erp_Tablesets_MscShpHdListRow] = obj["MscShpHdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MscShpHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available number is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales Order number for which this shipment is for.  This is a mandatory field.  Must be valid in the OrderHed file.  The order number cannot be changed if ShipDtl records exist for this packing slip.  """  
      self.ShipDate:str = obj["ShipDate"]
      """  The actual ship date for the packing slip. Default as system date.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master.  Can be blank or must be valid in the ShipVia. Use the OrderHed.ShipViaCode as default.  """  
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
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo ID to be used that this packing slip was for.  This can only be one of the ShipToNum that exist on one of the OrderRel records.  If the order only has one ShipTo the user will never be prompted for this. This MUST BE VALID IN THE SHIPVIA file.  Use the OrderHead.ShiptoNum as the default when creating new records.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number.  Not user maintainable, Duplicated from the related sales order.  Used to relate this record to the customer master.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that shipment was made from.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.Name:str = obj["Name"]
      """  Name of the ShipTo. When creating new records the Customer.Name is used as a default.  This can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the main address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the main address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the shipping  address.  """  
      self.State:str = obj["State"]
      """  State ID for the ShipTo.  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  The zip or postal code portion of the shipping  address.  """  
      self.Country:str = obj["Country"]
      """  The country is used as part of the mailing address. It can be left blank.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the customer. Optional field.  Displayed by Order entry when no shipping contact is given or that contact has a blank phone number.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Business Phone Number for the shipto location.. Displayed in Order entry when no shipping contact is given for or when contact has a blank phone number.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer to identify vendors.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is related to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is related to.  """  
      self.TrackingNumber:str = obj["TrackingNumber"]
      """  This optional field is the shipper's tracking number.  This can be used to look up status information from the shipper.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
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
      self.PkgCode:str = obj["PkgCode"]
      """  Packaging code  """  
      self.PkgClass:str = obj["PkgClass"]
      """  NMFC Packaging Classification code.  """  
      self.Weight:int = obj["Weight"]
      """  Package Weight  """  
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
      self.BOLNum:int = obj["BOLNum"]
      """  Bill of Lading Number the packing slip is linked to  """  
      self.BOLLine:int = obj["BOLLine"]
      """  Bill of Lading line number linked to  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
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
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Added for international shipping, Is a commercial invoice required  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Added for international shipping. Shipper's Export Declaration required  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  For International shipping.  Certificate of Orgin required.  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  For International shipping.  Shipper's Letter of Instruction.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Is this an International shipment  """  
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
      self.FFID:str = obj["FFID"]
      """  International Shipping. Frieght Forwarder ID  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  International Shipping. The third line of the Freight Forwarder main address.  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling Required flag  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Package flag.  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  International Shipping. The country number of the Freight Forwarder main address.  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping Bill To.  The third line of the Payers main address. An address is required when Pay Flag is Third party  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Shipping, The country number of the Payer main address.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping, The phone number of the Payer main address.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      """  Way Bill Number  """  
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      """  This is the ship via code the freighting system selected for shipping.  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantity View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantity View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantity View Memo  """  
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
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
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
      self.IsDMRPack:bool = obj["IsDMRPack"]
      """  Indicates if the Miscellaneous Shipment is a DMR Pack  """  
      self.DispatchReason:str = obj["DispatchReason"]
      """  Dispatch Reason Code used for Customer Shipment  """  
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
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number linked to the Miscellaneous Shipment.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line linked to the Miscellaneous Shipment.  """  
      self.FSAReady:bool = obj["FSAReady"]
      """  True if ready to send to FSA  """  
      self.FromDepotRepair:bool = obj["FromDepotRepair"]
      """  True if created as return shipment from RMA or DMR or Job  """  
      self.FromJobClosing:bool = obj["FromJobClosing"]
      """  True if MscShpHd was created from Job Closing for Misc Shipment to WIP functionality.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.CartonContentValue:int = obj["CartonContentValue"]
      """  The sum of the vlaue of items in the carton.  """  
      self.CartonHeight:int = obj["CartonHeight"]
      """  Carton Height  """  
      self.CartonLength:int = obj["CartonLength"]
      """  Carton length  """  
      self.CartonStageNbr:str = obj["CartonStageNbr"]
      """  Carton Stage number  """  
      self.CartonWidth:int = obj["CartonWidth"]
      """  Carton width  """  
      self.DspDigitalSignature:str = obj["DspDigitalSignature"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableWeight:bool = obj["EnableWeight"]
      """  logical indicating if the weight prompt is enabled.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.JobType:str = obj["JobType"]
      """  Job Type Description  """  
      self.LastCartonFlag:bool = obj["LastCartonFlag"]
      """  If Y, this is the last carton being shipped to the customer.  If N, then it is not the last carton.  Last Carton is set to Y when the sumo of the quantity packed equals the quantity ordered for each line.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.ManifestFlag:bool = obj["ManifestFlag"]
      """  Indicates if the manifest interface is enabled.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Pack ID of the Masterpack this shipment is on.  """  
      self.OnCreditHold:bool = obj["OnCreditHold"]
      """  Indicates if Customer is on credit Hold  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  A zero indicates the Packing height is to be enabled.  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Indicates if package length is to be enabled.  If the value is zero the prompt is enabled.  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  A zero indicates the packaging width field is to be enabled.  """  
      self.ShipStatusDescription:str = obj["ShipStatusDescription"]
      self.AddrList:str = obj["AddrList"]
      """  List delimited Address fields using the Address Format rules  """  
      self.QSUseBOL:bool = obj["QSUseBOL"]
      self.QSUseIntl:bool = obj["QSUseIntl"]
      self.QSUseCO:bool = obj["QSUseCO"]
      self.EnablePhantom:bool = obj["EnablePhantom"]
      """  Logical indicating if the PhantomPack checkbox is to be enabled.  """  
      self.PhantomCasesExist:bool = obj["PhantomCasesExist"]
      """  Logical indicating if CartonTrkDtl records exist for this pack. Used by the UI for row rules.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGInvoicingPointDescription:str = obj["AGInvoicingPointDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FreightedShipViaCodeWebDesc:str = obj["FreightedShipViaCodeWebDesc"]
      self.FreightedShipViaCodeDescription:str = obj["FreightedShipViaCodeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MscShpUPSRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PackNum:int = obj["PackNum"]
      """  When creating a new packing slip, the user is prompted for a packing slip number.  If the field is left blank, the next available # is assigned by the system.  The system generates a number by finding the last ShipHead on file and uses its PackNum + 1.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantity View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email adress to be used for notifications.  """  
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
      """  Logical indicating if the UPS quantum view is to be enabled.  """  
      self.ShipStatus:str = obj["ShipStatus"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ShipCOORow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.OrigCountry:int = obj["OrigCountry"]
      """  CountryNum for Country of Origin  """  
      self.QtyPerc:int = obj["QtyPerc"]
      """  Qty percent of this part which is from this country of origin.  """  
      self.ValuePerc:int = obj["ValuePerc"]
      """  Value percent of this part from this country of origin.  """  
      self.Primary:bool = obj["Primary"]
      """  Is this the primary country of origin for this part  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the country of origin is related. ?ShipDtl?, ?MscShpDt?, ?TFShipDtl?, and ?SubShipD?  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number that this detail record is linked with.  """  
      self.PackLine:int = obj["PackLine"]
      """  An integer that uniquely identifies a detail record within a Packing slip.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryDescription:str = obj["CountryDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtMiscShipTableset:
   def __init__(self, obj):
      self.MscShpHd:list[Erp_Tablesets_MscShpHdRow] = obj["MscShpHd"]
      self.MscShpHdAttch:list[Erp_Tablesets_MscShpHdAttchRow] = obj["MscShpHdAttch"]
      self.MscShpDt:list[Erp_Tablesets_MscShpDtRow] = obj["MscShpDt"]
      self.MscShpDtAttch:list[Erp_Tablesets_MscShpDtAttchRow] = obj["MscShpDtAttch"]
      self.ShipCOO:list[Erp_Tablesets_ShipCOORow] = obj["ShipCOO"]
      self.MscShpUPS:list[Erp_Tablesets_MscShpUPSRow] = obj["MscShpUPS"]
      self.CartonTrkDtl:list[Erp_Tablesets_CartonTrkDtlRow] = obj["CartonTrkDtl"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateDigitalSignature_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GenerateDigitalSignature_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAddrInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetAddrInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAllowsDecimals_input:
   """ Required : 
   IUMCode
   Qty
   """  
   def __init__(self, obj):
      self.IUMCode:str = obj["IUMCode"]
      self.Qty:str = obj["Qty"]
      pass

class GetAllowsDecimals_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

class GetCallInfo_input:
   """ Required : 
   updatedField
   ds
   """  
   def __init__(self, obj):
      self.updatedField:str = obj["updatedField"]
      """  Name of the field that changed, Order, Job, or PO  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetCallInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCartonPackaging_input:
   """ Required : 
   ipPkgCode
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      pass

class GetCartonPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPkgHeight:int = obj["parameters"]
      self.opPkgWidth:int = obj["parameters"]
      self.opPkgLength:int = obj["parameters"]
      pass

      """  output parameters  """  

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

class GetDMRSupplierInfo_input:
   """ Required : 
   ipDMRNum
   ds
   """  
   def __init__(self, obj):
      self.ipDMRNum:int = obj["ipDMRNum"]
      """  IPDMRNum DMR number supplied  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetDMRSupplierInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultUOM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetDefaultUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetLegalNumGenOpts_input:
   """ Required : 
   ipPackNum
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetLegalNumGenOpts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.opPromptForNum:bool = obj["opPromptForNum"]
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
      self.returnObj:list[Erp_Tablesets_MscShpHdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMtlInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetMtlInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCartonTrkDtl_input:
   """ Required : 
   ds
   shipmentType
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.shipmentType:str = obj["shipmentType"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewCartonTrkDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMscShpDtAttch_input:
   """ Required : 
   ds
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewMscShpDtAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMscShpDt_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewMscShpDt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMscShpHdAttch_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewMscShpHdAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMscShpHd_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetNewMscShpHd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMscShpUPS_input:
   """ Required : 
   ds
   packNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.packNum:int = obj["packNum"]
      pass

class GetNewMscShpUPS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewShipCOO_input:
   """ Required : 
   ds
   relatedToFile
   packNum
   packLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.packNum:int = obj["packNum"]
      self.packLine:int = obj["packLine"]
      pass

class GetNewShipCOO_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPOSupplierInfo_input:
   """ Required : 
   ipPONum
   ds
   """  
   def __init__(self, obj):
      self.ipPONum:int = obj["ipPONum"]
      """  IPPONum PO number supplied  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetPOSupplierInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackageClass_input:
   """ Required : 
   ipPkgClass
   ds
   """  
   def __init__(self, obj):
      self.ipPkgClass:str = obj["ipPkgClass"]
      """  package class to validate  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetPackageClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPackaging_input:
   """ Required : 
   ipPkgCode
   ds
   """  
   def __init__(self, obj):
      self.ipPkgCode:str = obj["ipPkgCode"]
      """  package code  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetPackaging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRMACustomerInfo_input:
   """ Required : 
   ipRMALine
   ds
   """  
   def __init__(self, obj):
      self.ipRMALine:int = obj["ipRMALine"]
      """  ipRMALine RMA line supplied  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetRMACustomerInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMscShpHd
   whereClauseMscShpHdAttch
   whereClauseMscShpDt
   whereClauseMscShpDtAttch
   whereClauseShipCOO
   whereClauseMscShpUPS
   whereClauseCartonTrkDtl
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMscShpHd:str = obj["whereClauseMscShpHd"]
      self.whereClauseMscShpHdAttch:str = obj["whereClauseMscShpHdAttch"]
      self.whereClauseMscShpDt:str = obj["whereClauseMscShpDt"]
      self.whereClauseMscShpDtAttch:str = obj["whereClauseMscShpDtAttch"]
      self.whereClauseShipCOO:str = obj["whereClauseShipCOO"]
      self.whereClauseMscShpUPS:str = obj["whereClauseMscShpUPS"]
      self.whereClauseCartonTrkDtl:str = obj["whereClauseCartonTrkDtl"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetScale_input:
   """ Required : 
   workstationID
   """  
   def __init__(self, obj):
      self.workstationID:str = obj["workstationID"]
      pass

class GetScale_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.scaleID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTranDocTypeID_input:
   """ Required : 
   ipTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.ipTranDocTypeID:str = obj["ipTranDocTypeID"]
      """  TranDocTypeID supplied  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class GetTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
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

class OnChangeIUM_input:
   """ Required : 
   pIUM
   ds
   """  
   def __init__(self, obj):
      self.pIUM:str = obj["pIUM"]
      """  IUM  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class OnChangeIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeQuantity_input:
   """ Required : 
   pdQty
   ds
   """  
   def __init__(self, obj):
      self.pdQty:int = obj["pdQty"]
      """  Transaction Qty  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class OnChangeQuantity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OpenCarton_input:
   """ Required : 
   iPackNum
   ipResetCODCharges
   ipResetInsCharges
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to open  """  
      self.ipResetCODCharges:bool = obj["ipResetCODCharges"]
      """  Indicates if the CODAmount is to be reset to zero  """  
      self.ipResetInsCharges:bool = obj["ipResetInsCharges"]
      """  Indicates if the DeclaredAmt is to be reset to zero  """  
      pass

class OpenCarton_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

class PrintSlip_input:
   """ Required : 
   packNum
   """  
   def __init__(self, obj):
      self.packNum:int = obj["packNum"]
      """  Packing Slip number  """  
      pass

class PrintSlip_output:
   def __init__(self, obj):
      pass

class SetUPSQVEnable_input:
   """ Required : 
   ipQVEnable
   ds
   """  
   def __init__(self, obj):
      self.ipQVEnable:bool = obj["ipQVEnable"]
      """  logical indicating if the quantum view is to enabled/disabled  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class SetUPSQVEnable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetUPSQVShipStatus_input:
   """ Required : 
   ipShipStatus
   ds
   """  
   def __init__(self, obj):
      self.ipShipStatus:str = obj["ipShipStatus"]
      """  Shipment status  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class SetUPSQVShipStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StageCarton_input:
   """ Required : 
   iPackNum
   ds
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to Stage  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class StageCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMiscShipTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMiscShipTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateManifestChargeAmts_input:
   """ Required : 
   ipAmountType
   ipAction
   ds
   """  
   def __init__(self, obj):
      self.ipAmountType:str = obj["ipAmountType"]
      """  COD or DeclaredAmt  """  
      self.ipAction:bool = obj["ipAction"]
      """  Yes = recalculate No = reset to zero  """  
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class UpdateManifestChargeAmts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackCODWithCarton_input:
   """ Required : 
   ipPackNum
   ipCaseNum
   ipOldCOD
   ipCOD
   ipFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipCaseNum:int = obj["ipCaseNum"]
      self.ipOldCOD:int = obj["ipOldCOD"]
      self.ipCOD:int = obj["ipCOD"]
      self.ipFlag:bool = obj["ipFlag"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class UpdatePackCODWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackDeclaredWithCarton_input:
   """ Required : 
   ipPackNum
   ipCaseNum
   ipOldDeclared
   ipDeclared
   ipDeclaredFlag
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipCaseNum:int = obj["ipCaseNum"]
      self.ipOldDeclared:int = obj["ipOldDeclared"]
      self.ipDeclared:int = obj["ipDeclared"]
      self.ipDeclaredFlag:bool = obj["ipDeclaredFlag"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class UpdatePackDeclaredWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdatePackWeightWithCarton_input:
   """ Required : 
   ipPackNum
   ipOldWeight
   ipWeight
   ds
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      self.ipOldWeight:int = obj["ipOldWeight"]
      self.ipWeight:int = obj["ipWeight"]
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class UpdatePackWeightWithCarton_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MiscShipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidCarton_input:
   """ Required : 
   iPackNum
   """  
   def __init__(self, obj):
      self.iPackNum:int = obj["iPackNum"]
      """  The carton number of the carton to void  """  
      pass

class VoidCarton_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

class VoidLegalNumber_input:
   """ Required : 
   ipPackNum
   ipVoidedReason
   """  
   def __init__(self, obj):
      self.ipPackNum:int = obj["ipPackNum"]
      """  Packing Slip number  """  
      self.ipVoidedReason:str = obj["ipVoidedReason"]
      """  Reason for the void  """  
      pass

class VoidLegalNumber_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MiscShipTableset] = obj["returnObj"]
      pass

