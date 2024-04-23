import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlLabelTypeSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlLabelTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlLabelTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlLabelTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlLabelTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlLabelTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlLabelTypes_Company_Plant_LabelType_PartNum_CustNum_ShipToNum_PkgCode_PkgControlIDCode(Company, Plant, LabelType, PartNum, CustNum, ShipToNum, PkgCode, PkgControlIDCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlLabelType item
   Description: Calls GetByID to retrieve the PkgControlLabelType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param LabelType: Desc: LabelType   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes(" + Company + "," + Plant + "," + LabelType + "," + PartNum + "," + CustNum + "," + ShipToNum + "," + PkgCode + "," + PkgControlIDCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlLabelTypes_Company_Plant_LabelType_PartNum_CustNum_ShipToNum_PkgCode_PkgControlIDCode(Company, Plant, LabelType, PartNum, CustNum, ShipToNum, PkgCode, PkgControlIDCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlLabelType for the service
   Description: Calls UpdateExt to update PkgControlLabelType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlLabelType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param LabelType: Desc: LabelType   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes(" + Company + "," + Plant + "," + LabelType + "," + PartNum + "," + CustNum + "," + ShipToNum + "," + PkgCode + "," + PkgControlIDCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlLabelTypes_Company_Plant_LabelType_PartNum_CustNum_ShipToNum_PkgCode_PkgControlIDCode(Company, Plant, LabelType, PartNum, CustNum, ShipToNum, PkgCode, PkgControlIDCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlLabelType item
   Description: Call UpdateExt to delete PkgControlLabelType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlLabelType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param LabelType: Desc: LabelType   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param CustNum: Desc: CustNum   Required: True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PkgCode: Desc: PkgCode   Required: True   Allow empty value : True
      :param PkgControlIDCode: Desc: PkgControlIDCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/PkgControlLabelTypes(" + Company + "," + Plant + "," + LabelType + "," + PartNum + "," + CustNum + "," + ShipToNum + "," + PkgCode + "," + PkgControlIDCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePkgControlLabelType, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClausePkgControlLabelType=" + whereClausePkgControlLabelType
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, labelType, partNum, custNum, shipToNum, pkgCode, pkgControlIDCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "labelType=" + labelType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "custNum=" + custNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "shipToNum=" + shipToNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pkgCode=" + pkgCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pkgControlIDCode=" + pkgControlIDCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_PopulateLabelType(epicorHeaders = None):
   """  
   Summary: Invoke method PopulateLabelType
   Description: Parameters:  none
   OperationID: PopulateLabelType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PopulateLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCustomer
   OperationID: ValidateCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShipTo
   OperationID: ValidateShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartNum
   OperationID: ValidatePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePkgCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePkgCode
   OperationID: ValidatePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePackageControlIDCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePackageControlIDCode
   OperationID: ValidatePackageControlIDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePackageControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePackageControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateReportID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateReportID
   OperationID: ValidateReportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedCustID
   OperationID: ChangedCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedLabelType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedLabelType
   Description: Called when the LabelType is changed
   OperationID: ChangedLabelType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedLabelType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedShipToNum
   OperationID: ChangedShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedPartNum
   OperationID: ChangedPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedReportID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedReportID
   OperationID: ChangedReportID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedStyleNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedStyleNum
   OperationID: ChangedStyleNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedStyleNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedStyleNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedPkgCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedPkgCode
   OperationID: ChangedPkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedPkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangedPkgControlIDCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedPkgControlIDCode
   OperationID: ChangedPkgControlIDCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedPkgControlIDCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedPkgControlIDCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyLabelTypeBySysRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyLabelTypeBySysRowID
   Description: Returns a copy of the current record
   OperationID: CopyLabelTypeBySysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyLabelTypeBySysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLabelTypeBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyLabelType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyLabelType
   Description: KInetic Returns a copy of the current record
   OperationID: CopyLabelType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyLabelType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlLabelType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlLabelType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlLabelType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlLabelType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlLabelType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlLabelTypeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlLabelTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlLabelTypeRow] = obj["value"]
      pass

class Erp_Tablesets_PkgControlLabelTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site ID  """  
      self.LabelType:str = obj["LabelType"]
      """  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  """  
      self.PartNum:str = obj["PartNum"]
      """  Any valid part for the site selected. This field is optional  """  
      self.CustNum:int = obj["CustNum"]
      """  Any valid customer. This field is optional  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Any valid ship to for the customer selected. This field is optional.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Any valid selection from Packing table. This field is optional  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Required field. The values comes from PkgControl.PkgControlIDCode field  """  
      self.IsPartDefault:bool = obj["IsPartDefault"]
      """  Checkbox. The default should be False  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Number Of Labels To Print. Required field, value must be greater than 0  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.Name:str = obj["Name"]
      self.CustID:str = obj["CustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site ID  """  
      self.LabelType:str = obj["LabelType"]
      """  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  """  
      self.PartNum:str = obj["PartNum"]
      """  Any valid part for the site selected. This field is optional  """  
      self.CustNum:int = obj["CustNum"]
      """  Any valid customer. This field is optional  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Any valid ship to for the customer selected. This field is optional.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Any valid selection from Packing table. This field is optional  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Required field. The values comes from PkgControl.PkgControlIDCode field  """  
      self.IsPartDefault:bool = obj["IsPartDefault"]
      """  Checkbox. The default should be False  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Number Of Labels To Print. Required field, value must be greater than 0  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.PromptForReportStyle:bool = obj["PromptForReportStyle"]
      """  If checked = true during the print routine the system will prompt the user with a dialogue box in which they will be able to pick a different Report Style. This dialogue box should be the standard dialogue we use for the STD application and HH. If this new checkbox is False then the system will use the data it has to print the label.  It will be up to the program calling the routine to notify the user the report was sent.  """  
      self.MaxPartQtyPerLabel:int = obj["MaxPartQtyPerLabel"]
      """  For Mixed Masters this is the number of distinct Part Qty’s that can be added to a single label  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Location of the Bartender Label file  """  
      self.Active:bool = obj["Active"]
      """  Active flag  """  
      self.StyleList:str = obj["StyleList"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangedCustID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedLabelType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedLabelType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedPkgCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedPkgCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedPkgControlIDCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedPkgControlIDCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedReportID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedReportID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedShipToNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedStyleNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class ChangedStyleNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyLabelTypeBySysRowID_input:
   """ Required : 
   originalSysRowID
   ds
   """  
   def __init__(self, obj):
      self.originalSysRowID:str = obj["originalSysRowID"]
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class CopyLabelTypeBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["returnObj"]
      pass

class CopyLabelType_input:
   """ Required : 
   originalSysRowID
   ds
   """  
   def __init__(self, obj):
      self.originalSysRowID:str = obj["originalSysRowID"]
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class CopyLabelType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   plant
   labelType
   partNum
   custNum
   shipToNum
   pkgCode
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.labelType:str = obj["labelType"]
      self.partNum:str = obj["partNum"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.pkgCode:str = obj["pkgCode"]
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PkgControlLabelTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site ID  """  
      self.LabelType:str = obj["LabelType"]
      """  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  """  
      self.PartNum:str = obj["PartNum"]
      """  Any valid part for the site selected. This field is optional  """  
      self.CustNum:int = obj["CustNum"]
      """  Any valid customer. This field is optional  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Any valid ship to for the customer selected. This field is optional.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Any valid selection from Packing table. This field is optional  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Required field. The values comes from PkgControl.PkgControlIDCode field  """  
      self.IsPartDefault:bool = obj["IsPartDefault"]
      """  Checkbox. The default should be False  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Number Of Labels To Print. Required field, value must be greater than 0  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.Name:str = obj["Name"]
      self.CustID:str = obj["CustID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelTypeListTableset:
   def __init__(self, obj):
      self.PkgControlLabelTypeList:list[Erp_Tablesets_PkgControlLabelTypeListRow] = obj["PkgControlLabelTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlLabelTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site ID  """  
      self.LabelType:str = obj["LabelType"]
      """  Available values are INTERNAL, GENERAL, STATIC, INDIVIDUAL, MASTER, MIXEDMASTER  """  
      self.PartNum:str = obj["PartNum"]
      """  Any valid part for the site selected. This field is optional  """  
      self.CustNum:int = obj["CustNum"]
      """  Any valid customer. This field is optional  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Any valid ship to for the customer selected. This field is optional.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Any valid selection from Packing table. This field is optional  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Required field. The values comes from PkgControl.PkgControlIDCode field  """  
      self.IsPartDefault:bool = obj["IsPartDefault"]
      """  Checkbox. The default should be False  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Number Of Labels To Print. Required field, value must be greater than 0  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive flag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.PromptForReportStyle:bool = obj["PromptForReportStyle"]
      """  If checked = true during the print routine the system will prompt the user with a dialogue box in which they will be able to pick a different Report Style. This dialogue box should be the standard dialogue we use for the STD application and HH. If this new checkbox is False then the system will use the data it has to print the label.  It will be up to the program calling the routine to notify the user the report was sent.  """  
      self.MaxPartQtyPerLabel:int = obj["MaxPartQtyPerLabel"]
      """  For Mixed Masters this is the number of distinct Part Qty’s that can be added to a single label  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Location of the Bartender Label file  """  
      self.Active:bool = obj["Active"]
      """  Active flag  """  
      self.StyleList:str = obj["StyleList"]
      self.StyleDescription:str = obj["StyleDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerCustID:str = obj["CustomerCustID"]
      self.PackingDescription:str = obj["PackingDescription"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelTypeTableset:
   def __init__(self, obj):
      self.PkgControlLabelType:list[Erp_Tablesets_PkgControlLabelTypeRow] = obj["PkgControlLabelType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPkgControlLabelTypeTableset:
   def __init__(self, obj):
      self.PkgControlLabelType:list[Erp_Tablesets_PkgControlLabelTypeRow] = obj["PkgControlLabelType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   labelType
   partNum
   custNum
   shipToNum
   pkgCode
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.labelType:str = obj["labelType"]
      self.partNum:str = obj["partNum"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.pkgCode:str = obj["pkgCode"]
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPkgControlLabelType_input:
   """ Required : 
   ds
   plant
   labelType
   partNum
   custNum
   shipToNum
   pkgCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.labelType:str = obj["labelType"]
      self.partNum:str = obj["partNum"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      self.pkgCode:str = obj["pkgCode"]
      pass

class GetNewPkgControlLabelType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePkgControlLabelType
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePkgControlLabelType:str = obj["whereClausePkgControlLabelType"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["returnObj"]
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

class PopulateLabelType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.valueList:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlLabelTypeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPkgControlLabelTypeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlLabelTypeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateCustomer_input:
   """ Required : 
   proposedCustID
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      pass

class ValidateCustomer_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class ValidatePackageControlIDCode_input:
   """ Required : 
   proposedPkgControlType
   proposedPkgControlIDCode
   """  
   def __init__(self, obj):
      self.proposedPkgControlType:str = obj["proposedPkgControlType"]
      self.proposedPkgControlIDCode:str = obj["proposedPkgControlIDCode"]
      pass

class ValidatePackageControlIDCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidatePartNum_input:
   """ Required : 
   proposedPartNum
   """  
   def __init__(self, obj):
      self.proposedPartNum:str = obj["proposedPartNum"]
      pass

class ValidatePartNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidatePkgCode_input:
   """ Required : 
   proposedPkgCode
   partNumber
   """  
   def __init__(self, obj):
      self.proposedPkgCode:str = obj["proposedPkgCode"]
      self.partNumber:str = obj["partNumber"]
      pass

class ValidatePkgCode_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ValidateReportID_input:
   """ Required : 
   proposedReportId
   """  
   def __init__(self, obj):
      self.proposedReportId:str = obj["proposedReportId"]
      pass

class ValidateReportID_output:
   def __init__(self, obj):
      pass

class ValidateShipTo_input:
   """ Required : 
   custNum
   proposedShipTo
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.proposedShipTo:str = obj["proposedShipTo"]
      pass

class ValidateShipTo_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

